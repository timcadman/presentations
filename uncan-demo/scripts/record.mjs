import { chromium } from 'playwright-chromium'
import { execFile } from 'node:child_process'
import { promisify } from 'node:util'
import { mkdir } from 'node:fs/promises'
import path from 'node:path'
import { ROOT, PAUSE_MS, SETTLE_MS, loadDeck, loadManifest, buildSteps } from './lib/deck.mjs'
import { startStaticServer } from './lib/static-server.mjs'

const run = promisify(execFile)
const PORT = 3999

function wait(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms))
}

async function main() {
  const deckPath = process.argv[2]
  if (!deckPath) {
    console.error('Usage: node scripts/record.mjs <deck-yaml>')
    process.exit(1)
  }

  const deck = await loadDeck(deckPath)
  const manifest = await loadManifest()
  const steps = await buildSteps(deck)

  const outDir = path.join(ROOT, 'recordings', path.basename(deckPath, '.yml'))
  const buildDir = path.join(ROOT, '.build-cache', path.basename(deckPath, '.yml'))
  await mkdir(outDir, { recursive: true })

  console.log('building static deck (no dev-server file watcher, avoids sandbox EMFILE)...')
  await run(path.join(ROOT, 'node_modules/.bin/slidev'), ['build', deck.slides, '--out', buildDir], {
    cwd: ROOT,
  })

  const server = await startStaticServer(buildDir, PORT)

  try {
    const browser = await chromium.launch()
    const context = await browser.newContext({
      viewport: { width: 1280, height: 720 },
      recordVideo: { dir: outDir, size: { width: 1280, height: 720 } },
    })
    const page = await context.newPage()
    await page.goto(`http://localhost:${PORT}/1`, { waitUntil: 'networkidle' })
    await wait(SETTLE_MS)

    let prevSegmentId = null
    let prevClicks = -1
    for (let i = 0; i < steps.length; i++) {
      const step = steps[i]
      // Crossing into a new slide always lands on ITS click 0, not on the
      // click value of the first step we're about to narrate — so that
      // crossing costs one press, plus one more per click to reach it.
      // Within the same slide, it's just the gap since the last click shown.
      const sameSegment = step.segmentId === prevSegmentId
      const presses = i === 0 ? 0 : sameSegment ? step.clicks - prevClicks : step.clicks + 1
      for (let p = 0; p < presses; p++) await page.keyboard.press('ArrowRight')
      prevSegmentId = step.segmentId
      prevClicks = step.clicks

      const entry = manifest[step.key]
      if (!entry) throw new Error(`No generated audio for ${step.key} — run scripts/tts.mjs first`)

      const pause = step.pauseAfterMs ?? PAUSE_MS
      console.log(`${step.key}: waiting ${entry.durationMs}ms + ${pause}ms pause`)
      await wait(entry.durationMs + pause)
    }

    const video = page.video()
    await context.close()
    await browser.close()

    console.log(`recorded: ${await video.path()}`)
  } finally {
    server.close()
  }
}

main().catch((err) => {
  console.error(err.message)
  process.exit(1)
})
