<script setup>
// Stacked breakdown of the remote round-trip per backend:
//   compute (server R work) + system overhead + network latency (ms).
// `rows` = [{ backend, compute, overhead, network }]. Overhead is taken from the
// localhost round-trip (network ~ 0 there); network is the remainder.
import { computed } from 'vue'

const props = defineProps({
  rows: { type: Array, required: true },
  note: { type: String, default: '' },
})

const seg = [
  { key: 'compute',  label: 'server compute', color: '#E6B96A' },
  { key: 'overhead', label: 'system overhead', color: '#0097A7' },
  { key: 'network',  label: 'network',         color: '#1E3A5F' },
]

const total = (r) => r.compute + r.overhead + r.network
const maxTotal = computed(() => Math.max(...props.rows.map(total)))
const pct = (v) => (v / maxTotal.value) * 100
</script>

<template>
  <div class="ls-wrap">
    <div class="ls-legend">
      <span v-for="s in seg" :key="s.key" class="ls-leg-item">
        <span class="ls-swatch" :style="{ background: s.color }" />{{ s.label }}
      </span>
    </div>

    <div class="ls-chart">
      <div v-for="r in rows" :key="r.backend" class="ls-row">
        <div class="ls-name"><code>{{ r.backend }}</code></div>
        <div class="ls-track">
          <div
            v-for="s in seg"
            :key="s.key"
            class="ls-seg"
            :style="{ width: pct(r[s.key]) + '%', background: s.color, color: s.key === 'compute' ? '#5c4410' : '#fff' }"
          >
            <span v-if="pct(r[s.key]) > 7" class="ls-seg-lbl">{{ s.key === 'network' ? '~' + r[s.key] : r[s.key] }}</span>
          </div>
          <span class="ls-total">{{ Math.round(total(r)) }} ms</span>
        </div>
      </div>
    </div>

    <div v-if="note" class="ls-note" v-html="note" />
  </div>
</template>

<style scoped>
.ls-wrap {
  display: flex;
  flex-direction: column;
  height: 100%;
  justify-content: center;
  gap: 1.5rem;
}
.ls-legend {
  display: flex;
  justify-content: center;
  gap: 1.75rem;
  font-family: var(--font-subtitle);
  font-size: 13px;
}
.ls-leg-item { display: inline-flex; align-items: center; gap: 0.4rem; }
.ls-swatch { width: 14px; height: 14px; border-radius: 3px; display: inline-block; }

.ls-chart { display: flex; flex-direction: column; gap: 1.1rem; }
.ls-row { display: flex; align-items: center; gap: 1rem; }
.ls-name { width: 14rem; text-align: right; flex-shrink: 0; }
.ls-name code { font-family: var(--font-subtitle); font-size: 14px; color: var(--slidev-theme-primary); }

.ls-track { position: relative; flex: 1; display: flex; height: 28px; }
.ls-seg {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}
.ls-seg:first-child { border-radius: 4px 0 0 4px; }
.ls-seg-lbl { font-family: var(--font-subtitle); font-size: 11px; }
.ls-total {
  position: absolute;
  left: 100%;
  top: 50%;
  transform: translateY(-50%);
  margin-left: 0.6rem;
  font-family: var(--font-subtitle);
  font-size: 12px;
  color: #555;
  white-space: nowrap;
}

.ls-note {
  text-align: center;
  font-family: var(--font-body);
  font-size: 14px;
  color: #777;
  line-height: 1.4;
}
</style>
