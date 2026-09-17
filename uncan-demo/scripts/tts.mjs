import { createHash } from 'node:crypto'
import { mkdir, readFile, writeFile, access } from 'node:fs/promises'
import path from 'node:path'
import { ROOT, AUDIO_DIR, MANIFEST_PATH, INTRA_PAUSE_MS, loadDeck, loadSegment, splitClauses } from './lib/deck.mjs'

const MODEL_ID = process.env.ELEVENLABS_MODEL_ID || 'eleven_turbo_v2_5'

function hashText(text) {
  return createHash('sha256').update(text).digest('hex').slice(0, 8)
}

async function fileExists(p) {
  try {
    await access(p)
    return true
  } catch {
    return false
  }
}

async function buildPlan(deck) {
  const plan = []
  for (const segmentId of deck.segments) {
    const segment = await loadSegment(segmentId)
    for (const step of segment.steps) {
      const clauses = []
      // step.voiceSettings can be a single object (applies to every clause)
      // or an array (per-clause override, indexed like the split clauses).
      // Only affects the hash when present, so steps that don't use it keep
      // their existing cache untouched.
      const perClauseSettings = Array.isArray(step.voiceSettings)
      const clauseTexts = splitClauses(step.text)
      for (const [index, rawText] of clauseTexts.entries()) {
        const voiceSettings = perClauseSettings ? step.voiceSettings[index] : step.voiceSettings
        // Adjacent clause text, passed as previous_text/next_text so the
        // model doesn't apply sentence-final trailing-off prosody to a clip
        // that's only split off for pacing control, not a real sentence end.
        // Opt-in only (useClauseContext) so existing steps' cache is untouched.
        const previousText = step.useClauseContext ? clauseTexts[index - 1] ?? null : null
        const nextText = step.useClauseContext ? clauseTexts[index + 1] ?? null : null
        // With next_text carrying the continuation, the clause's own
        // trailing em-dash is redundant and was still cueing a pause in the
        // model — strip it so the clip itself doesn't trail off.
        const text =
          step.useClauseContext && nextText ? rawText.replace(/\s*—\s*$/, '').trim() : rawText
        const settingsSuffix =
          (voiceSettings ? JSON.stringify(voiceSettings) : '') +
          (previousText ? `|prev:${previousText}` : '') +
          (nextText ? `|next:${nextText}` : '') +
          (step.modelId ? `|model:${step.modelId}` : '')
        const hash = hashText(text + settingsSuffix)
        const base = `${step.clicks}-${index}-${hash}`
        const audioPath = path.join(AUDIO_DIR, segmentId, `${base}.mp3`)
        const alignmentPath = path.join(AUDIO_DIR, segmentId, `${base}.json`)
        clauses.push({
          index,
          text,
          hash,
          audioPath,
          alignmentPath,
          voiceSettings,
          previousText,
          nextText,
          modelId: step.modelId ?? null,
          cached: await fileExists(audioPath),
        })
      }
      plan.push({
        segmentId,
        clicks: step.clicks,
        key: `${segmentId}:${step.clicks}`,
        clausePausesMs: step.clausePausesMs ?? null,
        clauses,
      })
    }
  }
  return plan
}

function printPlan(plan) {
  let totalChars = 0
  let toGenerate = 0
  for (const step of plan) {
    for (const clause of step.clauses) {
      const status = clause.cached ? 'cached' : 'WOULD CALL API'
      console.log(`${step.key} [clause ${clause.index}] ${clause.text.length} chars — ${status}`)
      if (!clause.cached) {
        totalChars += clause.text.length
        toGenerate += 1
      }
    }
  }
  console.log(`\n${toGenerate} clause(s) would call the API, ${totalChars} characters total.`)
}

async function fetchTts(text, voiceId, apiKey, voiceSettings, previousText, nextText, modelId) {
  const body = { text, model_id: modelId || MODEL_ID }
  if (voiceSettings) body.voice_settings = voiceSettings
  // Tells the model this clip isn't the end of the sentence, so it doesn't
  // apply sentence-final trailing-off prosody — needed because we split one
  // continuous thought into separate clips to control per-clause pacing.
  if (previousText) body.previous_text = previousText
  if (nextText) body.next_text = nextText
  const res = await fetch(
    `https://api.elevenlabs.io/v1/text-to-speech/${voiceId}/with-timestamps`,
    {
      method: 'POST',
      headers: {
        'xi-api-key': apiKey,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
    }
  )
  if (!res.ok) {
    throw new Error(`ElevenLabs API error ${res.status}: ${await res.text()}`)
  }
  return res.json()
}

function durationMsFromAlignment(alignment) {
  const ends = alignment.character_end_times_seconds
  return Math.round(ends[ends.length - 1] * 1000)
}

async function runReal(plan) {
  const apiKey = process.env.ELEVENLABS_API_KEY
  const voiceId = process.env.ELEVENLABS_VOICE_ID
  if (!apiKey) throw new Error('ELEVENLABS_API_KEY is not set (run with --env-file=.env)')
  if (!voiceId) throw new Error('ELEVENLABS_VOICE_ID is not set (run with --env-file=.env)')

  const manifest = (await fileExists(MANIFEST_PATH))
    ? JSON.parse(await readFile(MANIFEST_PATH, 'utf8'))
    : {}

  let calls = 0
  let chars = 0
  for (const step of plan) {
    const clips = []
    for (const clause of step.clauses) {
      if (clause.cached) {
        console.log(`skip (cached): ${step.key} [clause ${clause.index}]`)
        const alignment = JSON.parse(await readFile(clause.alignmentPath, 'utf8'))
        clause.durationMs = durationMsFromAlignment(alignment)
      } else {
        console.log(`generating: ${step.key} [clause ${clause.index}] (${clause.text.length} chars)`)
        const result = await fetchTts(
          clause.text,
          voiceId,
          apiKey,
          clause.voiceSettings,
          clause.previousText,
          clause.nextText,
          clause.modelId
        )
        await mkdir(path.dirname(clause.audioPath), { recursive: true })
        await writeFile(clause.audioPath, Buffer.from(result.audio_base64, 'base64'))
        await writeFile(clause.alignmentPath, JSON.stringify(result.alignment, null, 2))
        clause.durationMs = durationMsFromAlignment(result.alignment)
        calls += 1
        chars += clause.text.length
      }
      clips.push({
        audioPath: relPath(clause.audioPath),
        alignmentPath: relPath(clause.alignmentPath),
        hash: clause.hash,
        durationMs: clause.durationMs,
      })
    }
    let durationMs = clips.reduce((sum, c) => sum + c.durationMs, 0)
    for (let i = 0; i < clips.length - 1; i++) {
      durationMs += step.clausePausesMs?.[i] ?? INTRA_PAUSE_MS
    }
    manifest[step.key] = { clips, durationMs }
  }

  await mkdir(AUDIO_DIR, { recursive: true })
  await writeFile(MANIFEST_PATH, JSON.stringify(manifest, null, 2))
  console.log(`\n${calls} API call(s) made, ${chars} characters sent.`)
}

function relPath(p) {
  return path.relative(ROOT, p)
}

async function main() {
  const args = process.argv.slice(2)
  const dryRun = args.includes('--dry-run')
  const deckPath = args.find((a) => !a.startsWith('--'))
  if (!deckPath) {
    console.error('Usage: node scripts/tts.mjs <deck-yaml> [--dry-run]')
    process.exit(1)
  }

  const deck = await loadDeck(deckPath)
  const plan = await buildPlan(deck)

  if (dryRun) {
    printPlan(plan)
  } else {
    await runReal(plan)
  }
}

main().catch((err) => {
  console.error(err.message)
  process.exit(1)
})
