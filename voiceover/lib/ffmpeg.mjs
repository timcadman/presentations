// playwright-chromium bundles its own ffmpeg, but it's a stripped-down
// build for screencast encoding only (no mp3 decode, no filters) — use the
// full ffmpeg-static build instead for audio concat/mux.
export async function resolveFfmpegPath() {
  const { default: ffmpegPath } = await import('ffmpeg-static')
  return ffmpegPath
}
