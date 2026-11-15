---
theme: ../theme
title: Federated analysis with DataSHIELD and Armadillo
info: Draft — why share data, how DataSHIELD works, example projects, demos, infrastructure and legal
author: Tim Cadman & Mariska Slofstra
aspectRatio: '16/9'
publish: false
themeConfig:
  sections: [Who we are, Why share data, Federated analysis, DataSHIELD, Projects, Demo, Infrastructure, Legal]
transition: slide-left
mdc: true
---

# Federated analysis with DataSHIELD and Armadillo
Sharing data without moving it

<div class="author-info">
  <p><strong>Tim Cadman & Mariska Slofstra</strong></p>
</div>

<div class="title-logos">
  <img src="./public/molgenis-logo.png" class="logo-molgenis" />
  <img src="./public/umcg-logo.png" class="logo-umcg" />
</div>

---
layout: section
---

# Who we are

---
layout: content-img-right
heading: Background
section: 'Who we are'
subheading: MOLGENIS
image: ./public/molgenis-ecosystem.png
imageScale: '100'
---

- **MOLGENIS** data infrastructure accelerates **multi-center health research collaborations** — 60 projects, 35 FTE
- Armadillo is part of the **MOLGENIS suite**, which also includes the **EMX2 data warehouse** and the **MOLGENIS catalogue**

---
layout: content
heading: Our team
section: 'Who we are'
---

<style>
.team-label {
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: var(--slidev-theme-primary);
  margin: 0.25rem 0 0.4rem 0;
}
.team-rows {
  display: flex;
  flex-direction: column;
  gap: 0.7rem;
}
.team-row {
  display: flex;
  gap: 0.9rem;
}
.team-card {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  text-align: left;
  width: 96px;
}
.team-avatar {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background: rgba(148, 163, 184, 0.25);
  border: 2px dashed #aaa;
  object-fit: cover;
  margin-bottom: 0.25rem;
}
.team-name {
  font-size: 0.72rem;
  font-weight: 700;
  color: var(--slidev-theme-primary);
  line-height: 1.15;
}
.team-role {
  font-size: 0.62rem;
  color: #555;
}
.slide-header { min-height: 0; }
</style>

<div style="display: flex; gap: 2rem; margin-top: 0.5rem; align-items: stretch;">
<div style="flex: 1;">

<div class="team-label">Armadillo</div>
<div class="team-rows">
<div class="team-row">
  <div class="team-card">
    <img class="team-avatar" src="./public/team-tim.jpg" style="object-position: center 20%;" />
    <div class="team-name">Tim Cadman</div>
    <div class="team-role">Data Scientist</div>
  </div>
  <div class="team-card">
    <img class="team-avatar" src="./public/team-mariska.jpg" />
    <div class="team-name">Mariska Slofstra</div>
    <div class="team-role">Software Developer</div>
  </div>
  <div class="team-card">
    <img class="team-avatar" src="./public/team-dick.jpg" />
    <div class="team-name">Dick Postma</div>
    <div class="team-role">Ops</div>
  </div>
</div>
<div class="team-row">
  <div class="team-card">
    <div class="team-avatar" style="overflow: hidden; display: flex; align-items: center; justify-content: center; background: #e2e4e6;">
      <img src="./public/team-ruben.jpg" style="width: 100%; height: 100%; object-fit: cover; border-radius: 50%; transform: scale(0.9);" />
    </div>
    <div class="team-name">Ruben Veenstra</div>
    <div class="team-role">Ops</div>
  </div>
  <div class="team-card">
    <img class="team-avatar" src="./public/team-erik.jpg" />
    <div class="team-name">Erik Zwart</div>
    <div class="team-role">Data Manager</div>
  </div>
</div>
<div class="team-row">
  <div class="team-card">
    <img class="team-avatar" src="./public/team-niels.png" />
    <div class="team-name">Niels Kikkert</div>
    <div class="team-role">Team leader</div>
  </div>
  <div class="team-card">
    <img class="team-avatar" src="./public/team-morris.jpg" />
    <div class="team-name">Morris Swertz</div>
    <div class="team-role">PI</div>
  </div>
</div>
</div>

</div>
<div style="flex: 1.3; display: flex; flex-direction: column; min-height: 0;">

<div class="team-label">Wider MOLGENIS</div>
<div style="flex: 1; min-height: 0; margin-bottom: 2.6rem; position: relative; overflow: hidden; border-radius: 8px; box-shadow: 0 2px 12px rgba(0,0,0,0.18);">
  <img src="./public/team_2025.png" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: center 35%;" />
</div>

</div>
</div>

---
layout: content-two-cols
heading: About us
subheading: Tim Cadman & Mariska Slofstra
section: 'Who we are'
---

<template #left>

<img src="./public/team-tim.jpg" style="width: 120px; height: 120px; border-radius: 50%; object-fit: cover; object-position: center 20%;" />

**Tim Cadman** — Senior Data Scientist

- TODO: background
- TODO: role in DataSHIELD / Armadillo

</template>

<template #right>

<img src="./public/team-mariska.jpg" style="width: 120px; height: 120px; border-radius: 50%; object-fit: cover;" />

**Mariska Slofstra** — Software Developer

- TODO: background
- TODO: role in Armadillo

</template>

---
layout: content-two-cols
heading: Contents
---

<template #left>

1. Why share data
2. Federated analysis
3. DataSHIELD
4. Projects
5. Demo
6. Infrastructure
7. Legal

</template>

<template #right>

<img src="./public/contents-notebook-coffee.jpg" class="bleed-right" />

</template>

---
layout: section
---

# Why share data

---
src: ../library/combining-data/why.md
section: 'Why share data'
---

---
layout: content
heading: FAIR data
subheading: The research cycle
section: 'Why share data'
---

<style>
.fair-wrap { display: flex; align-items: center; gap: 3rem; height: 100%; }
.fair-svg { width: 48%; height: auto; flex: none; }
.fair-links { list-style: none; padding: 0 !important; margin: 0; }
.fair-links li { display: flex; align-items: center; gap: 0.75rem; font-size: 22px !important; margin-bottom: 1.25rem !important; }
.chips { display: flex; gap: 0.3rem; min-width: 4.6rem; }
.chip { width: 2.1rem; height: 2.1rem; border-radius: 6px; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 18px; color: #fff; }
.chip.f { background: #4285F4; }
.chip.a { background: #E6B96A; color: #333333; }
.chip.i { background: #0097A7; }
.chip.r { background: #6A4C93; }
</style>

<div class="fair-wrap">
<svg class="fair-svg" viewBox="0 0 480 420" role="img" aria-label="FAIR cycle: Findable, Accessible, Interoperable, Reusable">
  <defs>
    <marker id="fair-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#9AA0A6" />
    </marker>
  </defs>

  <g fill="none" stroke="#9AA0A6" stroke-width="3" marker-end="url(#fair-arrow)">
    <path d="M185.2,97.7 A125,125 0 0 1 294.8,97.7" />
    <path d="M352.3,155.2 A125,125 0 0 1 352.3,264.8" />
    <path d="M294.8,322.3 A125,125 0 0 1 185.2,322.3" />
    <path d="M127.7,264.8 A125,125 0 0 1 127.7,155.2" />
  </g>

  <rect x="30" y="30" width="140" height="110" rx="12" fill="#4285F4" />
  <text x="100" y="86" text-anchor="middle" font-size="48" font-weight="700" fill="#fff">F</text>
  <text x="100" y="118" text-anchor="middle" font-size="17" fill="#fff">Findable</text>

  <rect x="310" y="30" width="140" height="110" rx="12" fill="#E6B96A" />
  <text x="380" y="86" text-anchor="middle" font-size="48" font-weight="700" fill="#333333">A</text>
  <text x="380" y="118" text-anchor="middle" font-size="17" fill="#333333">Accessible</text>

  <rect x="310" y="280" width="140" height="110" rx="12" fill="#0097A7" />
  <text x="380" y="336" text-anchor="middle" font-size="48" font-weight="700" fill="#fff">I</text>
  <text x="380" y="368" text-anchor="middle" font-size="17" fill="#fff">Interoperable</text>

  <rect x="30" y="280" width="140" height="110" rx="12" fill="#6A4C93" />
  <text x="100" y="336" text-anchor="middle" font-size="48" font-weight="700" fill="#fff">R</text>
  <text x="100" y="368" text-anchor="middle" font-size="17" fill="#fff">Reusable</text>
</svg>

<ul class="fair-links">
  <li v-click><span class="chips"><span class="chip f">F</span></span>Catalogue</li>
  <li v-click><span class="chips"><span class="chip a">A</span><span class="chip r">R</span></span>DataSHIELD</li>
</ul>
</div>


---
layout: content
heading: Catalogue
section: 'Why share data'
subheading: Making collections discoverable
---

<div style="display: flex; gap: 2rem; margin-top: 1rem;">
<div style="flex: 2;">
<img src="./public/screenshot-catalogue.png" style="width: 80%; border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
</div>
<div style="flex: 1; font-size: 18px; line-height: 1.5; display: flex; flex-direction: column; gap: 1rem;">
<p>• Open source metadata catalogue — information about data, not the data itself</p>
<p>• Search across consortia for harmonised variables and collections</p>
<p>• Upload variables and Common Data Model mappings</p>
</div>
</div>

---
layout: section
---

# Federated analysis

---
src: ../library/combining-data/options.md
section: 'Federated analysis'
---

---
layout: content
heading: How it works
subheading: 
section: 'Federated analysis'
---

<DatashieldArchitecture />

---
layout: content
heading: How it works
subheading: Across a network
section: 'Federated analysis'
---

<div style="border: 2px dashed #9AA0A6; border-radius: 10px; height: 85%; display: flex; align-items: center; justify-content: center; color: #9AA0A6; font-size: 20px; text-align: center;">
TODO: map-based animation — same steps as the previous slide,<br />with Armadillo nodes shown at their locations on the map
</div>

---
layout: section
---

# DataSHIELD

---
layout: content
heading: What is DataSHIELD?
section: 'DataSHIELD'
subheading: Bringing the analysis to the data
---

<div style="font-size: 17px; line-height: 1.5;">

- Open-source, R-based platform for **privacy-preserving analysis** of biomedical, healthcare and social-science data
- Architecture consists of collection of:
    - (i) R-packages (user end) & (ii) java application installed alongside data

</div>

---
layout: content
heading: How DataSHIELD works
section: 'DataSHIELD'
---

<DatashieldArchitectureFinal />

---
layout: content
heading: Different frameworks
subheading: 
section: 'DataSHIELD'
clicks: 1
---

<style>
.fa-type-col { padding: 1rem 1.5rem; }
.fa-type-col h3 { font-size: 1.15rem; text-align: center; }
.fa-type-col .fa-type-desc { margin: 0 0 1.25rem 0; font-size: 14px; text-align: center; }
.fa-protocols { display: flex; flex-direction: column; gap: 1rem; align-items: center; }
.fa-protocol { display: flex; align-items: center; gap: 0.9rem; background: white; border-radius: 10px; padding: 0.6rem 1.2rem; width: 100%; box-sizing: border-box; }
.fa-protocol img { height: 32px; width: auto; flex: none; }
.fa-protocol span { font-size: 15px; font-weight: 600; color: #333; }
</style>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem;">
  <div class="tint-card fa-type-col" style="--c: #0097A7;" :class="$clicks < 1 ? 'active' : 'dimmed'">
    <h3>Pipeline</h3>
    <p class="fa-type-desc">Submit a job once, receive results</p>
    <div class="fa-protocols">
      <div class="fa-protocol">
        <img src="./public/logo-flower.png" />
        <span>Flower</span>
      </div>
      <div class="fa-protocol">
        <img src="./public/logo-vantage6.png" />
        <span>Vantage6</span>
      </div>
    </div>
  </div>
  <div class="tint-card fa-type-col" style="--c: #4285F4;" :class="$clicks >= 1 ? 'active' : 'dimmed'">
    <h3>Work interactively</h3>
    <p class="fa-type-desc">Researcher runs analyses as if working locally</p>
    <div class="fa-protocols">
      <div class="fa-protocol">
        <img src="./public/icon-datashield.png" style="height: 26px;" />
      </div>
    </div>
  </div>
</div>

---
src: ../library/datashield/analysis-options.md
section: 'DataSHIELD'
---

---
layout: content
heading: DataSHIELD
subheading: No access to individual-level data
section: 'DataSHIELD'
---

- Researchers <strong v-mark="{ at: 1, color: '#E6B96A', type: 'highlight' }">never see</strong> individual participant records — only aggregate results come back
- Every server-side function has built-in **disclosure checks**, e.g.:
  - Minimum cell counts in tables, and minimum subset sizes
  - Summaries returned instead of raw values (e.g. quantiles, not minima and maxima)
  - Plots built from smoothed or binned data, not raw points
- Functions that would return individual values are [**blocked**]{style="color: #D9534F"}
- Data owners set the disclosure thresholds on their own server

---
layout: content
heading: Deploying DataSHIELD
section: 'DataSHIELD'
subheading: 
clicks: 1
---

<style>
.deploy-card { flex: 1; padding: 1.2rem 1.5rem; }
.deploy-card h3 { font-size: 1.1rem; margin-bottom: 0.6rem; }
</style>

<div style="font-size: 18px; line-height: 1.6; margin-bottom: 1.5rem;">
To run DataSHIELD, each data owner installs a <strong>java application</strong> on a local server or VM. Two implementations exist:
</div>

<div style="display: flex; gap: 2rem; margin-top: 0.5rem;">
  <div class="tint-card deploy-card" style="--c: #4285F4;" :class="$clicks < 1 ? 'active' : 'dimmed'">
    <h3>Armadillo</h3>
    <p style="font-size: 16px; line-height: 1.5; margin: 0;">Lightweight server developed and maintained by UMCG as part of the <strong>MOLGENIS</strong> software suite.</p>
  </div>
  <div class="tint-card deploy-card" style="--c: #D3621F;" :class="$clicks >= 1 ? 'active' : 'dimmed'">
    <h3>Opal</h3>
    <p style="font-size: 16px; line-height: 1.5; margin: 0;">Multipurpose database and data harmonisation platform developed and maintained by <strong>OBiBa</strong>.</p>
  </div>
</div>

---
layout: section
---

# Projects

---
layout: chart-full
heading: DataSHIELD nodes managed by MOLGENIS
section: Projects
---

<div style="position: relative; width: 100%; height: 100%;">
  <img src="./public/map_all_nodes.png" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: contain; object-position: left;" />
  <div style="position: absolute; left: 48%; right: 2rem; top: 1rem;">
    <p style="font-size: 18px;">Three examples:</p>
    <ol style="padding-left: 1.5rem; margin: 0;">
      <li style="font-size: 18px; margin-bottom: 0.5rem;">ATHLETE</li>
      <li style="font-size: 18px; margin-bottom: 0.5rem;">NDTD</li>
      <li style="font-size: 18px; margin-bottom: 0.5rem;">TODO: Africa project</li>
    </ol>
  </div>
</div>

---
layout: chart-full
heading: "Example 1: ATHLETE"
section: Projects
---

<div style="position: relative; width: 100%; height: 100%;">
  <img src="./public/map_athlete.png" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: contain; object-position: left;" />
  <div style="position: absolute; left: 48%; right: 2rem; top: 1rem;">
    <ul style="padding-left: 1.5rem; margin: 0;">
      <li style="font-size: 18px; margin-bottom: 0.5rem;">H2020 project: <em>Advancing tools for exposome research</em></li>
      <li style="font-size: 18px; margin-bottom: 0.5rem;">TODO: aims, number of nodes, example analyses</li>
    </ul>
  </div>
</div>

---
layout: chart-full
heading: "Example 2: NDTD"
section: Projects
---

<div style="position: relative; width: 100%; height: 100%;">
  <img src="./public/map_ndtd.png" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: contain; object-position: left;" />
  <div style="position: absolute; left: 48%; right: 2rem; top: 1rem;">
    <ul style="padding-left: 1.5rem; margin: 0;">
      <li style="font-size: 18px; margin-bottom: 0.5rem;">Netherlands network for difficult-to-treat depression</li>
      <li style="font-size: 18px; margin-bottom: 0.5rem;">TODO: aims, number of nodes, example analyses</li>
    </ul>
  </div>
</div>

---
layout: chart-full
heading: "Example 3: TODO Africa project"
section: Projects
---

<div style="position: relative; width: 100%; height: 100%;">
  <div style="position: absolute; left: 0; top: 0; width: 45%; height: 100%; border: 2px dashed #9AA0A6; border-radius: 10px; display: flex; align-items: center; justify-content: center; color: #9AA0A6; font-size: 18px;">TODO: map with Africa nodes</div>
  <div style="position: absolute; left: 48%; right: 2rem; top: 1rem;">
    <ul style="padding-left: 1.5rem; margin: 0;">
      <li style="font-size: 18px; margin-bottom: 0.5rem;">TODO: project name, aims, nodes</li>
    </ul>
  </div>
</div>

---
layout: section
---

# Demo

---
layout: content
heading: Demo
subheading: Analyst perspective
section: Demo
---

---
layout: content
heading: Demo
subheading: Data manager perspective
section: Demo
---

---
layout: section
---

# Infrastructure

---
src: ../library/infrastructure/hosting.md
section: 'Infrastructure'
---

---
layout: section
---

# Legal

---
layout: content
heading: Legal
subheading: Agreements are still needed
section: Legal
---

- Data **does not leave** your institution, but you are still <strong v-mark="{ at: 1, color: '#E6B96A', type: 'highlight' }">allowing it to be processed</strong> by external researchers
- Most institutions therefore require a **legal agreement** before granting access
- TODO: types of agreement (e.g. data processing / data access agreement) and who signs

<div class="sticky-note" v-click style="right: 4rem; bottom: 5rem;">Who signs these at your institution?</div>
