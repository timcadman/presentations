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
    <div class="text-area">
      <div class="slide-header">
        <h1>{{ heading }}</h1>
        <h2 v-if="subheading">{{ subheading }}</h2>
      </div>
      <div class="slide-body">
        <slot />
      </div>
      <div class="logo-bar">
        <img :src="`${base}molgenis-logo.png`" class="slide-logo" />
      </div>
    </div>
    <div class="image-area">
      <img v-if="image" :src="resolvedImage" class="slide-image" />
    </div>
  </div>
</template>

<style scoped>
.content-img-right {
  display: flex;
  height: 100%;
}

.text-area {
  width: 55%;
  padding: 4.5rem 3rem 2rem 5rem;
  display: flex;
  flex-direction: column;
}

.image-area {
  width: 40%;
  margin-left: auto;
  height: 100%;
  overflow: hidden;
}

.slide-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.slide-header {
  margin-bottom: 1.5rem;
  padding-top: 0.75rem;
  position: relative;
}

.slide-header::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 60%;
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
  left: 1.5rem;
}

.slide-logo {
  height: 36px;
  opacity: 0.8;
}
</style>
