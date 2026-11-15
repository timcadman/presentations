---
theme: ../../theme
title: "IHEN tools: Federated analysis with DataSHIELD"
author: Juan Carlos Rivillas, Tim Cadman & Hüseyin Küçükali
aspectRatio: '16/9'
publish: true
themeConfig:
  sections: [Reusing data, 'What is DataSHIELD?', DataSHIELD demo, Sharing your data, Discussion]
transition: slide-left
mdc: true
---

# IHEN tools
Federated analysis with DataSHIELD

<div class="author-info">
  <p><strong>Juan Carlos Rivillas, Tim Cadman & Hüseyin Küçükali</strong></p>
</div>

<div class="title-logos">
  <img src="./public/molgenis-logo.png" class="logo-molgenis" />
  <img src="./public/umcg-logo.png" class="logo-umcg" />
</div>

---
layout: content-two-cols
heading: Contents
---

<template #left>

1. Reusing data
2. What is DataSHIELD?
3. DataSHIELD demo
4. Sharing your data
5. Discussion

</template>

<template #right>

<img src="./public/contents-notebook-coffee.jpg" class="bleed-right" />

</template>

---
layout: content
heading: FAIR data
subheading: "Recap: the research cycle"
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
  <li><span class="chips"><span class="chip f">F</span></span>Catalogue</li>
  <li><span class="chips"><span class="chip i">I</span><span class="chip r">R</span></span>Exposome tools</li>
  <li><span class="chips"><span class="chip a">A</span><span class="chip r">R</span></span>DataSHIELD</li>
</ul>
</div>

---
layout: section
---

# Reusing data

---
src: ../../library/combining-data/options.md
section: Reusing data
---

---
layout: section
---

# What is DataSHIELD?

---
layout: content
heading: What is it
subheading: 
section: 'What is DataSHIELD?'
---

- Analysis code — not raw data — is sent to where each dataset is stored
- Each site runs the computation **locally, on its own data**
- Only <strong v-mark="{ at: 1, color: '#E6B96A', type: 'highlight' }">non-disclosive, aggregate results</strong> (summary statistics or model updates) are returned
- Data never leaves its original location — governance, access control and ownership stay with the data holder

---
layout: content
heading: How it works
subheading: 
section: 'What is DataSHIELD?'
---

<DatashieldArchitecture />

---
src: ../../library/datashield/analysis-options.md
section: 'What is DataSHIELD?'
---

---
layout: section
---

# DataSHIELD demo

---
layout: section
---

# Sharing your data

---
layout: chart-full
heading: European DataSHIELD nodes
section: Sharing your data
---

<div style="position: relative; width: 100%; height: 100%;">
  <img src="./public/ihen_nodes_map.png" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: contain; object-position: left;" />
  <div style="position: absolute; left: 48%; right: 2rem; top: 1rem;">
    <ul style="padding-left: 1.5rem; margin: 0;">
      <li style="font-size: 18px; margin-bottom: 0.5rem; line-height: 1.5;">31 DataSHIELD nodes from LifeCycle, ATHLETE and LongITools cohorts.</li>
      <li style="font-size: 18px; margin-bottom: 0.5rem; line-height: 1.5;">This gives possibilities to connect analyses to additional data sources.</li>
    </ul>
  </div>
</div>

---
layout: content
heading: Setting up DataSHIELD
subheading: Why share your data with DataSHIELD?
section: Sharing your data
---

- A secure way to share your data with other researchers
- Opens opportunities for your own analyses by joining the network built through LifeCycle and ATHLETE

---
layout: content-two-cols
heading: Setting up DataSHIELD
subheading: Two options
section: Sharing your data
---

<template #left>

**Option 1: Set it up yourself**

- Server or virtual machine: 8–32 GB memory, 100 GB disk, 4–8 CPU cores
- Administration rights, Java 21 and Docker
- A domain name and SSL certificate
- Tutorial: [escri11.github.io/datashield-workshop-2025](https://escri11.github.io/datashield-workshop-2025/)

</template>

<template #right>

**Option 2: We set it up for you**

- The MOLGENIS team at UMCG can set up and maintain a server
- Fully private: only you have access to the data
- Contact [support@molgenis.org](mailto:support@molgenis.org)

<p style="font-size: 14px; color: #9AA0A6; margin-top: 2rem;">More: <a href="https://wiki.datashield.org/en/home">wiki.datashield.org</a> · <a href="https://datashield.org/">datashield.org</a></p>

</template>

---
layout: section
---

# Discussion

---
layout: content
heading: Discussion
subheading: 
section: Discussion
---

<v-clicks>

- Federated analysis gives an alternative to data transfer and sharing scripts
- Many exposome cohorts are already part of a large EU federated network
- UMCG can provide training and technical support
- We can also help develop new functionality for specific projects if required

</v-clicks>

---
layout: content
heading: Questions?
subheading: ""
section: Discussion
---

---
layout: content
heading: Further Information
subheading: ""
section: Discussion
---

<p style="margin-top: 2rem; font-size: 20px;">For questions and support contact: <strong>support@molgenis.org</strong></p>

<div style="margin-top: 1.5rem; font-size: 18px; line-height: 1.8;">

**Useful links:**
- DataSHIELD wiki: https://wiki.datashield.org/
- DataSHIELD website: https://datashield.org/
- Molgenis suite: https://molgenis.org/

</div>
