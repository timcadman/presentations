---
theme: ../theme
title: Opal vs Armadillo — DataSHIELD performance
info: A function-by-function performance benchmark of DataSHIELD backends
author: Tim Cadman
date: 2026-06-24
aspectRatio: '16/9'
publish: true
---

# Opal vs Armadillo
A function-by-function performance benchmark<br>of DataSHIELD backends

<div class="author-info">
  <p><strong>Tim Cadman</strong></p>
  <p>Senior Data Scientist</p>
</div>

<div class="title-logos">
  <img src="./public/molgenis-logo.png" class="logo-molgenis" />
  <img src="./public/umcg-logo.png" class="logo-umcg" />
</div>

---
layout: content
heading: What we compared
subheading: Three backends, one client
---

- Three DataSHIELD backends, all on localhost, driven by the **same dsBaseClient (6.3.5)**:
  - **Opal** — Obiba's reference server
  - **Armadillo (default)** — a fresh R session spun up per request
  - **Armadillo (Rock / Rserve)** — a persistent R session pool
- **~140 functions** exercised: the whole dsBaseClient `ds.*` surface plus the server round-trip `datashield.*` (DSI) calls
- Each call uses its **real dsBaseClient smoke-test form**, on the **real test data inflated to 100,000 rows × 30 variables**
- Metric is **operations per second**: run each function in a tight loop for 10 s, count completed calls, repeat **× 3**

---
layout: content
heading: How to read the charts
subheading: Speed relative to Opal
---

- Each bar is one function. The dashed line at **0** is **equal speed to Opal**.
- **← Left = Opal faster**, **Armadillo faster = right →**, measured in **fold units** (so "2x" = twice Opal's rate), clipped at 6x.
- Two bars per function:
  - <span style="color:#0072B2;font-weight:700">Blue</span> — Armadillo **default**
  - <span style="color:#E69F00;font-weight:700">Gold</span> — Armadillo **Rock / Rserve**
- The thin whisker shows the **min–max across the 3 repetitions** — how stable the measurement was.

---
layout: content
heading: Headline result
subheading: Persistent R sessions win; cold sessions don't
---

- **Rock / Rserve beats Opal on 100 of 109 functions** (median **1.5× faster**) — a warm, pooled R session avoids per-call startup.
- **Armadillo default is slower than Opal on 72 of 109** (median **0.75×**) — every call pays to spin up a fresh R session.
- **Opal wins login by ~10×**: Armadillo's first call in a session is dominated by session startup (`login` ≈ 0.4 ops/s vs Opal's 4.3).
- Once a session is warm, the ranking flips — `logout`, descriptives and matrix algebra are **2–4× faster** on Rock/Rserve.
- Median throughput: **Opal 7.0**, **default 4.7**, **Rock/Rserve 10.4** ops/s.

---
layout: section
---

# Function-by-function

One category per slide

---
layout: chart-full
heading: Metadata & inspection
---

<img src="./public/cat-metadata.png" style="height:100%;max-width:100%;object-fit:contain;display:block;margin:0 auto;" />

---
layout: chart-full
heading: DSI — server round-trips
---

<img src="./public/cat-dsi.png" style="height:100%;max-width:100%;object-fit:contain;display:block;margin:0 auto;" />

---
layout: chart-full
heading: Type coercion
---

<img src="./public/cat-coercion.png" style="height:100%;max-width:100%;object-fit:contain;display:block;margin:0 auto;" />

---
layout: chart-full
heading: Matrix algebra
---

<img src="./public/cat-matrix.png" style="height:100%;max-width:100%;object-fit:contain;display:block;margin:0 auto;" />

---
layout: chart-full
heading: Descriptive statistics
---

<img src="./public/cat-descriptive.png" style="height:100%;max-width:100%;object-fit:contain;display:block;margin:0 auto;" />

---
layout: chart-full
heading: Transformations
---

<img src="./public/cat-transform.png" style="height:100%;max-width:100%;object-fit:contain;display:block;margin:0 auto;" />

---
layout: chart-full
heading: Data-frame operations
---

<img src="./public/cat-dataframe.png" style="height:100%;max-width:100%;object-fit:contain;display:block;margin:0 auto;" />

---
layout: chart-full
heading: Generalised linear models
---

<img src="./public/cat-glm.png" style="height:100%;max-width:100%;object-fit:contain;display:block;margin:0 auto;" />

---
layout: chart-full
heading: Plotting
---

<img src="./public/cat-plot.png" style="height:100%;max-width:100%;object-fit:contain;display:block;margin:0 auto;" />

---
layout: chart-full
heading: Tabulation
---

<img src="./public/cat-tabulation.png" style="height:100%;max-width:100%;object-fit:contain;display:block;margin:0 auto;" />

---
layout: chart-full
heading: Correlation & covariance
---

<img src="./public/cat-correlation.png" style="height:100%;max-width:100%;object-fit:contain;display:block;margin:0 auto;" />

---
layout: chart-full
heading: Splines
---

<img src="./public/cat-spline.png" style="height:100%;max-width:100%;object-fit:contain;display:block;margin:0 auto;" />

---
layout: chart-full
heading: Vector operations
---

<img src="./public/cat-vector.png" style="height:100%;max-width:100%;object-fit:contain;display:block;margin:0 auto;" />

---
layout: chart-full
heading: Recoding
---

<img src="./public/cat-recode.png" style="height:100%;max-width:100%;object-fit:contain;display:block;margin:0 auto;" />

---
layout: chart-full
heading: Reshaping
---

<img src="./public/cat-reshape.png" style="height:100%;max-width:100%;object-fit:contain;display:block;margin:0 auto;" />

---
layout: chart-full
heading: Session — login / logout / load
---

<img src="./public/cat-session.png" style="height:100%;max-width:100%;object-fit:contain;display:block;margin:0 auto;" />

---
layout: chart-full
heading: Growth charts
---

<img src="./public/cat-growth.png" style="height:100%;max-width:100%;object-fit:contain;display:block;margin:0 auto;" />

---
layout: chart-full
heading: Imputation
---

<img src="./public/cat-imputation.png" style="height:100%;max-width:100%;object-fit:contain;display:block;margin:0 auto;" />

---
layout: chart-full
heading: Lists
---

<img src="./public/cat-list.png" style="height:100%;max-width:100%;object-fit:contain;display:block;margin:0 auto;" />

---
layout: chart-full
heading: Mixed-effects models
---

<img src="./public/cat-mixed-model.png" style="height:100%;max-width:100%;object-fit:contain;display:block;margin:0 auto;" />

---
layout: chart-full
heading: Distributional tests
---

<img src="./public/cat-distributional.png" style="height:100%;max-width:100%;object-fit:contain;display:block;margin:0 auto;" />

---
layout: chart-full
heading: Object management
---

<img src="./public/cat-objects.png" style="height:100%;max-width:100%;object-fit:contain;display:block;margin:0 auto;" />

---
layout: chart-full
heading: Survival
---

<img src="./public/cat-survival.png" style="height:100%;max-width:100%;object-fit:contain;display:block;margin:0 auto;" />

---
layout: section
---

# Takeaways

- **Rock / Rserve is the fast path** — persistent R sessions make Armadillo faster than Opal on almost every function (median 1.5×).
- **Cold-session overhead is real** — the default profile pays R-startup on every call and trails Opal; it hurts most on cheap, high-frequency calls.
- **First login favours Opal** — worth keeping in mind for short, interactive sessions.
