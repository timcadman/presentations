<script setup>
import { computed } from 'vue'
import { COHORTS, X } from './cohorts.js'

// FEV1 trajectories from Garcia-Aymerich et al. (2025) Lancet Respir Med 13:611-22,
// appendix figure S7(b): female, by smoking status. The paper publishes breakpoint
// ages and mL/year slopes but no absolute levels, so both strata start from the same
// FEV1 at age 4 — before either group smokes.
const props = defineProps({
  // restrict the curves to one cohort's observed age range, and show only its point
  only: {
    type: String,
    default: '',
  },
})

const START = 0.55
const STRATA = [
  { key: 'never', label: 'Never smoking', colour: '#119DA1', first: 0.249, segments: [[12, 0.068], [22, -0.027]] },
  { key: 'persistent', label: 'Persistent smoking', colour: '#DA594A', first: 0.203, segments: [[15, 0.081], [20, -0.029], [33, -0.033]] },
]

const Y = litres => 260 - 55 * litres

function knots(stratum) {
  const out = [[4, START]]
  let slope = stratum.first
  for (const [age, next] of stratum.segments) {
    const [a0, v0] = out[out.length - 1]
    out.push([age, v0 + slope * (age - a0)])
    slope = next
  }
  const [a0, v0] = out[out.length - 1]
  out.push([80, v0 + slope * (80 - a0)])
  return out
}

// monotone cubic (Fritsch-Carlson): interpolates the published breakpoints exactly
// and takes a zero slope at the peak, so it rounds without overshooting
function interpolator(ks) {
  const xs = ks.map(k => k[0])
  const ys = ks.map(k => k[1])
  const h = xs.slice(1).map((x, i) => x - xs[i])
  const m = h.map((hi, i) => (ys[i + 1] - ys[i]) / hi)
  const d = [m[0]]
  for (let i = 1; i < m.length; i++) {
    if (m[i - 1] * m[i] <= 0) {
      d.push(0)
    } else {
      const w1 = 2 * h[i] + h[i - 1]
      const w2 = h[i] + 2 * h[i - 1]
      d.push((w1 + w2) / (w1 / m[i - 1] + w2 / m[i]))
    }
  }
  d.push(m[m.length - 1])
  return age => {
    for (let i = 0; i < h.length; i++) {
      if (age >= xs[i] && age <= xs[i + 1]) {
        const t = (age - xs[i]) / h[i]
        return (2 * t ** 3 - 3 * t ** 2 + 1) * ys[i]
          + (t ** 3 - 2 * t ** 2 + t) * h[i] * d[i]
          + (-2 * t ** 3 + 3 * t ** 2) * ys[i + 1]
          + (t ** 3 - t ** 2) * h[i] * d[i + 1]
      }
    }
    return ys[ys.length - 1]
  }
}

const cohort = computed(() => COHORTS.find(c => c.name === props.only))
const from = computed(() => (cohort.value ? cohort.value.first : 4))
const to = computed(() => (cohort.value ? cohort.value.last : 80))

const curves = computed(() => STRATA.map((s) => {
  const f = interpolator(knots(s))
  const points = []
  for (let a = from.value; a <= to.value + 0.001; a += 0.5) {
    points.push(`${X(a).toFixed(1)},${Y(f(a)).toFixed(1)}`)
  }
  return { ...s, points: points.join(' ') }
}))

// each cohort sits three-quarters through its own observed range, nudged apart so
// no two markers collide; they stay on the never-smoking curve, not beside it
const MIN_GAP = 1.6
const markers = computed(() => {
  const never = interpolator(knots(STRATA[0]))
  const rows = (cohort.value ? [cohort.value] : COHORTS)
    .map(c => ({ ...c, age: c.first + 0.75 * (c.last - c.first) }))
    .sort((a, b) => a.age - b.age)
  const placed = []
  for (const row of rows) {
    const age = placed.length && row.age - placed[placed.length - 1].age < MIN_GAP
      ? placed[placed.length - 1].age + MIN_GAP
      : row.age
    placed.push({ ...row, age })
  }
  return placed.map(r => ({ ...r, x: X(r.age), y: Y(never(r.age)) }))
})

const ticks = [0, 10, 20, 30, 40, 50, 60, 70, 80]
</script>

<template>
  <svg viewBox="65 -4 655 314" preserveAspectRatio="xMinYMin meet">
    <line x1="160" y1="40" x2="160" y2="260" stroke="#999" stroke-width="1.5" />
    <line x1="160" y1="260" x2="700" y2="260" stroke="#999" stroke-width="1.5" />
    <text v-for="v in [0, 1, 2, 3, 4]" :key="`y${v}`" style="font-size: 14px"
          x="152" :y="Y(v) + 4" fill="#666" text-anchor="end">{{ v }}</text>
    <template v-for="t in ticks" :key="`x${t}`">
      <line :x1="X(t)" y1="260" :x2="X(t)" y2="265" stroke="#999" stroke-width="1.5" />
      <text style="font-size: 14px" :x="X(t)" y="278" fill="#666" text-anchor="middle">{{ t }}</text>
    </template>
    <text style="font-size: 16px" x="420" y="296" fill="#555" text-anchor="middle">Age (years)</text>
    <text style="font-size: 16px" x="0" y="0" fill="#555" text-anchor="middle"
          transform="translate(110,150) rotate(-90)">FEV₁ (L), female</text>

    <polyline v-for="c in curves" :key="c.key" :points="c.points" fill="none"
              :stroke="c.colour" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />

    <circle v-for="m in markers" :key="m.name" :cx="m.x" :cy="m.y" r="4.5"
            :fill="m.colour" stroke="#ffffff" stroke-width="1.2" />

    <template v-for="(s, i) in STRATA" :key="`l${s.key}`">
      <line :x1="300 + i * 200" y1="16" :x2="320 + i * 200" y2="16"
            :stroke="s.colour" stroke-width="4" stroke-linecap="round" />
      <text style="font-size: 15px" :x="326 + i * 200" y="21" fill="#333">{{ s.label }}</text>
    </template>
  </svg>
</template>
