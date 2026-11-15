<script setup>
// Illustrative exposome-wide association scan: every exposure tested against one
// outcome, -log10(p) up the y axis, with a Bonferroni-style threshold. The points
// are generated, not real results — this figure shows the shape of an ExWAS, it
// does not report one.
const GROUPS = [
  { name: 'Air', colour: 'var(--c-blue)', n: 14 },
  { name: 'Built', colour: 'var(--c-teal)', n: 12 },
  { name: 'Noise', colour: 'var(--c-gold)', n: 8 },
  { name: 'Green', colour: 'var(--c-purple)', n: 10 },
  { name: 'Social', colour: 'var(--c-red)', n: 12 },
]
const THRESHOLD = 4.2

// deterministic jitter, so the figure is identical on every render
let seed = 7
const rnd = () => (seed = (seed * 1103515245 + 12345) % 2147483648) / 2147483648

const X0 = 60
const X1 = 690
const Y0 = 250
const Y1 = 30
const yOf = v => Y0 - (v / 8) * (Y0 - Y1)

const total = GROUPS.reduce((a, g) => a + g.n, 0)
let i = 0
const points = GROUPS.flatMap(g => Array.from({ length: g.n }, () => {
  const x = X0 + ((i++ + 0.5) / total) * (X1 - X0)
  // a couple of hits per deck, the rest noise
  const v = rnd() < 0.06 ? 4.5 + rnd() * 3 : rnd() * 3.8
  return { x, y: yOf(v), colour: g.colour }
}))

const ticks = [0, 2, 4, 6, 8]
</script>

<template>
  <svg viewBox="0 10 720 300" preserveAspectRatio="xMinYMin meet">
    <line :x1="X0" :y1="Y0" :x2="X1" :y2="Y0" stroke="#999" stroke-width="1.5" />
    <line :x1="X0" :y1="Y1" :x2="X0" :y2="Y0" stroke="#999" stroke-width="1.5" />
    <text v-for="t in ticks" :key="t" style="font-size: 14px" :x="X0 - 8" :y="yOf(t) + 5"
          fill="#666" text-anchor="end">{{ t }}</text>
    <text style="font-size: 16px" x="0" y="0" fill="#555" text-anchor="middle"
          transform="translate(22,140) rotate(-90)">−log₁₀(p)</text>

    <line :x1="X0" :y1="yOf(THRESHOLD)" :x2="X1" :y2="yOf(THRESHOLD)"
          stroke="var(--c-grey)" stroke-width="1.5" stroke-dasharray="6 5" />
    <text style="font-size: 13px" :x="X1" :y="yOf(THRESHOLD) - 7" fill="var(--c-grey)"
          text-anchor="end">significance threshold</text>

    <circle v-for="(p, n) in points" :key="n" :cx="p.x" :cy="p.y" r="4.5"
            :fill="p.colour" fill-opacity="0.8" />

    <text v-for="(g, n) in GROUPS" :key="g.name" style="font-size: 14px"
          :x="X0 + ((n + 0.5) / GROUPS.length) * (X1 - X0)" :y="Y0 + 22"
          :fill="g.colour" text-anchor="middle">{{ g.name }}</text>
    <text style="font-size: 16px" :x="(X0 + X1) / 2" y="292" fill="#555"
          text-anchor="middle">Exposures</text>
  </svg>
</template>
