---
theme: ../theme
title: MOLGENIS Armadillo
info: A lightweight server for federated analysis with DataSHIELD
author: Tim Cadman
date: 2026-06-15
aspectRatio: '16/9'
---

# MOLGENIS Armadillo
A lightweight server for federated analysis

<div class="author-info">
  <p><strong>Tim Cadman</strong></p>
  <p>Senior Data Scientist</p>
</div>

<div class="title-logos">
  <img src="./public/molgenis-logo.png" class="logo-molgenis" />
</div>

---
layout: content
heading: Our team
---

<style>
.team-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.2rem 1rem;
  margin-top: 1.5rem;
}
.team-card {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  text-align: left;
}
.team-avatar {
  width: 92px;
  height: 92px;
  border-radius: 50%;
  background: rgba(148, 163, 184, 0.25);
  border: 2px dashed #aaa;
  object-fit: cover;
  margin-bottom: 0.5rem;
}
.team-name {
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--slidev-theme-primary);
  line-height: 1.2;
}
.team-role {
  font-size: 0.8rem;
  color: #555;
}
</style>

<!-- Replace each <div class="team-avatar"></div> with <img class="team-avatar" src="./public/team-<name>.jpg" /> once photos are added -->
<div class="team-grid">
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

---
layout: content
heading: What is DataSHIELD?
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
---

<DatashieldArchitectureFinal />

---
layout: content
heading: Deploying DataSHIELD
subheading: 
---

<style>
.deploy-card {
  flex: 1;
  border: 2px solid #bbb;
  border-radius: 10px;
  padding: 1.2rem 1.5rem;
  transition: border-color 0.4s ease, box-shadow 0.4s ease;
}
.deploy-card h3 {
  margin: 0 0 0.6rem 0;
  color: #555;
  transition: color 0.4s ease;
}
.deploy-card.active {
  border-color: var(--slidev-theme-primary);
  box-shadow: 0 2px 12px rgba(37, 99, 235, 0.18);
}
.deploy-card.active h3 {
  color: var(--slidev-theme-primary);
}
.deploy-card.opal.active {
  border-color: rgb(211, 98, 31);
  box-shadow: 0 2px 12px rgba(211, 98, 31, 0.18);
}
.deploy-card.opal.active h3 {
  color: rgb(211, 98, 31);
}
</style>

<div style="font-size: 18px; line-height: 1.6; margin-bottom: 1.5rem;">
To run DataSHIELD, each data owner installs a <strong>java application</strong> on a local server or VM. Two implementations exist:
</div>

<div v-click style="display: none;"></div>

<div style="display: flex; gap: 2rem; margin-top: 0.5rem;">
  <div :class="['deploy-card', { active: $clicks < 1 }]">
    <h3>Armadillo</h3>
    <p style="font-size: 16px; line-height: 1.5; margin: 0;">Lightweight server developed and maintained by UMCG as part of the <strong>MOLGENIS</strong> software suite.</p>
  </div>
  <div :class="['deploy-card', 'opal', { active: $clicks >= 1 }]">
    <h3>Opal</h3>
    <p style="font-size: 16px; line-height: 1.5; margin: 0;">Multipurpose database and data harmonisation platform developed and maintained by <strong>OBiBa</strong>.</p>
  </div>
</div>

---
layout: content
heading: Armadillo
subheading: "Goal: Making running DataSHIELD easier"
---

<div style="display: flex; gap: 2.5rem; align-items: center; margin-top: 1rem;">
<div style="flex: 2; font-size: 18px; line-height: 1.6;">

- <strong>Open-source server</strong> designed to securely store data and run DataSHIELD analysis
- Remove database engines so large tables can be served on modest hardware
- No need for a sysadmin to maintain a DataSHIELD server - one time install
- Integrated with **Life Sciences Authentication (LS AAI)** — no passwords in R

</div>
<div style="flex: 1; display: flex; align-items: center; justify-content: center;">
<img src="./public/armadillo-logo.png" style="width: 70%; max-width: 200px;" />
</div>
</div>

---
layout: content
heading: Armadillo
subheading: Key features
---

<div style="display: flex; gap: 2.5rem; align-items: center; margin-top: 1rem;">
<div style="flex: 2; font-size: 18px; line-height: 1.6;">

- <strong>User Interface (UI)</strong> for data managers to create projects, upload data, manage users
- Accompanying R package for data management
- Easy to add or update **profiles** that provide the analysis tools
- Connection to Armadillo managed using <strong>OIDC token-based authentication</strong>

</div>
<div style="flex: 1; display: flex; align-items: center; justify-content: center;">
<img src="./public/armadillo-logo.png" style="width: 70%; max-width: 200px;" />
</div>
</div>

---
layout: content
heading: Features
subheading: OIDC Authentication
---

<div style="display: flex; gap: 2rem; margin-top: 1rem; align-items: flex-start;">
<div style="flex: 1.2;">
<img src="./public/ui-login.png" style="width: 75%; border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.15);">
</div>
<div style="flex: 1; font-size: 18px; line-height: 1.6;">

- Armadillo delegates login to a **separate authentication server** via **OpenID Connect (OIDC)**
- Users **self-register** on the auth server with their **institutional login**
- Only users granted admin permission can log in to the UI

</div>
</div>

---
layout: content
heading: Features
subheading: Manage projects and data
---

<div style="display: flex; gap: 2rem; margin-top: 1rem; align-items: flex-start;">
<div style="flex: 1.4;">
<img src="./public/ui-projects.png" style="width: 100%; border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.15);">
</div>
<div style="flex: 1; font-size: 18px; line-height: 1.6;">

- Data are grouped into **projects** (e.g. per study or consortium)
- Each project can be shared with specific users
- Admins can add, edit and remove projects directly from the UI

</div>
</div>

---
layout: content
heading: Features
subheading: Data storage
---

<div style="display: flex; gap: 2rem; margin-top: 1rem; align-items: flex-start;">
<div style="flex: 1.5;">
<img src="./public/ui-data.png" style="width: 100%; border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.15);">
</div>
<div style="flex: 1; font-size: 18px; line-height: 1.6;">

- Data stored on the **server filesystem as Parquet files** 
- Upload through the **UI** (drag & drop) or the **R package**
- Organise into folders and tables; preview without downloading

</div>
</div>

---
layout: content
heading: Features
subheading: Users & permissions
---

<div style="display: flex; gap: 2rem; margin-top: 1rem; align-items: flex-start;">
<div style="flex: 1.4;">
<img src="./public/ui-users.png" style="width: 100%; border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.15);">
</div>
<div style="flex: 1; font-size: 18px; line-height: 1.6;">

- Add and remove users; grant access **per project**
- Mark trusted accounts as **admin**

</div>
</div>

---
layout: content
heading: Features 
subheading: Analysis profiles
---

<div style="display: flex; gap: 2rem; margin-top: 1rem; align-items: flex-start;">
<div style="flex: 1.6;">
<img src="./public/ui-profiles.png" style="width: 100%; border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.15);">
</div>
<div style="flex: 1; font-size: 18px; line-height: 1.6;">

- **Profiles** = versioned collections of DataSHIELD packages as Docker images
- Control which packages and functions are permitted via **whitelist / blacklist**
- Run side by side in separate containers for reproducibility

</div>
</div>

---
layout: content
heading: Features
subheading: Audit log
---

<div style="display: flex; gap: 2rem; margin-top: 1rem; align-items: flex-start;">
<div style="flex: 1.5;">
<img src="./public/ui-logs.png" style="width: 100%; border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.15);">
</div>
<div style="flex: 1; font-size: 18px; line-height: 1.6;">

- **Audit log** of every action — who connected and what they ran
- **Search**, sort, and filter to <br> **errors only**
- Download the log for external monitoring

</div>
</div>

---
layout: content
heading: Features 
subheading: Server metrics
---

<div style="display: flex; gap: 2rem; margin-top: 1rem; align-items: flex-start;">
<div style="flex: 1.5;">
<img src="./public/ui-metrics.png" style="width: 100%; border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.15);">
</div>
<div style="flex: 1; font-size: 18px; line-height: 1.6;">

- Live **server metrics** — disk usage, JVM/process, Rserve
- Per-user directory and file counts
- Download metrics for monitoring and alerting

</div>
</div>

---
layout: content
heading: Deployment
---

<div style="display: flex; gap: 3rem; align-items: center; height: 82%;">
<div style="flex: 2.6; display: flex; justify-content: flex-start; align-items: center; height: 100%;">
  <img src="./public/armadillo-overview.png" style="max-width: 100%; max-height: 100%; object-fit: contain;" />
</div>
<div style="flex: 1.3; font-size: 17px; line-height: 1.6; padding-left: 0.5rem;">

- Deployed alongside a **Central Analysis Server (CAS)** — a containerised JupyterHub environment for researchers
- Secured behind an NGINX reverse proxy with IP white-listing restricting access to the CAS

</div>
</div>

---
layout: content
heading: Deployment
subheading: 'Step 1: install Armadillo'
---

<div style="display: flex; gap: 2rem; margin-top: 1rem; align-items: center;">
<div style="flex: 1; font-size: 18px; line-height: 1.6;">

- **Linux server** with Java and Docker
- Connect to the **central authentication service**
- UMCG can also **host it for you** (we often do)

</div>
<div style="flex: 1.3;">
<img src="./public/docs-install.png" style="width: 100%; border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.15);">
</div>
</div>

---
layout: content
heading: Deployment
subheading: 'Step 2: install profile containers'
---

<div style="display: flex; gap: 2rem; margin-top: 1rem; align-items: center;">
<div style="flex: 1; font-size: 18px; line-height: 1.6;">

- A **profile** = a bundle of analysis tools you trust for a study
- Create an **NCC-specific profile** or reuse an existing one

</div>
<div style="flex: 1.3;">
<img src="./public/ui-profiles.png" style="width: 100%; border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.15);">
</div>
</div>

---
layout: content
heading: Deployment
subheading: 'Step 3: upload data and give access'
---

<div style="display: flex; gap: 1.5rem; margin-top: 1rem; align-items: center;">
<div style="flex: 1;">
<img src="./public/ui-data.png" style="width: 100%; border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.15);">
</div>
<div style="flex: 1;">
<img src="./public/ui-users.png" style="width: 100%; border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.15);">
</div>
</div>

---
layout: content
heading: Federated multi-center analysis
subheading: Active networks maintained by MOLGENIS
---

<div style="display: flex; gap: 2rem; margin-top: 0.5rem; align-items: center;">
<div style="flex: 1; font-size: 15px; line-height: 1.5;">

- **H2020 LifeCycle** (11 nodes) — *Early stressors and lifecourse health*
- **H2020 ATHLETE** (11 nodes) — *Advancing tools for human exposome research*
- **NDTD** (4 nodes) — *NL network for difficult-to-treat depression*
- **JOIN-MIND** (4-node pilot) — *NL data infrastructure for mental health indicators*

<p style="margin-top: 1rem; font-size: 14px;">See <a href="https://molgeniscatalogue.org/">molgeniscatalogue.org</a> for more information</p>

</div>
<div style="flex: 1.3;">
<img src="./public/cohort-map.png" style="width: 100%;">
</div>
</div>

---
layout: content
heading: Demo
---

---
layout: content
heading: Armadillo vs Opal
subheading: Feature comparison
---

<style>
.cmp-grid {
  display: grid;
  grid-template-columns: 0.8fr 1.3fr 1.3fr;
  border: 2px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  margin-top: 0.25rem;
}
.cmp-grid .h {
  padding: 0.4rem 1rem;
  font-weight: bold;
  font-size: 0.9rem;
  background: var(--slidev-theme-primary);
  color: white;
}
.cmp-grid .h:not(:last-child) { border-right: 1px solid rgba(255,255,255,0.3); }
.cmp-grid .lab {
  font-weight: bold;
  background: #f8f9fa;
  color: var(--slidev-theme-primary);
}
.cmp-grid .c {
  padding: 0.32rem 1rem;
  border-bottom: 1px solid #eee;
  border-right: 1px solid #eee;
  font-size: 0.78rem;
  line-height: 1.35;
}
.cmp-grid .c:nth-child(3n+1) { border-right: 1px solid #eee; }
.cmp-grid .c:nth-child(3n) { border-right: none; }
.cmp-grid .c:nth-last-child(-n+3) { border-bottom: none; }
.cmp-grid .c, .cmp-grid .h { transition: background-color 0.4s ease, opacity 0.4s ease; }
.cmp-grid .dim { opacity: 0.3; }
.cmp-grid .c.arm.active { background: rgba(37, 99, 235, 0.12); }
.cmp-grid .c.opal.active { background: rgba(211, 98, 31, 0.12); }
.cmp-grid .h.opal.active { background: rgb(211, 98, 31); }
</style>

<div v-click style="display: none;"></div>

<div class="cmp-grid">
  <div class="h"></div>
  <div class="h arm" :class="{ dim: $clicks >= 1 }">Armadillo</div>
  <div class="h opal" :class="{ active: $clicks >= 1, dim: $clicks < 1 }">Opal</div>

  <div class="c lab">What it is</div>
  <div class="c arm" :class="{ active: $clicks < 1, dim: $clicks >= 1 }">Lightweight DataSHIELD server</div>
  <div class="c opal" :class="{ active: $clicks >= 1, dim: $clicks < 1 }">DataSHIELD server plus additional features</div>

  <div class="c lab">Built for</div>
  <div class="c arm" :class="{ active: $clicks < 1, dim: $clicks >= 1 }">DataSHIELD federated analysis</div>
  <div class="c opal" :class="{ active: $clicks >= 1, dim: $clicks < 1 }">Full data management: storage, harmonisation, metadata, cataloguing</div>

  <div class="c lab">Storage</div>
  <div class="c arm" :class="{ active: $clicks < 1, dim: $clicks >= 1 }">Filesystem — Parquet files</div>
  <div class="c opal" :class="{ active: $clicks >= 1, dim: $clicks < 1 }">Relational DB (MySQL, PostgreSQL, MariaDB) or MongoDB</div>

  <div class="c lab">Advantages</div>
  <div class="c arm" :class="{ active: $clicks < 1, dim: $clicks >= 1 }">Easy to deploy, fewer dependencies, user-friendly, maintained and deployed by UMCG</div>
  <div class="c opal" :class="{ active: $clicks >= 1, dim: $clicks < 1 }">Additional features e.g. harmonisation, cataloguing, advanced admin options</div>

  <div class="c lab">Disadvantages</div>
  <div class="c arm" :class="{ active: $clicks < 1, dim: $clicks >= 1 }">Lacks additional functionality of Opal</div>
  <div class="c opal" :class="{ active: $clicks >= 1, dim: $clicks < 1 }">
    More dependencies, heavier infrastructure, UI more complex
  </div>
</div>

---
layout: content
heading: Documentation and resources
---

- **Armadillo documentation** — [molgenis.github.io/molgenis-service-armadillo](https://molgenis.github.io/molgenis-service-armadillo/)
- **Github repo** — [github.com/molgenis/molgenis-service-armadillo](https://github.com/molgenis/molgenis-service-armadillo)
- **Armadillo paper** — [doi.org/10.1093/bioinformatics/btae726](https://doi.org/10.1093/bioinformatics/btae726)
- **MOLGENIS Catalogue** — [molgeniscatalogue.org](https://molgeniscatalogue.org)

<p style="margin-top: 2rem; font-size: 20px;">Questions? <strong>support@molgenis.org</strong></p>
