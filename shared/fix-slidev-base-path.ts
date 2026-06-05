/**
 * Vite plugin to fix a Slidev bug where getSlidePath() prepends BASE_URL
 * to navigation paths, but Vue Router already adds the base — causing the
 * path to be doubled when using --base with a nested directory.
 *
 * See: @slidev/client/logic/slides.ts, line ~24
 * Upstream: https://github.com/slidevjs/slidev
 */
import type { Plugin } from 'vite'

export function fixSlidevBasePath(): Plugin {
  return {
    name: 'fix-slidev-base-path',
    transform(code, id) {
      if (id.includes('@slidev/client/logic/slides')) {
        return code.replace(
          '`${import.meta.env.BASE_URL}${path}`',
          '`/${path}`',
        )
      }
    },
  }
}
