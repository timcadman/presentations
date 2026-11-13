<script setup>
// Row of headline numbers, one revealed per click. Each tile has an icon, a
// half-circle gauge whose arc and needle sweep while the number counts up.
import { ref, watch, onBeforeUnmount } from 'vue'

const props = defineProps({
  // [{ value, label, icon: 'function' | 'commit' | 'code' | 'tests' | 'clock', color, total?, decimals?, suffix? }]
  // `total` makes the gauge stop at value / total instead of full.
  // `decimals` and `suffix` control how the number is written, e.g. 3.7 h.
  stats: { type: Array, required: true },
  clicks: { type: Number, default: 0 },
  duration: { type: Number, default: 1500 },
})

const progress = ref(props.stats.map(() => 0))
const frames = []

function play(i) {
  cancelAnimationFrame(frames[i])
  const start = performance.now()
  const tick = (now) => {
    const t = Math.min(1, (now - start) / props.duration)
    progress.value[i] = 1 - Math.pow(1 - t, 3)
    if (t < 1) frames[i] = requestAnimationFrame(tick)
  }
  progress.value[i] = 0
  frames[i] = requestAnimationFrame(tick)
}

const shown = (i) => props.clicks > i

watch(() => props.clicks, (now, before) => {
  props.stats.forEach((_, i) => {
    if (shown(i) && !(before > i)) play(i)
    if (!shown(i)) progress.value[i] = 0
  })
}, { immediate: true })

onBeforeUnmount(() => frames.forEach(cancelAnimationFrame))

const fill = (s, i) => progress.value[i] * (s.total ? s.value / s.total : 1)
const format = (s, i) => {
  const digits = s.decimals ?? 0
  const number = (s.value * progress.value[i]).toLocaleString('en-GB', { minimumFractionDigits: digits, maximumFractionDigits: digits })
  return number + (s.suffix ?? '')
}
</script>

<template>
  <div class="stt-row">
    <div
      v-for="(s, i) in stats"
      :key="s.label"
      class="stt-tile"
      :class="{ hidden: !shown(i) }"
      :style="{ '--c': s.color }"
    >
      <svg class="stt-icon" viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <text v-if="s.icon === 'function'" x="12" y="17" text-anchor="middle" class="stt-icon-text">f(x)</text>
        <template v-else-if="s.icon === 'commit'">
          <line x1="1" y1="12" x2="8" y2="12" />
          <circle cx="12" cy="12" r="4" />
          <line x1="16" y1="12" x2="23" y2="12" />
        </template>
        <template v-else-if="s.icon === 'code'">
          <polyline points="8,6 2,12 8,18" />
          <polyline points="16,6 22,12 16,18" />
          <line x1="14" y1="4" x2="10" y2="20" />
        </template>
        <template v-else-if="s.icon === 'tests'">
          <circle cx="12" cy="12" r="10" />
          <polyline points="7,12 10.5,15.5 17,8.5" />
        </template>
        <template v-else-if="s.icon === 'clock'">
          <circle cx="12" cy="12" r="10" />
          <polyline points="12,6 12,12 16,14" />
        </template>
      </svg>

      <div class="stt-gauge">
        <svg viewBox="0 0 100 58">
          <path d="M 10 52 A 40 40 0 0 1 90 52" class="stt-track" pathLength="100" />
          <path
            d="M 10 52 A 40 40 0 0 1 90 52"
            class="stt-arc"
            pathLength="100"
            stroke-dasharray="100"
            :stroke-dashoffset="100 * (1 - fill(s, i))"
          />
          <line
            x1="50" y1="52" x2="50" y2="20"
            class="stt-needle"
            :transform="`rotate(${-90 + 180 * fill(s, i)} 50 52)`"
          />
          <circle cx="50" cy="52" r="3" class="stt-hub" />
        </svg>
      </div>

      <span class="stt-num">{{ format(s, i) }}</span>
      <div class="stt-label">{{ s.label }}</div>
    </div>
  </div>
</template>

<style scoped>
.stt-row {
  display: flex;
  justify-content: space-around;
  align-items: flex-start;
  height: 100%;
}

.stt-tile {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  width: 23%;
  transition: opacity 0.4s;
}
.stt-tile.hidden { opacity: 0; }

.stt-icon {
  width: 34px;
  height: 34px;
  stroke: var(--c);
}
.stt-icon-text {
  font-family: var(--font-subtitle);
  font-size: 9px;
  font-weight: 700;
  fill: var(--c);
  stroke: none;
}

.stt-gauge { width: 150px; }
.stt-gauge svg { width: 100%; display: block; }
.stt-track, .stt-arc { fill: none; stroke-width: 9; stroke-linecap: round; }
.stt-track { stroke: #E6E6E6; }
.stt-arc { stroke: var(--c); }
.stt-needle { stroke: var(--slidev-theme-text); stroke-width: 2.5; stroke-linecap: round; }
.stt-hub { fill: var(--slidev-theme-text); }

.stt-num {
  font-family: var(--font-title);
  font-size: 44px;
  line-height: 1;
  color: var(--c);
  font-variant-numeric: tabular-nums;
}

.stt-label {
  font-family: var(--font-subtitle);
  font-size: 15px;
  color: var(--slidev-theme-text);
  text-align: center;
}
</style>
