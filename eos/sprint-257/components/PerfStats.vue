<script setup>
import summary from '../data/perf_summary.json'

defineProps({
  clicks: { type: Number, default: 0 },   // bind to $clicks from the slide
  revealAt: { type: Number, default: 1 }, // appear at this click
})

const stats = [
  { value: summary.mean, label: 'mean' },
  { value: summary.median, label: 'median' },
  { value: summary.max, label: 'max' },
]
</script>

<template>
  <div class="ps-wrap" :class="{ shown: clicks >= revealAt }">
    <div class="ps-title">Improvement</div>
    <div class="ps-stat" v-for="s in stats" :key="s.label">
      <div class="ps-num">{{ s.value.toFixed(1) }}×</div>
      <div class="ps-lab">{{ s.label }}</div>
    </div>
  </div>
</template>

<style scoped>
.ps-wrap {
  display: flex;
  flex-direction: column;
  gap: 1.4rem;
  opacity: 0;
  transform: translateY(8px);
  transition: opacity 450ms ease, transform 450ms ease;
}

.ps-wrap.shown {
  opacity: 1;
  transform: none;
}

.ps-title {
  font-family: var(--font-subtitle);
  font-size: 15px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #999;
  margin-bottom: 0.25rem;
}

.ps-num {
  font-family: var(--font-title);
  font-size: 52px;
  font-weight: 700;
  line-height: 1;
  color: var(--slidev-theme-primary);
}

.ps-lab {
  font-family: var(--font-subtitle);
  font-size: 19px;
  color: var(--slidev-theme-text);
  margin-top: 0.1rem;
}
</style>
