---
theme: ../../theme
title: DataSHIELD performance — 6.3.3 vs 7.0
info: Performance of dsBase/dsBaseClient 6.3.3 compared with the 7.0 refactor
author: Tim Cadman, Stuart Wheater, Demetris Avraam
date: 2026-09-23
aspectRatio: '16/9'
publish: false
themeConfig:
  sections: [Problem, Solution, Methods, Results, Demonstration, Summary]
---

# Doubling the speed of DataSHIELD
A community-led optimisation of dsBase <br> and dsBaseClient

<div class="author-info">
  <p><strong>Tim Cadman</strong>, Stuart Wheater, Demetris Avraam</p>
</div>

<div class="title-logos">
  <img src="./public/molgenis-logo.png" class="logo-molgenis" />
  <img src="./public/umcg-logo.png" class="logo-umcg" />
</div>

---
layout: section
---

# Background

---
layout: content-two-cols
heading: The problem
subheading: DataSHIELD is quite slow
section: Background
---

<template #left>

- Many users report that datashield is slow
- There are many rival federated analysis products - we need to keep improving
- **Example:** in R returning column names takes 0.0002 seconds vs 1.6 seconds <br> in DataSHIELD

</template>

<template #right>

<img src="./public/snail.jpg" class="bleed-right" />

</template>

---
layout: content-two-cols
heading: The diagnosis
subheading: Many round trips
section: Background
---

<template #left>

- Most datashield functions make **several separate calls** to the server:
  - Check object exists
  - Check object class
  - Run function
  - Check function ran correctly

</template>

<template #right>

<RoundTrips show="before" />

</template>

---
layout: content
heading: The diagnosis
subheading: Each round trip is expensive
section: Problem
---

<LatencyStack :clicks="$clicks" note="ms per operation" :rows="[
  { backend: '', compute: 5.3, overhead: 36.8, network: 159.4 },
]"/>

<span v-for="i in 3" :key="i" v-click style="display:none" />

---
layout: content
heading: The diagnosis
subheading: An analogy
section: Background
---

<ShoppingTrips :clicks="$clicks" show="before" note="Imagine going to the shop, but instead of buying everything in one go, making a separate trip for each item" />

<span v-click style="display:none" />

---
layout: section
---

# The solution

---
layout: content
heading: Make only one trip
subheading: Efficient shopping trip
section: Background
---

<ShoppingTrips :clicks="$clicks" show="after" noteAfter="Now imagine we go to the shop once, and buy everything" />

<span v-click style="display:none" />




---
layout: content-two-cols
heading: Make only one trip
subheading: Put more technically
section: Background
---

<template #left>

- One API call to per function
- All checks happen on the serverside
- Either result or error returned

</template>

<template #right>

<RoundTrips show="after" :afterSteps="['One API POST request']" />

</template>

---
layout: section
---

# Methods

---
layout: content
heading: Methods
section: Methods
---

- AI refactor pipeline using Claude Code (Anthropic)
- Human always in the loop
- **Evaluation:** pre / post performance tests, run in randomised order

---
layout: content
heading: Workflow
section: Solution
---

<ProcessCards :clicks="$clicks" :groups="[
  { steps: [
    { title: 'Review code', desc: 'Manual review of all the code' },
    { title: 'Draft plan', desc: 'Sketch the refactor plan' },
    { title: 'Review', desc: 'DataSHIELD Statistics theme' },
    { title: 'Write plan', desc: 'Write the refactor plan with Claude' },
    { title: 'Split into batches', desc: 'Split functions into 11 batches' },
  ] },
  { loop: true, label: 'iterate', steps: [
    { title: 'Apply', desc: 'Apply plan to first batch' },
    { title: 'Review problems', desc: 'Manual review of problems' },
    { title: 'Revise plan', desc: 'Refine the plan' },
  ] },
  { steps: [
    { title: 'Run pipeline', desc: 'Apply to batch 1' },
    { title: 'Agent review', desc: 'Derived from refactor plan' },
    { title: 'Code review (me)' },
    { title: 'PR review', desc: 'Stuart + others'},
  ] },
]" />

<span v-for="i in 11" :key="i" v-click style="display:none" />

---
layout: section
---

# Results

---
layout: content
heading: In numbers
section: Results
---

<StatTiles :clicks="$clicks" :stats="[
  { value: 218, label: 'functions refactored', icon: 'function', color: '#1E3A5F' },
  { value: 437, label: 'commits', icon: 'commit', color: 'var(--slidev-theme-primary)' },
  { value: 4153, label: 'fewer lines of R code', icon: 'code', color: 'var(--slidev-theme-accent)' },
  { value: 8510, label: 'new lines of tests', icon: 'tests', color: 'var(--slidev-theme-secondary)' },
]" />

<span v-for="i in 4" :key="i" v-click style="display:none" />

---
layout: content
heading: Original vs refactored speed
section: Results
---

<div style="display: flex; gap: 2rem; height: 100%;">
  <div style="flex: 1; min-width: 0;"><RatesBars :clicks="$clicks" /></div>
  <div style="flex: 0 0 22%; display: flex; flex-direction: column; justify-content: center;"><PerfStats :clicks="$clicks" :reveal-at="2" /></div>
</div>

<span v-click style="display:none" />
<span v-click style="display:none" />

---
layout: content-img-right
heading: What this means for a real analysis
subheading: Example paper
image: ./public/paper-aje.png
imageWidth: '55'
---

<v-clicks>

- About **16,900** calls to the servers
- Around **6 hours** before the refactor
- Around **3.7 hours** with v7.0

</v-clicks>

---
layout: content
heading: Bonus results
section: Results
clicks: 2
---

<style>
.fq-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 0.7rem; height: 100%; }
.fq-card { border: 2px solid #ddd; border-left: 5px solid var(--c); border-radius: 10px; padding: 0.7rem 1rem; background: color-mix(in srgb, var(--c) 8%, white); display: flex; flex-direction: column; justify-content: center; overflow: hidden; opacity: 0.28; filter: grayscale(85%); transition: opacity 0.4s ease, filter 0.4s ease, box-shadow 0.4s ease; }
.fq-card.fq-active { opacity: 1; filter: grayscale(0%); box-shadow: 0 2px 12px rgba(0, 0, 0, 0.10); }
.fq-card h3 { margin: 0 0 0.35rem 0; font-family: var(--font-subtitle); font-size: 1rem; font-weight: 600; color: var(--title, var(--c)); }
.fq-card p { margin: 0 0 0.25rem 0; font-size: 14px; line-height: 1.45; }
.fq-card p:last-child { margin-bottom: 0; }
</style>

<div class="fq-grid">
  <div class="fq-card" style="--c: #4285F4;" :class="{ 'fq-active': $clicks === 0 }">
    <h3>Server-side safety</h3>
    <p>Closed a code-injection route with <span style="font-family: var(--font-subtitle);">eval(parse)</span>.</p>
  </div>
  <div class="fq-card" style="--c: #0097A7;" :class="{ 'fq-active': $clicks === 1 }">
    <h3>Less boilerplate</h3>
    <p>Shared helpers make the code more readable and reusable.</p>
  </div>
  <div class="fq-card" style="--c: #E6B96A; --title: #B9852A;" :class="{ 'fq-active': $clicks === 2 }">
    <h3>Consistent errors</h3>
    <p>Helper functions standardise <br> error messages.</p>
  </div>
</div>

---
layout: section
---

# Demonstration

---
layout: chart-full
heading: 'ds.cov'
section: Demonstration
---

<div style="display: flex; gap: 3.5rem;">
  <div>
    <div style="font-family: var(--font-subtitle); font-size: 25px; font-weight: 600; color: var(--slidev-theme-heading); margin-bottom: 0.5rem;">6.3.3</div>
    <div style="position: relative; height: 21rem; aspect-ratio: 1542 / 1432;"><VideoPlayer hide-button src="/cov-633.mov" :timer-start="0.33" :timer-end="3.17" /></div>
  </div>
  <div>
    <div style="font-family: var(--font-subtitle); font-size: 25px; font-weight: 600; color: var(--slidev-theme-heading); margin-bottom: 0.5rem;">7.0</div>
    <div style="position: relative; height: 21rem; aspect-ratio: 1542 / 1432;"><VideoPlayer hide-button src="/cov-700.mov" :timer-start="0.3" :timer-end="1.03" /></div>
  </div>
</div>

---
layout: chart-full
heading: 'ds.asInteger'
section: Demonstration
---

<div style="display: flex; gap: 3.5rem;">
  <div>
    <div style="font-family: var(--font-subtitle); font-size: 25px; font-weight: 600; color: var(--slidev-theme-heading); margin-bottom: 0.5rem;">6.3.3</div>
    <div style="position: relative; height: 21rem; aspect-ratio: 1542 / 1432;"><VideoPlayer hide-button src="/asInteger-633.mov" :timer-start="0.27" :timer-end="3.13" /></div>
  </div>
  <div>
    <div style="font-family: var(--font-subtitle); font-size: 25px; font-weight: 600; color: var(--slidev-theme-heading); margin-bottom: 0.5rem;">7.0</div>
    <div style="position: relative; height: 21rem; aspect-ratio: 1542 / 1432;"><VideoPlayer hide-button src="/asInteger-700.mov" :timer-start="0.27" :timer-end="1.27" /></div>
  </div>
</div>

---
layout: content
heading: Summary
section: Summary
---

<v-clicks>

- We Refactored 218 functions across dsBase and dsBaseClient
- We reduced number of round trips between client and server
- This gave a significant performance improvement: 2.3× faster on average, up to 7.3×
- V7.0 available soon!

</v-clicks>

---
layout: content-img-right
heading: Acknowledgements
image: ./public/team-photo.jpg
imageWidth: '42'
---

- **Stuart Wheater** endless pull request reviews
- **UMCG Armadillo team:** Mariska Slofstra, Ruben Veenstra, Dick Postma, Erik Zwart and <br> Morris Swertz
- **Demetris & Olly:** additional PR reviews
- **DataSHIELD Statistics theme:**
- **Funders:** EU via International Human Exposome Network (IHEN), FLEX4HEALTH (OSCARS)

<div style="display: flex; justify-content: flex-start; align-items: center; gap: 1.25rem; margin-top: 1rem;">
  <img src="./public/ihen-logo.svg" style="height: 1.75rem; width: 9.62rem; max-width: none; flex: none;" />
  <img src="./public/funder-logo.svg" style="height: 1.75rem; width: 5.72rem; max-width: none; flex: none;" />
  <img src="./public/eu-funded-logo.png" style="height: 1.75rem; width: 7.69rem; max-width: none; flex: none;" />
</div>
