---
theme: ../theme
title: Armadillo vs Opal — DataSHIELD benchmark
info: Comparing DataSHIELD performance across Armadillo and Opal backends
author: Tim Cadman
date: 2026-06-25
aspectRatio: '16/9'
publish: false
---

# Armadillo vs Opal

A DataSHIELD performance benchmark

<div class="title-logos">
  <img src="./public/molgenis-logo.png" class="logo-molgenis" />
</div>

---
layout: content
heading: What we measure, and why
subheading: "Two test suites, one aligned comparison"
---

- Goal: compare DataSHIELD performance across **three backends** running the **same** serverside package (**dsBase 6.3.5** — so the comparison is fair)
- The function set is **analysis-driven** — derived from real project scripts + the official tutorials, not the whole API
- We separate **true server speed** from **what the end-user feels**, because most client-observed time is *not* server work:

<div class="suite-cards">
  <div class="suite-card">
    <div class="suite-tag">Suite 1</div>
    <div class="suite-title">True server compute</div>
    <div class="suite-body">The most-used single-command calls, timed from the server's own <code>endDate − startDate</code> record. Excludes network + client poll-sleep. Many reps.</div>
  </div>
  <div class="suite-card">
    <div class="suite-tag">Suite 2</div>
    <div class="suite-title">End-user experience</div>
    <div class="suite-body">The same calls timed as the <b>client</b> observes them — through the DSI async poll loop (default <b>50&nbsp;ms</b> poll-sleep). What an analyst actually waits for.</div>
  </div>
</div>

<style scoped>
.suite-cards {
  display: flex;
  gap: 1.5rem;
  margin-top: 1.75rem;
}
.suite-card {
  flex: 1;
  border: 1px solid #d8e0f3;
  border-top: 4px solid var(--slidev-theme-primary);
  border-radius: 8px;
  padding: 1rem 1.25rem;
  background: #fafbff;
}
.suite-tag {
  font-family: var(--font-subtitle);
  font-size: 12px;
  color: var(--slidev-theme-accent);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
.suite-title {
  font-family: var(--font-title);
  font-size: 26px;
  color: var(--slidev-theme-primary);
  margin: 0.15rem 0 0.4rem 0;
}
.suite-body {
  font-family: var(--font-body);
  font-size: 14px;
  line-height: 1.45;
  color: var(--slidev-theme-text);
}
.suite-body code {
  font-family: var(--font-subtitle);
  font-size: 12.5px;
  color: var(--slidev-theme-primary);
}
</style>

---
layout: content
heading: The three backends
subheading: "A server + a serverside R execution engine"
---

- Each backend = a **DataSHIELD server** paired with a **serverside R execution engine**:

| backend | server | R engine |
|---|---|---|
| **opal-rock** | Opal | Rock |
| **armadillo-rock** | MOLGENIS Armadillo (default profile) | Rock |
| **armadillo-rserve** | MOLGENIS Armadillo (Rserve profile) | Rserve |

- **Rock** — newer **HTTP**-based R server; **process-per-session** → more isolation, more per-call overhead
- **Rserve** — long-standing **binary-protocol** R server; **lighter** per call
- So the comparison isolates two things at once: the **server** (Opal vs Armadillo) and the **R engine** (Rock vs Rserve)
- All three run **dsBase 6.3.5**, so any difference is the platform, not the analysis code

---
layout: content
heading: A measurement caveat
subheading: "Why the benchmark *under*-sells Armadillo"
---

- DataSHIELD runs operations **asynchronously**: the client submits, then **polls** "is it done?"
- After the first (immediate) poll, the client **sleeps a flat 50&nbsp;ms** between checks <span style="color:#999">(`datashield.polling.sleep.0`)</span>
- Completion is only **noticed at a poll boundary** — so measured time rounds **up** to the next 50&nbsp;ms tick
- This is a **client-side timing artefact**, not server work:
  - **Opal** (slow op) — the 50&nbsp;ms quantum is a small % of a long compute
  - **Armadillo** (fast op) — compute finishes inside the *first* sleep, so most of the measured time is the client **asleep on an answer that already exists**
- The faster the backend, the **bigger the share of measured time that is pure waiting**

---
layout: content
heading: A measurement caveat
subheading: "Result already done — but the client is still asleep"
---

<PollPenalty />

---
layout: content
heading: Raw server compute times
subheading: "True execution time — read from each server's own command record"
---

| operation | Armadillo | Rserve | Opal |
|---|--:|--:|--:|
| `dimDS('D')` — dimensions | 7.9 | 0.7 | 9.0 |
| `numNaDS('D$LAB_HDL')` — count NAs | 6.8 | 1.3 | 9.0 |
| `quantileMeanDS('D$LAB_HDL')` | 6.2 | 1.2 | 9.0 |
| `D$LAB_TSC * 2` — assign | 8.2 | 1.5 | 9.0 |
| `asNumericDS('D$GENDER')` — coerce | 34.5 | 34.8 | 31.0 |
| `assign.table` — load table | 100 | 144 | 543 |

<div style="margin-top:1rem; color:#777; font-size:14px">
milliseconds, median of 30 reps on localhost. Metadata/aggregate calls sit near a fixed
per-command floor (~7 ms Armadillo, ~9 ms Opal, ~1 ms Rserve); coercion and table-load are heavier.
For the cheap ops the client <em>observes</em> ~65–96 ms — many times the true compute (previous slide).
</div>

---
layout: content
heading: How the compute times were measured
---

- Both servers record **per-command execution timestamps**; we read those back instead of timing the client
  - `compute = endDate − startDate` — **excludes the network and the client poll-sleep**
  - Armadillo: `GET /lastcommand`; Opal: command-by-id — ISO-8601 timestamps
- Each op submitted **async** → poll until done → read the command record **before** fetching
- **Single-command primitives only**: Armadillo keeps just the *last* command, so compound `ds.*` ops can't be summed
- **Median of 30 reps**, localhost servers

```bash
COMPUTE=1 COMPUTE_REPS=30 Rscript bench.R   # → results/compute.csv
Rscript plot_compute.R                       # → results/compute.png
```

---
layout: chart-full
heading: "Suite 1 — true server compute"
---

<BackendBars :rows="[
  { op: 'dimDS', values: { 'armadillo-rserve': 0.7, 'armadillo-rock': 7.9, 'opal-rock': 9.0 } },
  { op: 'numNaDS', values: { 'armadillo-rserve': 1.3, 'armadillo-rock': 6.8, 'opal-rock': 9.0 } },
  { op: 'quantileMeanDS', values: { 'armadillo-rserve': 1.2, 'armadillo-rock': 6.2, 'opal-rock': 9.0 } },
  { op: 'D$LAB_TSC * 2 (assign)', values: { 'armadillo-rserve': 1.5, 'armadillo-rock': 8.2, 'opal-rock': 9.0 } },
]" unit=" ms" />

<div style="text-align:center; color:#777; font-size:13px; margin-top:0.5rem">
  Most-used single-command calls · server <code>endDate − startDate</code> · median of reps · ms (lower is faster).
  Rserve sits near a ~1 ms floor; Rock-based backends near ~7–9 ms.
</div>

---
layout: chart-full
heading: "Suite 2 — end-user experience"
---

<BackendBars :rows="[
  { op: 'dimDS', values: { 'armadillo-rserve': 45, 'armadillo-rock': 66, 'opal-rock': 94 } },
  { op: 'numNaDS', values: { 'armadillo-rserve': 48, 'armadillo-rock': 64, 'opal-rock': 96 } },
  { op: 'quantileMeanDS', values: { 'armadillo-rserve': 47, 'armadillo-rock': 65, 'opal-rock': 93 } },
]" unit=" ms" />

<div style="text-align:center; color:#777; font-size:13px; margin-top:0.5rem">
  Same calls, timed as the <b>client</b> observes them through the DSI async poll loop (default 50&nbsp;ms poll-sleep) · ms.
  <br>Illustrative pending the full Suite-2 run across all three backends:
</div>

<Placeholder caption="Suite 2 — client-observed ops/sec for the full core ds.*/datashield.* set, all three backends (results/rates.csv)" />

---
layout: chart-full
heading: "Where the client-observed time goes"
---

<LatencyStack :rows="[
  { backend: 'armadillo-rserve', compute: 1, network: 4, poll: 40 },
  { backend: 'armadillo-rock', compute: 8, network: 8, poll: 50 },
  { backend: 'opal-rock', compute: 9, network: 37, poll: 48 },
]" />

<div style="text-align:center; color:#777; font-size:12.5px; margin-top:0.25rem">
  Illustrative split (ms) for a fast op. Only <code>opal/dimDS</code> is fully measured today
  (compute ≈ 9, round-trip ≈ 46, client ≈ 94 ms); the per-backend compute/network/poll split below is pending:
</div>

<Placeholder caption="per-backend compute vs network vs poll-wait split for the fast ops (needs roundtrip_ms + client_ms for all three backends)" />
