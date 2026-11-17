<script setup>
import { computed } from 'vue'

// A forest plot that builds up one cohort per click, then the pooled estimate if given.
//
//   <CohortForest
//     :studies="[{ label: 'ALSPAC', n: 4795, or: 0.58, lo: 0.21, hi: 1.61, weight: 1.93 }]"
//     :pooled="{ label: 'All cohorts', or: 1.12, lo: 0.95, hi: 1.32 }"
//     axis-label="Odds ratio" />
//
// ForestPlot.vue is hard-coded to one dataset, so this takes the data as props.
// Odds ratios sit on a log axis. `weight` sizes the marker. `at` (optional) is the
// click a cohort appears on, so several can share one; it defaults to one per click.
const props = defineProps({
  studies: { type: Array, required: true },
  pooled: { type: Object, default: null },
  domain: { type: Array, default: () => [0.04, 8] },
  ticks: { type: Array, default: () => [0.1, 0.5, 1, 2, 5] },
  axisLabel: { type: String, default: 'Odds ratio' },
  rowHeader: { type: String, default: 'Cohort' },
})

const W = 760
const ROW = 40
const PLOT = { left: 230, right: 540 }
const pooledY = computed(() => 56 + props.studies.length * ROW + 14)
// the axis sits under the pooled row, or straight under the last cohort when there is none
const baseY = computed(() => (props.pooled ? pooledY.value : 56 + (props.studies.length - 1) * ROW + 14))
const H = computed(() => baseY.value + 78)
// start the view just above the header text so the figure's top lines up with the bullets beside it
const TOP = 8

const x = (v) => {
  const [lo, hi] = props.domain
  const t = (Math.log(v) - Math.log(lo)) / (Math.log(hi) - Math.log(lo))
  return PLOT.left + t * (PLOT.right - PLOT.left)
}

const ci = (r) => `${r.or.toFixed(2)} (${r.lo.toFixed(2)}, ${r.hi.toFixed(2)})`
// the pooled estimate appears on the click after the last cohort
const pooledAt = computed(() => Math.max(...rows.value.map(r => r.at)) + 1)
const maxWeight = computed(() => Math.max(...props.studies.map(s => s.weight)))

const rows = computed(() =>
  props.studies.map((s, i) => ({
    ...s,
    y: 56 + i * ROW,
    at: s.at ?? i + 1,
    size: 6 + (s.weight / maxWeight.value) * 6,
  }))
)
</script>

<template>
  <svg :viewBox="`0 ${TOP} ${W} ${H - TOP}`" preserveAspectRatio="xMinYMin meet" class="cf" role="img" aria-label="Forest plot of odds ratios by cohort">
    <text x="0" y="22" class="cf-head">{{ rowHeader }}</text>
    <text x="170" y="22" class="cf-head" text-anchor="end">N</text>
    <text :x="W" y="22" class="cf-head" text-anchor="end">OR (95% CI)</text>
    <line x1="0" :x2="W" y1="32" :y2="32" stroke="#c8ced4" stroke-width="1" />

    <line :x1="x(1)" :x2="x(1)" y1="40" :y2="baseY + 16" stroke="#9aa0a6" stroke-width="1.5" stroke-dasharray="1.5 4" stroke-linecap="round" />

    <g v-for="r in rows" :key="r.label" v-click="r.at">
      <text x="0" :y="r.y + 5" class="cf-label">{{ r.label }}</text>
      <text x="170" :y="r.y + 5" class="cf-num" text-anchor="end">{{ r.n.toLocaleString('en-GB') }}</text>
      <line :x1="x(r.lo)" :x2="x(r.hi)" :y1="r.y" :y2="r.y" stroke="#4285F4" stroke-width="2" />
      <line :x1="x(r.lo)" :x2="x(r.lo)" :y1="r.y - 4" :y2="r.y + 4" stroke="#4285F4" stroke-width="2" />
      <line :x1="x(r.hi)" :x2="x(r.hi)" :y1="r.y - 4" :y2="r.y + 4" stroke="#4285F4" stroke-width="2" />
      <rect :x="x(r.or) - r.size / 2" :y="r.y - r.size / 2" :width="r.size" :height="r.size" fill="#4285F4" />
      <text :x="W" :y="r.y + 5" class="cf-num" text-anchor="end">{{ ci(r) }}</text>
    </g>

    <g v-if="pooled" v-click="pooledAt">
      <line x1="0" :x2="W" :y1="pooledY - 20" :y2="pooledY - 20" stroke="#e7eaee" stroke-width="1" />
      <text x="0" :y="pooledY + 5" class="cf-label cf-bold">{{ pooled.label }}</text>
      <polygon
        :points="`${x(pooled.lo)},${pooledY} ${x(pooled.or)},${pooledY - 8} ${x(pooled.hi)},${pooledY} ${x(pooled.or)},${pooledY + 8}`"
        fill="#02529B"
      />
      <text :x="W" :y="pooledY + 5" class="cf-num cf-bold" text-anchor="end">{{ ci(pooled) }}</text>
    </g>

    <line :x1="PLOT.left" :x2="PLOT.right" :y1="baseY + 26" :y2="baseY + 26" stroke="#c8ced4" stroke-width="1" />
    <text v-for="t in ticks" :key="t" :x="x(t)" :y="baseY + 48" class="cf-tick" text-anchor="middle">{{ t }}</text>
    <text :x="(PLOT.left + PLOT.right) / 2" :y="baseY + 72" class="cf-axis" text-anchor="middle">{{ axisLabel }} (log scale)</text>
  </svg>
</template>

<style scoped>
.cf { display: block; width: 100%; height: auto; max-height: 70vh; flex: none; }
.cf-head { font-family: var(--font-subtitle); font-size: 16px; fill: #6b7480; }
.cf-label { font-family: var(--font-subtitle); font-size: 18px; fill: #2b3440; }
.cf-num { font-family: var(--font-subtitle); font-size: 17px; fill: #2b3440; font-variant-numeric: tabular-nums; }
.cf-bold { font-weight: 700; }
.cf-tick { font-family: var(--font-subtitle); font-size: 15px; fill: #9aa0a6; }
.cf-axis { font-family: var(--font-subtitle); font-size: 15px; fill: #6b7480; }
</style>
