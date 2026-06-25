<script setup>
// ONE real measured example (Armadillo, median of 30 reps):
//   datashield.aggregate(cn, "dimDS('D')")
//   true server compute (endDate - startDate)        =  7.5 ms
//   client-observed (high-level call, 50 ms poll)    = 67.8 ms
// The server finishes in ~7.5 ms but the client doesn't look again until the
// next 50 ms poll boundary, then fetches — so it MEASURES ~68 ms.
const QUANTUM = 50 // ms — datashield.polling.sleep.0 default (0.05 s)
const SCALE = 7.3 // px per ms

const ex = {
  backend: 'Armadillo',
  command: 'datashield.aggregate(cn, "dimDS(\'D\')")',
  compute: 7.9, // server endDate - startDate
  client: 66.1, // high-level call, default 50 ms poll
}
const noticed = Math.ceil(ex.compute / QUANTUM) * QUANTUM // first poll that sees it done = 50
const px = (ms) => ms * SCALE + 'px'
const wasted = Math.round(((ex.client - ex.compute) / ex.client) * 100) // 89%
const ticks = [0, QUANTUM] // submit poll (not done) + 50 ms poll (done)
</script>

<template>
  <div class="pp-wrap">
    <div class="pp-cmd"><span class="pp-cmd-lbl">measured:</span> <code>{{ ex.command }}</code>
      <span class="pp-cmd-note">— {{ ex.backend }}, median of 30 reps</span></div>

    <div class="pp-row">
      <div class="pp-track" :style="{ width: px(ex.client) }">
        <!-- actual server work -->
        <div class="pp-seg pp-compute" :style="{ width: px(ex.compute) }">work</div>
        <!-- result exists, client still asleep until the next poll -->
        <div class="pp-seg pp-dead" :style="{ left: px(ex.compute), width: px(noticed - ex.compute) }">
          client asleep — result already done
        </div>
        <!-- fetch round trip after the poll sees completion -->
        <div class="pp-seg pp-fetch" :style="{ left: px(noticed), width: px(ex.client - noticed) }">fetch</div>

        <!-- poll boundaries -->
        <template v-for="t in ticks" :key="t">
          <div class="pp-tick" :style="{ left: px(t) }" />
          <div class="pp-tick-lbl" :style="{ left: px(t) }">{{ t === 0 ? 'poll: not done' : 'poll: done' }}</div>
        </template>

        <!-- measured end -->
        <div class="pp-end" :style="{ left: px(ex.client) }"><span class="pp-end-dot" /></div>
      </div>
    </div>

    <div class="pp-axis" :style="{ width: px(ex.client) }">
      <div class="pp-brace pp-brace-compute" :style="{ width: px(ex.compute) }">
        server compute <b>{{ ex.compute }} ms</b>
      </div>
      <div class="pp-brace pp-brace-client">client-observed <b>{{ ex.client }} ms</b></div>
    </div>

    <div class="pp-punch">
      <b>{{ wasted }}%</b> of the measured time is the client waiting on the 50 ms poll — not the server working
    </div>
  </div>
</template>

<style scoped>
.pp-wrap {
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 2rem;
  height: 100%;
}

.pp-cmd {
  text-align: center;
  font-family: var(--font-body);
  font-size: 14px;
  color: var(--slidev-theme-text);
}
.pp-cmd-lbl { font-family: var(--font-subtitle); color: #999; }
.pp-cmd code {
  font-family: var(--font-subtitle);
  font-size: 14px;
  color: var(--slidev-theme-primary);
  background: #f3f6fd;
  padding: 0.1rem 0.4rem;
  border-radius: 4px;
}
.pp-cmd-note { color: #999; font-size: 12.5px; }

.pp-row { display: flex; justify-content: center; }

.pp-track {
  position: relative;
  height: 38px;
}

.pp-seg {
  position: absolute;
  top: 0;
  height: 38px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-body);
  font-size: 11px;
  white-space: nowrap;
  border-radius: 4px;
}

.pp-compute { left: 0; background: var(--slidev-theme-primary); color: #fff; overflow: hidden; }

.pp-dead {
  background: repeating-linear-gradient(45deg,
    rgba(217, 83, 79, 0.18), rgba(217, 83, 79, 0.18) 6px,
    rgba(217, 83, 79, 0.32) 6px, rgba(217, 83, 79, 0.32) 12px);
  border: 1px dashed #d9534f;
  color: #b52b27;
}

.pp-fetch { background: #e6ecf7; color: #5b6b8c; border: 1px solid #cdd8ee; }

.pp-tick { position: absolute; top: -8px; width: 1px; height: 54px; background: #b9b9b9; }
.pp-tick-lbl {
  position: absolute;
  top: 46px;
  transform: translateX(-50%);
  font-family: var(--font-subtitle);
  font-size: 10px;
  color: #888;
  white-space: nowrap;
}

.pp-end { position: absolute; top: -8px; transform: translateX(-50%); }
.pp-end-dot {
  display: block;
  width: 10px; height: 10px;
  border-radius: 50%;
  background: var(--slidev-theme-accent);
  margin-top: -3px;
}

.pp-axis { position: relative; margin: 1.5rem auto 0 auto; height: 1.6rem; }
.pp-brace {
  position: absolute;
  top: 0;
  height: 1.6rem;
  font-family: var(--font-subtitle);
  font-size: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.pp-brace-compute {
  left: 0;
  border-left: 1px solid var(--slidev-theme-primary);
  border-right: 1px solid var(--slidev-theme-primary);
  border-top: 1px solid var(--slidev-theme-primary);
  border-radius: 4px 4px 0 0;
  color: var(--slidev-theme-primary);
  font-size: 11px;
}
.pp-brace-client {
  left: 0; right: 0;
  border-left: 1px solid var(--slidev-theme-text);
  border-right: 1px solid var(--slidev-theme-text);
  border-top: 1px solid var(--slidev-theme-text);
  border-radius: 4px 4px 0 0;
  color: var(--slidev-theme-text);
  margin-top: 0.7rem;
  height: 1.6rem;
}

.pp-punch {
  text-align: center;
  font-family: var(--font-body);
  font-size: 15px;
  color: #b52b27;
}
.pp-punch b { color: #b52b27; }
</style>
