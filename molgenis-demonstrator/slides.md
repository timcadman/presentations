---
theme: ../theme
title: Molgenis Demonstrator
info: Molgenis Demonstrator
author: Tim Cadman
aspectRatio: '16/9'
---

# From Data Discovery to Federated Analysis
Supporting the Research Journey

<div class="author-info">
  <p><strong>Tim Cadman</strong></p>
  <p>Senior Data Scientist</p>
</div>

---
layout: content-img-right
heading: The problem
subheading: A fragmented researcher journey
image: ./public/screenshot-combining-data.jpeg
---

- Large quantities of existing data (e.g. cohort studies, biobanks)
- Combining data sources increases statistical power and enables replication
- However, researchers face a fragmented landscape when trying to find and reuse data

---
layout: content
heading: Our Journey
subheading: From FAIR at Source to FAIR Research Federations
---

<style>
.journey-grid {
  display: grid;
  grid-template-columns: auto 1fr 1fr;
  gap: 0;
  border: 2px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
}
.journey-grid .header {
  padding: 0.5rem 1rem;
  font-weight: bold;
  font-size: 0.95rem;
  background: var(--slidev-theme-primary, #2563eb);
  color: white;
  border-bottom: 2px solid #ddd;
}
.journey-grid .header:not(:last-child) {
  border-right: 1px solid rgba(255,255,255,0.3);
}
.journey-grid .cell.label {
  font-weight: bold;
  background: #f8f9fa;
  color: var(--slidev-theme-primary, #2563eb);
}
.journey-grid .cell {
  padding: 0.5rem 1rem;
  border-bottom: 1px solid #eee;
  border-right: 1px solid #eee;
  font-size: 0.85rem;
  transition: opacity 0.4s ease;
}
.journey-grid .cell:nth-child(3n+2) {
  border-right: none;
}
.journey-grid .cell:nth-last-child(-n+3) {
  border-bottom: none;
}
.slidev-vclick-hidden {
  opacity: 0.15 !important;
  pointer-events: none;
}
</style>

<div class="journey-grid">
  <div class="header"></div>
  <div class="header">Challenge</div>
  <div class="header">Solution</div>

  <div v-click="1" class="cell label">Local data</div>
  <div v-click="1" class="cell">Not structured or reusable</div>
  <div v-click="1" class="cell">Harmonise to established open standards</div>

  <div v-click="2" class="cell label">Catalogue</div>
  <div v-click="2" class="cell">Collections not discoverable</div>
  <div v-click="2" class="cell">Open source metadata catalogue</div>

  <div v-click="3" class="cell label">Request</div>
  <div v-click="3" class="cell">Months lost negotiating collection-by-collection</div>
  <div v-click="3" class="cell">Central point of access for all requests</div>

  <div v-click="4" class="cell label">Access</div>
  <div v-click="4" class="cell">Each holder manages permissions separately</div>
  <div v-click="4" class="cell">Federated identity & access</div>

  <div v-click="5" class="cell label">Analyse</div>
  <div v-click="5" class="cell">Data transfer carries ethical, legal and practical difficulties</div>
  <div v-click="5" class="cell">Federated analysis — data never moves</div>
</div>

---
layout: content
heading: "Our approach"
subheading: "One open stack — same at every scale"
---

<style>
.stack-container {
  display: inline-flex;
  flex-direction: column;
  align-items: stretch;
  justify-content: flex-start;
  gap: 0.4rem;
  padding: 1rem 1.2rem;
  border: 2px solid #ddd;
  border-radius: 10px;
  background: rgba(148, 163, 184, 0.15);
}
.stack-card {
  width: auto;
  padding: 0.7rem 1.5rem;
  gap: 6rem;
  border-radius: 8px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: white;
  font-size: 0.95rem;
  transition: opacity 0.4s ease;
}
.stack-card .layer-name {
  font-weight: bold;
}
.stack-card .layer-tool {
  font-style: italic;
  opacity: 0.9;
}
.stack-card:nth-child(1) { background: #93c5fd; }
.stack-card:nth-child(2) { background: #60a5fa; }
.stack-card:nth-child(3) { background: #3b82f6; }
.stack-card:nth-child(4) { background: #2563eb; }
.stack-card:nth-child(5) { background: #1e3a5f; }
.slidev-vclick-hidden {
  opacity: 0.15 !important;
}
</style>

<div class="stack-container">
  <div v-click class="stack-card">
    <span class="layer-name">Local data</span>
    <span class="layer-tool">Harmonise to established standards</span>
  </div>
  <div v-click class="stack-card">
    <span class="layer-name">Catalogue</span>
    <span class="layer-tool">MOLGENIS meta-data catalogue</span>
  </div>
  <div v-click class="stack-card">
    <span class="layer-name">Request</span>
    <span class="layer-tool">BBMRI-ERIC Negotiator</span>
  </div>
  <div v-click class="stack-card">
    <span class="layer-name">Access</span>
    <span class="layer-tool">LS AAI + OIDC</span>
  </div>
  <div v-click class="stack-card">
    <span class="layer-name">Analyse</span>
    <span class="layer-tool">DataSHIELD + Molgenis Armadillo</span>
  </div>
</div>

---
layout: content
heading: Local Data
subheading: Harmonise to established standards
---

- *Placeholder — content to be added*

---
layout: content
heading: Catalogue
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
layout: content
heading: Negotiator
subheading: One request — not twenty emails
---

<div style="display: flex; gap: 2rem; margin-top: 1rem;">
<div style="flex: 2;">
<img src="./public/screenshot-negotiator.png" style="width: 80%; border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
</div>
<div style="flex: 1; font-size: 18px; line-height: 1.5; display: flex; flex-direction: column; gap: 1rem;">
<p>• Open-source access negotiation for research infrastructures</p>
<p>• One request fans out to many holders — each keeps its own yes/no</p>
<p>• Customisable workflows, messaging, and moderation</p>
</div>
</div>

---
layout: content
heading: Access
subheading: Federated identity & access
---

<div style="display: flex; gap: 2rem; margin-top: 1rem;">
<div style="flex: 2;">
<img src="./public/screenshot-ls-login.png" style="width: 80%; border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
</div>
<div style="flex: 1; font-size: 18px; line-height: 1.5; display: flex; flex-direction: column; gap: 1rem;">
<p>• LS Login — federated identity service from EOSC-Life</p>
<p>• Researchers authenticate with home institution credentials</p>
<p>• Single sign-on across research infrastructures — no separate accounts</p>
</div>
</div>

---
layout: content
heading: Analyse
subheading: Federated analysis — data never moves
---

<div style="display: flex; gap: 2rem; margin-top: 1rem;">
<div style="flex: 2;">
<div style="display: flex; gap: 1rem; align-items: center; justify-content: center;">
<img src="./public/armadillo-logo.png" style="height: 50px;">
<img src="./public/icon-datashield.png" style="height: 35px;">
</div>
<img src="./public/armadillo-architecture.png" style="width: 90%; margin-top: 0.5rem;">
</div>
<div style="flex: 1; font-size: 18px; line-height: 1.5; display: flex; flex-direction: column; gap: 1rem;">
<p>• Analysis travels to the data — only safe summary statistics shared</p>
<p>• MOLGENIS Armadillo — lightweight server per cohort</p>
<p>• 20+ nodes in production across LifeCycle, ATHLETE, LongITools, EUCAN-Connect</p>
</div>
</div>

---
layout: content
heading: "Demo"
subheading: "Research question"
---

<div style="display: flex; align-items: center; justify-content: center; height: 60%; text-align: center;">
  <p style="font-size: 1.6rem; font-style: italic; line-height: 1.6; max-width: 80%;">"How is mode of delivery (e.g. vaginal, caesarean) associated with maternal mental health across different EU countries?"</p>
</div>

---
layout: content
heading: "Demo"
subheading: "Local data"
---

<DemoSlide step="Local data" image="./public/screenshot-lc-map.png" text="Health data harmonised in previous EU 'LifeCycle' project" />

---
layout: content
heading: "Demo"
subheading: "Catalogue"
---

<DemoSlide step="Catalogue" image="./public/screenshot-catalogue-search.png" text="Search for birth cohorts with relevant harmonised data" />

---
layout: content
heading: "Demo"
subheading: "Catalogue"
---

<DemoSlide step="" text="TODO: feature request to select multiple variables and view in harmonisation matrix" />

---
layout: content
heading: "Demo"
subheading: "Catalogue"
---

<DemoSlide step="Request" text="TODO: feature request to send multiple variable request to Negotiator without going via BBMRI directory" />

---
layout: content
heading: "Demo"
subheading: "Request"
---

<DemoSlide step="Request" image="./public/screenshot-neg-project.png" text="Enter project details" />

---
layout: content
heading: "Demo"
subheading: "Request"
---

<DemoSlide step="Request" image="./public/screenshot-neg-request.png" text="Provide study description" />

---
layout: content
heading: "Demo"
subheading: "Request"
---

<DemoSlide step="Request" image="./public/screenshot-neg-ethics.png" text="Enter ethics details" />

---
layout: content
heading: "Demo"
subheading: "Request"
---

<DemoSlide step="Request" image="./public/screenshot-neg-review.png" text="Submit request" />

---
layout: content
heading: "Demo"
subheading: "Request"
---

<DemoSlide step="Request" image="./public/screenshot-neg-submitted.png" text="Await approval" />

---
layout: content
heading: "Demo"
subheading: "Request"
---

<DemoSlide step="Request" text="TODO: Screenshots for cohorts receiving and approving request" />

---
layout: content
heading: "Demo"
subheading: "Request"
---

<DemoSlide step="Request" text="TODO(?): Process to add user automatically to Armadillo " />


---
layout: content
heading: "Demo"
subheading: "Access"
---

<DemoSlide step="Access" image="./public/screenshot-arma-login.png" text="Data manager logs on to local Armadillo instance" />

---
layout: content
heading: "Demo"
subheading: "Access"
---

<DemoSlide step="Access" image="./public/screenshot-arma-view.png" text="Creates view with approved variables" />

---
layout: content
heading: "Demo"
subheading: "Access"
---

<DemoSlide step="Access" image="./public/screenshot-arma-users.png" text="Adds user and grants them access to their project view, notifies user" />

---
layout: content
heading: "Demo"
subheading: "Analyse"
---

<DemoSlide step="Analyse" image="./public/screenshot-jupyter.png" text="Researcher logs into Central Analysis Server using OIDC" />


---
layout: content
heading: "Demo"
subheading: "Analyse"
---

<DemoSlide step="Analyse" image="./public/screenshot-ds-scripts.png" text="Researcher connects to cohorts via DataSHIELD and writes analysis scripts" />

---
layout: content
heading: "Demo"
subheading: "Analyse"
---

<DemoSlide step="Analyse" image="./public/screenshot-forest-plot.jpg" text="Preliminary results: mode of delivery and postpartum depression" />
