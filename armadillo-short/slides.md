---
theme: ../theme
title: MOLGENIS Armadillo & DataSHIELD
info: Short technical introduction to DataSHIELD and Armadillo
author: Tim Cadman
aspectRatio: '16/9'
publish: true
themeConfig:
  sections: [Federated analysis, Projects, Setup, UNCAN]
transition: slide-left
mdc: true
---

# MOLGENIS Armadillo & DataSHIELD
Secure Federated Analysis

<div class="author-info">
  <p><strong>Tim Cadman</strong></p>
</div>

<div class="title-logos">
  <img src="./public/molgenis-logo.png" class="logo-molgenis" />
  <img src="./public/umcg-logo.png" class="logo-umcg" />
</div>

<style>
.slidev-layout.cover .title-logos { right: 5rem; justify-content: space-between; }
</style>

---
layout: section
---

# Federated analysis<br>with DataSHIELD

---
layout: content-two-cols
heading: DataSHIELD
subheading: What is it?
leftWidth: '34'
section: 'Federated analysis'
transition: slide-up
---

::left::

- R Studio based federated analysis platform

<v-clicks>

- Developed over 15 years in EU research projects
- Used primarily in epidemiology and population health science

</v-clicks>

::right::

<Terminal light title="Plots"><ForestPlot style="margin: 0 auto; align-self: flex-start" /></Terminal>

---
layout: content
heading: Example research questions
section: 'Federated analysis'
transition: slide-up
---

<v-clicks>

- Does exposure to PFAS ('forever chemicals') increase the risk of kidney cancer?
- Does regular physical activity reduce the risk of colorectal cancer?
- Does quality of life at diagnosis predict cancer outcomes?

</v-clicks>

---
layout: content
heading: DataSHIELD
subheading: Key ideas
clicks: 3
section: 'Federated analysis'
transition: slide-up
---

<FocusCards :items="[
  { title: 'Federated analysis', color: 'var(--c-blue)', body: ['Distributed analysis with central aggregation'] },
  { title: 'Disclosure control', color: 'var(--c-teal)', body: ['Per-function checks ensure no participant data returns'] },
  { title: 'Authentication', color: 'var(--c-gold-dark)', body: ['Life Science AAI'] },
  { title: 'Deployment', color: 'var(--c-purple)', body: ['Via MOLGENIS Armadillo'] },
]" />

---
src: ../library/datashield/analysis-options.md
subheading: 1- and 2-stage analysis options
section: 'Federated analysis'
transition: slide-up
---

---
layout: section
transition: slide-left
---

# DataSHIELD demo

<style>
.slidev-layout.section { --slidev-theme-section-bg: var(--c-teal); --slidev-theme-section-fg: #fff; }
</style>

---
layout: section
---

# Example projects

---
layout: content
heading: Existing DataSHIELD nodes
subheading: 
section: 'Projects'
---

<NodeMap simple legend="below" height="16rem" note="" />

---
layout: content-two-cols
heading: "Example 1: EU Child Cohort Network"
subheading: 2017–2022
section: 'Projects'
leftWidth: '55'
clicks: 2
---

::left::

<NodeMap simple project="LifeCycle" colour="#6AA2FF" map="world" zoom="auto" legend="none" note="" />

::right::

<img src="./public/logo-eu-child-cohort-network.png" style="height: 4rem; width: 14rem; object-fit: contain; object-position: left center; margin-bottom: 1.25rem;" />

<div v-click="2">

- <strong style="color: var(--slidev-theme-primary)">Aim:</strong> study early life stressors and health across the life course
- Harmonised >2000 variables from EU birth cohorts

</div>

---
layout: content-two-cols
heading: "Example 2: ATHLETE"
subheading: 2020–2024
section: 'Projects'
leftWidth: '55'
clicks: 2
---

::left::

<NodeMap simple project="Athlete" colour="#03DBE2" builds-on="LifeCycle" builds-on-colour="#6AA2FF" map="world" zoom="auto" legend="none" note="" />

::right::

<img src="./public/logo-athlete.jpg" style="height: 4rem; width: 14rem; object-fit: contain; object-position: left center; margin-bottom: 1.25rem;" />

<div v-click="2">

- <strong style="color: var(--slidev-theme-primary)">Aim:</strong> study how chemicals and environmental exposures affect human health
- Onboarded new cohorts to the<br>EU Child Cohort Network,<br>adding environmental data

</div>

---
layout: content-two-cols
heading: "Example 3: Netherlands Cohorts Consortium"
subheading: 2026–2036
section: 'Projects'
leftWidth: '55'
clicks: 2
---

::left::

<NodeMap simple project="NCC" colour="#FF6917" map="europe" zoom="auto" legend="none" note="" />

::right::

<img src="./public/logo-ncc.jpg" style="height: 4rem; width: 14rem; object-fit: contain; object-position: left center; margin-bottom: 1.25rem; object-view-box: inset(14% 7% 14% 7%);" />

<div v-click="2">

- <strong style="color: var(--slidev-theme-primary)">Aim:</strong> align, harmonise and pool data to understand the causes of chronic diseases
- 11 population cohorts, over 440,000 participants

</div>

---
layout: section
---

# Setting up DataSHIELD

---
layout: content
heading: As a data owner
subheading: Setup steps
section: 'Setup'
transition: slide-up
---

<SetupSteps :steps="[
  { name: 'Install node application', points: ['MOLGENIS Armadillo'] },
  { name: 'Secure connection', points: ['TLS certificates', 'Authentication', 'Reverse proxy'] },
  { name: 'Upload data and manage access', points: ['Upload data', 'Manage access'] },
]" />

<style>
.slidev-layout .steps { grid-template-columns: repeat(3, 1fr); }
</style>

---
src: ../library/infrastructure/what-is-armadillo.md
section: 'Setup'
transition: slide-up
---

---
layout: section
transition: slide-up
---

# Armadillo demo

<style>
.slidev-layout.section { --slidev-theme-section-bg: var(--c-teal); --slidev-theme-section-fg: #fff; }
</style>


---
layout: content
heading: DataSHIELD/Armadillo in UNCAN
section: 'UNCAN'
transition: slide-up
---

<div class="uncan-cards">
  <div class="tint-card active" style="--c: var(--c-blue)">
    <h3>Use case</h3>
    <p>WP11: how does baseline quality of life predict cancer treatment outcomes?</p>
  </div>
  <div class="tint-card active" style="--c: var(--c-teal)">
    <h3>Collaboration</h3>
    <p>UMCG epidemiology department (Oncolifes study)</p>
  </div>
</div>

<h3 class="uncan-progress">Progress</h3>

<Timeline horizontal :items="[
  { text: 'Armadillo deployed at UMCG', status: 'done' },
  { text: 'Synthetic data uploaded', status: 'done' },
  { text: 'Awaiting DPAs for real data', status: 'current' },
  { text: 'Identify additional UNCAN partners' },
  { text: 'Harmonise study data to CDM' },
  { text: 'Deploy Armadillo at additional sites' },
  { text: 'Analysis and write-up' },
]" />

<style>
.uncan-cards { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; }
.uncan-progress { margin: 2rem 0 1rem 0; font-family: var(--font-subtitle); color: var(--c-blue); }
</style>

---
layout: content
heading: References
subheading: ""
---

<div class="refs" style="font-size: 15px; line-height: 1.5;">

**Armadillo**
Cadman T, Slofstra MK, van der Geest MA, et al. MOLGENIS Armadillo: a lightweight server for federated analysis using DataSHIELD. *Bioinformatics* 2025;41(1):btae726. https://doi.org/10.1093/bioinformatics/btae726

**Useful links**
- Armadillo documentation: https://molgenis.github.io/molgenis-service-armadillo/
- DataSHIELD wiki: https://wiki.datashield.org/
- MOLGENIS suite: https://molgenis.org/

</div>

<style>
.refs p { margin: 0 0 1.1rem 0; }
</style>
