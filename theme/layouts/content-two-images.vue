<script setup>
import { computed } from 'vue'

const props = defineProps({
  heading: {
    type: String,
    default: '',
  },
  subheading: {
    type: String,
    default: '',
  },
  imageLeft: {
    type: String,
    default: '',
  },
  imageRight: {
    type: String,
    default: '',
  },
  imageLeftScale: {
    type: String,
    default: '100',
  },
  imageRightScale: {
    type: String,
    default: '100',
  },
})

const base = import.meta.env.BASE_URL
function resolveImage(path) {
  if (!path) return ''
  return `${base}${path.replace(/^\.\/public\//, '')}`
}
const resolvedLeft = computed(() => resolveImage(props.imageLeft))
const resolvedRight = computed(() => resolveImage(props.imageRight))
</script>

<template>
  <div class="slidev-layout content-two-images">
    <div class="slide-header">
      <h1>{{ heading }}</h1>
      <h2 v-if="subheading">{{ subheading }}</h2>
    </div>
    <div class="slide-body">
      <slot />
    </div>
    <div class="images-row">
      <div class="image-panel">
        <img v-if="imageLeft" :src="resolvedLeft" class="panel-image" :style="{ maxWidth: imageLeftScale + '%', maxHeight: imageLeftScale + '%' }" />
      </div>
      <div class="image-panel">
        <img v-if="imageRight" :src="resolvedRight" class="panel-image" :style="{ maxWidth: imageRightScale + '%', maxHeight: imageRightScale + '%' }" />
      </div>
    </div>
    <div class="logo-bar">
      <img :src="`${base}molgenis-logo.png`" class="slide-logo" />
    </div>
  </div>
</template>

<style scoped>
.content-two-images {
  display: flex;
  flex-direction: column;
  /* bottom padding clears the logo (~3.25rem) so images never overlap it */
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
  font-size: 18px;
  margin-bottom: 0.75rem;
}

.images-row {
  flex: 1;
  display: flex;
  gap: 2rem;
  align-items: flex-start;
  min-height: 0;
}

.image-panel {
  flex: 1;
  height: 100%;
  display: flex;
  align-items: flex-start;
  justify-content: center;
}

.panel-image {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
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
</style>
