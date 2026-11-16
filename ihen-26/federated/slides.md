---
theme: ../../theme
title: "IHEN tools: Federated analysis with DataSHIELD"
author: Juan Carlos Rivillas, Tim Cadman & Hüseyin Küçükali
aspectRatio: '16/9'
publish: true
themeConfig:
  sections: [Reusing data, DataSHIELD, Demonstration, Setting up DataSHIELD, Discussion]
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
layout: contents
image: ./public/contents-notebook-coffee.jpg
---

1. **Reusing data**
2. **What is DataSHIELD?**
3. **DataSHIELD demo**
4. **Setting up DataSHIELD**
5. **Discussion**

---
layout: content
heading: FAIR data
subheading: "Recap: the research cycle"
clicks: 1
---

<div class="fair-wrap">
<FairCycle :focus="$clicks >= 1 ? 4 : 0" />
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

# DataSHIELD

---
src: ../../library/datashield/introducing-datashield.md
section: 'DataSHIELD'
---

---
src: ../../library/datashield/what-is-datashield.md
section: 'DataSHIELD'
---

---
layout: figure-cite
heading: How it works
section: 'DataSHIELD'
sideWidth: '36'
---

<template #side>

<ul class="fq-steps">
<li v-click="1">Connect to the servers</li>
<li v-click="2">Send analysis commands</li>
<li v-click="3">Receive aggregate results</li>
</ul>

<div v-click="3" class="fq-exwas">
<ExwasPlot />
</div>

</template>

<template #default>

<FederatedQuery />

</template>

---
src: ../../library/datashield/group-exercise.md
section: 'DataSHIELD'
---

---
src: ../../library/datashield/pooling-means.md
section: 'DataSHIELD'
---

---
layout: content
heading: Privacy-preserving statistics
subheading: 
section: 'DataSHIELD'
---

<table>
<thead>
<tr><th>Result</th><th>Condition</th></tr>
</thead>
<tbody>
<tr v-click><td>Mean, SD, quantiles</td><td>Group has at least N participants</td></tr>
<tr v-click><td>Counts and tables</td><td>Minimun cell size to display</td></tr>
<tr v-click><td>Model coefficients and SEs</td><td>Model not saturated; no cell too small</td></tr>
<tr v-click><td>Correlations, covariances</td><td>Minimum N, and not a near-perfect fit</td></tr>
<tr v-click><td>Plots (histograms, heatmaps)</td><td>Binned or noise-added</td></tr>
</tbody>
</table>

---
src: ../../library/datashield/analysis-options.md
section: 'DataSHIELD'
---

---
layout: content
heading: Current DataSHIELD network
subheading: 
section: 'DataSHIELD'
clicks: 3
---

<NodeMap :planned="false" />

---
layout: content
heading: Exposome research using DataSHIELD
subheading: A few examples
section: 'DataSHIELD'
---

<ExamplePapers />


---
layout: section
---

# Demonstration

---
layout: section
---

# Setting up DataSHIELD

---
layout: content
heading: Setting up DataSHIELD
subheading: As a user
section: Setting up DataSHIELD
---

<v-clicks>

- Arrange data access agreements with providers
- Install R packages
- Connect and analyse with RStudio

</v-clicks>

---
layout: content
heading: Setting up DataSHIELD
subheading: As a data owner
section: Setting up DataSHIELD
---

<v-clicks>

- A secure way to share your data with other researchers
- Opens opportunities for your own analyses by joining the network built through LifeCycle and ATHLETE

</v-clicks>

---
src: ../../library/infrastructure/what-is-armadillo.md
section: Setting up DataSHIELD
---

---
src: ../../library/infrastructure/setup-options.md
section: Setting up DataSHIELD
---

---
src: ../../library/infrastructure/armadillo-setup-short.md
section: Setting up DataSHIELD
---

---
src: ../../library/infrastructure/hosted-by-us.md
section: Setting up DataSHIELD
---

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
