import path from 'node:path'
import { mkdir, writeFile } from 'node:fs/promises'
import { ROOT, PAUSE_MS, SETTLE_MS, loadDeck, loadManifest, buildSteps, loadSegment } from './lib/deck.mjs'
import { resolveFfmpegPath } from './lib/ffmpeg.mjs'
import { buildNarrationTrack } from './lib/audio.mjs'

async function main() {
  const deckPath = process.argv[2]
  if (!deckPath) {
    console.error('Usage: node scripts/narrate.mjs <deck-yaml>')
    process.exit(1)
  }

  const deck = await loadDeck(deckPath)
  const manifest = await loadManifest()
  const steps = await buildSteps(deck)
  const ffmpeg = await resolveFfmpegPath()

  const outDir = path.join(ROOT, 'recordings', path.basename(deckPath, '.yml'))
  await mkdir(outDir, { recursive: true })
  const narrationPath = path.join(outDir, 'narration.wav')

  console.log('building narration track...')
  await buildNarrationTrack(ffmpeg, steps, manifest, narrationPath)
  console.log(`narration track: ${narrationPath}\n`)

  const segmentTexts = {}
  for (const segmentId of deck.segments) {
    const segment = await loadSegment(segmentId)
    segmentTexts[segmentId] = Object.fromEntries(segment.steps.map((s) => [s.clicks, s.text]))
  }

  const lines = ['Cue sheet — when each step starts, and the text spoken over it:', '']
  let t = SETTLE_MS
  steps.forEach((step) => {
    const entry = manifest[step.key]
    const mm = Math.floor(t / 60000)
    const ss = ((t % 60000) / 1000).toFixed(1).padStart(4, '0')
    lines.push(`[${mm}:${ss}] (${step.key}) ${segmentTexts[step.segmentId][step.clicks]}`)
    t += entry.durationMs + (step.pauseAfterMs ?? PAUSE_MS)
  })

  const cueSheetPath = path.join(outDir, 'cue-sheet.txt')
  await writeFile(cueSheetPath, lines.join('\n') + '\n')
  console.log(lines.join('\n'))
  console.log(`\ncue sheet: ${cueSheetPath}`)
}

main().catch((err) => {
  console.error(err.message)
  process.exit(1)
})
