<script setup>
// Client-side polling penalty: the DSI loop submits an async op, then polls
// "is it done?" — but after the first (immediate) poll it sleeps a flat 50ms
// between checks. Completion is only *noticed* at a poll boundary, so measured
// time rounds up to the next 50ms tick. Fast ops pay almost a whole quantum of
// dead time; slow ops barely notice.
const QUANTUM = 50 // ms — datashield.polling.sleep.0 default (0.05s)
const SCALE = 2.4 // px per ms

defineProps({
  rows: {
    type: Array,
    default: () => [
      { name: 'Armadillo', compute: 8, fast: true },
      { name: 'Opal', compute: 170, fast: false },
    ],
  },
})

const noticed = (c) => Math.ceil(c / QUANTUM) * QUANTUM // next poll boundary
const ticks = (c) => {
  const out = []
  for (let t = 0; t <= noticed(c); t += QUANTUM) out.push(t)
  return out
}
const px = (ms) => ms * SCALE + 'px'
const wasted = (c) => Math.round(((noticed(c) - c) / noticed(c)) * 100)
</script>

<template>
  <div class="pp-wrap">
    <div v-for="row in rows" :key="row.name" class="pp-row" :class="{ 'pp-fast': row.fast }">
      <div class="pp-side">
        <div class="pp-name">{{ row.name }}</div>
        <div class="pp-real">real compute ≈ {{ row.compute }}&nbsp;ms</div>
      </div>

      <div class="pp-track-area">
        <div class="pp-track" :style="{ width: px(noticed(row.compute)) }">
          <!-- actual server work -->
          <div class="pp-compute" :style="{ width: px(row.compute) }">work</div>
          <!-- dead time: result exists, client still asleep -->
          <div
            class="pp-dead"
            :style="{ left: px(row.compute), width: px(noticed(row.compute) - row.compute) }"
          >
            <span v-if="row.fast">client asleep — result already done</span>
          </div>

          <!-- poll boundaries (every 50ms = one sleep) -->
          <template v-for="t in ticks(row.compute)" :key="t">
            <div class="pp-tick" :style="{ left: px(t) }" />
            <div class="pp-tick-lbl" :style="{ left: px(t) }">{{ t }}</div>
          </template>

          <!-- where the client first SEES completion -->
          <div class="pp-noticed" :style="{ left: px(noticed(row.compute)) }">
            <span class="pp-noticed-dot" />
            <span class="pp-noticed-lbl">noticed</span>
          </div>
        </div>

        <div class="pp-measured" :style="{ width: px(noticed(row.compute)) }">
          measured ≈ {{ noticed(row.compute) }}&nbsp;ms
          <span class="pp-waste">· {{ wasted(row.compute) }}% wasted waiting</span>
        </div>
      </div>
    </div>

    <div class="pp-key">
      submit <code>POST /execute</code> → poll <code>GET /lastcommand</code> (immediate, then every {{ QUANTUM }}&nbsp;ms) → <code>GET /lastresult</code>
    </div>
  </div>
</template>

<style scoped>
.pp-wrap {
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 2.75rem;
  height: 100%;
  padding-top: 0.5rem;
}

.pp-row {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.pp-side {
  width: 11rem;
  flex: none;
  text-align: right;
}

.pp-name {
  font-family: var(--font-subtitle);
  font-size: 18px;
  font-weight: 600;
  color: #999;
}

.pp-fast .pp-name { color: var(--slidev-theme-primary); }

.pp-real {
  font-family: var(--font-body);
  font-size: 12px;
  color: var(--slidev-theme-text);
}

.pp-track-area {
  display: flex;
  flex-direction: column;
  gap: 0.55rem;
}

.pp-track {
  position: relative;
  height: 30px;
}

.pp-compute {
  position: absolute;
  top: 0;
  left: 0;
  height: 30px;
  background: #bbb;
  border-radius: 4px;
  font-family: var(--font-body);
  font-size: 11px;
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.pp-fast .pp-compute { background: var(--slidev-theme-primary); }

.pp-dead {
  position: absolute;
  top: 0;
  height: 30px;
  border-radius: 4px;
  background: repeating-linear-gradient(
    45deg,
    rgba(217, 83, 79, 0.18),
    rgba(217, 83, 79, 0.18) 6px,
    rgba(217, 83, 79, 0.32) 6px,
    rgba(217, 83, 79, 0.32) 12px
  );
  border: 1px dashed #d9534f;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-body);
  font-size: 10.5px;
  color: #b52b27;
  white-space: nowrap;
}

.pp-tick {
  position: absolute;
  top: -7px;
  width: 1px;
  height: 44px;
  background: #cfcfcf;
}

.pp-tick-lbl {
  position: absolute;
  top: 38px;
  transform: translateX(-50%);
  font-family: var(--font-subtitle);
  font-size: 9.5px;
  color: #aaa;
}

.pp-noticed {
  position: absolute;
  top: -7px;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
}

.pp-noticed-dot {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: var(--slidev-theme-accent);
  margin-top: -3px;
}

.pp-noticed-lbl {
  position: absolute;
  top: -16px;
  font-family: var(--font-subtitle);
  font-size: 10px;
  color: var(--slidev-theme-accent);
}

.pp-measured {
  position: relative;
  height: 1.4rem;
  border-left: 1px solid var(--slidev-theme-text);
  border-right: 1px solid var(--slidev-theme-text);
  border-top: 1px solid var(--slidev-theme-text);
  border-radius: 4px 4px 0 0;
  font-family: var(--font-subtitle);
  font-size: 12px;
  color: var(--slidev-theme-text);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 1.1rem;
}

.pp-waste { color: #b52b27; margin-left: 0.4rem; }

.pp-key {
  text-align: center;
  font-family: var(--font-body);
  font-size: 12.5px;
  color: #777;
  margin-top: 0.5rem;
}

.pp-key code {
  font-family: var(--font-subtitle);
  font-size: 11.5px;
  color: var(--slidev-theme-primary);
  background: #f3f6fd;
  padding: 0.05rem 0.3rem;
  border-radius: 3px;
}
</style>
