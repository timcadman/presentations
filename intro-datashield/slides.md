---
theme: ../theme
title: Introduction to DataSHIELD
info: Bringing the analysis to the data
author: Tim Cadman
aspectRatio: '16/9'
---

# DataSHIELD, Armadillo and Opal

DataSHIELD deployment options

<div class="author-info">
  <p><strong>Tim Cadman</strong></p>
  <p>Senior Data Scientist</p>
</div>

<div class="title-logos">
  <img src="/molgenis-logo.png" class="logo-molgenis" />
  <img src="/umcg-logo.png" class="logo-umcg" />
</div>

---
layout: content
heading: DataSHIELD
subheading: What is DataSHIELD?
---

- Mature R-based federated analysis platform
- **USP**: running interactive statistical analyses
- **Ideal use case**: Epidemiology and Population health (generalised linear models, 1 and 2-stage meta-analysis)
- **Less ideal for**: AI, machine learning

---
layout: content
heading: Example Use Case
subheading: Air pollution and child health
---

<div style="display: flex; gap: 2rem; align-items: flex-start;">
  <div style="flex: 1;">
    <img src="/example-ds-article-air-pollution.png" style="width: 100%;" />
    <p style="margin-top: 2rem;">Is increased exposure to air pollution associated with higher childhood BMI?</p>
  </div>
  <div style="flex: 1; display: flex; align-items: flex-start; justify-content: center;">
    <img src="/example-ds-article-air-pollution-forest-plot.png" style="width: 80%;" />
  </div>
</div>

---
layout: content
heading: Architecture
subheading: How DataSHIELD works
---

<DatashieldArchitectureSimple />

---
layout: content-img-left
heading: Combining data
subheading: "Option 1: Data transfer"
image: /slide2_img3.jpg
---

- **Strategy:** Transfer to one location
- **Pros:** One researcher conducts all analyses
- **Cons:**
  - Ethico-legal restrictions
  - Data owners lose control of data
  - Storage demands (e.g. omics)

---
layout: section
---

# DataSHIELD
An introduction

---
layout: content
heading: DataSHIELD
subheading: What is it?
---

- R-based federated platform
- Facilitates connection to multiple data sources
- Data controllers host data and control access rights

---
layout: content
heading: Thank you!
subheading: ""
---

---
layout: section
---

# Background
Combining data sources


**Questions?** support@molgenis.org

**Useful links:**
- DataSHIELD wiki: https://wiki.datashield.org/
- DataSHIELD website: https://datashield.org/
- Molgenis suite: https://molgenis.org/
