---
layout: content
heading: DataSHIELD
subheading: Key ideas
clicks: 3
---

<FocusCards :items="[
  { title: 'Remote analysis', color: 'var(--c-blue)', body: ['One model across data held at several sites'] },
  { title: 'Code travels, not data', color: 'var(--c-teal)', body: ['Code is sent to the data; each site computes <strong>locally</strong>'] },
  { title: 'Only aggregates return', color: 'var(--c-gold-dark)', body: ['Means, SDs, coefficients — <strong>never individual-level data</strong>'] },
  { title: 'Data never moves', color: 'var(--c-purple)', body: ['Governance and access stay with the data holder'] },
]" />
