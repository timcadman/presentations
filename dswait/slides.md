---
theme: ../theme
title: dsWait
info: Proposal to replace DSI's client-side polling loop with HTTP long-polling
author: Tim Cadman
date: 2026-09-18
aspectRatio: '16/9'
publish: false
themeConfig:
  sections: [Problem, Proposal]
---

# dsWait

Proposed change to DSI to improve performance

<div class="title-logos">
  <img src="./public/molgenis-logo.png" class="logo-molgenis" />
</div>

---
layout: section
---

# Problem

---
layout: content
heading: DataSHIELD speed
subheading: Where the time goes
section: Problem
---

<div class="ld-bar">
  <div class="seg" v-click style="flex:2.4;--c:#1E3A5F"><b>Network</b><small>round-trips on the wire</small></div>
  <div class="seg" v-click style="flex:1.5;--c:#0097A7"><b>System overhead</b><small>serialise · protocol · dispatch · auth</small></div>
  <div class="seg" v-click style="flex:1.1;--c:#E6B96A;--tc:#5c4410"><b>Server compute</b><small>the function runs in R</small></div>
  <div class="seg" v-click style="flex:1.0;--c:#6A4C93"><b>Polling delay</b><small>client waits between async status checks</small></div>
</div>

<style scoped>
.ld-bar { display: flex; border-radius: 8px; overflow: hidden; box-shadow: 0 1px 5px rgba(0,0,0,0.13); margin-top: 1.5rem; }
.seg { min-width: 0; padding: 1rem 0.85rem; text-align: center; display: flex; flex-direction: column; gap: 0.28rem; background: var(--c); color: var(--tc, #fff); }
.seg b { font-family: var(--font-subtitle); font-size: 1rem; line-height: 1.2; }
.seg small { font-size: 0.8rem; line-height: 1.25; }
.callout { margin-top: 1.6rem; font-size: 15px; color: #556; line-height: 1.6; border-left: 4px solid #6A4C93; padding: 0.6rem 1rem; background: #f4f1f8; border-radius: 0 6px 6px 0; max-width: 40rem; }
.callout b { color: #4d3670; }
</style>

---
layout: content
heading: DataSHIELD speed
subheading: Where the time goes
section: Problem
---

<LatencyStack note="median total time (ms) per operation" :rows="[
  { backend: 'opal · remote', compute: 9.0, overhead: 72.3, network: 157.5 },
  { backend: 'armadillo-rock · remote', compute: 4.6, overhead: 21.4, network: 158.3 },
  { backend: 'armadillo-rserve · remote', compute: 2.2, overhead: 16.6, network: 162.5 },
]"/>


---
layout: content
heading: Network latency
subheading: How DSI works
section: Problem
---

<PollLoop
  submit-label="Submit"
  submit-desc="POST (e.g.) /load-table"
  final-label="Finalize"
  final-desc="GET /lastresult"
/>

<style scoped>
.callout { margin-top: 1.4rem; font-size: 15px; color: #556; line-height: 1.6; border-left: 4px solid var(--slidev-theme-accent); padding: 0.6rem 1rem; background: #eefaf9; border-radius: 0 6px 6px 0; max-width: 44rem; }
.callout code { font-size: 0.85em; }
</style>

---
layout: content
heading: Measuring http calls
subheading: 'datashield.assign.table() using demo server'
section: Problem
---

<div class="tbl-cols">
<table class="call-tbl">
<thead><tr><th>#</th><th>Call</th><th>Status</th></tr></thead>
<tbody>
<tr><td>1</td><td><code>POST /load-table</code></td><td>201</td></tr>
<tr><td>2</td><td><code>GET /lastcommand</code></td><td>200</td></tr>
<tr class="sleep"><td></td><td>Sleep 50ms</td><td></td></tr>
<tr><td>3</td><td><code>GET /lastcommand</code></td><td>200</td></tr>
<tr class="sleep"><td></td><td>Sleep 50ms</td><td></td></tr>
<tr><td>4</td><td><code>GET /lastcommand</code></td><td>200</td></tr>
<tr class="sleep"><td></td><td>Sleep 50ms</td><td></td></tr>
<tr><td>5</td><td><code>GET /lastcommand</code></td><td>200</td></tr>
<tr class="sleep"><td></td><td>Sleep 50ms</td><td></td></tr>
<tr><td>6</td><td><code>GET /lastcommand</code></td><td>200</td></tr>
</tbody>
</table>
<table class="call-tbl">
<thead><tr><th>#</th><th>Call</th><th>Status</th></tr></thead>
<tbody>
<tr class="sleep"><td></td><td>Sleep 50ms</td><td></td></tr>
<tr><td>7</td><td><code>GET /lastcommand</code></td><td>200</td></tr>
<tr class="sleep"><td></td><td>Sleep 50ms</td><td></td></tr>
<tr><td>8</td><td><code>GET /lastcommand</code></td><td>200</td></tr>
<tr class="sleep"><td></td><td>Sleep 50ms</td><td></td></tr>
<tr><td>9</td><td><code>GET /lastcommand</code></td><td>200</td></tr>
<tr class="sleep"><td></td><td>Sleep 50ms</td><td></td></tr>
<tr><td>10</td><td><code>GET /lastcommand</code></td><td>200</td></tr>
<tr><td>11</td><td><code>GET /lastresult</code></td><td>404</td></tr>
<tr><td>12</td><td><code>GET /lastcommand</code></td><td>200</td></tr>
</tbody>
</table>
</div>

<style scoped>
.tbl-cols { display: flex; gap: 1.5rem; margin-top: 0.5rem; }
.call-tbl { border-collapse: collapse; flex: 1; }
.call-tbl th, .call-tbl td { font-size: 11px; padding: 0.1rem 0.5rem; line-height: 1.3; border-bottom: 1px solid #e3e8f2; text-align: left; }
.call-tbl th { font-family: var(--font-subtitle); color: var(--slidev-theme-primary); border-bottom: 2px solid var(--slidev-theme-primary); }
.call-tbl code { font-size: 10px; }
.call-tbl tr.sleep td { color: #9aa4b0; font-style: italic; }
.callout { margin-top: 0.7rem; font-size: 13px; color: #556; line-height: 1.4; border-left: 4px solid #D9534F; padding: 0.4rem 0.8rem; background: #fdf3f2; border-radius: 0 6px 6px 0; max-width: 44rem; }
.callout code { font-size: 0.85em; }
</style>

---
layout: section
---

# Proposal

---
layout: content
heading: 'dsWait: wait once, get the result'
subheading: One call instead of many
section: Proposal
---

<div class="flow">
  <div class="node submit"><b>Submit</b><small><code>POST /load-table</code></small></div>
  <span class="arrow">→</span>

  <div class="waitcol">
    <svg class="loopsvg" viewBox="0 0 100 30" preserveAspectRatio="none">
      <path d="M 22 26 C 22 2, 78 2, 78 26" fill="none" stroke="#6A4C93" stroke-width="2.5" />
      <polygon points="78,26 66,22 70,32" fill="#6A4C93" />
    </svg>
    <div class="node wait"><b>Wait</b><small><code>GET /lastresult</code><br /><code>Prefer: wait=10</code></small></div>
    <div class="outcomes">
      <div class="outcome loop"><code>202</code> not done yet → send this exact same request again</div>
      <div class="outcome done"><code>200</code> / <code>204</code> done → the result is already in <b>this</b> response</div>
    </div>
  </div>
</div>

<div class="callout ok">
  <b>12 calls become 1</b> (or a few, if it times out) — <code>Wait</code> is the check <b>and</b> the fetch, in one call.
</div>

<style scoped>
.flow { display: flex; align-items: center; gap: 0.5rem; margin-top: 1.8rem; }
.node { padding: 0.75rem 0.75rem; border-radius: 8px; text-align: center; color: #fff; box-shadow: 0 1px 5px rgba(0,0,0,0.13); min-width: 6.5rem; }
.node b { display: block; font-family: var(--font-subtitle); font-size: 0.85rem; }
.node small { display: block; font-size: 0.65rem; opacity: 0.9; margin-top: 0.25rem; line-height: 1.3; }
.node code { font-size: 0.95em; background: transparent; color: inherit; padding: 0; }
.submit { background: #1e3a5f; }
.wait { background: #6A4C93; }
.arrow { color: #9aa4b0; font-size: 1.2rem; }
.waitcol { display: flex; flex-direction: column; align-items: center; gap: 0.5rem; }
.loopsvg { width: 6.5rem; height: 1.6rem; overflow: visible; }
.outcomes { display: flex; flex-direction: column; gap: 0.35rem; align-items: flex-start; }
.outcome { font-size: 0.72rem; color: #556; font-family: var(--font-subtitle); line-height: 1.3; }
.outcome code { font-size: 1em; background: transparent; padding: 0; font-weight: 600; }
.outcome.loop code { color: #6A4C93; }
.outcome.done code { color: #1a7a3c; }
.outcome.done b { color: #1a7a3c; }
.callout.ok { margin-top: 1.6rem; font-size: 15px; color: #556; line-height: 1.6; border-left: 4px solid #6A4C93; padding: 0.6rem 1rem; background: #f4f1f8; border-radius: 0 6px 6px 0; max-width: 42rem; }
.callout.ok b { color: #4d3670; }
</style>

---
layout: content
heading: What needs to change
subheading: The actual code changes, by package
section: Proposal
---

<table class="st-tbl">
<thead><tr><th>Package</th><th>Change</th></tr></thead>
<tbody>
<tr><td><b>DSI</b></td><td>New <code>dsWait(res, timeout)</code> generic. <code>datashield.assign.*</code>/<code>aggregate</code> call it instead of <code>dsIsCompleted()</code>+<code>Sys.sleep()</code>, for any connection that supports it</td></tr>
<tr><td><b>Armadillo</b> <span class="tag">server</span></td><td><code>GET /lastresult</code> now honours <code>Prefer: wait=N</code>:<br />1. attaches to the R job already running in the background<br />2. races it against a timer, capped at 20s<br />3. job finishes first → returns the result; timer wins → returns <code>202</code>, job keeps running</td></tr>
<tr><td><b>Opal</b> <span class="tag">server</span></td><td class="unknown">??</td></tr>
</tbody>
</table>

<style scoped>
.st-tbl { border-collapse: collapse; width: 100%; margin-top: 1.2rem; }
.st-tbl th, .st-tbl td { font-size: 13px; padding: 0.5rem 0.7rem; border-bottom: 1px solid #e3e8f2; text-align: left; vertical-align: top; line-height: 1.4; }
.st-tbl th { font-family: var(--font-subtitle); color: var(--slidev-theme-primary); border-bottom: 2px solid var(--slidev-theme-primary); }
.st-tbl code { font-size: 11.5px; }
.st-tbl .tag { display: block; font-size: 10px; color: #8a94a6; font-family: var(--font-subtitle); font-weight: normal; }
.st-tbl td.missing { color: #B52B27; }
.st-tbl td.done { color: #1a7a3c; }
.st-tbl td.unknown { color: #B52B27; font-weight: 600; font-size: 16px; }
</style>

---
layout: content
heading: What the R clients would need
subheading: DSMolgenisArmadillo and DSOpal both need a dsWait() method
section: Proposal
---

<div class="impl-cols">
  <div class="impl-col">
    <div class="impl-h">DSMolgenisArmadillo</div>
    <ol>
      <li><code>dsWait(res, timeout)</code>: <code>GET /lastresult</code> with <code>Prefer: wait=&lt;timeout&gt;</code></li>
      <li><code>200</code>/<code>204</code> → done, return the result (or nothing, for assign)</li>
      <li><code>202</code> → not done, return <code>FALSE</code> so DSI calls it again</li>
      <li>Add <code>wait = TRUE</code> to what <code>dsIsAsync()</code> reports</li>
    </ol>
  </div>
  <div class="impl-col">
    <div class="impl-h">DSOpal</div>
    <p class="unknown">??</p>
  </div>
</div>

<style scoped>
.impl-cols { display: flex; gap: 1.5rem; margin-top: 1rem; }
.impl-col { flex: 1; }
.impl-h { font-family: var(--font-subtitle); font-weight: 600; color: var(--slidev-theme-primary); font-size: 15px; margin-bottom: 0.5rem; }
.impl-col ol { padding-left: 1.2rem; margin: 0; }
.impl-col li { font-size: 12.5px; color: #556; line-height: 1.45; margin-bottom: 0.5rem; }
.impl-col code { font-size: 11px; }
.impl-col .unknown { color: #B52B27; font-weight: 600; font-size: 16px; margin: 0; }
</style>

---
layout: content
heading: Backward compatibility
subheading: This is entirely opt-in, per connection
section: Proposal
---

<v-clicks>

- DSI's `dsWait()` has a default implementation: it just calls `dsIsCompleted()` — today's behaviour, unchanged
- A connection only gets the new path if its own package explicitly overrides `dsWait()` **and** reports `dsIsAsync()$wait = TRUE`
- Until DSMolgenisArmadillo and DSOpal are updated, **every existing analysis keeps working exactly as it does today** — nothing to migrate, nothing that can break
- Armadillo and Opal can be updated independently, in either order, on their own schedule

</v-clicks>

---
layout: content
heading: Next steps
section: Proposal
---

<v-clicks>

- Release DSI's `dsWait()` — it's a no-op for any connection that doesn't implement it
- Release Armadillo's `Prefer: wait=N` support, and fix the null-result 404 on the plain (non-wait) path too
- Add `dsWait()` to **DSMolgenisArmadillo** — the actual missing piece for Armadillo
- Add `dsWait()` to **DSOpal**, wired to the `wait=true` capability Opal already has
- Re-run a real trial against both, like we just did, to confirm the call count actually drops

</v-clicks>

