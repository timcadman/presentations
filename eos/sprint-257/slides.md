---
theme: ../../theme
title: Team Armadillo — Sprint 257
info: End-of-sprint review
author: Tim Cadman
date: 2026-06-18
aspectRatio: '16/9'
publish: false
---

# Team Armadillo

EOS 257

<div class="title-logos">
  <img src="./public/molgenis-logo.png" class="logo-molgenis" />
</div>

---
layout: content
heading: End of Sprint 257
subheading: Highlights
---

1. **Grants submitted**
   - Treatment resistant depression
   - 2× AI
2. **Security fix** _(demo)_
3. **Performance improvements** _(demo)_
4. **Update from UI** _(ongoing)_

---
layout: section
---

# Demo 1
Login backoff

---
layout: content
heading: "Demo 1: Login backoff"
subheading: The problem
---

- Penetration test: failed logins are **unlimited and unpenalised**
- Leaves the login open to **brute-force** attacks

---
layout: content
heading: "Demo 1: Login backoff"
subheading: The solution
---

- **5 free attempts**
- After that, an **exponential backoff** on each further failure
- Capped at a **30-minute** maximum delay

---
layout: section
---

# Demo 2
DataSHIELD performance improvements

---
layout: content
heading: "Demo 2: DataSHIELD performance"
subheading: The problem
---

- Most datashield functions make **several separate calls** to the server for a single operation
  - Checking serverside object exists
  - Checking object is correct class
  - Running function
  - Checking function ran correctly

---
layout: content
heading: "Demo 2: DataSHIELD performance"
subheading: "The solution: one round trip"
---

<RoundTrips />

---
layout: content
heading: Another problem ...
subheading: There are >100 DataSHIELD functions in core package
---

- Niels' idea: use Claude to do the refactor...

---
layout: content
heading: Workflow
---

<ProcessCards :clicks="$clicks" :groups="[
  { steps: [
    { title: 'Review code', desc: 'Manual review of all the code' },
    { title: 'Draft plan', desc: 'Sketch the refactor plan' },
    { title: 'Review', desc: 'DataSHIELD Statistics theme' },
    { title: 'Write plan', desc: 'Write the refactor plan with Claude' },
  ] },
  { loop: true, label: 'iterate', steps: [
    { title: 'Apply', desc: 'Apply plan to first batch' },
    { title: 'Review problems', desc: 'Manual review of problems' },
    { title: 'Revise plan', desc: 'Refine the plan' },
  ] },
  { steps: [
    { title: 'Run pipeline', desc: 'Apply to batch 1' },
    { title: 'Code review (me)' },
    { title: 'Code review (Stuart)' },
    { title: 'Performance evaluation' },
  ] },
]" />

<span v-for="i in 10" :key="i" v-click style="display:none" />

---
layout: content
heading: Results
subheading: Faster across the board
---

- **91 of 111** function-pairs refactored
- **83 (91%)** improved in performance tests
- Median improvement **+109%** (mean **+142%**)
- Biggest wins where redundant round trips were most common:
  - `ds.reShape` **+769%** · `ds.recodeValues` **+475%** · `ds.asCharacter` **+401%**
  - `ds.corTest` **+386%** · `ds.dataFrameSort` **+344%**
