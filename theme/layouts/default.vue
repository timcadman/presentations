<script setup>
import { configs } from '@slidev/client'

const base = import.meta.env.BASE_URL
const logo = configs.themeConfig?.logo ?? 'molgenis-logo.png'
</script>

<template>
  <div class="slidev-layout default">
    <div class="default-content">
      <slot />
    </div>
    <div class="logo-bar">
      <img :src="`${base}${logo}`" class="slide-logo" />
    </div>
  </div>
</template>

<style scoped>
.default {
  padding: 2.5rem 3rem;
  display: flex;
  flex-direction: column;
  height: 100%;
}

.default-content {
  flex: 1;
}

.logo-bar {
  display: flex;
  justify-content: flex-end;
  align-items: flex-end;
}

.slide-logo {
  height: 28px;
  opacity: 0.8;
}
</style>
