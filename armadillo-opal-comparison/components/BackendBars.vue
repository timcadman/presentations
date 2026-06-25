<script setup>
// Grouped horizontal-bar chart across the 3 backends.
// `rows` = [{ op: 'dimDS', values: { 'armadillo-rserve': 1, 'armadillo-rock': 7, 'opal-rock': 9 } }]
import { computed } from 'vue'

const props = defineProps({
  rows: { type: Array, required: true },
  unit: { type: String, default: 'ms' },
  // fixed backend order + colours
  backends: {
    type: Array,
    default: () => [
      { key: 'armadillo-rserve', label: 'armadillo-rserve', color: '#0097A7' },
      { key: 'armadillo-rock', label: 'armadillo-rock', color: '#4285F4' },
      { key: 'opal-rock', label: 'opal-rock', color: '#9aa7c7' },
    ],
  },
})

const maxVal = computed(() => {
  let m = 0
  for (const r of props.rows)
    for (const b of props.backends) {
      const v = r.values[b.key]
      if (typeof v === 'number' && v > m) m = v
    }
  return m || 1
})

const pct = (v) => (typeof v === 'number' ? (v / maxVal.value) * 100 : 0)
</script>

<template>
  <div class="bb-wrap">
    <div class="bb-legend">
      <span v-for="b in backends" :key="b.key" class="bb-leg-item">
        <span class="bb-swatch" :style="{ background: b.color }" />{{ b.label }}
      </span>
    </div>

    <div class="bb-chart">
      <div v-for="r in rows" :key="r.op" class="bb-group">
        <div class="bb-op"><code>{{ r.op }}</code></div>
        <div class="bb-bars">
          <div v-for="b in backends" :key="b.key" class="bb-bar-row">
            <div class="bb-bar" :style="{ width: pct(r.values[b.key]) + '%', background: b.color }">
              <span class="bb-val">{{ r.values[b.key] }}{{ unit }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.bb-wrap {
  display: flex;
  flex-direction: column;
  height: 100%;
  gap: 0.75rem;
}
.bb-legend {
  display: flex;
  justify-content: center;
  gap: 1.5rem;
  font-family: var(--font-subtitle);
  font-size: 13px;
  color: var(--slidev-theme-text);
}
.bb-leg-item { display: inline-flex; align-items: center; gap: 0.4rem; }
.bb-swatch { width: 14px; height: 14px; border-radius: 3px; display: inline-block; }

.bb-chart {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 0.9rem;
}
.bb-group { display: flex; align-items: center; gap: 1rem; }
.bb-op {
  width: 11rem;
  text-align: right;
  flex-shrink: 0;
}
.bb-op code {
  font-family: var(--font-subtitle);
  font-size: 13px;
  color: var(--slidev-theme-primary);
}
.bb-bars { flex: 1; display: flex; flex-direction: column; gap: 3px; }
.bb-bar-row { display: flex; align-items: center; }
.bb-bar {
  height: 16px;
  min-width: 2px;
  border-radius: 0 3px 3px 0;
  display: flex;
  align-items: center;
}
.bb-val {
  font-family: var(--font-subtitle);
  font-size: 11px;
  color: #555;
  margin-left: 6px;
  white-space: nowrap;
}
</style>
