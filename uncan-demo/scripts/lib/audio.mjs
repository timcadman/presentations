import { execFile } from 'node:child_process'
import { promisify } from 'node:util'
import path from 'node:path'
import { ROOT, PAUSE_MS, SETTLE_MS, INTRA_PAUSE_MS } from './deck.mjs'

const run = promisify(execFile)

function silenceInput(seconds) {
  return ['-f', 'lavfi', '-i', `anullsrc=r=44100:cl=mono:d=${seconds}`]
}

// The concat filter requires every input to share the exact same sample
// format, not just rate/channels — otherwise it produces audible artifacts
// (hiss/clicks) at the seams. Normalize each input with aformat first.
const NORMALIZE = 'aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=mono'

export async function buildNarrationTrack(ffmpeg, steps, manifest, outPath) {
  const args = ['-y']
  const inputIndexes = []

  args.push(...silenceInput(SETTLE_MS / 1000))
  inputIndexes.push(inputIndexes.length)

  steps.forEach((step, i) => {
    const entry = manifest[step.key]
    entry.clips.forEach((clip, clauseIndex) => {
      args.push('-i', path.resolve(ROOT, clip.audioPath))
      inputIndexes.push(inputIndexes.length)
      if (clauseIndex < entry.clips.length - 1) {
        const pauseMs = step.clausePausesMs?.[clauseIndex] ?? INTRA_PAUSE_MS
        if (pauseMs > 0) {
          args.push(...silenceInput(pauseMs / 1000))
          inputIndexes.push(inputIndexes.length)
        }
      }
    })
    if (i < steps.length - 1) {
      args.push(...silenceInput((step.pauseAfterMs ?? PAUSE_MS) / 1000))
      inputIndexes.push(inputIndexes.length)
    }
  })

  const normalized = inputIndexes.map((idx) => `[${idx}:a]${NORMALIZE}[n${idx}]`)
  const labels = inputIndexes.map((idx) => `[n${idx}]`)

  args.push(
    '-filter_complex',
    `${normalized.join(';')};${labels.join('')}concat=n=${labels.length}:v=0:a=1[out]`,
    '-map',
    '[out]',
    outPath
  )

  await run(ffmpeg, args)
}

export async function getDurationSeconds(ffmpeg, mediaPath) {
  try {
    await run(ffmpeg, ['-i', mediaPath])
  } catch (err) {
    // ffmpeg exits non-zero with no output path given — stderr still has
    // the "Duration: HH:MM:SS.ss" line we need.
    const match = err.stderr.match(/Duration: (\d+):(\d+):(\d+\.\d+)/)
    if (!match) throw new Error(`Could not read duration of ${mediaPath}`)
    const [, hh, mm, ss] = match
    return Number(hh) * 3600 + Number(mm) * 60 + Number(ss)
  }
  throw new Error(`Expected ffmpeg to fail with no output path for ${mediaPath}`)
}

// If the video is shorter than the narration it's about to be muxed with,
// hold its last frame for the deficit rather than letting -shortest (or a
// player's undefined end-of-stream behaviour) truncate the audio.
export async function padVideoToMatch(ffmpeg, videoPath, targetSeconds, outPath) {
  const videoSeconds = await getDurationSeconds(ffmpeg, videoPath)
  const deficit = targetSeconds - videoSeconds
  if (deficit <= 0) return videoPath

  const lastFramePath = `${outPath}.last-frame.png`
  await run(ffmpeg, ['-y', '-sseof', '-0.1', '-i', videoPath, '-vframes', '1', lastFramePath])
  const holdPath = `${outPath}.hold.mp4`
  await run(ffmpeg, [
    '-y',
    '-loop',
    '1',
    '-i',
    lastFramePath,
    '-t',
    String(deficit),
    '-r',
    '60',
    '-vf',
    'format=yuv420p',
    '-c:v',
    'libx264',
    '-preset',
    'fast',
    '-crf',
    '18',
    holdPath,
  ])
  await run(ffmpeg, [
    '-y',
    '-i',
    videoPath,
    '-i',
    holdPath,
    '-filter_complex',
    '[0:v][1:v]concat=n=2:v=1:a=0[outv]',
    '-map',
    '[outv]',
    '-c:v',
    'libx264',
    '-preset',
    'fast',
    '-crf',
    '18',
    outPath,
  ])
  return outPath
}

export async function muxVideo(ffmpeg, videoPath, narrationPath, outPath) {
  await run(ffmpeg, [
    '-y',
    '-i',
    videoPath,
    '-i',
    narrationPath,
    // explicit stream mapping: without this, ffmpeg's default stream
    // selection can pick the source video's own audio track (if it has
    // one, e.g. a real screen recording) instead of the narration.
    '-map',
    '0:v:0',
    '-map',
    '1:a:0',
    '-c:v',
    'libx264',
    '-c:a',
    'aac',
    // no -shortest: audio must never be truncated (cuts off speech). If the
    // video is shorter than the narration, it should be padded to match
    // before calling this (see stitch.mjs's video/narration length check).
    outPath,
  ])
}
