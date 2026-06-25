<script setup>
// Stacked breakdown of client-observed time per backend:
//   compute (true server work)  +  network (round-trip)  +  poll-wait (DSI 50 ms sleep)
// Values are ms. `rows` = [{ backend, compute, network, poll }]
import { computed } from 'vue'

const props = defineProps({
  rows: { type: Array, required: true },
})

const seg = [
  { key: 'compute', label: 'server compute', color: '#4285F4' },
  { key: 'network', label: 'network round-trip', color: '#0097A7' },
  { key: 'poll', label: 'poll-wait (50 ms sleep)', color: '#d9534f' },
]

const total = (r) => r.compute + r.network + r.poll
const maxTotal = computed(() => Math.max(...props.rows.map(total)))
const pct = (v) => (v / maxTotal.value) * 100
const pollShare = (r) => Math.round((r.poll / total(r)) * 100)
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
            :style="{ width: pct(r[s.key]) + '%', background: s.color }"
          >
            <span v-if="pct(r[s.key]) > 6" class="ls-seg-lbl">{{ r[s.key] }}</span>
          </div>
          <span class="ls-total">{{ total(r) }} ms · poll = {{ pollShare(r) }}%</span>
        </div>
      </div>
    </div>

    <div class="ls-note">
      For fast ops the <b style="color:#d9534f">poll-wait</b> is the dominant slice of
      client-observed time — the server has already answered.
    </div>
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
.ls-name { width: 11rem; text-align: right; flex-shrink: 0; }
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
.ls-seg-lbl { font-family: var(--font-subtitle); font-size: 11px; color: #fff; }
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
}
</style>
