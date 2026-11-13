<script setup>
import { configs } from '@slidev/client'

defineProps({
  heading: {
    type: String,
    default: '',
  },
  section: {
    type: String,
    default: '',
  },
})

const base = import.meta.env.BASE_URL
const logo = configs.themeConfig?.logo ?? 'molgenis-logo.png'
const sections = configs.themeConfig?.sections || ['Background', 'Methods', 'Results', 'Conclusions']
</script>

<template>
  <div class="slidev-layout chart-full">
    <div class="ch-header">
      <h1>{{ heading }}</h1>
    </div>
    <div class="ch-body">
      <slot />
    </div>
    <div class="logo-bar">
      <img :src="`${base}${logo}`" class="slide-logo" />
    </div>
    <div v-if="section" class="section-rail">
      <template v-for="(s, i) in sections" :key="s">
        <span :class="{ cur: s.toLowerCase() === section.toLowerCase() }">{{ s }}</span>
        <span v-if="i < sections.length - 1" class="sep">·</span>
      </template>
    </div>
  </div>
</template>

<style scoped>
.chart-full {
  display: flex;
  flex-direction: column;
  /* compact padding so the chart gets the vertical space */
  /* bottom padding clears the logo (~2.75rem) so content never overlaps it */
  padding: 2.5rem 3.5rem 3rem 3.5rem;
  height: 100%;
}

.ch-header {
  position: relative;
  padding-top: 0.5rem;
  margin-bottom: 0.75rem;
}

.ch-header::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 33%;
  height: var(--slidev-theme-header-bar, 3px);
  background-color: var(--slidev-theme-primary);
}

.ch-header h1 {
  font-family: var(--font-title);
  font-size: 40px;
  font-weight: 400;
  color: var(--slidev-theme-heading);
  margin: 0;
  line-height: 1.2;
}

.ch-body {
  flex: 1;
  min-height: 0;
}

.logo-bar {
  position: absolute;
  bottom: 0.75rem;
  right: 1.5rem;
}

.slide-logo {
  height: 32px;
  opacity: 0.8;
}

/* Same section rail as the content layout, aligned to this layout's left padding. */
.section-rail {
  position: absolute;
  bottom: 1.15rem;
  left: 3.5rem;
  display: flex;
  align-items: center;
  gap: 0.4rem;
  font-family: var(--font-subtitle);
  font-size: 12px;
  letter-spacing: 0.01em;
  color: #9aa4b0;
}
.section-rail .cur {
  color: var(--slidev-theme-primary);
  font-weight: 600;
}
.section-rail .sep {
  opacity: 0.5;
}
</style>
