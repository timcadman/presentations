import { createServer } from 'node:http'
import { readFile, stat } from 'node:fs/promises'
import path from 'node:path'

const MIME = {
  '.html': 'text/html',
  '.js': 'text/javascript',
  '.mjs': 'text/javascript',
  '.css': 'text/css',
  '.json': 'application/json',
  '.svg': 'image/svg+xml',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.mov': 'video/quicktime',
  '.mp4': 'video/mp4',
  '.woff2': 'font/woff2',
}

// Serves a Slidev static build with SPA fallback — no file watching, so it
// avoids the EMFILE crash the `slidev` dev server hits under this sandbox.
export async function startStaticServer(rootDir, port) {
  const server = createServer(async (req, res) => {
    const urlPath = decodeURIComponent(req.url.split('?')[0])
    let filePath = path.join(rootDir, urlPath)

    const isFile = await stat(filePath).then((s) => s.isFile()).catch(() => false)
    if (!isFile) filePath = path.join(rootDir, 'index.html')

    try {
      const body = await readFile(filePath)
      res.writeHead(200, { 'Content-Type': MIME[path.extname(filePath)] || 'application/octet-stream' })
      res.end(body)
    } catch {
      res.writeHead(404)
      res.end('not found')
    }
  })

  await new Promise((resolve) => server.listen(port, resolve))
  return server
}
