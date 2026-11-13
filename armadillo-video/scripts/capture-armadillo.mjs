import { chromium } from 'playwright-chromium'
import { mkdir } from 'node:fs/promises'
import path from 'node:path'
import { ROOT, PAUSE_MS, SETTLE_MS, loadDeck, loadManifest, loadSegment, buildSteps } from '../../voiceover/lib/deck.mjs'

// Selectors follow the Armadillo v5.12.2 UI (ui/src/views/*.vue in molgenis-service-armadillo).
const BASE_URL = process.env.ARMADILLO_URL || 'http://localhost:8080'
const USER = process.env.ARMADILLO_USER || 'admin'
const PASSWORD = process.env.ARMADILLO_PASSWORD || 'admin'
const PROJECT = 'project-1'
const FOLDER = 'data'
const DATA_FILE = path.join(ROOT, 'data', 'core.csv')
const PROFILE = 'default'
const TYPING_DELAY_MS = 90
// Rough speaking rate (~15 characters a second) for --rehearse, which checks
// the clicks before any narration audio exists.
const REHEARSAL_MS_PER_CHAR = 65

function wait(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms))
}

async function callApi(method, apiPath, body) {
  const res = await fetch(`${BASE_URL}${apiPath}`, {
    method,
    headers: {
      Authorization: `Basic ${Buffer.from(`${USER}:${PASSWORD}`).toString('base64')}`,
      'Content-Type': 'application/json',
    },
    body: body ? JSON.stringify(body) : undefined,
  })
  if (!res.ok) throw new Error(`${method} ${apiPath} failed: ${res.status} ${await res.text()}`)
  return res
}

async function projectExists() {
  const projects = await (await callApi('GET', '/access/projects')).json()
  return projects.some((p) => p.name === PROJECT)
}

// Deleting the demo project only happens with --reset, so a re-run never
// removes it silently.
async function removeDemoProject(reset) {
  if (!(await projectExists())) return
  if (!reset) throw new Error(`project "${PROJECT}" already exists; re-run with --reset to delete and recreate it`)
  await callApi('DELETE', `/access/projects/${PROJECT}`)
}

// Each video must start from the state its narration describes.
async function prepareServer(deckName, reset) {
  if (deckName === 'armadillo-create-project') await removeDemoProject(reset)
  if (deckName === 'armadillo-upload-data') {
    await removeDemoProject(reset)
    await callApi('PUT', '/access/projects', { name: PROJECT, users: [] })
  }
  if (deckName === 'armadillo-start-container') await callApi('POST', `/ds-profiles/${PROFILE}/stop`)
}

async function saveLoginState(browser) {
  const context = await browser.newContext()
  const page = await context.newPage()
  await page.goto(`${BASE_URL}/`, { waitUntil: 'networkidle' })
  const localLogin = page.getByRole('button', { name: /Local account/ })
  await localLogin.click()
  await page.getByPlaceholder('Username').fill(USER)
  await page.getByPlaceholder('Password').fill(PASSWORD)
  await page.getByRole('button', { name: /Log in/ }).click()
  await localLogin.waitFor({ state: 'detached' })
  const state = await context.storageState()
  await context.close()
  return state
}

async function typeSlowly(locator, text) {
  await locator.click()
  await locator.pressSequentially(text, { delay: TYPING_DELAY_MS })
}

function profileRow(page) {
  return page.locator('tr', { hasText: PROFILE }).filter({ has: page.getByRole('button', { name: /Start|Stop/ }) })
}

// Page each video opens on, and the UI actions performed at the start of
// each narration step, keyed by `segment:clicks`.
const SCENES = {
  'armadillo-create-project': {
    startPath: '/#/projects',
    actions: {
      'armadillo-create-project:1': async (page) => {
        await page.locator('button:has(i.bi-plus-lg)').click()
        await typeSlowly(page.locator('tr.table-info textarea').first(), PROJECT)
      },
      'armadillo-create-project:2': async (page) => {
        await page.locator('tr.table-info th button').first().click()
        await page.getByText(PROJECT, { exact: true }).first().waitFor()
      },
    },
  },
  'armadillo-upload-data': {
    startPath: '/#/projects',
    actions: {
      'armadillo-upload-data:0': async (page) => {
        await page.locator(`a[href="#/projects-explorer/${PROJECT}"]`).click()
        await page.locator('button:has(i.bi-folder-plus)').click()
        await typeSlowly(page.getByPlaceholder('Folder name'), FOLDER)
        await page.locator('button:has(i.bi-check-lg)').click()
      },
      'armadillo-upload-data:1': async (page) => {
        await page.locator('.list-group-item', { hasText: FOLDER }).first().click()
        await page.locator('.project-file-upload input[type="file"]').setInputFiles(DATA_FILE)
        await page.getByRole('button', { name: /Upload/ }).click()
        await page.locator('.list-group-item', { hasText: 'core' }).first().waitFor()
      },
      'armadillo-upload-data:2': async (page) => {
        await page.locator('.list-group-item', { hasText: 'core' }).first().click()
      },
    },
  },
  'armadillo-start-container': {
    startPath: '/#/projects',
    actions: {
      'armadillo-start-container:1': async (page) => {
        await page.getByText('Profiles', { exact: true }).first().click()
        await profileRow(page).getByRole('button', { name: /Start/ }).click()
      },
      'armadillo-start-container:2': async (page) => {
        await profileRow(page).getByRole('button', { name: /Stop/ }).waitFor({ timeout: 120000 })
      },
    },
  },
}

// Step i must begin exactly when its narration does in the track stitch.mjs
// builds: SETTLE_MS of silence, then each clip followed by its pause. An action
// that runs long pushes later steps off cue, so it is reported, not hidden.
async function playSteps(page, steps, manifest, scene, startedAt) {
  let offsetMs = SETTLE_MS
  for (const step of steps) {
    const entry = manifest[step.key]
    if (!entry) throw new Error(`No generated audio for ${step.key} — run ../voiceover/tts.mjs first`)
    const lateMs = Date.now() - startedAt - offsetMs
    if (lateMs > 0) console.warn(`${step.key}: started ${lateMs}ms late — previous action overran its narration`)
    else await wait(-lateMs)
    console.log(`${step.key}: ${entry.durationMs}ms narration`)
    await scene.actions[step.key]?.(page)
    offsetMs += entry.durationMs + (step.pauseAfterMs ?? PAUSE_MS)
  }
  const remainingMs = startedAt + offsetMs - Date.now()
  if (remainingMs > 0) await wait(remainingMs)
}

async function estimateDurations(steps) {
  const manifest = {}
  for (const step of steps) {
    const segment = await loadSegment(step.segmentId)
    const text = segment.steps.find((s) => s.clicks === step.clicks).text
    manifest[step.key] = { durationMs: text.length * REHEARSAL_MS_PER_CHAR }
  }
  return manifest
}

async function recordScene(browser, loginState, deckName, steps, manifest) {
  const outDir = path.join(ROOT, 'recordings', deckName)
  await mkdir(outDir, { recursive: true })
  const context = await browser.newContext({
    storageState: loginState,
    viewport: { width: 1280, height: 720 },
    recordVideo: { dir: outDir, size: { width: 1280, height: 720 } },
  })
  const page = await context.newPage()
  const startedAt = Date.now()
  await page.goto(`${BASE_URL}${SCENES[deckName].startPath}`, { waitUntil: 'networkidle' })
  await playSteps(page, steps, manifest, SCENES[deckName], startedAt)
  const video = page.video()
  await context.close()
  return video.path()
}

async function main() {
  const deckPath = process.argv[2]
  const reset = process.argv.includes('--reset')
  const rehearse = process.argv.includes('--rehearse')
  const deckName = deckPath && path.basename(deckPath, '.yml')
  if (!SCENES[deckName]) {
    console.error(
      `Usage: node scripts/capture-armadillo.mjs decks/<${Object.keys(SCENES).join('|')}>.yml [--reset] [--rehearse]`
    )
    process.exit(1)
  }
  const steps = await buildSteps(await loadDeck(deckPath))
  const manifest = rehearse ? await estimateDurations(steps) : await loadManifest()
  await prepareServer(deckName, reset)

  const browser = await chromium.launch()
  try {
    const loginState = await saveLoginState(browser)
    console.log(`recorded: ${await recordScene(browser, loginState, deckName, steps, manifest)}`)
  } finally {
    await browser.close()
  }
}

main().catch((err) => {
  console.error(err.message)
  process.exit(1)
})
