---
theme: ../theme
title: Armadillo + Flower
info: Federated learning apps via Armadillo and Flower
author: Tim Cadman
date: 2026-09-10
aspectRatio: '16/9'
publish: true
---

# Armadillo + Flower

<div class="author-info">
  <p><strong>Tim Cadman</strong></p>
  <p>Senior Data Scientist</p>
</div>

<div class="title-logos">
  <img src="./public/molgenis-logo.png" class="logo-molgenis" />
</div>

---
layout: chart-full
heading: Armadillo and Flower proposed flow
---

<AppStoreFlow />

---
layout: content
heading: Implementation
---

<style>
.impl-row { display: flex; gap: 1.5rem; height: 100%; align-items: flex-start; }
.impl-card { flex: 1; border: 2px solid #ddd; border-left: 5px solid; border-radius: 10px; padding: 1rem 1.25rem; transition: opacity 0.4s ease; }
.impl-card h3 { margin: 0 0 0.6rem 0; font-family: var(--font-subtitle); font-size: 1rem; font-weight: 600; }
.impl-card p { margin: 0 0 0.5rem 0; font-size: 14px; color: #555; }
.impl-card ul { padding-left: 1.2rem; margin: 0; }
.impl-card li { font-size: 14px; line-height: 1.4; margin-bottom: 0.3rem; }
.impl-card.armadillo { border-left-color: #4285F4; background: rgba(66, 133, 244, 0.06); }
.impl-card.armadillo h3 { color: #4285F4; }
.impl-card.py { border-left-color: #E6B96A; background: rgba(230, 185, 106, 0.12); }
.impl-card.py h3 { color: #B9852A; }
</style>

<div class="impl-row">
  <div v-click="1" class="impl-card armadillo">
    <h3>molgenis-service-armadillo</h3>
    <ul>
      <li>Flower container classes &amp; Docker integration</li>
      <li>Push-data-to-container endpoint</li>
      <li>Whitelist config &amp; endpoint</li>
      <li>Container UI</li>
    </ul>
  </div>
  <div v-click="2" class="impl-card py">
    <h3>molgenis-flwr-armadillo (Python)</h3>
    <ul>
      <li>Auth CLI &amp; token routing</li>
      <li>App load data helper, API helpers &amp; resources CLI</li>
      <li>Custom superexec image with whitelist plugin</li>
      <li>Review-app &amp; approve-app CLIs, example app</li>
    </ul>
  </div>
</div>

---
layout: chart-full
heading: Implementation
---

<StepsToPRs />

---
layout: chart-full
heading: Suggested review order
---

<ReviewOrder />
