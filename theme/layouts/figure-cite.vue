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
  // Source of the figure, rendered small and grey beneath it. Citation only —
  // no article title and no methods note, so it reads the same on every slide.
  citation: {
    type: String,
    default: '',
  },
  // width of the text column as a % of the body; the figure takes the rest.
  // Reserved on every slide, so the figure box is identical with or without text.
  sideWidth: {
    type: String,
    default: '34',
  },
})

const base = import.meta.env.BASE_URL
const logo = configs.themeConfig?.logo ?? 'molgenis-logo.png'
const sections = configs.themeConfig?.sections || ['Background', 'Methods', 'Results', 'Conclusions']
</script>

<template>
  <div class="slidev-layout figure-cite">
    <div v-if="heading || subheading" class="slide-header">
      <h1 v-if="heading">{{ heading }}</h1>
      <h2 v-if="subheading">{{ subheading }}</h2>
    </div>
    <div class="fig-row">
      <div class="fig-area"><slot /></div>
      <div v-if="$slots.legend" class="fig-legend"><slot name="legend" /></div>
      <div class="fig-side" :style="{ flexBasis: sideWidth + '%' }"><slot name="side" /></div>
    </div>
    <p class="fig-cite">{{ citation }}</p>
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
/* Figure + citation slides. The figure takes the whole body height, with any
   bullets in a reserved column to its right and the citation on a reserved row
   beneath, so the figure box — and with it the axes and the citation line —
   lands in exactly the same place on every slide that uses this layout. */
.figure-cite {
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

.fig-row {
  flex: 1;
  min-height: 0;
  display: flex;
  gap: 2.5rem;
}

/* The figure takes the full body height and never spills past it. */
.fig-area {
  flex: 1;
  min-width: 0;
  min-height: 0;
  overflow: hidden;
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
}

/* Key for the figure, sized by its own content. Only rendered when a slide
   provides one, so slides without a key keep the plain two-column split. */
.fig-legend {
  flex: 0 0 auto;
  min-width: 0;
  font-size: 15px;
  color: var(--slidev-theme-text);
  white-space: nowrap;
}

.fig-side {
  flex: 0 0 auto;
  min-width: 0;
  min-height: 0;
  overflow: hidden;
}

/* Size figures here, not on the slide, so they share one box. SVGs need
   preserveAspectRatio="xMinYMin meet" to stay flush left once height-capped. */
.fig-area :deep(svg) {
  width: 100%;
  max-width: 620px;
  height: 100%;
  max-height: 100%;
  display: block;
}

.fig-area :deep(img) {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}

/* Text beside the figure keeps the body size used by the other layouts. */
.fig-side :deep(ul) {
  padding-left: 1.5rem;
  margin: 0;
}

.fig-side :deep(li),
.fig-side :deep(p) {
  font-size: 18px;
  margin-bottom: 0.5rem;
  line-height: 1.5;
}

.fig-cite {
  flex: none;
  min-height: 1.1rem;
  margin: 0.35rem 0 0 0;
  font-size: 12px;
  color: #9aa0a6;
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

/* Same section rail as the content layout. */
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
