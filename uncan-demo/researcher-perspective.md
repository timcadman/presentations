---
theme: ../theme-uncan
title: Researcher perspective — RStudio
info: Placeholder deck
author: Tim Cadman
aspectRatio: '16/9'
publish: false
layout: content
heading: Federated analysis
subheading: Logging in to the Armadillo servers
clicks: 6
---

<ResearcherSession :start-at="1" :end-at="5" :show-banner="true" />

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
