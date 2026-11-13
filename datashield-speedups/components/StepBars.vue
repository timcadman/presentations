<script setup>
// Grouped horizontal bars: one row per function, one bar per arm (ms, lower is
// better). Arms appear one per click so each step can be told in turn; the axis
// is fixed to every listed arm so bars never rescale as they appear.
import { computed } from 'vue'
import data from '../data/steps.json'

const props = defineProps({
  show: { type: Array, required: true },   // arm keys, in reveal order
  clicks: { type: Number, default: 0 },    // bind to $clicks
  ratio: { type: Array, default: null },   // [fromKey, toKey]: speed-up column
})

const arms = computed(() => props.show.map((k) => data.arms.find((a) => a.key === k)))
const visible = (i) => i <= props.clicks
const allShown = computed(() => props.clicks >= props.show.length - 1)
const axisMax = computed(() => Math.max(...data.functions.flatMap((f) => props.show.map((k) => f[k]))))
const pct = (v) => (v / axisMax.value) * 100
const fmt = (ms) => (ms >= 1000 ? (ms / 1000).toFixed(1) + ' s' : Math.round(ms) + ' ms')
const speedup = (f) => (f[props.ratio[0]] / f[props.ratio[1]]).toFixed(1) + '×'
</script>

<template>
  <div class="sb-wrap">
    <div class="sb-legend">
      <span v-for="(a, i) in arms" :key="a.key" class="sb-key" :class="{ shown: visible(i) }">
        <i class="sb-sw" :style="{ background: a.color }" />{{ a.label }}
      </span>
    </div>
    <div class="sb-rows">
      <div v-for="f in data.functions" :key="f.name" class="sb-row">
        <div class="sb-label">{{ f.name }}</div>
        <div class="sb-bars">
          <div v-for="(a, i) in arms" :key="a.key" class="sb-line">
            <div
              class="sb-bar"
              :style="{ width: (visible(i) ? pct(f[a.key]) : 0) + '%', background: a.color }"
            />
            <span class="sb-val" :class="{ shown: visible(i) }">{{ fmt(f[a.key]) }}</span>
          </div>
        </div>
        <div v-if="ratio" class="sb-ratio" :class="{ shown: allShown }">{{ speedup(f) }}</div>
      </div>
    </div>
    <div class="sb-xtitle">Median time per call, 5 servers (lower is better)</div>
  </div>
</template>

<style scoped>
.sb-wrap {
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
  height: 100%;
  font-family: var(--font-body);
}

.sb-legend {
  display: flex;
  gap: 1.4rem;
  font-size: 14px;
}

.sb-key {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  opacity: 0;
  transition: opacity 400ms ease;
}

.sb-key.shown { opacity: 1; }

.sb-sw {
  width: 14px;
  height: 14px;
  border-radius: 3px;
  display: inline-block;
}

.sb-rows {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.sb-row {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.sb-label {
  flex: 0 0 7.5rem;
  text-align: right;
  font-family: var(--font-subtitle);
  font-size: 15px;
  font-weight: 600;
  color: var(--slidev-theme-text);
}

.sb-bars {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.sb-line {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  height: 11px;
}

.sb-bar {
  height: 100%;
  border-radius: 0 3px 3px 0;
  transition: width 700ms cubic-bezier(0.22, 1, 0.36, 1);
}

.sb-val {
  font-size: 11px;
  color: #777;
  white-space: nowrap;
  opacity: 0;
  transition: opacity 400ms ease 300ms;
}

.sb-val.shown { opacity: 1; }

.sb-ratio {
  flex: 0 0 3.5rem;
  font-family: var(--font-subtitle);
  font-size: 18px;
  font-weight: 600;
  color: #B9852A;
  opacity: 0;
  transition: opacity 400ms ease;
}

.sb-ratio.shown { opacity: 1; }

.sb-xtitle {
  padding-left: 8.5rem;
  font-size: 12px;
  color: #777;
}
</style>
