<script setup>
import { computed } from 'vue'
import { configs } from '@slidev/client'

const props = defineProps({
  heading: {
    type: String,
    default: 'Contents',
  },
  subheading: {
    type: String,
    default: '',
  },
  section: {
    type: String,
    default: '',
  },
  // full-bleed image down the right edge; omit for a plain contents list
  image: {
    type: String,
    default: '',
  },
  // its width as a % of the slide — 40 is the deck standard (see .bleed-right)
  imageWidth: {
    type: String,
    default: '40',
  },
})

const base = import.meta.env.BASE_URL
const logo = configs.themeConfig?.logo ?? 'molgenis-logo.png'
const sections = configs.themeConfig?.sections || ['Background', 'Methods', 'Results', 'Conclusions']
const resolvedImage = computed(() => {
  if (!props.image) return ''
  return `${base}${props.image.replace(/^\.\/public\//, '')}`
})
</script>

<template>
  <div class="slidev-layout contents-layout">
    <div class="slide-header">
      <h1>{{ heading }}</h1>
      <h2 v-if="subheading">{{ subheading }}</h2>
    </div>
    <div class="slide-body"><slot /></div>
    <img v-if="image" :src="resolvedImage" class="contents-image" :style="{ width: imageWidth + '%' }" />
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
.contents-layout {
  display: flex;
  flex-direction: column;
  /* bottom padding clears the logo (~3.25rem) so content never overlaps it */
  padding: 4.5rem 5rem 3.75rem 5rem;
  height: 100%;
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
  height: var(--slidev-theme-header-bar, 3px);
  background-color: var(--slidev-theme-primary);
}

.slide-header h1 {
  font-family: var(--font-title);
  font-size: 44px;
  font-weight: 400;
  color: var(--slidev-theme-heading);
  margin: 0;
  line-height: 1.2;
}

.slide-header h2 {
  font-family: var(--font-subtitle);
  font-size: 25px;
  font-weight: 400;
  color: var(--slidev-theme-heading);
  margin: 0.25rem 0 0 0;
}

.slide-body {
  flex: 1;
  min-height: 0;
  padding-right: 3rem;
}

.contents-image {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  height: 100%;
  object-fit: cover;
}

.slide-body :deep(ul),
.slide-body :deep(ol) {
  padding-left: 1.5rem;
  margin: 0;
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
