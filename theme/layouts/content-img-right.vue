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
  image: {
    type: String,
    default: '',
  },
  imageScale: {
    type: String,
    default: '100',
  },
  // width of the image column as a % of the slide (text takes the rest).
  // 50 = default even split; lower (e.g. 25, 20) gives the text more room.
  imageWidth: {
    type: String,
    default: '50',
  },
  // horizontal alignment of the image within its column: center | flex-start | flex-end
  imageAlign: {
    type: String,
    default: 'center',
  },
})

const base = import.meta.env.BASE_URL
const resolvedImage = computed(() => {
  if (!props.image) return ''
  const path = props.image.replace(/^\.\/public\//, '')
  return `${base}${path}`
})
</script>

<template>
  <div class="slidev-layout content-img-right">
    <div class="slide-header">
      <h1>{{ heading }}</h1>
      <h2 v-if="subheading">{{ subheading }}</h2>
    </div>
    <div class="body-row">
      <div class="text-area">
        <div class="slide-body">
          <slot />
        </div>
      </div>
      <div class="image-area" :style="{ flexBasis: imageWidth + '%', justifyContent: imageAlign }">
        <img v-if="image" :src="resolvedImage" class="slide-image" :style="{ maxWidth: imageScale + '%', maxHeight: imageScale + '%' }" />
      </div>
    </div>
    <div class="logo-bar">
      <img :src="`${base}molgenis-logo.png`" class="slide-logo" />
    </div>
  </div>
</template>

<style scoped>
.content-img-right {
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

.body-row {
  flex: 1;
  display: flex;
  gap: 2.5rem;
  min-height: 0;
}

.text-area {
  flex: 1;
  min-width: 0;
}

.image-area {
  flex: 0 0 auto;
  min-width: 0;
  display: flex;
  align-items: flex-start;
  justify-content: center;
}

.slide-image {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
  border-radius: 6px;
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
</style>
