---
theme: ../theme-uncan
title: What is federated analysis?
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
    <h3>Remote analysis</h3>
    <p>Combines multiple data sources in one model</p>
  </div>
  <div class="fq-card" :class="{ 'fq-active': $clicks === 1 }">
    <h3>Code travels, not data</h3>
    <p>Each site runs the computation <strong>locally, on its own data</strong>.</p>
  </div>
  <div class="fq-card" :class="{ 'fq-active': $clicks === 2 }">
    <h3>Only summary-statistics return</h3>
    <p>Only <strong>non-disclosive parameters </strong>are shared</p>
    <p>&mdash; e.g. means, sd, coefficients.</p>
  </div>
  <div class="fq-card" :class="{ 'fq-active': $clicks === 3 }">
    <h3>The software</h3>
    <p><strong>Armadillo</strong> &mdash; server application to manager data access;</p>
    <p><strong>DataSHIELD</strong> &mdash; federated framework to analyse data.</p>
  </div>
</div>

---
layout: content
heading: Federated analysis
subheading: How it works
---

<DatashieldArchitectureArmadillo />
