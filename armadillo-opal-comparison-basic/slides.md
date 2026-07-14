---
theme: ../theme
title: Armadillo vs Opal — DataSHIELD benchmark
info: Comparing DataSHIELD performance across Armadillo and Opal backends
author: Tim Cadman
date: 2026-06-25
aspectRatio: '16/9'
publish: false
themeConfig:
  sections: [Background, Methods, Results, Conclusions]
---

# Armadillo vs Opal

Performance benchmark

<div class="title-logos">
  <img src="./public/molgenis-logo.png" class="logo-molgenis" />
</div>

---
layout: section
---

# Background


---
layout: content
heading: Why benchmark?
section: Background
---

<v-clicks>

- We **assume** that Armadillo is faster than Opal — but we haven't systematically measured it
- We know Armadillo is more light-weight, but again we have not measured it
- Leon (NCC) asked for benchmarks to help choose between Armadillo and Opal
- Stats could be useful in the future when marketting Armadillo

</v-clicks>

---
layout: content
heading: Objectives
subheading: 'To test the following:'
section: Background
---

<ProcessCards size="lg" direction="column" :clicks="$clicks" :groups="[
  { steps: [
    { title: 'Footprint', desc: 'Resting memory and on-disk storage efficiency' },
    { title: 'Speed', desc: 'How fast Armadillo (Rock) and Opal are when deployed' },
  ] }
]" />

<span v-for="i in 1" :key="i" v-click style="display:none" />

---
layout: section
---

# Methods


---
layout: content
heading: Servers tested
section: Methods
---

<table class="srv-tbl">
<thead><tr><th>Server</th><th>R engine</th><th>Host</th><th>Version</th><th>Spec</th></tr></thead>
<tbody>
<tr v-click="1"><td><b>Armadillo</b></td><td>Rock</td><td>armadillo-demo.molgenis.net</td><td>5.12.2</td><td>2 vCPU · 8 GiB</td></tr>
<tr v-click="1"><td><b>Armadillo</b></td><td>Rock</td><td>localhost</td><td>5.14.0-SNAPSHOT</td><td>2 vCPU · 8 GiB</td></tr>
<tr v-click="2"><td><b>Opal</b></td><td>Rock</td><td>opal.molgeniscloud.org</td><td>5.7.2</td><td>2 vCPU · 8 GiB</td></tr>
<tr v-click="2"><td><b>Opal</b></td><td>Rock</td><td>localhost</td><td>5.7.1</td><td>2 vCPU · 8 GiB</td></tr>
</tbody>
</table>

<div class="srv-note">All R engines ran <b>dsBase 6.3.5</b>; client <b>dsBaseClient 6.3.0</b>.</div>

<style scoped>
.srv-tbl { border-collapse: collapse; width: 100%; margin-top: 0.9rem; }
.srv-tbl th, .srv-tbl td { font-size: 15px; padding: 0.42rem 0.6rem; border-bottom: 1px solid #e3e8f2; text-align: left; }
.srv-tbl th { font-family: var(--font-subtitle); color: var(--slidev-theme-primary); border-bottom: 2px solid var(--slidev-theme-primary); }
.srv-note { margin-top: 0.9rem; font-size: 12px; color: #667; }
</style>

---
layout: content
heading: Footprint
subheading: 'What was measured and how'
section: Methods
---

<table class="fp-tbl">
<thead><tr><th>Metric</th><th>Armadillo</th><th>Opal</th></tr></thead>
<tbody>
<tr v-click><td><b>Resting memory</b></td><td>Armadillo + Rock engine</td><td>Opal + MongoDB + Rock engine</td></tr>
<tr v-click><td><b>Data on disk</b></td><td>Example 10,000-row data, stored as Parquet</td><td>Same data file, stored in MongoDB</td></tr>
</tbody>
</table>

<div v-click class="fp-note">
<b>How (idle):</b> <b>Memory</b> — containers via <code>docker stats</code> (RSS); Armadillo server (host JVM) via <code>vmmap</code> physical footprint. <b>Disk</b> — <code>du</code> per store.
</div>

<style scoped>
.fp-tbl { border-collapse: collapse; width: 100%; margin-top: 0.9rem; }
.fp-tbl th, .fp-tbl td { font-size: 14px; padding: 0.42rem 0.55rem; border-bottom: 1px solid #e3e8f2; text-align: left; vertical-align: top; }
.fp-tbl th { font-family: var(--font-subtitle); color: var(--slidev-theme-primary); border-bottom: 2px solid var(--slidev-theme-primary); }
.fp-tbl code { font-size: 12.5px; }
.fp-tbl .sub { color: #8a94a6; font-size: 11px; font-weight: normal; }
.fp-note { margin-top: 1rem; font-size: 12px; color: #667; line-height: 1.55; }
.fp-note code { font-size: 11px; }
</style>

---
layout: content
heading: Speed
subheading: Where the time goes
section: Methods
---

<div class="lead">
  <span v-if="$clicks < 5">The client-observed <b style="color:#333">round-trip</b> of a call is a layer of operations:</span>
  <span v-else>Each element was measured as follows:</span>
</div>

<div class="ld" :class="{ shown: $clicks >= 5 }">
  <div class="ld-bar">
    <div class="seg" :class="{ on: $clicks >= 1 }" style="flex:2.4;--c:#1E3A5F"><b>Network</b><small>round-trips on the wire</small></div>
    <div class="seg" :class="{ on: $clicks >= 2 }" style="flex:1.5;--c:#0097A7"><b>System overhead</b><small>serialise · protocol · dispatch · auth</small></div>
    <div class="seg" :class="{ on: $clicks >= 3 }" style="flex:1.1;--c:#E6B96A;--tc:#5c4410"><b>Server compute</b><small>the function runs in R</small></div>
    <div class="seg" :class="{ on: $clicks >= 4 }" style="flex:1.0;--c:#6A4C93"><b>Polling delay</b><small>client waits between async&nbsp;status&nbsp;checks</small></div>
  </div>
  <div class="ld-cap" :class="{ hide: $clicks >= 5 }">═══ round-trip time ═══</div>

  <div class="ld-cards">
    <div class="mcard">
      <div class="ml" style="border-color:#E6B96A"><div class="mname" style="color:#B9852A">Server compute</div><div class="mdesc">the function runs in R</div></div>
      <div class="mr"><div>command end &ensp;−&ensp; start<div class="fetch"><b>Armadillo</b> <code>GET /lastcommand</code> &ensp;·&ensp; <b>Opal</b> <code>GET /datashield/…/command/{id}</code></div></div></div>
    </div>
    <div class="mcard">
      <div class="ml" style="border-color:#0097A7"><div class="mname" style="color:#0097A7">System overhead</div><div class="mdesc">serialise · protocol · dispatch · auth</div></div>
      <div class="mr"><span style="color:#333">(localhost round-trip)</span> &ensp;−&ensp; <span style="color:#B9852A">compute</span></div>
    </div>
    <div class="mcard">
      <div class="ml" style="border-color:#1E3A5F"><div class="mname" style="color:#1E3A5F">Network</div><div class="mdesc">round-trips on the wire</div></div>
      <div class="mr"><span style="color:#333">(remote round-trip)</span> &ensp;−&ensp; <span style="color:#B9852A">compute</span> &ensp;−&ensp; <span style="color:#0097A7">overhead</span></div>
    </div>
    <div class="mcard">
      <div class="ml" style="border-color:#6A4C93"><div class="mname" style="color:#6A4C93">Polling delay</div><div class="mdesc">client waits between async&nbsp;status&nbsp;checks</div></div>
      <div class="mr">DSI poll-sleep fixed at 2 ms (0.002 s)</div>
    </div>
  </div>
</div>

<span v-for="i in 5" :key="i" v-click style="display:none" />

<style scoped>
.lead { font-size: 15px; color: #445; margin: 0.2rem 0 0; }
.lead .hint { color: #9aa4b0; font-style: italic; }
.ld { margin-top: 0.7rem; }
.ld-bar { display: flex; border-radius: 8px; overflow: hidden; box-shadow: 0 1px 5px rgba(0, 0, 0, 0.13); background: #eef1f6; max-height: 8rem; opacity: 1; transition: max-height 0.45s ease, opacity 0.3s ease; }
.ld.shown .ld-bar { max-height: 0; opacity: 0; box-shadow: none; }
.seg { min-width: 0; padding: 1rem 0.85rem; text-align: center; display: flex; flex-direction: column; gap: 0.28rem; background: transparent; color: transparent; transition: background 0.4s ease, color 0.4s ease; }
.seg.on { background: var(--c); color: var(--tc, #fff); }
.seg b { font-family: var(--font-subtitle); font-size: 1rem; line-height: 1.2; }
.seg small { font-size: 0.8rem; line-height: 1.25; }
.ld-cap { text-align: center; color: #333; font-family: var(--font-subtitle); font-size: 0.9rem; letter-spacing: 0.04em; margin-top: 0.6rem; max-height: 2rem; opacity: 1; overflow: hidden; transition: opacity 0.3s ease, max-height 0.4s ease, margin 0.4s ease; }
.ld-cap.hide { opacity: 0; max-height: 0; margin-top: 0; }
.ld-cards { display: flex; flex-direction: column; gap: 0.45rem; max-width: 54rem; max-height: 0; overflow: hidden; transition: max-height 0.55s ease; }
.ld.shown .ld-cards { max-height: 40rem; }
.mcard { display: flex; align-items: stretch; border: 1px solid #e3e8f2; border-radius: 8px; overflow: hidden; background: #fff; opacity: 0; transform: translateY(14px); transition: opacity 0.45s ease, transform 0.45s ease; }
.ld.shown .mcard { opacity: 1; transform: none; }
.ld.shown .mcard:nth-child(1) { transition-delay: 0.15s; }
.ld.shown .mcard:nth-child(2) { transition-delay: 0.27s; }
.ld.shown .mcard:nth-child(3) { transition-delay: 0.39s; }
.ld.shown .mcard:nth-child(4) { transition-delay: 0.51s; }
.ml { flex: 0 0 13.5rem; border-left: 6px solid; padding: 0.38rem 0.85rem; background: #fafbfe; }
.mname { font-family: var(--font-subtitle); font-weight: 600; font-size: 13.5px; }
.mdesc { font-size: 10.5px; color: #8a94a6; margin-top: 0.1rem; }
.mr { flex: 1; display: flex; align-items: center; padding: 0.38rem 0.9rem; font-size: 13px; color: #556; }
.fetch { margin-top: 0.22rem; font-family: var(--font-subtitle); font-size: 10px; color: #8a94a6; }
.fetch b { color: #667; font-weight: 600; }
.fetch code { font-size: 9.5px; color: #556; }
</style>

---
layout: content
heading: Performance
subheading: Functions benchmarked
section: Methods
---
Speed was benchmarked using the following common functions:
<table class="fn-tbl">
<thead><tr><th>Family</th><th>n</th><th>Functions (dsBase server function)</th></tr></thead>
<tbody>
<tr><td><b>Summary statistics</b></td><td>5</td><td><code>meanDS</code> · <code>varDS</code> · <code>quantileMeanDS</code> · <code>corDS</code> · <code>tableDS</code></td></tr>
<tr><td><b>Metadata / introspection</b></td><td>8</td><td><code>classDS</code> · <code>dimDS</code> · <code>colnamesDS</code> · <code>lengthDS</code> · <code>levelsDS</code> · <code>numNaDS</code> · <code>lsDS</code> · <code>isValidDS</code></td></tr>
<tr><td><b>Transform &amp; recode</b></td><td>11</td><td><code>asFactorDS1</code> · <code>asFactorDS2</code> · <code>asIntegerDS</code> · <code>asCharacterDS</code> · <code>asDataMatrixDS</code> · <code>BooleDS</code> · <code>recodeValuesDS</code> · <code>recodeLevelsDS</code> · <code>changeRefGroupDS</code> · <code>repDS</code> · <code>replaceNaDS</code></td></tr>
<tr><td><b>Data-frame manipulation</b></td><td>6</td><td><code>dataFrameDS</code> · <code>dataFrameSubsetDS1</code> · <code>dataFrameSubsetDS2</code> · <code>cbindDS</code> · <code>mergeDS</code> · <code>reShapeDS</code></td></tr>
<tr><td><b>Modelling</b></td><td>5</td><td><code>glmDS1</code> · <code>glmDS2</code> · <code>glmSLMADS1</code> · <code>glmSLMADS.assign</code> · <code>lmerSLMADS2</code></td></tr>
<tr><td><b>DSI</b></td><td>9</td><td><code>rmDS</code> · <code>login</code> · <code>workspace_save</code> · <code>workspace_load</code> · <code>assign.table</code> · <code>tables</code> · <code>profiles</code> · <code>workspaces</code> · <code>pkg_status</code></td></tr>
</tbody>
</table>

<style scoped>
.fn-tbl { border-collapse: collapse; width: 100%; margin-top: 0.5rem; }
.fn-tbl th, .fn-tbl td { font-size: 11px; padding: 0.24rem 0.42rem; line-height: 1.3; border-bottom: 1px solid #e3e8f2; text-align: left; vertical-align: top; }
.fn-tbl th { font-family: var(--font-subtitle); color: var(--slidev-theme-primary); border-bottom: 2px solid var(--slidev-theme-primary); }
.fn-tbl code { font-size: 10.5px; }
</style>

---
layout: content
heading: Performance
subheading: Repeats & shuffling
section: Methods
---

Each call was timed over <b>5 shuffled passes</b> — every pass randomises the call order, then repeats each call <b>5 times</b>:

<div v-click class="passes">
  <div class="pcard">
    <div class="ph">Pass 1</div>
    <div class="ord"><span style="background:#E6B96A"></span><span style="background:#4285F4"></span><span style="background:#1E3A5F"></span><span style="background:#0097A7"></span><span style="background:#6A4C93"></span></div>
    <div class="pr">×5 reps</div>
  </div>
  <div class="pcard">
    <div class="ph">Pass 2</div>
    <div class="ord"><span style="background:#4285F4"></span><span style="background:#6A4C93"></span><span style="background:#0097A7"></span><span style="background:#1E3A5F"></span><span style="background:#E6B96A"></span></div>
    <div class="pr">×5 reps</div>
  </div>
  <div class="pcard">
    <div class="ph">Pass 3</div>
    <div class="ord"><span style="background:#0097A7"></span><span style="background:#1E3A5F"></span><span style="background:#E6B96A"></span><span style="background:#6A4C93"></span><span style="background:#4285F4"></span></div>
    <div class="pr">×5 reps</div>
  </div>
  <div class="pcard">
    <div class="ph">Pass 4</div>
    <div class="ord"><span style="background:#6A4C93"></span><span style="background:#E6B96A"></span><span style="background:#4285F4"></span><span style="background:#1E3A5F"></span><span style="background:#0097A7"></span></div>
    <div class="pr">×5 reps</div>
  </div>
  <div class="pcard">
    <div class="ph">Pass 5</div>
    <div class="ord"><span style="background:#1E3A5F"></span><span style="background:#0097A7"></span><span style="background:#6A4C93"></span><span style="background:#E6B96A"></span><span style="background:#4285F4"></span></div>
    <div class="pr">×5 reps</div>
  </div>
</div>

<style scoped>
.passes { display: flex; gap: 1rem; justify-content: center; margin: 1.4rem 0 0.6rem; }
.pcard { flex: 1; max-width: 8.5rem; border: 1px solid #dce3ef; border-radius: 10px; padding: 0.8rem 0.7rem; display: flex; flex-direction: column; align-items: center; gap: 0.7rem; background: #fafbfe; }
.ph { font-family: var(--font-subtitle); font-weight: 600; color: var(--slidev-theme-primary); font-size: 14px; }
.ord { display: flex; flex-direction: column; gap: 0.34rem; width: 100%; }
.ord span { display: block; height: 14px; border-radius: 4px; }
.pr { font-family: var(--font-subtitle); font-size: 12.5px; color: #8a94a6; }
.pleg { text-align: center; font-size: 11.5px; color: #9aa4b0; margin-top: 0.5rem; font-family: var(--font-subtitle); }
</style>

---
layout: section
---

# Results


---
layout: content
heading: Footprint
section: Results
subheading: Memory and disk space
---

<div class="fit">
  <div class="res-figs">
    <img v-click src="./public/res_memory.png" />
    <img v-click src="./public/res_storage.png" />
  </div>
</div>

---
layout: content
heading: Speed
subheading: Armadillo speed vs Opal
section: Results
---

<div class="corner-note">
  <div class="leg">
    <span><span class="k" style="background:#4285F4"></span>Armadillo</span>
  </div>
  <div class="formula">Opal round-trip ÷ Armadillo round-trip · log₂ scale</div>
</div>

<div class="fit">
  <div class="res-figs left">
    <img v-click src="./public/total_local.png" />
    <img v-click src="./public/total_remote.png" />
  </div>
</div>

---
layout: content
heading: Speed
subheading: DSI variance
section: Results
---

<div class="corner-note">
  <div class="leg">
    <span><span class="k" style="background:#4285F4"></span>Armadillo</span>
  </div>
  <div class="formula">Opal round-trip ÷ Armadillo round-trip · log₂ scale</div>
</div>

<div class="fit">
  <div class="res-figs left">
    <img v-click src="./public/session_local.png" />
    <img v-click src="./public/session_remote.png" />
  </div>
</div>

---
layout: content
heading: Speed
subheading: Where is Armadillo faster?
section: Results
---

<LatencyStack note="median total time (ms) per operation" :rows="[
  { backend: 'opal · remote', compute: 9.0, overhead: 72.3, network: 157.5 },
  { backend: 'armadillo-rock · remote', compute: 4.6, overhead: 21.4, network: 158.3 },
]"/>

---
layout: section
---

# Conclusions


---
layout: content
heading: Conclusions
section: Conclusions
---

<v-clicks>

- **Armadillo is faster than Opal** — locally **~3×** ; remotely **~1.2×**
- Deployment is dominated by **network latency** (~160 ms, shared) — so Armadillo's comparative advantage diminishes when deployed
- We should **improve the few operations where Armadillo did worse** — `login` and `workspace_load`
- We can confidently say that Armadillo is **quicker and more light-weight**
</v-clicks>

---
layout: content
heading: Feedback
subheading: "Open questions"
section: Conclusions
---

<v-clicks>

- Anything else worth measuring?
- Do we want to put these figures in the docs/website?

</v-clicks>
