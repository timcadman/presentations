---
theme: ../theme-uncan
title: What is federated analysis?
info: Placeholder deck
author: Tim Cadman
aspectRatio: '16/9'
publish: false
layout: content
heading: Federated analysis
subheading: What is it
clicks: 4
---

<FocusCards :columns="3" :items="[
  { title: 'Remote analysis', color: 'var(--c-blue)', body: ['One model across data held at several sites'] },
  { title: 'Code travels, not data', color: 'var(--c-teal)', body: ['Code is sent to the data; each site computes <strong>locally</strong>'] },
  { title: 'Only aggregates return', color: 'var(--c-gold-dark)', body: ['Means, SDs, coefficients — <strong>never individual-level data</strong>'] },
  { title: 'Data never moves', color: 'var(--c-purple)', body: ['Governance and access stay with the data holder'] },
  { title: 'The software', color: 'var(--c-blue-dark)', body: ['<strong>Armadillo</strong> manages data access; <strong>DataSHIELD</strong> runs the analysis'] },
]" />

---
layout: content
heading: Federated analysis
subheading: How it works
---

<DatashieldArchitecture server="armadillo" />
