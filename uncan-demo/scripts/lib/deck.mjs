import { readFile } from 'node:fs/promises'
import path from 'node:path'
import { parse } from 'yaml'

export const ROOT = path.resolve(import.meta.dirname, '../..')
export const AUDIO_DIR = path.join(ROOT, 'narration/audio')
export const MANIFEST_PATH = path.join(AUDIO_DIR, 'manifest.json')

export const SETTLE_MS = 1000
export const PAUSE_MS = 600
export const INTRA_PAUSE_MS = 500

// Splits a step's narration into clauses at sentence-ending punctuation
// (full stops, question marks, em dashes). Each clause is generated as its
// own natural TTS clip and joined with real silence — tried ElevenLabs'
// <break> SSML tag first, but it visibly changes the model's prosody
// around the tag, which reads as less natural than genuine clip + silence.
export function splitClauses(text) {
  return text
    .split(/(?<=[.?—])\s+/)
    .map((s) => s.trim())
    .filter(Boolean)
}

export async function loadDeck(deckPath) {
  const raw = await readFile(path.resolve(ROOT, deckPath), 'utf8')
  return parse(raw)
}

export async function loadSegment(id) {
  const raw = await readFile(path.join(ROOT, 'narration/segments', `${id}.yml`), 'utf8')
  return parse(raw)
}

export async function loadManifest() {
  const raw = await readFile(MANIFEST_PATH, 'utf8')
  return JSON.parse(raw)
}

// Ordered list of every fragment-advance across the whole deck. The first
// step is shown on page load with no key press; every step after it is
// reached by exactly one ArrowRight, whether that advances a fragment on
// the same slide or moves to the next slide entirely.
export async function buildSteps(deck) {
  const steps = []
  for (const segmentId of deck.segments) {
    const segment = await loadSegment(segmentId)
    for (const step of segment.steps) {
      steps.push({
        segmentId,
        clicks: step.clicks,
        key: `${segmentId}:${step.clicks}`,
        pauseAfterMs: step.pauseAfterMs ?? null,
        clausePausesMs: step.clausePausesMs ?? null,
      })
    }
  }
  return steps
}
