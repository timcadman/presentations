<script setup>
import { computed } from 'vue'

const BREAKS = [0, 10.47, 20.94, 31.40, 41.87, 52.34, 62.81, 73.28, 83.75, 94.21, 104.68]

const COHORTS = [
  { name: 'server_1', colour: '#4285F4', counts: [35, 27, 42, 78, 63, 49, 44, 68, 15, 15] },
  { name: 'server_2', colour: '#B9852A', counts: [56, 47, 55, 126, 75, 65, 89, 94, 30, 31] },
  { name: 'server_3', colour: '#6A4C93', counts: [22, 26, 21, 50, 39, 32, 25, 40, 15, 6] },
]

const W = 150
const H = 172
const M = { top: 8, right: 4, bottom: 18, left: 20 }
const plotW = W - M.left - M.right
const plotH = H - M.top - M.bottom

const yMax = 150
const yTicks = [0, 50, 100, 150]
const xTicks = [0, 50, 100]

const x = (v) => M.left + ((v - BREAKS[0]) / (BREAKS[BREAKS.length - 1] - BREAKS[0])) * plotW
const y = (v) => M.top + plotH - (v / yMax) * plotH

const panels = computed(() =>
  COHORTS.map((c) => ({
    ...c,
    bars: c.counts.map((count, i) => {
      const x0 = x(BREAKS[i]) + 0.6
      const x1 = x(BREAKS[i + 1]) - 0.6
      return {
        x: x0,
        width: Math.max(x1 - x0, 0.8),
        y: y(count),
        height: y(0) - y(count),
        label: `${BREAKS[i].toFixed(0)}-${BREAKS[i + 1].toFixed(0)}: ${count}`,
      }
    }),
  }))
)
</script>

<template>
  <div class="q-grid">
    <figure v-for="p in panels" :key="p.name" class="q-panel">
      <figcaption class="q-caption">
        <span class="q-swatch" :style="{ background: p.colour }"></span>{{ p.name }}
      </figcaption>
      <svg :viewBox="`0 0 ${W} ${H}`" role="img" :aria-label="`Baseline QoL distribution, ${p.name}`">
        <line
          v-for="t in yTicks"
          :key="`g${t}`"
          :x1="M.left"
          :x2="W - M.right"
          :y1="y(t)"
          :y2="y(t)"
          stroke="#edf0f3"
          stroke-width="0.7"
        />
        <text v-for="t in yTicks" :key="`y${t}`" :x="M.left - 3" :y="y(t) + 2.5" class="q-tick" text-anchor="end">{{ t }}</text>
        <text v-for="t in xTicks" :key="`x${t}`" :x="x(t)" :y="H - 6" class="q-tick" text-anchor="middle">{{ t }}</text>
        <line :x1="M.left" :x2="W - M.right" :y1="y(0)" :y2="y(0)" stroke="#c8ced4" stroke-width="0.7" />
        <rect
          v-for="(b, i) in p.bars"
          :key="i"
          :x="b.x"
          :y="b.y"
          :width="b.width"
          :height="b.height"
          :fill="p.colour"
          rx="1"
        >
          <title>{{ b.label }}</title>
        </rect>
      </svg>
    </figure>
  </div>
</template>

<style scoped>
.q-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.4rem;
  margin-top: 0.15rem;
}

.q-panel {
  margin: 0;
}

.q-caption {
  font-family: var(--font-subtitle);
  font-size: 8px;
  color: #4a5561;
  display: flex;
  align-items: center;
  gap: 0.25rem;
  margin-bottom: 0.1rem;
}

.q-swatch {
  width: 7px;
  height: 7px;
  border-radius: 1px;
  display: inline-block;
}

.q-tick {
  font-family: var(--font-subtitle);
  font-size: 6px;
  fill: #9aa0a6;
}
</style>
