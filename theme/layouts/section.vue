<script setup>
import { configs } from '@slidev/client'

const base = import.meta.env.BASE_URL
const logoOnDark = configs.themeConfig?.logoOnDark
</script>

<template>
  <div class="slidev-layout section">
    <div class="section-content">
      <slot />
    </div>
    <div v-if="logoOnDark" class="logo-bar">
      <img :src="`${base}${logoOnDark}`" class="slide-logo" />
    </div>
  </div>
</template>

<style scoped>
.section {
  background-color: var(--slidev-theme-section-bg);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 4rem 5rem;
  height: 100%;
  position: relative;
}

.logo-bar {
  position: absolute;
  bottom: 1.4rem;
  right: 1.5rem;
}

.slide-logo {
  height: 32px;
  opacity: 0.9;
}

.section-content {
  text-align: center;
  width: 100%;
}

.section :deep(h1) {
  font-family: var(--font-title);
  font-size: 55px;
  font-weight: 400;
  color: var(--slidev-theme-section-fg);
  margin-bottom: 0.5rem;
  line-height: 1.2;
}

.section :deep(p) {
  font-family: var(--font-subtitle);
  font-size: 25px;
  color: var(--slidev-theme-section-fg);
  font-weight: 400;
}
</style>
