---
theme: ../../theme
title: IHEN exposome tools introduction
info: UMCG's role, existing infrastructure and what's next
author: Juan Carlos Rivillas, Tim Cadman & Hüseyin Küçükali
date: 2026-11-16
aspectRatio: '16/9'
publish: true
themeConfig:
  sections: [Combining data, FAIR data, Exposome tools]
transition: slide-left
mdc: true
---

# IHEN exposome tools
Introduction

<div class="author-info">
  <p><strong>Tim Cadman, Juan Carlos Rivillas & Hüseyin Küçükali</strong></p>
</div>

<div class="title-logos">
  <img src="./public/molgenis-logo.png" class="logo-molgenis" />
  <img src="./public/umcg-logo.png" class="logo-umcg" />
  <img src="./public/uu-logo.webp" class="logo-uu" />
  <img src="./public/isglobal-logo.png" class="logo-isglobal" />
</div>

---
layout: contents
image: ./public/contents-notebook-coffee.jpg
---

1. **Combining data**
   - Why combine data?
   - Examples
2. **FAIR data cycle**
3. **Exposome tools**
   - Global Exposome Cohorts Catalogue
   - Exposome Maps
   - Federated analysis with DataSHIELD

---
layout: section
---

# Introduction

---
src: ../../library/combining-data/why.md
section: 'Combining data'
---

---
layout: content
heading: Combining data
subheading: Example research question
section: 'Combining data'
transition: slide-up
---

<ResearchQuestion
  question="Does exposure to air pollution in pregnancy predict maternal perinatal depression?"
  reference="Cadman et al. (2024) Environ Int 185:108453" />

---
layout: figure-cite
heading: Example 1
subheading: Increased exposure contrast
section: 'Combining data'
transition: slide-up
citation: 'Cadman et al. (2024) Environ Int 185:108453'
---

<template #side>

- A single location may only cover part of the range of exposure values

</template>

<template #default>

<ExposureContrast />

</template>

---
layout: figure-cite
heading: Example 2
subheading: Increased power
section: 'Combining data'
transition: slide-up
citation: 'Cadman et al. (2024) Environ Int 185:108453'
---

<template #side>

- Many outcomes are rare
- Single cohorts lack the power to detect associations

</template>

<template #default>

<PowerCurve />

</template>

---
layout: content
heading: Combining data
subheading: Example research question
section: 'Combining data'
transition: slide-up
---

<ResearchQuestion
  question="How does lung function change across the life course, and when does decline begin?"
  reference="Garcia-Aymerich et al. (2025) Lancet Respir Med 13:611–22" />

---
layout: figure-cite
heading: Example 3
subheading: Lifecourse modelling
citation: 'Garcia-Aymerich et al. (2025) Lancet Respir Med 13:611–22'
transition: none
section: 'Combining data'
---

<template #side>

- One cohort covers a limited age range

</template>

<template #default>

<CohortCoverage only="ALSPAC" />

</template>

---
layout: figure-cite
heading: Example 3
subheading: Lifecourse modelling
citation: 'Garcia-Aymerich et al. (2025) Lancet Respir Med 13:611–22'
transition: none
section: 'Combining data'
---

<template #side>

- One cohort covers a limited age range

</template>

<template #default>

<FevTrajectory only="ALSPAC" />

</template>

---
layout: figure-cite
heading: Example 3
subheading: Lifecourse modelling
citation: 'Garcia-Aymerich et al. (2025) Lancet Respir Med 13:611–22'
transition: none
section: 'Combining data'
---

<template #side>

- One cohort covers a limited age range
- With multiple cohorts we can model across the lifespan

</template>

<template #default>

<CohortCoverage />

</template>

---
layout: figure-cite
heading: Example 3
subheading: Lifecourse modelling
citation: 'Garcia-Aymerich et al. (2025) Lancet Respir Med 13:611–22'
transition: slide-up
section: 'Combining data'
---

<template #side>

- One cohort covers a limited age range
- With multiple cohorts we can model across the lifespan

</template>

<template #default>

<FevTrajectory />

</template>

---
layout: figure-cite
heading: Example 4
subheading: Different confounding structures
section: 'Combining data'
citation: 'Robinson et al. (2018) Environ Health Perspect 126(7):077005'
---

<template #legend>

<div style="border: 1px solid #b4b4b4; border-radius: 4px; padding: 0.6rem 0.8rem;">
<div style="font-weight: 600; margin-bottom: 0.6rem;">High-SEP areas have</div>
<div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.4rem;">
<svg width="16" height="16" viewBox="0 0 14 14"><polygon points="1,2 13,2 7,12" fill="#119DA1" stroke="#ffffff" stroke-width="0.8" /></svg>
Lower NO₂
</div>
<div style="display: flex; align-items: center; gap: 0.5rem;">
<svg width="16" height="16" viewBox="0 0 14 14"><polygon points="7,2 13,12 1,12" fill="#DA594A" stroke="#ffffff" stroke-width="0.8" /></svg>
Higher NO₂
</div>
</div>

</template>

<template #side>
<v-clicks>

- With one cohort, separating a true effect and confounding is difficult
- A **consistent** association across different confounding structures is hard to explain
- Combining countries **strengthens causal inference**

</v-clicks>
</template>

<template #default>

<SepNo2Map />

</template>

---
layout: section
---

# FAIR data

---
src: ../../library/datashield/fair-cycle.md
section: 'FAIR data'
---

---
layout: content
heading: FAIR data
subheading: Exposome tools
section: 'Exposome tools'
---

<ul class="fair-links">
  <li v-click><span class="chips"><span class="chip f">F</span><span class="chip a">A</span><span class="chip r">R</span></span>Global Exposome Cohorts Catalogue</li>
  <li v-click><span class="chips"><span class="chip i">I</span><span class="chip r">R</span></span>Exposome maps & tools</li>
  <li v-click><span class="chips"><span class="chip a">A</span><span class="chip r">R</span></span>Federated exposome analysis with DataSHIELD</li>
</ul>

