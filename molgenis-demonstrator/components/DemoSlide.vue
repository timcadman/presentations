<script setup>
import { computed } from 'vue'

const props = defineProps({
  step: {
    type: String,
    required: true,
  },
  image: {
    type: String,
    default: '',
  },
  text: {
    type: String,
    default: '',
  },
  imageStyle: {
    type: String,
    default: '',
  },
})

const steps = ['Local data', 'Catalogue', 'Request', 'Access', 'Analyse']

const resolvedImage = computed(() => {
  if (!props.image) return ''
  const path = props.image.replace(/^\.\/public\//, '')
  return `${import.meta.env.BASE_URL}${path}`
})
</script>

<template>
  <div class="demo-slide">
    <p class="demo-text">{{ text || '&nbsp;' }}</p>

    <div class="demo-layout">
      <div class="demo-screenshot">
        <img v-if="image" :src="resolvedImage" :style="imageStyle">
        <span v-else>Screenshot placeholder</span>
      </div>
      <div class="demo-tracker">
        <div
          v-for="s in steps"
          :key="s"
          class="demo-step"
          :class="{ active: s === step }"
        >
          {{ s }}
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.demo-text {
  margin-top: 0.5rem;
  font-size: 18px;
}

.demo-layout {
  display: flex;
  gap: 2rem;
  margin-top: 1rem;
  align-items: stretch;
  height: 220px;
}

.demo-screenshot {
  flex: 2;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(148, 163, 184, 0.15);
  border: 2px dashed #ccc;
  color: #999;
  font-size: 1.1rem;
}

.demo-screenshot img {
  max-height: 100%;
  max-width: 100%;
  object-fit: contain;
  overflow: hidden;
}

.demo-tracker {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}

.demo-step {
  flex: 1;
  display: flex;
  align-items: center;
  padding: 0.6rem 1rem;
  border-radius: 6px;
  font-size: 0.85rem;
  font-weight: bold;
  color: white;
  opacity: 0.25;
}

.demo-step.active {
  opacity: 1;
}

.demo-step:nth-child(1) { background: #93c5fd; color: #1e3a5f; }
.demo-step:nth-child(2) { background: #60a5fa; }
.demo-step:nth-child(3) { background: #3b82f6; }
.demo-step:nth-child(4) { background: #2563eb; }
.demo-step:nth-child(5) { background: #1e3a5f; }
</style>
