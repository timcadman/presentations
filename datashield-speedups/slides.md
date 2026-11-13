---
theme: ../theme
title: DataSHIELD speed — next steps
info: Stepwise speed-ups after dsBase 7.0, dsWait in DSI and waiting on all servers at once
author: Tim Cadman
date: 2026-11-03
aspectRatio: '16/9'
publish: false
themeConfig:
  sections: [v7.0, dsWait, Together, Overall, Plan]
---

# Making DataSHIELD faster: next steps
From dsBase 7.0 to waiting on servers instead of polling them

<div class="author-info">
  <p><strong>Tim Cadman</strong></p>
</div>

<div class="title-logos">
  <img src="./public/molgenis-logo.png" class="logo-molgenis" />
  <img src="./public/umcg-logo.png" class="logo-umcg" />
</div>

---
layout: section
---

# v7.0: fewer round trips

---
layout: content
heading: Original vs refactored speed
subheading: dsBase / dsBaseClient 7.0
section: v7.0
---

<div style="display: flex; gap: 2rem; height: 100%;">
  <div style="flex: 1; min-width: 0;"><RatesBars :clicks="$clicks" /></div>
  <div style="flex: 0 0 22%; display: flex; flex-direction: column; justify-content: center;"><PerfStats :clicks="$clicks" :reveal-at="2" /></div>
</div>

<span v-click style="display:none" />
<span v-click style="display:none" />

---
layout: content-two-cols
heading: Where the time goes now
subheading: Waiting, not computing
section: v7.0
---

<template #left>

- Every server call: submit, ask "done?", **sleep 50 ms**, ask again, then fetch
- A fast call is finished long before the client looks
- DSI asks the servers **one after another**: 5 servers = 5 round trips per step

</template>

<template #right>

<PollPenalty :rows="[{ name: 'Fast call', compute: 8, fast: true }]" />

</template>

---
layout: section
---

# Step 1: dsWait

---
layout: content-two-cols
heading: Ask once and wait
subheading: The server answers when the result is ready
section: dsWait
---

<template #left>

- **DSI:** new generic `dsWait(res, timeout)`; no sleep for connections that can wait
- **Armadillo:** `GET /lastresult` holds the request until done (`Prefer: wait=10`, at most 20 s)
- **DSMolgenisArmadillo:** implements `dsWait`
- Older servers and drivers keep polling, unchanged

</template>

<template #right>

<div class="req-box">
  <div class="req-title">Today</div>
  <code>POST /execute</code><br>
  <code>GET /lastcommand</code> … sleep … <code>GET /lastcommand</code><br>
  <code>GET /lastresult</code>
</div>

<div class="req-box req-new">
  <div class="req-title">dsWait</div>
  <code>POST /execute</code><br>
  <code>GET /lastresult</code> (held until done)
</div>

<style>
.req-box { border-left: 5px solid #9AA0A6; padding: 0.6rem 1rem; margin-bottom: 1.2rem; background: #f6f6f6; border-radius: 6px; font-size: 15px; line-height: 1.8; }
.req-new { border-left-color: #0097A7; background: color-mix(in srgb, #0097A7 8%, white); }
.req-title { font-family: var(--font-subtitle); font-weight: 600; margin-bottom: 0.2rem; }
.req-box code { background: none; color: var(--slidev-theme-text); padding: 0; }
</style>

</template>

---
layout: content
heading: 'Step 1: dsWait'
subheading: 7.0 polling vs 7.0 with dsWait
section: dsWait
---

<StepBars :clicks="$clicks" :show="['v70', 'wait']" :ratio="['v70', 'wait']" />

<span v-click style="display:none" />

---
layout: section
---

# Step 2: ask all servers at once

---
layout: content-two-cols
heading: Ask all servers at once
subheading: One wait instead of one per server
section: Together
---

<template #left>

- Today DSI waits on server 1, then server 2, …
- **DSI:** new generic `dsWaitAll(conn, results, timeout)`; the default keeps waiting one at a time
- **DSMolgenisArmadillo:** sends all waits at the same time (`httr2::req_perform_parallel`)
- Needs DSMolgenisArmadillo to move from httr to httr2 first

</template>

<template #right>

<div class="lane-title">One at a time</div>
<div class="lane"><span v-for="i in 5" :key="i" class="hop">server {{ i }}</span></div>

<div class="lane-title">Together</div>
<div class="lane lane-col"><span v-for="i in 5" :key="i" class="hop hop-new">server {{ i }}</span></div>

<style>
.lane-title { font-family: var(--font-subtitle); font-weight: 600; margin: 0.6rem 0 0.4rem; }
.lane { display: flex; gap: 4px; margin-bottom: 1rem; }
.lane-col { flex-direction: column; width: 20%; }
.hop { flex: 0 0 20%; padding: 0.3rem 0; text-align: center; font-size: 12px; border-radius: 4px; background: color-mix(in srgb, #0097A7 15%, white); border: 1px solid #0097A7; }
.hop-new { flex: none; background: color-mix(in srgb, #E6B96A 25%, white); border-color: #B9852A; }
</style>

</template>

---
layout: content
heading: 'Step 2: together'
subheading: dsWait vs dsWait + all servers at once
section: Together
---

<StepBars :clicks="$clicks" :show="['wait', 'together']" :ratio="['wait', 'together']" />

<span v-click style="display:none" />

---
layout: section
---

# Overall

---
layout: content
heading: All steps vs 6.3.5
subheading: 'All five calls together: 12.2 s → 3.4 s (3.6×)'
section: Overall
---

<StepBars :clicks="$clicks" :show="['v635', 'v70', 'wait', 'together']" :ratio="['v635', 'together']" />

<span v-for="i in 3" :key="i" v-click style="display:none" />

---
layout: content
heading: Plan
subheading: Each step is released and usable on its own
section: Plan
---

<v-clicks>

1. **dsWait** (Armadillo, DSI, DSMolgenisArmadillo), released together
2. **DSMolgenisArmadillo on httr2**, no change in behaviour
3. **dsWaitAll** (DSI, DSMolgenisArmadillo)

</v-clicks>

<div v-click style="margin-top: 1.5rem;">

**Asking for:** sign-off to start step 1, and to discuss the `dsWaitAll` design with the DSI maintainers

</div>

---
layout: content
heading: How this was measured
section: Plan
---

- 5 Armadillo servers on one laptop, each with **+25 ms each way** of added network delay
- dsBase / dsBaseClient 7.0-dev; 6.3.5 runs with DSI and DSMolgenisArmadillo as released
- Median of 25 runs per call; results identical across all versions
- Real sites differ in speed: with step 2 the slowest server sets the pace
