<script setup>
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'

const props = defineProps({
  value: { type: Number, default: 29 },   // refactored
  total: { type: Number, default: 123 },  // total functions
  label: { type: String, default: 'of functions refactored' },
  duration: { type: Number, default: 1500 }, // sweep time (ms)
})

// --- geometry (viewBox 0 0 100 100) ---
const R = 42
const C = 2 * Math.PI * R
const fraction = computed(() => props.value / props.total)

// progress = 0..1 of how far through the sweep we are
const progress = ref(0)
const dashoffset = computed(() => C * (1 - fraction.value * progress.value))
const shownValue = computed(() => Math.round(props.value * progress.value))
const shownPct = computed(() => Math.round(100 * fraction.value * progress.value))

const root = ref(null)
let raf = null
let io = null

function play() {
  cancelAnimationFrame(raf)
  const start = performance.now()
  const tick = (now) => {
    const t = Math.min(1, (now - start) / props.duration)
    progress.value = 1 - Math.pow(1 - t, 3) // easeOutCubic — fast then settles
    if (t < 1) raf = requestAnimationFrame(tick)
  }
  progress.value = 0
  raf = requestAnimationFrame(tick)
}

onMounted(() => {
  // Replay the sweep each time the slide scrolls into view.
  io = new IntersectionObserver((entries) => {
    for (const e of entries) {
      if (e.isIntersecting && e.intersectionRatio > 0.4) play()
      else progress.value = 0
    }
  }, { threshold: [0, 0.4, 1] })
  io.observe(root.value)
})

onBeforeUnmount(() => {
  if (io) io.disconnect()
  cancelAnimationFrame(raf)
})
</script>

<template>
  <div ref="root" class="pd-wrap">
    <div class="pd-donut">
      <svg viewBox="0 0 100 100">
        <!-- track -->
        <circle cx="50" cy="50" :r="R" class="pd-track" :stroke-width="12" fill="none" />
        <!-- progress arc, starts at 12 o'clock -->
        <circle
          cx="50" cy="50" :r="R" class="pd-arc" :stroke-width="12" fill="none"
          stroke-linecap="round"
          :stroke-dasharray="C"
          :stroke-dashoffset="dashoffset"
          transform="rotate(-90 50 50)"
        />
      </svg>
      <div class="pd-center">
        <div class="pd-num">{{ shownValue }} <span class="pd-den">/ {{ total }}</span></div>
      </div>
    </div>
    <div class="pd-label">{{ shownPct }}% {{ label }}</div>
  </div>
</template>

<style scoped>
.pd-wrap {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1.25rem;
  height: 100%;
}

.pd-donut {
  position: relative;
  width: 320px;
  height: 320px;
}

.pd-donut svg {
  width: 100%;
  height: 100%;
}

.pd-track {
  stroke: #E6E6E6;
}

.pd-arc {
  stroke: var(--slidev-theme-primary);
}

.pd-center {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.15rem;
}

.pd-num {
  font-family: var(--font-title);
  font-size: 58px;
  font-weight: 700;
  line-height: 1;
  color: var(--slidev-theme-primary);
}

.pd-den {
  font-weight: 400;
  color: var(--slidev-theme-primary);
  opacity: 0.55;
}

.pd-label {
  font-family: var(--font-subtitle);
  font-size: 22px;
  color: var(--slidev-theme-text);
}
</style>
