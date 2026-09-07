---
theme: ../theme
title: UNCAN demo
info: Placeholder deck
author: Tim Cadman
aspectRatio: '16/9'
publish: false
layout: content
heading: Federated analysis
subheading: What is it
clicks: 3
---

<style>
.fq-grid { display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 0.7rem; height: 100%; }
.fq-card { border: 2px solid #ddd; border-left: 5px solid var(--slidev-theme-primary); border-radius: 10px; padding: 0.7rem 1rem; background: rgba(66, 133, 244, 0.05); display: flex; flex-direction: column; justify-content: center; overflow: hidden; opacity: 0.28; filter: grayscale(85%); transition: opacity 0.4s ease, filter 0.4s ease, box-shadow 0.4s ease; }
.fq-card.fq-active { opacity: 1; filter: grayscale(0%); box-shadow: 0 2px 12px rgba(0, 0, 0, 0.10); }
.fq-card h3 { margin: 0 0 0.35rem 0; font-family: var(--font-subtitle); font-size: 1rem; font-weight: 600; color: var(--slidev-theme-primary); }
.fq-card p { margin: 0 0 0.25rem 0; font-size: 14px; line-height: 1.45; }
.fq-card p:last-child { margin-bottom: 0; }
</style>

<div class="fq-grid">
  <div class="fq-card" :class="{ 'fq-active': $clicks === 0 }">
    <h3>Code travels, not data</h3>
    <p>Analysis code is sent to where each dataset is stored.</p>
  </div>
  <div class="fq-card" :class="{ 'fq-active': $clicks === 1 }">
    <h3>Computation stays local</h3>
    <p>Each site runs the computation <strong>locally, on its own data</strong>.</p>
  </div>
  <div class="fq-card" :class="{ 'fq-active': $clicks === 2 }">
    <h3>Only aggregates return</h3>
    <p>Only <strong>non-disclosive, aggregate results</strong> &mdash; summary statistics or model updates.</p>
  </div>
  <div class="fq-card" :class="{ 'fq-active': $clicks === 3 }">
    <h3>The software</h3>
    <p><strong>Armadillo</strong> &mdash; server app that lets data owners manage access.</p>
    <p><strong>DataSHIELD</strong> &mdash; framework researchers use to analyse it.</p>
  </div>
</div>

---
layout: content
heading: Federated analysis
subheading: How it works
---

<DatashieldArchitectureArmadillo />


---
layout: section
---

# Data manager

---
layout: default
class: p-0
---

<video src="/login.mov" controls muted playsinline onclick="this.paused ? this.play() : this.pause()" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: contain; background: #000; cursor: pointer;"></video>

---
layout: default
class: p-0
---

<video src="/project.mov" controls muted playsinline onclick="this.paused ? this.play() : this.pause()" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: contain; background: #000; cursor: pointer;"></video>

---
layout: content
heading: Data manager
subheading: Inbox
---

<EmailScreen
  link="http://localhost:8081/#/r/project-1/a.researcher@umcg.nl/dW5jYW4tY29ubmVjdC9kYXRhL2NvcmUucGFycXVldHxxbDJfYmFzZWxpbmUsY2hlbW9fbW9kaWZpY2F0aW9uX3JlYXNvbixhZ2VfYXRfZGlhZ25vc2lzLGZpZ29fc3RhZ2UsY2hhcmxzb25fc2NvcmU="
/>

---
layout: default
class: p-0
---

<video src="/approve.mov" autoplay controls muted playsinline onclick="this.paused ? this.play() : this.pause()" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: contain; background: #000; cursor: pointer;"></video>

---
layout: section
---

# Researcher

---
layout: content
heading: Federated analysis
subheading: Logging in to the Armadillo servers
clicks: 6
---

<ResearcherSession :start-at="1" :end-at="5" />

<div v-show="$clicks === 4" style="position: absolute; inset: 0; background: rgba(0,0,0,0.55); display: flex; align-items: center; justify-content: center; z-index: 20;">
  <img src="/login-lsri.png" style="width: 78%; max-height: 74vh; object-fit: contain; border: 1px solid #9aa0a6; border-radius: 6px; box-shadow: 0 12px 40px rgba(0,0,0,0.4);" />
</div>

---
layout: content
heading: Federated analysis
subheading: Logging in and assigning the data
clicks: 2
---

<ResearcherSession :start-at="6" :end-at="6" />

---
layout: content
heading: Federated analysis
subheading: Inspecting the data
clicks: 4
---

<ResearcherSession :start-at="7" :end-at="8" />

---
layout: content
heading: Federated analysis
subheading: Tabulating the outcome
clicks: 2
---

<ResearcherSession :start-at="9" :end-at="9" />

---
layout: content
heading: Federated analysis
subheading: Modelling the outcome
clicks: 2
---

<ResearcherSession :start-at="10" :end-at="10" />

---
layout: content
heading: Federated analysis
subheading: Pooling across cohorts
clicks: 2
---

<ResearcherSession :start-at="11" />
