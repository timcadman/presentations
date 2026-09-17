import { execFile } from 'node:child_process'
import { promisify } from 'node:util'
import { mkdir } from 'node:fs/promises'
import path from 'node:path'
import { ROOT, loadDeck } from './lib/deck.mjs'
import { resolveFfmpegPath } from './lib/ffmpeg.mjs'

const run = promisify(execFile)

// Every part is scaled/padded (letterboxed, never stretched) to this common
// size before concatenation — the individual recordings have genuinely
// different resolutions (real screen captures vs. the Slidev viewport).
const WIDTH = 1920
const HEIGHT = 1080
const FPS = 30

async function main() {
  const manifestPath = process.argv[2] || 'decks/full-demo.yml'
  const manifest = await loadDeck(manifestPath)

  // Each part is either a plain segment id, or {id, pauseBeforeMs} — the
  // pause is applied by holding the PRECEDING part's last frame/silence,
  // so a part's own final.mp4 stays untouched and reusable on its own.
  const parts = manifest.parts.map((part) => (typeof part === 'string' ? { id: part } : part))
  const ffmpeg = await resolveFfmpegPath()
  const inputs = parts.map((part) => path.join(ROOT, 'recordings', part.id, 'final.mp4'))

  const args = ['-y']
  for (const input of inputs) args.push('-i', input)

  const videoLabels = []
  const audioLabels = []
  const filters = []
  inputs.forEach((_, i) => {
    const holdSeconds = (parts[i + 1]?.pauseBeforeMs ?? 0) / 1000
    const tpad = holdSeconds > 0 ? `,tpad=stop_mode=clone:stop_duration=${holdSeconds}` : ''
    const apad = holdSeconds > 0 ? `,apad=pad_dur=${holdSeconds}` : ''
    filters.push(
      `[${i}:v]scale=${WIDTH}:${HEIGHT}:force_original_aspect_ratio=decrease,` +
        `pad=${WIDTH}:${HEIGHT}:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=${FPS}${tpad}[v${i}]`
    )
    filters.push(`[${i}:a]aresample=44100,aformat=sample_fmts=fltp:channel_layouts=mono${apad}[a${i}]`)
    videoLabels.push(`[v${i}]`)
    audioLabels.push(`[a${i}]`)
  })

  const concatInputs = inputs.map((_, i) => `${videoLabels[i]}${audioLabels[i]}`).join('')
  filters.push(`${concatInputs}concat=n=${inputs.length}:v=1:a=1[outv][outa]`)

  const outDir = path.join(ROOT, 'recordings', 'full-demo')
  await mkdir(outDir, { recursive: true })
  const outPath = path.join(outDir, 'final.mp4')

  args.push(
    '-filter_complex',
    filters.join(';'),
    '-map',
    '[outv]',
    '-map',
    '[outa]',
    '-c:v',
    'libx264',
    '-preset',
    'fast',
    '-crf',
    '18',
    '-c:a',
    'aac',
    outPath
  )

  console.log(`assembling ${parts.length} parts...`)
  parts.forEach((part) => console.log(`  - ${part.id}${part.pauseBeforeMs ? ` (+${part.pauseBeforeMs}ms pause before)` : ''}`))
  await run(ffmpeg, args, { maxBuffer: 1024 * 1024 * 64 })

  console.log(`done: ${outPath}`)
}

main().catch((err) => {
  console.error(err.message)
  process.exit(1)
})
