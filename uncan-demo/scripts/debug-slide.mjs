import { chromium } from 'playwright-chromium'
import { execFile } from 'node:child_process'
import { promisify } from 'node:util'
import path from 'node:path'
import { ROOT } from './lib/deck.mjs'
import { startStaticServer } from './lib/static-server.mjs'

const run = promisify(execFile)
const PORT = 3998

function wait(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms))
}

async function main() {
  const deckSlides = process.argv[2]
  const clicks = Number(process.argv[3] || 0)
  if (!deckSlides) {
    console.error('Usage: node scripts/debug-slide.mjs <slides.md> [clicks-to-press]')
    process.exit(1)
  }

  const buildDir = path.join(ROOT, '.build-cache', 'debug')
  console.log('building...')
  await run(path.join(ROOT, 'node_modules/.bin/slidev'), ['build', deckSlides, '--out', buildDir], {
    cwd: ROOT,
  })

  const server = await startStaticServer(buildDir, PORT)
  try {
    const browser = await chromium.launch()
    const page = await browser.newPage({ viewport: { width: 1280, height: 720 } })
    page.on('console', (msg) => console.log(`[console.${msg.type()}] ${msg.text()}`))
    page.on('pageerror', (err) => console.log(`[pageerror] ${err.message}`))
    page.on('requestfailed', (req) => console.log(`[requestfailed] ${req.url()} — ${req.failure()?.errorText}`))
    page.on('response', (res) => {
      if (!res.ok()) console.log(`[response ${res.status()}] ${res.url()}`)
    })

    await page.goto(`http://localhost:${PORT}/1`, { waitUntil: 'networkidle' })
    await wait(1000)

    for (let i = 0; i < clicks; i++) {
      await page.keyboard.press('ArrowRight')
      await wait(500)
    }
    await wait(1500)

    const bodyLength = await page.evaluate(() => document.body.innerHTML.length)
    console.log(`body innerHTML length: ${bodyLength}`)
    const stylesheets = await page.evaluate(() =>
      [...document.styleSheets].map((s) => ({ href: s.href, rules: (() => { try { return s.cssRules.length } catch { return 'blocked' } })() }))
    )
    console.log('stylesheets:', JSON.stringify(stylesheets))
    const bodySnippet = await page.evaluate(() => document.body.innerHTML.slice(0, 1500))
    console.log('body snippet:', bodySnippet)

    const outPath = path.join(ROOT, '.build-cache', process.argv[4] || 'debug-screenshot.png')
    await page.screenshot({ path: outPath })
    console.log(`screenshot: ${outPath}`)

    await browser.close()
  } finally {
    server.close()
  }
}

main().catch((err) => {
  console.error(err.message)
  process.exit(1)
})
