---
theme: ../theme
title: MOLGENIS Armadillo
info: A lightweight server for federated analysis with DataSHIELD
author: Tim Cadman
date: 2026-06-15
aspectRatio: '16/9'
---

# MOLGENIS Armadillo
A lightweight server for federated analysis<br>using DataSHIELD (and Flower)

<div class="author-info">
  <p><strong>Tim Cadman</strong></p>
  <p>Senior Data Scientist</p>
</div>

<div class="title-logos">
  <img src="./public/molgenis-logo.png" class="logo-molgenis" />
  <img src="./public/umcg-logo.png" class="logo-umcg" />
</div>

---
layout: content-img-right
heading: Background
subheading: MOLGENIS
image: ./public/molgenis-ecosystem.png
imageScale: '100'
---

- **MOLGENIS** data infrastructure accelerates **multi-center health research collaborations** — 60 projects, 35 FTE
- Armadillo is part of the **MOLGENIS suite**, which also includes the **EMX2 data warehouse** and the **MOLGENIS catalogue**

---
layout: content
heading: Our team
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
layout: content-img-right
heading: Background
subheading: Armadillo
image: ./public/armadillo-logo-border.png
imageScale: '60'
---

- We built Armadillo (**since 2019**) to help a large consortium that was struggling with other implementations of federated (DataSHIELD) analysis
- Armadillo is now **mature** and a **cornerstone of the core DataSHIELD community project**
- **30 nodes** maintained by us (and an unknown number maintained by others)

---
layout: content-img-right
heading: Background
subheading: Active MOLGENIS networks
image: ./public/cohort-map-new.png
imageScale: '100'
---

- **H2020 LifeCycle** (11 nodes) — *Early stressors and lifecourse health*
- **H2020 ATHLETE** (11 nodes) — *Advancing tools for exposome research*
- **NDTD** (4 nodes) — *NL network for difficult-to-treat depression*
- **JOIN-MIND** (4-node pilot) — *NL network for mental health indicators*

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
layout: content-img-right
heading: What is Armadillo?
subheading: Design
image: ./public/armadillo-logo-border.png
imageScale: '75'
imageWidth: '22'
imageAlign: 'flex-start'
---

- **Open-source server** designed to securely <br> store data and run DataSHIELD analysis
- **Lightweight, easy to install and operate**:
    - Remove database engines so large tables <br>can be served on modest hardware
    - No need for a sysadmin to maintain server
    - Easy to add or update **profiles** that <br> provide the analysis tools
- Integrated with **LS AAI** — no passwords in R

---
layout: content-img-right
heading: What is Armadillo?
subheading: Features
image: ./public/armadillo-logo-border.png
imageScale: '75'
imageWidth: '22'
imageAlign: 'flex-start'
---

- **Backend** data storage, access management <br> & Docker container management
- **User Interface (UI)**  for data managers 
    - create projects & upload data 
    - manage users 
    - manage DataSHIELD packages
- **R package** for data management
- *Ongoing:* **Flower** integration 

---
layout: content-img-right
heading: Features
subheading: 'OIDC authentication'
image: ./public/ui-login.png
imageScale: '85'
---

- Armadillo delegates login to a separate **authentication server** via OpenID Connect (OIDC), e.g. **SURFconext, Life Science AAI, SRAM**
- Users **self-register** on the auth server with their **institutional login**
- Data managers at each node grant researcher access
- Only users granted admin permission can log in to the UI

---
layout: content-img-right
heading: Features
subheading: Manage projects and data
image: ./public/ui-projects.png
imageScale: '100'
---

- Data are grouped into **projects** <br> (e.g. per study or consortium)
- Each project can be shared with <br> specific users
- Admins can add, edit and remove <br> projects directly from the UI

---
layout: content-img-right
heading: Features
subheading: Data storage
image: ./public/ui-data.png
imageScale: '100'
---

- Data stored on the server filesystem as **Parquet files** 
- Upload through the **UI** (drag & drop) or <br> the **R package**
- Create **views** for different research projects so data don't need to be <br> uploaded twice

---
layout: content-img-right
heading: Features 
subheading: Analysis profiles
image: ./public/profile-packages.png
imageScale: '100'
---

- **Profiles** = versioned collections of DataSHIELD packages as Docker images (e.g. core statistical functions, <br> exposome package)
- UMCG actively manages profiles in the **DataSHIELD community**
- Can create a **custom profile** for <br> NCC projects or reuse existing

---
layout: content-img-right
heading: Features 
subheading: Analysis profiles
image: ./public/ui-containers.png
imageScale: '100'
---

- Run **multiple profiles side by side** in separate containers for reproducibility
- Control which packages and functions are permitted via **whitelist / blacklist**
- **Start, stop and add** profiles from the UI

---
layout: content-img-right
heading: Features
subheading: Users & permissions
image: ./public/ui-users.png
imageScale: '100'
---

- Add and remove users; grant access <br> **per project**
- Mark trusted accounts as **admin**

---
layout: content-img-right
heading: Features
subheading: Audit log
image: ./public/ui-logs.png
imageScale: '100'
---

- **Audit log** of every action — who connected and what they ran
- **Search**, sort, and filter to **errors only**
- Download the log for external monitoring

---
layout: content-img-right
heading: Features 
subheading: Server metrics
image: ./public/ui-metrics.png
imageScale: '100'
---

- Live **server metrics** — disk usage, JVM/process, Rserve
- Per-user directory and file counts
- Download metrics for monitoring <br> and alerting

---
layout: content-img-left
heading: Deployment
subheading: 1. Central Analysis Server (CAS)
image: ./public/armadillo-overview.png
imageScale: '100'
---

- Deployed alongside a **Central Analysis Server (CAS)** — a containerised JupyterHub researcher environment
- CAS lets us control researcher environment (e.g. package versions)

---
layout: content-img-right
heading: Deployment
subheading: '2: Install Armadillo'
image: ./public/docs-install.png
imageScale: '100'
---

- **On-premises support** — we help you install Armadillo on your own server
- UMCG can also **host it for you** on the **UMCG Azure Cloud**
- Contact **support@molgenis.org**
- Support via the DataSHIELD Slack community **#armadillo-support**

---
layout: content
heading: Deployment
subheading: Variants
---

<style>
.hw-grid {
  display: grid;
  grid-template-columns: 1.4fr 1fr 1fr 1fr;
  border: 2px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
}
.hw-grid .h {
  padding: 0.5rem 0.9rem;
  font-weight: bold;
  font-size: 0.8rem;
  background: var(--slidev-theme-primary);
  color: white;
}
.hw-grid .h:not(:last-child) { border-right: 1px solid rgba(255,255,255,0.3); }
.hw-grid .c {
  padding: 0.45rem 0.9rem;
  border-bottom: 1px solid #eee;
  border-right: 1px solid #eee;
  font-size: 0.8rem;
}
.hw-grid .c:nth-child(4n) { border-right: none; }
.hw-grid .c:nth-last-child(-n+4) { border-bottom: none; }
.hw-grid .lab { font-weight: 600; color: var(--slidev-theme-primary); background: #f8f9fa; }
</style>

<div style="display: flex; gap: 2rem; margin-top: 0.75rem; align-items: flex-start;">
<div style="flex: 1.1; font-size: 15px; line-height: 1.5;">

- **Docker Quickstart** (`docker-compose.yml`) — evaluation / training with Keycloak as OIDC
- **Native Linux install** (systemd) via installation script — *production and Docker management*
- **Kubernetes** (Helm deployment) — advanced cloud deployments

<div style="margin-top: 0.6rem;">

**Requirements**
- Linux · Java 21 · Docker engine
- SSL frontend (Nginx with certificate) and a domain name

</div>

</div>
<div style="flex: 1; font-size: 14px;">

<div style="font-size: 16px; font-weight: 700; color: var(--slidev-theme-primary); margin-bottom: 0.5rem; text-align: center;">Hardware requirements</div>

<div class="hw-grid">
  <div class="h">Participants</div>
  <div class="h">Memory (GB)</div>
  <div class="h">Disk (GB)</div>
  <div class="h">CPU cores</div>

  <div class="c lab">0–20,000</div>
  <div class="c">8</div>
  <div class="c">100</div>
  <div class="c">4</div>

  <div class="c lab">20,000–70,000</div>
  <div class="c">16</div>
  <div class="c">100</div>
  <div class="c">4</div>

  <div class="c lab">70,000 +</div>
  <div class="c">32</div>
  <div class="c">150</div>
  <div class="c">8</div>
</div>

</div>
</div>

---
layout: content
heading: Deployment
subheading: 3. Security
---

<div style="font-size: 18px; line-height: 1.7; margin-top: 1rem;">

- **SSL certificate** (Nginx)
- **Firewalling** — only whitelist the Central Analysis Server and the IPs of data managers
- **Update regularly**
- Data stored on disk on the VM (`/usr/share/armadillo/data`) — **not publicly available**
- **Back up** the data directory (`/usr/share/armadillo/data`) and configuration (`/etc/armadillo/`)

</div>

---
layout: content
heading: Demo
---

---
layout: content
heading: Potential advantages for NCC
subheading: To be discussed…
---

<style>
.adv-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.2rem 1.5rem;
  margin-top: 1.25rem;
}
.adv-card {
  border: 2px solid #ddd;
  border-left: 5px solid #c7ccd1;
  border-radius: 10px;
  padding: 1rem 1.25rem;
  opacity: 0.45;
  transition: opacity 0.4s ease, border-color 0.4s ease, box-shadow 0.4s ease, background-color 0.4s ease;
}
.adv-card.active {
  opacity: 1;
  border-color: var(--slidev-theme-primary);
  border-left-color: var(--slidev-theme-primary);
  background: rgba(37, 99, 235, 0.08);
  box-shadow: 0 2px 12px rgba(37, 99, 235, 0.18);
}
.adv-card h3 {
  margin: 0 0 0.4rem 0;
  font-size: 1.15rem;
  color: var(--slidev-theme-primary);
}
.adv-card p {
  margin: 0;
  font-size: 1rem;
  line-height: 1.5;
  color: #444;
}
</style>

<div v-click style="display: none;"></div>
<div v-click style="display: none;"></div>
<div v-click style="display: none;"></div>
<div v-click style="display: none;"></div>

<div class="adv-grid">
  <div class="adv-card" :class="{ active: $clicks >= 1 }">
    <h3>Install</h3>
    <p>Lightweight, with fewer dependencies</p>
  </div>
  <div class="adv-card" :class="{ active: $clicks >= 2 }">
    <h3>User experience</h3>
    <p>More intuitive UI; the extra Opal features may not be needed for NCC</p>
  </div>
  <div class="adv-card" :class="{ active: $clicks >= 3 }">
    <h3>Control</h3>
    <p>We maintain Armadillo — not dependent on a partner (OBiBa) outside the network</p>
  </div>
  <div class="adv-card" :class="{ active: $clicks >= 4 }">
    <h3>Deployment</h3>
    <p>Proven workflow with CAS, auth server and nodes already deployed >30 sites</p>
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
