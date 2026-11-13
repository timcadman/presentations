import { chromium } from 'playwright-chromium'
import path from 'node:path'
import { ROOT } from './lib/deck.mjs'

function wait(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms))
}

async function describePage(page, label) {
  await wait(1500)
  const outPath = path.join(ROOT, '.build-cache', `armadillo-${label}.png`)
  await page.screenshot({ path: outPath })

  const summary = await page.evaluate(() => {
    const text = (el) => el.textContent.trim().replace(/\s+/g, ' ').slice(0, 60)
    return {
      url: location.href,
      title: document.title,
      buttons: [...document.querySelectorAll('button')].map(text).filter(Boolean),
      links: [...document.querySelectorAll('a')].map((a) => `${text(a)} -> ${a.getAttribute('href')}`),
      inputs: [...document.querySelectorAll('input')].map(
        (i) => `${i.type} name=${i.name} placeholder=${i.placeholder} id=${i.id}`
      ),
      headings: [...document.querySelectorAll('h1,h2,h3')].map(text).filter(Boolean),
    }
  })

  console.log(`\n=== ${label} ===`)
  console.log(JSON.stringify(summary, null, 2))
  console.log(`screenshot: ${outPath}`)
}

async function main() {
  const browser = await chromium.launch()
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 } })
  page.on('console', (msg) => {
    if (msg.type() === 'error') console.log(`[console.error] ${msg.text()}`)
  })

  await page.goto('http://localhost:8081/', { waitUntil: 'networkidle' })
  await describePage(page, '01-landing')

  await browser.close()
}

main().catch((err) => {
  console.error(err.message)
  process.exit(1)
})
