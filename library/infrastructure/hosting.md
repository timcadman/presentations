---
layout: content
heading: Setting up a node
subheading: Three hosting options
---

<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1.5rem; margin-top: 1rem;">
  <div class="tint-card" style="--c: #4285F4; padding: 1rem;">
    <h3><carbon-bare-metal-server />1. Self-hosting</h3>
    <p style="font-size: 15px;">Install Armadillo on your own server or VM</p>
  </div>
  <div class="tint-card" style="--c: #0097A7; padding: 1rem;">
    <h3><carbon-cloud />2. MOLGENIS Azure</h3>
    <p style="font-size: 15px;">UMCG hosts and maintains it for you on the UMCG Azure cloud</p>
  </div>
  <div class="tint-card" style="--c: #6A4C93; padding: 1rem;">
    <h3><carbon-data-center />3. SURF</h3>
    <p style="font-size: 15px;">TODO: hosting on SURF infrastructure</p>
  </div>
</div>

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
heading: "Option 1: Self-hosting"
subheading: Main steps
---

1. **Install** — Ubuntu server with Java 21 and Docker; run the Armadillo install script (runs as a `systemd` service)
2. **Nginx** — reverse proxy in front of Armadillo, with an SSL certificate for your domain
3. **Firewall** — only allow the Central Analysis Server and the data managers' IP addresses
4. **Authentication** — register your domain with an OIDC server (e.g. the DataSHIELD authentication server, Keycloak)

<p style="font-size: 14px; color: #9AA0A6; margin-top: 2rem;">Guide: molgenis.github.io/molgenis-service-armadillo</p>

---
layout: content
heading: "Option 2: MOLGENIS Azure hosting"
subheading:
---

- The MOLGENIS team at UMCG sets up and maintains the server on the **UMCG Azure cloud**
- Fully private: only you have access to the data
- TODO: costs, contract, what the data manager still does
- Contact [support@molgenis.org](mailto:support@molgenis.org)

---
layout: content
heading: "Option 3: SURF hosting"
subheading:
---

- TODO
