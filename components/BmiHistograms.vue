<script setup>
import { computed } from 'vue'

const BREAKS = [14.72, 18.89, 23.06, 27.23, 31.40, 35.57, 39.74, 43.91]

const COHORTS = [
  { name: 'server_1', n: 500, colour: '#4285F4', counts: [29, 113, 157, 109, 41, 16, 0] },
  { name: 'server_2', n: 800, colour: '#B9852A', counts: [42, 182, 242, 159, 57, 13, 5] },
  { name: 'server_3', n: 300, colour: '#6A4C93', counts: [16, 62, 93, 66, 30, 4, 5] },
]

const W = 268
const H = 208
const M = { top: 10, right: 10, bottom: 28, left: 38 }
const plotW = W - M.left - M.right
const plotH = H - M.top - M.bottom

const yMax = 250
const yTicks = [0, 50, 100, 150, 200, 250]
const xTicks = [20, 30, 40]

const x = (v) => M.left + ((v - BREAKS[0]) / (BREAKS[BREAKS.length - 1] - BREAKS[0])) * plotW
const y = (v) => M.top + plotH - (v / yMax) * plotH

const panels = computed(() =>
  COHORTS.map((c) => ({
    ...c,
    bars: c.counts.map((count, i) => {
      const x0 = x(BREAKS[i]) + 1
      const x1 = x(BREAKS[i + 1]) - 1
      return {
        count,
        x: x0,
        width: Math.max(x1 - x0, 1),
        y: y(count),
        height: y(0) - y(count),
        label: `${BREAKS[i].toFixed(1)}–${BREAKS[i + 1].toFixed(1)}: ${count}`,
      }
    }),
  }))
)
</script>

<template>
  <div class="bh-grid">
    <figure v-for="p in panels" :key="p.name" class="bh-panel">
      <figcaption class="bh-caption">
        <span class="bh-swatch" :style="{ background: p.colour }"></span>
        {{ p.name }} <span class="bh-n">n = {{ p.n }}</span>
      </figcaption>

      <svg :viewBox="`0 0 ${W} ${H}`" role="img" :aria-label="`BMI distribution for ${p.name}`">
        <g>
          <line
            v-for="t in yTicks"
            :key="t"
            :x1="M.left"
            :x2="W - M.right"
            :y1="y(t)"
            :y2="y(t)"
            stroke="#edf0f3"
            stroke-width="1"
          />
        </g>

        <g>
          <text v-for="t in yTicks" :key="t" :x="M.left - 6" :y="y(t) + 3" class="bh-tick" text-anchor="end">{{ t }}</text>
          <text v-for="t in xTicks" :key="t" :x="x(t)" :y="H - 10" class="bh-tick" text-anchor="middle">{{ t }}</text>
        </g>

        <line :x1="M.left" :x2="W - M.right" :y1="y(0)" :y2="y(0)" stroke="#c8ced4" stroke-width="1" />

        <g>
          <rect
            v-for="(b, i) in p.bars"
            :key="i"
            :x="b.x"
            :y="b.y"
            :width="b.width"
            :height="b.height"
            :fill="p.colour"
            rx="2"
          >
            <title>{{ b.label }}</title>
          </rect>
        </g>

        <text :x="M.left + plotW / 2" :y="H - 1" class="bh-axis-title" text-anchor="middle">BMI</text>
      </svg>
    </figure>
  </div>
</template>

<style scoped>
.bh-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  align-items: start;
  margin-top: 0.5rem;
}

.bh-caption {
  font-family: var(--font-subtitle);
  font-size: 12px;
  color: #333;
  display: flex;
  align-items: center;
  gap: 0.4rem;
  margin-bottom: 0.2rem;
}

.bh-swatch {
  width: 10px;
  height: 10px;
  border-radius: 2px;
  display: inline-block;
}

.bh-n {
  color: #9aa0a6;
}

.bh-tick {
  font-family: var(--font-subtitle);
  font-size: 8px;
  fill: #9aa0a6;
}

.bh-axis-title {
  font-family: var(--font-subtitle);
  font-size: 8px;
  fill: #6b7480;
}
</style>
