import { defineConfig } from 'vite'
import { fixSlidevBasePath } from '../shared/fix-slidev-base-path'

export default defineConfig({
  assetsInclude: ['**/*.mov'],
  plugins: [fixSlidevBasePath()],
})
