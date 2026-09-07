<script setup>
import { computed } from 'vue'

const STUDIES = [
  { label: 'server_1', n: 436, or: 0.805, lo: 0.739, hi: 0.877, weight: 29.0, colour: '#4285F4' },
  { label: 'server_2', n: 668, or: 0.835, lo: 0.781, hi: 0.892, weight: 48.8, colour: '#B9852A' },
  { label: 'server_3', n: 276, or: 0.949, lo: 0.860, hi: 1.047, weight: 22.2, colour: '#6A4C93' },
]
const POOLED = { label: 'Combined', n: 1380, or: 0.857, lo: 0.786, hi: 0.935, colour: '#1E3A5F' }
const I2 = 70

const W = 760
const ROW = 34
const H = ROW * (STUDIES.length + 3) + 66
const PLOT = { left: 300, right: 520 }
const DOMAIN = [0.70, 1.15]

const x = (v) => {
  const t = (Math.log(v) - Math.log(DOMAIN[0])) / (Math.log(DOMAIN[1]) - Math.log(DOMAIN[0]))
  return PLOT.left + t * (PLOT.right - PLOT.left)
}
const ticks = [0.7, 0.8, 0.9, 1.0, 1.1]

const ci = (r) => `${r.or.toFixed(2)} (${r.lo.toFixed(2)}, ${r.hi.toFixed(2)})`

const rows = computed(() =>
  STUDIES.map((s, i) => ({
    ...s,
    y: 52 + i * ROW,
    size: 5 + (s.weight / 48.8) * 6,
  }))
)
const pooledY = computed(() => 52 + STUDIES.length * ROW + 14)
</script>

<template>
  <svg :viewBox="`0 0 ${W} ${H}`" class="fp" role="img" aria-label="Forest plot of odds ratios by cohort">
    <text x="0" y="22" class="fp-head">Study</text>
    <text x="150" y="22" class="fp-head" text-anchor="end">N</text>
    <text :x="W" y="22" class="fp-head" text-anchor="end">OR (95% CI)</text>

    <line x1="0" :x2="W" y1="30" :y2="30" stroke="#c8ced4" stroke-width="1" />

    <line :x1="x(1)" :x2="x(1)" y1="38" :y2="pooledY + 16" stroke="#9aa0a6" stroke-width="1.5" stroke-dasharray="1.5 4" stroke-linecap="round" />

    <g v-for="r in rows" :key="r.label">
      <text x="0" :y="r.y + 4" class="fp-label">{{ r.label }}</text>
      <text x="150" :y="r.y + 4" class="fp-num" text-anchor="end">{{ r.n }}</text>
      <line :x1="x(r.lo)" :x2="x(r.hi)" :y1="r.y" :y2="r.y" :stroke="r.colour" stroke-width="2" />
      <line :x1="x(r.lo)" :x2="x(r.lo)" :y1="r.y - 4" :y2="r.y + 4" :stroke="r.colour" stroke-width="2" />
      <line :x1="x(r.hi)" :x2="x(r.hi)" :y1="r.y - 4" :y2="r.y + 4" :stroke="r.colour" stroke-width="2" />
      <rect
        :x="x(r.or) - r.size / 2"
        :y="r.y - r.size / 2"
        :width="r.size"
        :height="r.size"
        :fill="r.colour"
      />
      <text :x="W" :y="r.y + 4" class="fp-num" text-anchor="end">{{ ci(r) }}</text>
    </g>

    <line x1="0" :x2="W" :y1="pooledY - 18" :y2="pooledY - 18" stroke="#e7eaee" stroke-width="1" />

    <text x="0" :y="pooledY + 4" class="fp-label fp-bold">{{ POOLED.label }}</text>
    <text x="150" :y="pooledY + 4" class="fp-num fp-bold" text-anchor="end">{{ POOLED.n }}</text>
    <polygon
      :points="`${x(POOLED.lo)},${pooledY} ${x(POOLED.or)},${pooledY - 7} ${x(POOLED.hi)},${pooledY} ${x(POOLED.or)},${pooledY + 7}`"
      :fill="POOLED.colour"
    />
    <text :x="W" :y="pooledY + 4" class="fp-num fp-bold" text-anchor="end">{{ ci(POOLED) }}</text>

    <g>
      <line :x1="PLOT.left" :x2="PLOT.right" :y1="pooledY + 22" :y2="pooledY + 22" stroke="#c8ced4" stroke-width="1" />
      <text v-for="t in ticks" :key="t" :x="x(t)" :y="pooledY + 46" class="fp-tick" text-anchor="middle">{{ t.toFixed(1) }}</text>
      <text :x="(PLOT.left + PLOT.right) / 2" :y="pooledY + 70" class="fp-axis" text-anchor="middle">
        Odds ratio per 10-point higher baseline QoL
      </text>
    </g>

    <text x="0" :y="pooledY + 34" class="fp-note">Heterogeneity: I&#178; = {{ I2 }}%</text>
  </svg>
</template>

<style scoped>
.fp {
  display: block;
  width: 100%;
  height: auto;
  max-height: 70vh;
  flex: none;
}

.fp-head {
  font-family: var(--font-subtitle);
  font-size: 17px;
  fill: #6b7480;
}

.fp-label {
  font-family: var(--font-subtitle);
  font-size: 18px;
  fill: #2b3440;
}

.fp-num {
  font-family: var(--font-subtitle);
  font-size: 18px;
  fill: #2b3440;
  font-variant-numeric: tabular-nums;
}

.fp-bold {
  font-weight: 700;
}

.fp-tick {
  font-family: var(--font-subtitle);
  font-size: 15px;
  fill: #9aa0a6;
}

.fp-axis {
  font-family: var(--font-subtitle);
  font-size: 15px;
  fill: #6b7480;
}

.fp-note {
  font-family: var(--font-subtitle);
  font-size: 15px;
  fill: #6b7480;
}
</style>
