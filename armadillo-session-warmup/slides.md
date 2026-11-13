---
theme: ../theme
title: Async Session Warmup
info: Proposal to make Armadillo's R-session creation asynchronous, removing R-engine boot time from the DataSHIELD login call
author: Tim Cadman
date: 2026-09-18
aspectRatio: '16/9'
publish: false
themeConfig:
  sections: [Problem, Proposal, Status]
---

# Async Session Warmup

A proposal to stop `login` blocking on the R engine

<div class="title-logos">
  <img src="./public/molgenis-logo.png" class="logo-molgenis" />
</div>

---
layout: section
---

# Problem

---
layout: content
heading: One command, four HTTP calls
subheading: What datashield.login + one assignment actually costs
section: Problem
---

<div class="lead">A single DataSHIELD command is not one HTTP call — it's a sequence:</div>

<div class="ld-bar">
  <div class="seg" v-click style="flex:2.6;--c:#D9534F"><b>1. POST /select-profile</b><small>creates the R engine — blocks until it boots</small></div>
  <div class="seg" v-click style="flex:1.3;--c:#1E3A5F"><b>2. POST /load-table</b><small>submits the command, async=TRUE</small></div>
  <div class="seg" v-click style="flex:1.6;--c:#0097A7"><b>3. GET /lastcommand</b><small>polled until status = COMPLETED</small></div>
  <div class="seg" v-click style="flex:1.2;--c:#E6B96A;--tc:#5c4410"><b>4. GET /lastcommand</b><small>fetch the result payload</small></div>
</div>

<div v-click class="callout">
  Calls 2–4 are the normal async pattern. Call 1 is different: the HTTP response doesn't return until <b>Rserve/Rock has fully booted</b> — that wait is invisible, hidden inside a single request.
</div>

<style scoped>
.lead { font-size: 15px; color: #445; margin: 0.2rem 0 1rem; }
.ld-bar { display: flex; border-radius: 8px; overflow: hidden; box-shadow: 0 1px 5px rgba(0,0,0,0.13); }
.seg { min-width: 0; padding: 1rem 0.85rem; text-align: center; display: flex; flex-direction: column; gap: 0.3rem; background: var(--c); color: var(--tc, #fff); }
.seg b { font-family: var(--font-subtitle); font-size: 0.95rem; line-height: 1.2; }
.seg small { font-size: 0.78rem; line-height: 1.3; opacity: 0.9; }
.callout { margin-top: 1.4rem; font-size: 14px; color: #556; line-height: 1.6; border-left: 4px solid #D9534F; padding: 0.6rem 1rem; background: #fdf3f2; border-radius: 0 6px 6px 0; }
.callout b { color: #B52B27; }
</style>

---
layout: content
heading: We already saw this
subheading: From the Armadillo vs Opal benchmark
section: Problem
---

<div class="quote-block">
  "We should <b>improve the few operations where Armadillo did worse</b> — <code>login</code> and <code>workspace_load</code>"
  <div class="src">— conclusion, Armadillo vs Opal benchmark deck</div>
</div>

<div v-click class="explain">
  Both operations go through <code>select-profile</code>. The R-engine boot time isn't a network or protocol cost — it's server-side compute that happens to be synchronous with the client's request.
</div>

<style scoped>
.quote-block { font-size: 20px; color: #333; line-height: 1.6; border-left: 4px solid var(--slidev-theme-primary); padding: 0.8rem 1.2rem; background: #f4f7fd; border-radius: 0 8px 8px 0; margin-top: 1rem; }
.quote-block code { font-size: 0.85em; background: #e3e8f2; padding: 0.1em 0.4em; border-radius: 4px; }
.src { margin-top: 0.6rem; font-size: 13px; color: #8a94a6; font-family: var(--font-subtitle); }
.explain { margin-top: 1.6rem; font-size: 15px; color: #556; line-height: 1.6; max-width: 38rem; }
</style>

---
layout: section
---

# Proposal

---
layout: content
heading: Make session creation async
subheading: 'CommandsImpl.java — the change'
section: Proposal
---

<div class="cmp">
  <div class="col">
    <div class="colh before">Before</div>
    <ul>
      <li><code>armadilloSession</code> is a plain <code>ArmadilloSession</code></li>
      <li><code>selectProfile()</code> constructs it inline</li>
      <li>the constructor blocks until Rserve/Rock is up</li>
      <li>the HTTP response waits for all of it</li>
    </ul>
  </div>
  <div class="col" v-click>
    <div class="colh after">After</div>
    <ul>
      <li><code>armadilloSession</code> is a <code>CompletableFuture&lt;ArmadilloSession&gt;</code></li>
      <li><code>selectProfile()</code> calls <code>createSessionAsync()</code> and returns immediately</li>
      <li>the engine boots in the background</li>
      <li><code>schedule()</code> only awaits the future when a real command runs</li>
    </ul>
  </div>
</div>

<div v-click class="callout">
  Net effect: boot time moves off the <code>select-profile</code> response and overlaps with whatever the client does next, instead of serializing in front of it.
</div>

<style scoped>
.cmp { display: flex; gap: 1.5rem; margin-top: 0.8rem; }
.col { flex: 1; border: 1px solid #e3e8f2; border-radius: 8px; padding: 0.9rem 1.1rem; background: #fafbfe; }
.colh { font-family: var(--font-subtitle); font-weight: 600; font-size: 15px; margin-bottom: 0.6rem; }
.colh.before { color: #B52B27; }
.colh.after { color: #1a7a3c; }
.col ul { padding-left: 1.1rem; margin: 0; }
.col li { font-size: 13.5px; color: #556; line-height: 1.5; margin-bottom: 0.4rem; }
.col code { font-size: 0.85em; }
.callout { margin-top: 1.4rem; font-size: 14px; color: #556; line-height: 1.6; border-left: 4px solid var(--slidev-theme-accent); padding: 0.6rem 1rem; background: #eefaf9; border-radius: 0 6px 6px 0; }
</style>

---
layout: content
heading: The client already expects this
subheading: DSI's session API
section: Proposal
---

<div class="lead">DSI already ships the plumbing to poll a session that isn't ready yet, called at the top of every assign/aggregate/workspace/symbol call:</div>

<v-clicks>

- `dsIsAsync()` — can this connection create sessions asynchronously?
- `dsSession(conn, async = TRUE)` — kick off session creation without waiting
- `dsIsReady()` / `dsStateMessage()` — poll readiness, show progress
- `datashield.sessions()` — the client-side loop that ties these together

</v-clicks>

<style scoped>
.lead { font-size: 15px; color: #445; margin: 0.2rem 0 1rem; max-width: 40rem; }
</style>

---
layout: section
---

# Status

---
layout: content
heading: Where things stand
section: Status
---

<table class="st-tbl">
<thead><tr><th>Piece</th><th>State</th></tr></thead>
<tbody>
<tr v-click><td><b>DSI</b> (client)</td><td>Done — <code>dsIsAsync</code>, <code>dsSession</code>, <code>dsIsReady</code>, <code>dsStateMessage</code>, <code>datashield.sessions()</code> all merged</td></tr>
<tr v-click><td><b>Armadillo</b> (server, Java)</td><td>Written — <code>CommandsImpl</code> async-session change on <code>feat/async-session-warmup</code>, not yet committed</td></tr>
<tr v-click><td><b>DSMolgenisArmadillo</b> (R client)</td><td>Missing — no <code>dsIsAsync</code>/<code>dsSession</code> methods yet, so nothing calls the new async path today</td></tr>
</tbody>
</table>

<style scoped>
.st-tbl { border-collapse: collapse; width: 100%; margin-top: 1rem; }
.st-tbl th, .st-tbl td { font-size: 15px; padding: 0.55rem 0.7rem; border-bottom: 1px solid #e3e8f2; text-align: left; vertical-align: top; }
.st-tbl th { font-family: var(--font-subtitle); color: var(--slidev-theme-primary); border-bottom: 2px solid var(--slidev-theme-primary); }
.st-tbl code { font-size: 13px; }
</style>

---
layout: content
heading: Next steps
section: Status
---

<v-clicks>

- Commit and land the `CommandsImpl` async-session change
- Implement `dsIsAsync` / `dsSession(async = TRUE)` in DSMolgenisArmadillo
- Re-run the `login` / `workspace_load` benchmarks to confirm the win

</v-clicks>
