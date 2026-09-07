import { chromium } from 'playwright-chromium'
const url = process.argv[2], clicks = parseInt(process.argv[3] || '0', 10), out = process.argv[4]
const b = await chromium.launch()
const p = await b.newPage({ viewport: { width: 1280, height: 720 } })
await p.goto(url, { waitUntil: 'networkidle' })
await p.waitForTimeout(1200)
for (let i = 0; i < clicks; i++) { await p.keyboard.press('ArrowRight'); await p.waitForTimeout(700) }
await p.waitForTimeout(800)
const text = await p.evaluate(() => document.body.innerText.slice(0, 600))
console.log('--- visible text ---\n' + text)
await p.screenshot({ path: out })
await b.close()
