import path from 'node:path'
import { ROOT, loadDeck, loadManifest, buildSteps } from './lib/deck.mjs'
import { resolveFfmpegPath } from './lib/ffmpeg.mjs'
import { buildNarrationTrack, muxVideo, getDurationSeconds, padVideoToMatch } from './lib/audio.mjs'

async function main() {
  const deckPath = process.argv[2]
  const videoPath = process.argv[3]
  if (!deckPath || !videoPath) {
    console.error('Usage: node scripts/stitch.mjs <deck-yaml> <recorded-video>')
    process.exit(1)
  }

  const deck = await loadDeck(deckPath)
  const manifest = await loadManifest()
  const steps = await buildSteps(deck)
  const ffmpeg = await resolveFfmpegPath()

  const outDir = path.dirname(path.resolve(ROOT, videoPath))
  const narrationPath = path.join(outDir, 'narration.wav')
  const finalPath = path.join(outDir, 'final.mp4')

  console.log('building narration track...')
  await buildNarrationTrack(ffmpeg, steps, manifest, narrationPath)

  const narrationSeconds = await getDurationSeconds(ffmpeg, narrationPath)
  const paddedPath = path.join(outDir, 'video-padded.mp4')
  const videoForMux = await padVideoToMatch(
    ffmpeg,
    path.resolve(ROOT, videoPath),
    narrationSeconds,
    paddedPath
  )
  if (videoForMux === paddedPath) {
    console.log(`video was shorter than narration — held last frame to match (${narrationSeconds.toFixed(2)}s)`)
  }

  console.log('muxing onto video...')
  await muxVideo(ffmpeg, videoForMux, narrationPath, finalPath)

  console.log(`done: ${finalPath}`)
}

main().catch((err) => {
  console.error(err.message)
  process.exit(1)
})
