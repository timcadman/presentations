<script setup>
import { computed } from 'vue'
import { COHORTS, X, thickness } from './cohorts.js'

const props = defineProps({
  // show one cohort only; the other rows keep their place but are drawn in white,
  // so the visible row does not move when the rest appear on the next slide
  only: {
    type: String,
    default: '',
  },
})

const rows = computed(() => COHORTS.map((c, i) => {
  const shown = !props.only || c.name === props.only
  const cy = 54 + 28 * i
  const t = thickness(c.n)
  return {
    ...c,
    cy,
    label: shown ? c.colour : '#ffffff',
    fill: shown ? c.colour : '#ffffff',
    opacity: shown ? 0.75 : 1,
    x: X(c.first),
    width: X(c.last) - X(c.first),
    y: cy - t / 2,
    height: t,
    rx: t / 2,
  }
}))

const separators = Array.from({ length: 9 }, (_, i) => 40 + 28 * i)
const ticks = [0, 10, 20, 30, 40, 50, 60, 70, 80]
const key = [
  { x: 380, n: 1000, label: '1,000' },
  { x: 470, n: 5000, label: '5,000' },
  { x: 580, n: 9000, label: '9,000' },
].map(k => ({ ...k, t: thickness(k.n) }))
</script>

<template>
  <svg viewBox="65 6 655 314" preserveAspectRatio="xMinYMin meet">
    <text style="font-size: 14px" x="300" y="24" fill="#555">Participants:</text>
    <template v-for="k in key" :key="k.n">
      <rect :x="k.x" :y="20 - k.t / 2" width="24" :height="k.t" :rx="k.t / 2"
            fill="#888" fill-opacity="0.6" />
      <text style="font-size: 13px" :x="k.x + 30" y="24" fill="#555">{{ k.label }}</text>
    </template>

    <line v-for="y in separators" :key="`s${y}`" x1="160" :y1="y" x2="700" :y2="y"
          stroke="#eee" stroke-width="1" />

    <text v-for="r in rows" :key="`l${r.name}`" style="font-size: 14px"
          x="150" :y="r.cy + 4" :fill="r.label" text-anchor="end">{{ r.name }}</text>

    <rect v-for="r in rows" :key="`b${r.name}`" :x="r.x" :y="r.y" :width="r.width"
          :height="r.height" :rx="r.rx" :fill="r.fill" :fill-opacity="r.opacity" />

    <line x1="160" y1="270" x2="700" y2="270" stroke="#999" stroke-width="1.5" />
    <template v-for="t in ticks" :key="`t${t}`">
      <line :x1="X(t)" y1="270" :x2="X(t)" y2="275" stroke="#999" stroke-width="1.5" />
      <text style="font-size: 14px" :x="X(t)" y="286" fill="#666" text-anchor="middle">{{ t }}</text>
    </template>
    <text style="font-size: 16px" x="420" y="304" fill="#555" text-anchor="middle">Age (years)</text>
  </svg>
</template>
