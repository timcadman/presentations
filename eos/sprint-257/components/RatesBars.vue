<script setup>
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'
import data from '../data/rates.json'

const props = defineProps({
  origDuration: { type: Number, default: 700 }, // sweep time per phase (ms)
  clicks: { type: Number, default: 0 },         // bind to $clicks from the slide
  revealAt: { type: Number, default: 1 },       // reveal refactored bars at this click
})

const items = data

// round the axis up to the next 0.5 so bars never touch the edge
const axisMax = computed(() => {
  const m = Math.max(...items.flatMap((d) => [d.original, d.refactored]))
  return Math.ceil(m / 0.5) * 0.5
})
const ticks = computed(() => {
  const out = []
  for (let t = 0; t <= axisMax.value + 1e-9; t += 0.5) out.push(Number(t.toFixed(1)))
  return out
})
const stepPct = computed(() => (0.5 / axisMax.value) * 100) // gridline spacing
function pct(v) {
  return (v / axisMax.value) * 100
}

const started = ref(false)
const root = ref(null)
let io = null
onMounted(() => {
  // Replay whenever the slide scrolls into view (mirrors ProgressDonut).
  io = new IntersectionObserver(
    (entries) => {
      for (const e of entries) started.value = e.isIntersecting && e.intersectionRatio > 0.3
    },
    { threshold: [0, 0.3, 1] },
  )
  io.observe(root.value)
})
onBeforeUnmount(() => {
  if (io) io.disconnect()
})
</script>

<template>
  <div
    ref="root"
    class="rb-wrap"
    :class="{ started }"
    :style="{
      '--orig-dur': origDuration + 'ms',
      '--step': stepPct + '%',
    }"
  >
    <div class="rb-legend">
      <span class="rb-key"><i class="rb-sw rb-orig" />6.3.6 (original)</span>
      <span class="rb-key"><i class="rb-sw rb-ref" />7.0 (refactored)</span>
    </div>

    <div class="rb-rows">
      <div class="rb-row" v-for="d in items" :key="d.name">
        <div class="rb-label">{{ d.name }}</div>
        <div class="rb-track">
          <div class="rb-bar rb-orig" :style="{ width: (started ? pct(d.original) : 0) + '%' }" />
          <div
            class="rb-bar rb-ref"
            :style="{ width: (started && clicks >= revealAt ? pct(d.refactored) : 0) + '%' }"
          />
        </div>
      </div>
    </div>

    <div class="rb-axis">
      <span class="rb-axis-spacer" />
      <div class="rb-axis-scale">
        <span
          v-for="t in ticks"
          :key="t"
          class="rb-tick"
          :style="{ left: (t / axisMax) * 100 + '%' }"
          >{{ t }}</span
        >
      </div>
    </div>
    <div class="rb-xtitle">Calls / second</div>
  </div>
</template>

<style scoped>
.rb-wrap {
  --label-w: 150px;
  --col-gap: 12px;
  height: 100%;
  display: flex;
  flex-direction: column;
  font-family: var(--font-body);
}

/* legend */
.rb-legend {
  display: flex;
  justify-content: center;
  gap: 2.5rem;
  margin-bottom: 0.6rem;
  font-family: var(--font-subtitle);
  font-size: 17px;
  color: var(--slidev-theme-text);
}
.rb-key {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
}
.rb-sw {
  width: 18px;
  height: 12px;
  border-radius: 2px;
  display: inline-block;
}

/* rows fill the available height evenly */
.rb-rows {
  flex: 1;
  min-height: 0;
  display: flex;
  flex-direction: column;
}
.rb-row {
  flex: 1;
  min-height: 0;
  display: flex;
  align-items: center;
  gap: var(--col-gap);
}
.rb-label {
  flex: 0 0 var(--label-w);
  text-align: right;
  font-size: 14px;
  color: var(--slidev-theme-text);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.rb-track {
  flex: 1;
  height: 100%;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 3px;
  /* faint vertical gridlines at each 0.5 tick */
  background: repeating-linear-gradient(
    to right,
    #ededed 0,
    #ededed 1px,
    transparent 1px,
    transparent var(--step)
  );
}

.rb-bar {
  height: 7px;
  border-radius: 3px;
  width: 0;
  transition: width var(--orig-dur) cubic-bezier(0.22, 1, 0.36, 1);
}
.rb-orig {
  background: #9aa0a6;
}
.rb-ref {
  background: var(--slidev-theme-primary);
}
.rb-sw.rb-orig {
  background: #9aa0a6;
}
.rb-sw.rb-ref {
  background: var(--slidev-theme-primary);
}

/* axis */
.rb-axis {
  display: flex;
  gap: var(--col-gap);
  margin-top: 6px;
}
.rb-axis-spacer {
  flex: 0 0 var(--label-w);
}
.rb-axis-scale {
  flex: 1;
  position: relative;
  height: 18px;
}
.rb-tick {
  position: absolute;
  top: 0;
  transform: translateX(-50%);
  font-size: 13px;
  color: #777;
}
.rb-xtitle {
  padding-left: calc(var(--label-w) + var(--col-gap));
  text-align: center;
  font-family: var(--font-subtitle);
  font-size: 26px;
  font-weight: 700;
  color: var(--slidev-theme-text);
  margin-top: 2px;
}
</style>
