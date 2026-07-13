<script setup>
import { configs } from '@slidev/client'

defineProps({
  heading: {
    type: String,
    default: '',
  },
  subheading: {
    type: String,
    default: '',
  },
  section: {
    type: String,
    default: '',
  },
})

const base = import.meta.env.BASE_URL
const sections = configs.themeConfig?.sections || ['Background', 'Methods', 'Results', 'Conclusions']
</script>

<template>
  <div class="slidev-layout content-layout">
    <div v-if="heading || subheading" class="slide-header">
      <h1 v-if="heading">{{ heading }}</h1>
      <h2 v-if="subheading">{{ subheading }}</h2>
    </div>
    <div class="slide-body">
      <slot />
    </div>
    <div class="logo-bar">
      <img :src="`${base}molgenis-logo.png`" class="slide-logo" />
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
.content-layout {
  display: flex;
  flex-direction: column;
  /* bottom padding clears the logo (~3.25rem) so content never overlaps it */
  padding: 4.5rem 5rem 3.75rem 5rem;
  height: 100%;
}

/* Hard lower boundary: the body may shrink but never spill past the padding
   into the logo. Content that would exceed it is clipped, not laid over the logo. */
.slide-body {
  min-height: 0;
  overflow: hidden;
}

.slide-header {
  min-height: 7.25rem;
  margin-bottom: 1.5rem;
  padding-top: 0.75rem;
  position: relative;
}

.slide-header::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 33%;
  height: 3px;
  background-color: var(--slidev-theme-primary);
}

.slide-header h1 {
  font-family: var(--font-title);
  font-size: 55px;
  font-weight: 400;
  color: var(--slidev-theme-primary);
  margin: 0;
  line-height: 1.2;
}

.slide-header h2 {
  font-family: var(--font-subtitle);
  font-size: 25px;
  font-weight: 400;
  color: var(--slidev-theme-primary);
  margin: 0.25rem 0 0 0;
}

.slide-body {
  flex: 1;
}

.slide-body :deep(ul) {
  padding-left: 1.5rem;
}

.slide-body :deep(li) {
  font-size: 18px;
  margin-bottom: 0.5rem;
  line-height: 1.5;
}

.logo-bar {
  position: absolute;
  bottom: 1rem;
  right: 1.5rem;
}

.slide-logo {
  height: 36px;
  opacity: 0.8;
}

/* Section progress rail, bottom-left (logo stays bottom-right). Uses the deck's
   IBM Plex Mono subtitle face; current section in molgenis blue, rest in grey. */
.section-rail {
  position: absolute;
  bottom: 1.4rem;
  left: 5rem;
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
