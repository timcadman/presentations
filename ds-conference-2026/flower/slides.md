---
theme: ../../theme
title: Flower in Armadillo
info: Federated learning with Flower on MOLGENIS Armadillo
author: Tim Cadman and Armadillo Team
date: 2026-09-28
aspectRatio: '16/9'
publish: false
themeConfig:
  sections: [Background, Implementation, Demonstration, Discussion]
---

# Extending MOLGENIS Armadillo 
A unified server for DataSHIELD and Flower

<div class="author-info">
  <p><strong>Tim Cadman</strong> and <strong>Armadillo Team</strong></p>
</div>

<div class="title-logos">
  <img src="./public/molgenis-logo.png" class="logo-molgenis" />
  <img src="./public/umcg-logo.png" class="logo-umcg" />
</div>

---
layout: section
---

# Background

---
layout: content-img-right
heading: What is Armadillo?
image: ./public/armadillo-logo.png
imageScale: '75'
imageWidth: '22'
imageAlign: 'flex-start'
---

- **Open-source server** to securely enable DataSHIELD analysis
- **Lightweight**, easy to install and operate
- Data storage, access management and Docker container management, with a **user interface** for data managers

---
layout: content-img-right
heading: What is Flower?
---

- Federated machine learning platform
- Similar hub-and-spoke architecture <br> to DataSHIELD
- Implemented in python
- Open-source with paid layer with deployment features

<img src="/flower-architecture.png" style="position: fixed; top: 3.5rem; right: 4rem; height: 26rem;" />

<div style="position: fixed; top: 29.6rem; right: 4rem; font-size: 11px; color: #9AA0A6;">Diagram: flower.ai</div>

---
layout: content
heading: Why Flower in Armadillo?
section: Background
---

- DataSHIELD is industry-standard for epidemiology but lacks AI & machine-learning
- Many research consortia need both
- We want to minimise technical and maintenance burden for data owners
- Datashield + Flower covers 99.9% of public health federated use cases
- 'Interoperability' between platforms

---
layout: content
heading: Our vision
pptxClicks: true
section: Background
clicks: 2
---

<style>
.vision { position: relative; width: 820px; height: 270px; margin: 0 auto; }
.vision .box { position: absolute; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; padding: 0 16px; border: 2px solid var(--c); border-radius: 10px; background: color-mix(in srgb, var(--c) 9%, white); transition: opacity 0.5s ease, left 0.6s ease; }
.vision .box b { font-size: 16px; color: var(--title, var(--c)); }
.vision .box span { font-size: 12px; }
.vision .line { position: absolute; background: #9AA0A6; transition: opacity 0.5s ease, left 0.6s ease, width 0.6s ease; }
.vision .dash { position: absolute; border-top: 2px dashed var(--c, #1E3A5F); transition: opacity 0.5s ease; }
.vision .dash-down { position: absolute; border-left: 2px dashed var(--c); transition: opacity 0.5s ease; }
.vision .off { opacity: 0; }
.vision .armadillo { left: 260px; top: 64px; width: 240px; height: 72px; flex-direction: row; align-items: center; justify-content: flex-start; gap: 12px; }
.vision .armadillo img { height: 40px; }
.vision .box .logo { height: 30px; width: auto; align-self: flex-start; margin: 0 0 6px 0; }
.vision .node { top: 186px; width: 240px; height: 84px; }
.vision .bar { left: 190px; top: 160px; width: 380px; height: 2px; }
.vision .drop { top: 160px; width: 2px; height: 26px; }
.vision .drop-ds { left: 190px; }
.vision .drop-fl { left: 568px; }
.vision .ds { left: 70px; }
.vision .fl { left: 450px; }
.vision .v6 { left: 520px; }
.vision.three .bar { left: 120px; width: 260px; }
.vision.three .drop-ds { left: 120px; }
.vision.three .drop-fl { left: 379px; }
.vision.three .ds { left: 0; }
.vision.three .fl { left: 260px; }
</style>

<div class="vision" :class="{ three: $clicks >= 2 }">
  <div class="box armadillo" style="--c: var(--slidev-theme-primary);">
    <img src="/armadillo-logo-transparent.png" />
    <div><b>Armadillo</b><br><span>Data, access and containers</span></div>
  </div>
  <div class="line" :class="{ off: $clicks < 1 }" style="left: 379px; top: 136px; width: 2px; height: 26px;"></div>
  <div class="line bar" :class="{ off: $clicks < 1 }"></div>
  <div class="line drop drop-ds" :class="{ off: $clicks < 1 }"></div>
  <div class="line drop drop-fl" :class="{ off: $clicks < 1 }"></div>
  <div class="box node ds" :class="{ off: $clicks < 1 }" style="--c: #E35000;">
    <img class="logo" src="/datashield-logo.png" /><span>Statistics and epidemiology</span>
  </div>
  <div class="box node fl" :class="{ off: $clicks < 1 }" style="--c: #FDAE00; --title: #B9852A;">
    <img class="logo" src="/flower-logo.svg" style="width: 129px;" /><span>Machine learning and AI</span>
  </div>
  <div class="dash" :class="{ off: $clicks < 2 }" style="--c: #9AA0A6; left: 381px; top: 160px; width: 260px;"></div>
  <div class="dash-down" :class="{ off: $clicks < 2 }" style="--c: #9AA0A6; left: 639px; top: 160px; height: 26px;"></div>
  <div class="box node v6" :class="{ off: $clicks < 2 }" style="--c: #0097A7; border-style: dashed;">
    <img class="logo" src="/vantage6-logo.png" /><span>Federated learning</span>
  </div>
  <div class="line" style="left: 379px; top: 44px; width: 2px; height: 20px; background: #1E3A5F;"></div>
  <div class="box" style="--c: #1E3A5F; left: 285px; top: 0; width: 190px; height: 44px; align-items: center; background: white;">
    <b>OIDC authentication</b>
  </div>
</div>

<span v-for="i in 2" :key="i" v-click style="display:none" />

---
layout: content-two-cols
heading: ds-Flower vs Flower in Armadillo
pptxClicks: true
section: Background
leftWidth: '66'
clicks: 1
---

<style>
.fp-heading { position: relative; height: 2.2rem; margin-bottom: 0.6rem; }
.fp-heading span { position: absolute; left: 0; top: 0; font-family: var(--font-subtitle); font-size: 25px; font-weight: 600; color: var(--slidev-theme-heading); opacity: 0; transition: opacity 0.5s ease; }
.fp-heading span.now { opacity: 1; }
.fp-notes-box { margin-top: 2.8rem; height: 230px; display: flex; align-items: flex-start; }
.fp-notes { margin: 0; }
.fp-notes li { font-size: 18px; line-height: 1.4; margin-bottom: 0.9rem; opacity: 0; transition: opacity 0.5s ease; }
.fp-notes li.now { opacity: 1; }
</style>

<template #left>

<div class="fp-heading">
  <span :class="{ now: $clicks < 1 }">dsFlower</span>
  <span :class="{ now: $clicks >= 1 }">Flower in Armadillo</span>
</div>

<FlowerPlacement :standalone-at="1" :scale="1.15" />

</template>

<template #right>

<div class="fp-notes-box">
<ul class="fp-notes">
  <li v-show="$clicks < 1" class="now">Flower runs inside Rock</li>
  <li v-show="$clicks < 1" class="now">The analyst uses Flower within a DataSHIELD session</li>
  <li v-show="$clicks >= 1" class="now">DataSHIELD and Flower run as separate docker containers</li>
  <li v-show="$clicks >= 1" class="now">Flower can be used as a stand-alone framework</li>
</ul>
</div>

<span v-click style="display:none" />

</template>


<!--
- As you've seen, David & Juan-Ramon have implemented Flower within DataSHIELD.
- Our approach is to implement Flower as stand-alone, alongside DataSHIELD
-->

---
layout: section
---

# Implementation

---
layout: content
heading: Enhancements from open-source Flower
section: Implementation
clicks: 6
---

<FlowerGaps />

---
layout: section
---

# Demonstration

---
layout: content-img-right
heading: Research question
imageWidth: '40'
clicks: 3
---

<style>
.rq-bands { position: fixed; top: 14.1rem; right: 6.25rem; width: 287px; height: 253px; }
.rq-band { height: 84.2px; overflow: hidden; border-radius: 4px; transform-origin: top left; transition: transform 0.9s ease; }
.rq-band img { display: block; width: 287px; max-width: none; }
.rq-hub { position: absolute; inset: 0; opacity: 0; transition: opacity 0.5s ease; }
.rq-bands.rq-split .rq-hub { opacity: 1; transition-delay: 0.7s; }
.rq-hub .superlink { position: absolute; left: 88.5px; top: 0; width: 110px; height: 34px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid #FDAE00; border-radius: 8px; background: #FFEFCC; font-family: var(--font-subtitle); font-size: 14px; font-weight: 600; color: #B9852A; }
.rq-hub .line { position: absolute; background: #9AA0A6; }
.rq-hub .site { position: absolute; top: 94px; height: 30px; width: auto; }
</style>

<div class="rq-bands" :class="{ 'rq-split': $clicks >= 3 }">
  <div v-for="i in 3" :key="i" class="rq-band" :style="$clicks >= 3 ? { transform: `translate(${99 * (i - 1)}px, ${132 - 84.2 * (i - 1)}px) scale(0.31)` } : {}"><img src="/cifar10-dogs.png" :style="{ marginTop: `${-84.2 * (i - 1)}px` }" /></div>
  <div class="rq-hub">
    <div class="superlink">SuperLink</div>
    <div class="line" style="left: 142.5px; top: 34px; width: 2px; height: 28px;"></div>
    <div class="line" style="left: 43.5px; top: 60px; width: 200px; height: 2px;"></div>
    <div v-for="i in 3" :key="i" class="line" :style="{ left: `${43.5 + 99 * (i - 1)}px`, top: '60px', width: '2px', height: '30px' }"></div>
    <img v-for="i in 3" :key="i" class="site" src="/armadillo-logo.png" :style="{ left: `${31 + 99 * (i - 1)}px` }" />
  </div>
</div>

<v-clicks>

- **Aim:** Can we train a model to recognise pets in photos distributed across three Armadillo nodes?
- **Model:** a small convolutional network in PyTorch, based on Flower quick-start example
- **Data:** CIFAR-10, small colour photos in 10 classes <br> of animals

</v-clicks>


---
layout: chart-full
heading: '1. Publish app to Flower Hub'
section: Demonstration
---

<img src="/flower-hub-app.png" style="height: 23rem; margin: 0; border: 1px solid #9AA0A6; border-radius: 6px;" />

<!-- <div style="position: relative; height: 23rem;"><VideoPlayer src="/demo-3-publish.mov" /></div> -->

---
layout: chart-full
heading: '2. Setup Superlink'
section: Demonstration
---

<style>
ul { padding-left: 1.5rem; }
li { font-size: 18px; line-height: 1.5; margin-bottom: 0.5rem; }
</style>

<div style="display: flex; gap: 2rem; align-items: flex-start;">
<div style="flex: 2 1 0; min-width: 0;">

- We have installed and hosted a Superlink (central aggregator)
- TLS certificates and authentication setup between Superlink and Supernodes with the standard Flower approach

</div>
<div style="flex: 1 1 0; min-width: 0;">
<div style="width: 260px; height: 201px; overflow: hidden; border-radius: 6px;"><img src="/flower-architecture.png" style="display: block; width: 559.6px; max-width: none; margin: -171.9px 0 0 -9.4px;" /></div>
<div style="font-size: 11px; color: #9AA0A6; margin-top: 0.3rem;">Diagram: flower.ai</div>
</div>
</div>

---
layout: chart-full
heading: '3. Setup Flower Docker containers (per node)'
section: Demonstration
---

<div style="position: relative; height: 23rem; aspect-ratio: 2862 / 1596;"><VideoPlayer hide-button src="/demo-0-containers.mov" /></div>

---
layout: chart-full
heading: '4. Create project and upload data (per node)'
section: Demonstration
---

<div style="position: relative; height: 23rem; aspect-ratio: 2864 / 1598;"><VideoPlayer hide-button src="/demo-1-project.mov" /></div>

---
layout: chart-full
heading: '5. Grant a researcher access (per node)'
section: Demonstration
---

<div style="position: relative; height: 23rem; aspect-ratio: 2864 / 1598;"><VideoPlayer hide-button src="/demo-2-access.mov" /></div>

---
layout: chart-full
heading: '6. Review app and whitelist on Armadillo'
pptxVideo: ./public/rec-6-review.mov
section: Demonstration
clicks: 7
---

<style>
.review-panes { display: flex; gap: 1rem; height: 23rem; }
.review-panes > * { flex: 1 1 0; min-width: 0; }
.review-code { display: block; max-width: 100%; max-height: 100%; border-radius: 8px; opacity: 0; animation: review-code-in 0.3s ease forwards; }
@keyframes review-code-in { to { opacity: 1; } }
.review-ui { position: relative; width: 100%; aspect-ratio: 2640 / 944; opacity: 0; animation: review-code-in 0.3s ease forwards; }
.review-ui .full { display: block; width: 100%; border: 1px solid #9AA0A6; border-radius: 6px; }
.review-ui .zoom { position: absolute; left: 57.99%; top: 50.00%; width: 40.38%; border-radius: 6px; box-shadow: 0 6px 18px rgba(0, 0, 0, 0.25); animation: review-zoom 0.9s ease 1.2s forwards; }
@keyframes review-zoom { to { left: 0; top: 112%; width: 100%; } }
</style>

<div class="review-panes">
<TerminalSession height="23rem">
<div v-show="$clicks < 4">
<pre class="cmd" :class="{ 'type-go': $clicks >= 1 }">$ <span class="typed" style="--t: 0.100s">a</span><span class="typed" style="--t: 0.125s">r</span><span class="typed" style="--t: 0.150s">m</span><span class="typed" style="--t: 0.175s">a</span><span class="typed" style="--t: 0.200s">d</span><span class="typed" style="--t: 0.225s">i</span><span class="typed" style="--t: 0.250s">l</span><span class="typed" style="--t: 0.275s">l</span><span class="typed" style="--t: 0.300s">o</span><span class="typed" style="--t: 0.325s">-</span><span class="typed" style="--t: 0.350s">f</span><span class="typed" style="--t: 0.375s">l</span><span class="typed" style="--t: 0.400s">w</span><span class="typed" style="--t: 0.425s">r</span><span class="typed" style="--t: 0.450s">-</span><span class="typed" style="--t: 0.475s">r</span><span class="typed" style="--t: 0.500s">e</span><span class="typed" style="--t: 0.525s">v</span><span class="typed" style="--t: 0.550s">i</span><span class="typed" style="--t: 0.575s">e</span><span class="typed" style="--t: 0.600s">w</span><span class="typed" style="--t: 0.625s">-</span><span class="typed" style="--t: 0.650s">a</span><span class="typed" style="--t: 0.675s">p</span><span class="typed" style="--t: 0.700s">p</span><span class="typed" style="--t: 0.725s"> </span><span class="typed" style="--t: 0.750s">@</span><span class="typed" style="--t: 0.775s">t</span><span class="typed" style="--t: 0.800s">i</span><span class="typed" style="--t: 0.825s">m</span><span class="typed" style="--t: 0.850s">m</span><span class="typed" style="--t: 0.875s">y</span><span class="typed" style="--t: 0.900s">j</span><span class="typed" style="--t: 0.925s">c</span><span class="typed" style="--t: 0.950s">/</span><span class="typed" style="--t: 0.975s">q</span><span class="typed" style="--t: 1.000s">u</span><span class="typed" style="--t: 1.025s">i</span><span class="typed" style="--t: 1.050s">c</span><span class="typed" style="--t: 1.075s">k</span><span class="typed" style="--t: 1.100s">s</span><span class="typed" style="--t: 1.125s">t</span><span class="typed" style="--t: 1.150s">a</span><span class="typed" style="--t: 1.175s">r</span><span class="typed" style="--t: 1.200s">t</span><span class="typed" style="--t: 1.225s">-</span><span class="typed" style="--t: 1.250s">p</span><span class="typed" style="--t: 1.275s">y</span><span class="typed" style="--t: 1.300s">t</span><span class="typed" style="--t: 1.325s">o</span><span class="typed" style="--t: 1.350s">r</span><span class="typed" style="--t: 1.375s">c</span><span class="typed" style="--t: 1.400s">h</span><span class="typed" style="--t: 1.425s">-</span><span class="typed" style="--t: 1.450s">a</span><span class="typed" style="--t: 1.475s">r</span><span class="typed" style="--t: 1.500s">m</span><span class="typed" style="--t: 1.525s">a</span><span class="typed" style="--t: 1.550s">d</span><span class="typed" style="--t: 1.575s">i</span><span class="typed" style="--t: 1.600s">l</span><span class="typed" style="--t: 1.625s">l</span><span class="typed" style="--t: 1.650s">o</span></pre>
<div class="stage" :class="{ go: $clicks >= 2 }">
<pre class="out" style="--t: 1.20s">Review the app in: /Users/tcadman/.flwr/reviews/apps/timmyjc.quickstart-pytorch-armadillo.1.0.4.c0945432</pre>
<pre class="out" style="--t: 1.32s">- fab_id: timmyjc/quickstart-pytorch-armadillo</pre>
<pre class="out" style="--t: 1.44s">  fab_version: 1.0.4</pre>
<pre class="out" style="--t: 1.56s">  fab_hash: c0945432626f2e7c64fbcc264dadf78f26e3caf318da421f06067ad820ccfa7a</pre>
<pre class="out" style="--t: 1.68s"> </pre>
<pre class="out" style="--t: 1.80s">When you are satisfied, approve exactly this file with:</pre>
<pre class="out" style="--t: 1.92s">  armadillo-flwr-approve-app /Users/tcadman/.flwr/reviews/timmyjc-quickstart-pytorch-armadillo.fab --armadillo &lt;URL&gt; --container &lt;name&gt;</pre>
<pre class="out cmd" style="--t: 2.22s">$</pre>
</div>
</div>
<div v-show="$clicks >= 4">
<pre class="cmd" :class="{ 'type-go': $clicks >= 4 }">$ <span class="typed" style="--t: 0.100s">a</span><span class="typed" style="--t: 0.125s">r</span><span class="typed" style="--t: 0.150s">m</span><span class="typed" style="--t: 0.175s">a</span><span class="typed" style="--t: 0.200s">d</span><span class="typed" style="--t: 0.225s">i</span><span class="typed" style="--t: 0.250s">l</span><span class="typed" style="--t: 0.275s">l</span><span class="typed" style="--t: 0.300s">o</span><span class="typed" style="--t: 0.325s">-</span><span class="typed" style="--t: 0.350s">f</span><span class="typed" style="--t: 0.375s">l</span><span class="typed" style="--t: 0.400s">w</span><span class="typed" style="--t: 0.425s">r</span><span class="typed" style="--t: 0.450s">-</span><span class="typed" style="--t: 0.475s">a</span><span class="typed" style="--t: 0.500s">p</span><span class="typed" style="--t: 0.525s">p</span><span class="typed" style="--t: 0.550s">r</span><span class="typed" style="--t: 0.575s">o</span><span class="typed" style="--t: 0.600s">v</span><span class="typed" style="--t: 0.625s">e</span><span class="typed" style="--t: 0.650s">-</span><span class="typed" style="--t: 0.675s">a</span><span class="typed" style="--t: 0.700s">p</span><span class="typed" style="--t: 0.725s">p</span><span class="typed" style="--t: 0.750s"> </span><span class="typed" style="--t: 0.775s">~</span><span class="typed" style="--t: 0.800s">/</span><span class="typed" style="--t: 0.825s">.</span><span class="typed" style="--t: 0.850s">f</span><span class="typed" style="--t: 0.875s">l</span><span class="typed" style="--t: 0.900s">w</span><span class="typed" style="--t: 0.925s">r</span><span class="typed" style="--t: 0.950s">/</span><span class="typed" style="--t: 0.975s">r</span><span class="typed" style="--t: 1.000s">e</span><span class="typed" style="--t: 1.025s">v</span><span class="typed" style="--t: 1.050s">i</span><span class="typed" style="--t: 1.075s">e</span><span class="typed" style="--t: 1.100s">w</span><span class="typed" style="--t: 1.125s">s</span><span class="typed" style="--t: 1.150s">/</span><span class="typed" style="--t: 1.175s">t</span><span class="typed" style="--t: 1.200s">i</span><span class="typed" style="--t: 1.225s">m</span><span class="typed" style="--t: 1.250s">m</span><span class="typed" style="--t: 1.275s">y</span><span class="typed" style="--t: 1.300s">j</span><span class="typed" style="--t: 1.325s">c</span><span class="typed" style="--t: 1.350s">-</span><span class="typed" style="--t: 1.375s">q</span><span class="typed" style="--t: 1.400s">u</span><span class="typed" style="--t: 1.425s">i</span><span class="typed" style="--t: 1.450s">c</span><span class="typed" style="--t: 1.475s">k</span><span class="typed" style="--t: 1.500s">s</span><span class="typed" style="--t: 1.525s">t</span><span class="typed" style="--t: 1.550s">a</span><span class="typed" style="--t: 1.575s">r</span><span class="typed" style="--t: 1.600s">t</span><span class="typed" style="--t: 1.625s">-</span><span class="typed" style="--t: 1.650s">p</span><span class="typed" style="--t: 1.675s">y</span><span class="typed" style="--t: 1.700s">t</span><span class="typed" style="--t: 1.725s">o</span><span class="typed" style="--t: 1.750s">r</span><span class="typed" style="--t: 1.775s">c</span><span class="typed" style="--t: 1.800s">h</span><span class="typed" style="--t: 1.825s">-</span><span class="typed" style="--t: 1.850s">a</span><span class="typed" style="--t: 1.875s">r</span><span class="typed" style="--t: 1.900s">m</span><span class="typed" style="--t: 1.925s">a</span><span class="typed" style="--t: 1.950s">d</span><span class="typed" style="--t: 1.975s">i</span><span class="typed" style="--t: 2.000s">l</span><span class="typed" style="--t: 2.025s">l</span><span class="typed" style="--t: 2.050s">o</span><span class="typed" style="--t: 2.075s">.</span><span class="typed" style="--t: 2.100s">f</span><span class="typed" style="--t: 2.125s">a</span><span class="typed" style="--t: 2.150s">b</span><span class="typed" style="--t: 2.175s"> </span><span class="typed" style="--t: 2.200s">\</span></pre>
<pre class="cmd" :class="{ 'type-go': $clicks >= 4 }">    <span class="typed" style="--t: 2.225s">-</span><span class="typed" style="--t: 2.250s">-</span><span class="typed" style="--t: 2.275s">a</span><span class="typed" style="--t: 2.300s">r</span><span class="typed" style="--t: 2.325s">m</span><span class="typed" style="--t: 2.350s">a</span><span class="typed" style="--t: 2.375s">d</span><span class="typed" style="--t: 2.400s">i</span><span class="typed" style="--t: 2.425s">l</span><span class="typed" style="--t: 2.450s">l</span><span class="typed" style="--t: 2.475s">o</span><span class="typed" style="--t: 2.500s"> </span><span class="typed" style="--t: 2.525s">h</span><span class="typed" style="--t: 2.550s">t</span><span class="typed" style="--t: 2.575s">t</span><span class="typed" style="--t: 2.600s">p</span><span class="typed" style="--t: 2.625s">:</span><span class="typed" style="--t: 2.650s">/</span><span class="typed" style="--t: 2.675s">/</span><span class="typed" style="--t: 2.700s">l</span><span class="typed" style="--t: 2.725s">o</span><span class="typed" style="--t: 2.750s">c</span><span class="typed" style="--t: 2.775s">a</span><span class="typed" style="--t: 2.800s">l</span><span class="typed" style="--t: 2.825s">h</span><span class="typed" style="--t: 2.850s">o</span><span class="typed" style="--t: 2.875s">s</span><span class="typed" style="--t: 2.900s">t</span><span class="typed" style="--t: 2.925s">:</span><span class="typed" style="--t: 2.950s">8</span><span class="typed" style="--t: 2.975s">0</span><span class="typed" style="--t: 3.000s">9</span><span class="typed" style="--t: 3.025s">0</span><span class="typed" style="--t: 3.050s"> </span><span class="typed" style="--t: 3.075s">-</span><span class="typed" style="--t: 3.100s">-</span><span class="typed" style="--t: 3.125s">c</span><span class="typed" style="--t: 3.150s">o</span><span class="typed" style="--t: 3.175s">n</span><span class="typed" style="--t: 3.200s">t</span><span class="typed" style="--t: 3.225s">a</span><span class="typed" style="--t: 3.250s">i</span><span class="typed" style="--t: 3.275s">n</span><span class="typed" style="--t: 3.300s">e</span><span class="typed" style="--t: 3.325s">r</span><span class="typed" style="--t: 3.350s"> </span><span class="typed" style="--t: 3.375s">s</span><span class="typed" style="--t: 3.400s">u</span><span class="typed" style="--t: 3.425s">p</span><span class="typed" style="--t: 3.450s">e</span><span class="typed" style="--t: 3.475s">r</span><span class="typed" style="--t: 3.500s">e</span><span class="typed" style="--t: 3.525s">x</span><span class="typed" style="--t: 3.550s">e</span><span class="typed" style="--t: 3.575s">c</span><span class="typed" style="--t: 3.600s">-</span><span class="typed" style="--t: 3.625s">d</span><span class="typed" style="--t: 3.650s">e</span><span class="typed" style="--t: 3.675s">m</span><span class="typed" style="--t: 3.700s">o</span><span class="typed" style="--t: 3.725s"> </span><span class="typed" style="--t: 3.750s">-</span><span class="typed" style="--t: 3.775s">-</span><span class="typed" style="--t: 3.800s">u</span><span class="typed" style="--t: 3.825s">s</span><span class="typed" style="--t: 3.850s">e</span><span class="typed" style="--t: 3.875s">r</span><span class="typed" style="--t: 3.900s"> </span><span class="typed" style="--t: 3.925s">a</span><span class="typed" style="--t: 3.950s">d</span><span class="typed" style="--t: 3.975s">m</span><span class="typed" style="--t: 4.000s">i</span><span class="typed" style="--t: 4.025s">n</span></pre>
<div class="stage" :class="{ go: $clicks >= 5 }">
<pre class="out" style="--t: 0.40s">Password for admin at http://localhost:8090:</pre>
<pre class="out" style="--t: 1.90s">- fab_id: timmyjc/quickstart-pytorch-armadillo</pre>
<pre class="out" style="--t: 2.02s">  fab_version: 1.0.4</pre>
<pre class="out" style="--t: 2.14s">  fab_hash: c0945432626f2e7c64fbcc264dadf78f26e3caf318da421f06067ad820ccfa7a</pre>
<pre class="out" style="--t: 2.26s"> </pre>
<pre class="out" style="--t: 2.38s">Adding an app to the whitelist means that approved researchers can run it against your local data.</pre>
<pre class="out" :class="{ 'type-go': $clicks >= 6 }" style="--t: 2.50s">Type APPROVE to add this entry to the whitelist: <span class="typed" style="--t: 0.30s">A</span><span class="typed" style="--t: 0.44s">P</span><span class="typed" style="--t: 0.58s">P</span><span class="typed" style="--t: 0.72s">R</span><span class="typed" style="--t: 0.86s">O</span><span class="typed" style="--t: 1.00s">V</span><span class="typed" style="--t: 1.14s">E</span></pre>
</div>
<div class="stage" :class="{ go: $clicks >= 6 }">
<pre class="out" style="--t: 2.14s">✓ timmyjc/quickstart-pytorch-armadillo 1.0.4 whitelisted on superexec-demo</pre>
</div>
</div>
</TerminalSession>
<div>
<img v-show="$clicks === 3" class="review-code" src="/review-code.png" />
<div v-show="$clicks >= 7" class="review-ui"><img class="full" src="/review-ui-full.png" /><img class="zoom" src="/review-whitelist.png" /></div>
</div>
</div>

---
layout: chart-full
heading: '7. Researcher logs in via OIDC'
pptxVideo: ./public/rec-7-login.mov
section: Demonstration
clicks: 4
---

<style>
.login-panes { display: flex; gap: 1rem; height: 23rem; }
.login-panes > * { flex: 1 1 0; min-width: 0; }
.browser { height: 100%; box-sizing: border-box; display: flex; flex-direction: column; border: 1px solid #9AA0A6; border-radius: 8px; overflow: hidden; background: white; opacity: 0; animation: browser-in 0.3s ease 2.4s forwards; }
@keyframes browser-in { to { opacity: 1; } }
.browser-chrome { display: flex; align-items: center; gap: 0.45rem; padding: 0.3rem 0.5rem; background: var(--slidev-theme-text); color: var(--slidev-theme-text-light); font-size: 11px; }
.browser-url { flex: 1; min-width: 0; padding: 0.12rem 0.6rem; border-radius: 999px; background: rgba(255, 255, 255, 0.14); font-size: 9.5px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.browser-bar { padding: 0.35rem 0.7rem; border-bottom: 1px solid #9AA0A6; font-family: var(--font-title); font-size: 15px; color: var(--slidev-theme-text); }
.browser-body { flex: 1; display: flex; align-items: center; justify-content: center; }
.device-card { width: 54%; padding: 0.6rem 0.7rem 0.7rem; border: 1px solid #9AA0A6; }
.device-card h3 { margin: 0 0 0.5rem; font-family: var(--font-title); font-size: 17px; font-weight: 400; color: var(--slidev-theme-text); }
.device-card p { margin: 0 0 0.4rem; font-size: 10px; }
.code-row { display: flex; justify-content: center; align-items: center; gap: 0.2rem; margin-bottom: 0.4rem; font-size: 14px; }
.code-row span { width: 1.05rem; padding: 0.15rem 0; border: 1px solid #9AA0A6; border-radius: 3px; text-align: center; }
.code-row i { font-style: normal; }
.submit { padding: 0.25rem 0; background: var(--slidev-theme-primary); color: white; text-align: center; font-size: 10px; }
</style>

<div class="login-panes">
<TerminalSession height="23rem">
<pre class="cmd" :class="{ 'type-go': $clicks >= 1 }">$ <span class="typed" style="--t: 0.100s">a</span><span class="typed" style="--t: 0.125s">r</span><span class="typed" style="--t: 0.150s">m</span><span class="typed" style="--t: 0.175s">a</span><span class="typed" style="--t: 0.200s">d</span><span class="typed" style="--t: 0.225s">i</span><span class="typed" style="--t: 0.250s">l</span><span class="typed" style="--t: 0.275s">l</span><span class="typed" style="--t: 0.300s">o</span><span class="typed" style="--t: 0.325s">-</span><span class="typed" style="--t: 0.350s">f</span><span class="typed" style="--t: 0.375s">l</span><span class="typed" style="--t: 0.400s">w</span><span class="typed" style="--t: 0.425s">r</span><span class="typed" style="--t: 0.450s">-</span><span class="typed" style="--t: 0.475s">a</span><span class="typed" style="--t: 0.500s">u</span><span class="typed" style="--t: 0.525s">t</span><span class="typed" style="--t: 0.550s">h</span><span class="typed" style="--t: 0.575s">e</span><span class="typed" style="--t: 0.600s">n</span><span class="typed" style="--t: 0.625s">t</span><span class="typed" style="--t: 0.650s">i</span><span class="typed" style="--t: 0.675s">c</span><span class="typed" style="--t: 0.700s">a</span><span class="typed" style="--t: 0.725s">t</span><span class="typed" style="--t: 0.750s">e</span><span class="typed" style="--t: 0.775s"> </span><span class="typed" style="--t: 0.800s">-</span><span class="typed" style="--t: 0.825s">-</span><span class="typed" style="--t: 0.850s">c</span><span class="typed" style="--t: 0.875s">o</span><span class="typed" style="--t: 0.900s">n</span><span class="typed" style="--t: 0.925s">f</span><span class="typed" style="--t: 0.950s">i</span><span class="typed" style="--t: 0.975s">g</span><span class="typed" style="--t: 1.000s"> </span><span class="typed" style="--t: 1.025s">f</span><span class="typed" style="--t: 1.050s">l</span><span class="typed" style="--t: 1.075s">o</span><span class="typed" style="--t: 1.100s">w</span><span class="typed" style="--t: 1.125s">e</span><span class="typed" style="--t: 1.150s">r</span><span class="typed" style="--t: 1.175s">-</span><span class="typed" style="--t: 1.200s">n</span><span class="typed" style="--t: 1.225s">o</span><span class="typed" style="--t: 1.250s">d</span><span class="typed" style="--t: 1.275s">e</span><span class="typed" style="--t: 1.300s">s</span><span class="typed" style="--t: 1.325s">.</span><span class="typed" style="--t: 1.350s">y</span><span class="typed" style="--t: 1.375s">a</span><span class="typed" style="--t: 1.400s">m</span><span class="typed" style="--t: 1.425s">l</span></pre>
<div class="stage" :class="{ go: $clicks >= 2 }">
<pre class="out" style="--t: 0.40s">Authenticating to 3 Armadillo nodes from flower-nodes.yaml</pre>
<pre class="out" style="--t: 0.90s">http://172.20.10.161:8080</pre>
<pre class="out" style="--t: 1.20s">Open this code: MSDJNJ</pre>
</div>
<div class="stage" :class="{ go: $clicks >= 4 }">
<pre class="out" style="--t: 0.40s">http://172.20.10.161:8081</pre>
<pre class="out" style="--t: 0.70s">Open this code: LRZWWL</pre>
<pre class="out" style="--t: 2.50s">http://172.20.10.161:8082</pre>
<pre class="out" style="--t: 2.80s">Open this code: QH7TZD</pre>
<pre class="out" style="--t: 4.60s">          Authenticated nodes</pre>
<pre class="out" style="--t: 4.72s">┏━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┓</pre>
<pre class="out" style="--t: 4.84s">┃ URL                       ┃ Status  ┃</pre>
<pre class="out" style="--t: 4.96s">┡━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━┩</pre>
<pre class="out" style="--t: 5.08s">│ http://172.20.10.161:8080 │ ✓ Ready │</pre>
<pre class="out" style="--t: 5.20s">│ http://172.20.10.161:8081 │ ✓ Ready │</pre>
<pre class="out" style="--t: 5.32s">│ http://172.20.10.161:8082 │ ✓ Ready │</pre>
<pre class="out" style="--t: 5.44s">└───────────────────────────┴─────────┘</pre>
<pre class="out" style="--t: 5.74s">Ready to run: armadillo-flwr-run</pre>
</div>
</TerminalSession>
<div>
<div v-show="$clicks === 2 || $clicks === 3" class="browser">
  <div class="browser-chrome"><span>&larr;</span><span>&rarr;</span><span>&#8635;</span><span v-show="$clicks === 3" class="browser-url">login.aai.lifescience-ri.eu/proxy/module.php/perun/disco.php?entityID=https%3A%2F%2Fproxy.aai.lifescience-ri.eu…</span><span v-show="$clicks !== 3" class="browser-url">auth1.molgenis.net/realms/Armadillo/login-actions/authenticate?execution=ede0c18d-6394-4b1d…</span></div>
  <div v-show="$clicks === 3" class="browser-body"><img src="/login-lifescience.png" style="display: block; width: 92%; max-width: none; margin: 0;" /></div>
  <div v-show="$clicks !== 3" class="browser-bar">MOLGENIS</div>
  <div v-show="$clicks !== 3" class="browser-body">
    <div class="device-card">
      <h3>Device login</h3>
      <p>Enter your user code</p>
      <div class="code-row"><span>M</span><span>S</span><span>D</span><i>-</i><span>J</span><span>N</span><span>J</span></div>
      <div class="submit">&rarr; Submit</div>
    </div>
  </div>
</div>
</div>
</div>

<span v-for="i in 4" :key="i" v-click style="display:none" />

---
layout: chart-full
heading: '8. Researcher runs job using access token'
pptxVideo: ./public/rec-8-run.mov
section: Demonstration
clicks: 2
---

<style>
.run-panes { display: flex; gap: 1rem; height: 23rem; }
.run-panes > * { flex: 1 1 0; min-width: 0; }
.run-diagram { position: relative; height: 368px; width: 400px; margin: 0 auto; }
.run-diagram .superlink { position: absolute; left: 10px; top: 164px; width: 120px; height: 40px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid #FDAE00; border-radius: 8px; background: #FFEFCC; font-family: var(--font-subtitle); font-size: 15px; font-weight: 600; color: #B9852A; }
.run-diagram .line { position: absolute; background: #9AA0A6; }
.run-diagram .node { position: absolute; left: 240px; width: 150px; height: 60px; box-sizing: border-box; display: flex; align-items: center; gap: 10px; padding: 0 10px; border: 2px solid #ddd; border-radius: 8px; background: white; }
.run-diagram .node > img { height: 34px; width: auto; margin: 0; }
.run-diagram .thumb { width: 89px; height: 26px; overflow: hidden; border-radius: 3px; }
.run-diagram .thumb img { display: block; width: 89px; max-width: none; margin: 0; }
.hl { position: absolute; box-sizing: border-box; border: 3px solid var(--slidev-theme-primary); border-radius: 6px; background: color-mix(in srgb, var(--slidev-theme-primary) 18%, transparent); opacity: 0; }
@keyframes hl-server { 0.00% { opacity: 0; } 3.79% { opacity: 0; } 5.30% { opacity: 1; } 41.67% { opacity: 1; } 43.18% { opacity: 0; } 65.15% { opacity: 0; } 66.67% { opacity: 1; } 69.70% { opacity: 1; } 71.21% { opacity: 0; } 80.30% { opacity: 0; } 81.82% { opacity: 1; } 100.00% { opacity: 1; } }
.run-diagram.go .hl-server { animation: hl-server 13.2s linear forwards; }
@keyframes hl-clients { 0.00% { opacity: 0; } 42.42% { opacity: 0; } 43.94% { opacity: 1; } 65.91% { opacity: 1; } 67.42% { opacity: 0; } 68.94% { opacity: 0; } 70.45% { opacity: 1; } 80.30% { opacity: 1; } 81.82% { opacity: 0; } 100.00% { opacity: 0; } }
.run-diagram.go .hl-clients { animation: hl-clients 13.2s linear forwards; }
</style>

<div class="run-panes">
<TerminalSession height="23rem" :start="$clicks >= 2">
<pre class="cmd" :class="{ 'type-go': $clicks >= 1 }">$ <span class="typed" style="--t: 0.100s">a</span><span class="typed" style="--t: 0.125s">r</span><span class="typed" style="--t: 0.150s">m</span><span class="typed" style="--t: 0.175s">a</span><span class="typed" style="--t: 0.200s">d</span><span class="typed" style="--t: 0.225s">i</span><span class="typed" style="--t: 0.250s">l</span><span class="typed" style="--t: 0.275s">l</span><span class="typed" style="--t: 0.300s">o</span><span class="typed" style="--t: 0.325s">-</span><span class="typed" style="--t: 0.350s">f</span><span class="typed" style="--t: 0.375s">l</span><span class="typed" style="--t: 0.400s">w</span><span class="typed" style="--t: 0.425s">r</span><span class="typed" style="--t: 0.450s">-</span><span class="typed" style="--t: 0.475s">r</span><span class="typed" style="--t: 0.500s">u</span><span class="typed" style="--t: 0.525s">n</span><span class="typed" style="--t: 0.550s"> </span><span class="typed" style="--t: 0.575s">@</span><span class="typed" style="--t: 0.600s">t</span><span class="typed" style="--t: 0.625s">i</span><span class="typed" style="--t: 0.650s">m</span><span class="typed" style="--t: 0.675s">m</span><span class="typed" style="--t: 0.700s">y</span><span class="typed" style="--t: 0.725s">j</span><span class="typed" style="--t: 0.750s">c</span><span class="typed" style="--t: 0.775s">/</span><span class="typed" style="--t: 0.800s">q</span><span class="typed" style="--t: 0.825s">u</span><span class="typed" style="--t: 0.850s">i</span><span class="typed" style="--t: 0.875s">c</span><span class="typed" style="--t: 0.900s">k</span><span class="typed" style="--t: 0.925s">s</span><span class="typed" style="--t: 0.950s">t</span><span class="typed" style="--t: 0.975s">a</span><span class="typed" style="--t: 1.000s">r</span><span class="typed" style="--t: 1.025s">t</span><span class="typed" style="--t: 1.050s">-</span><span class="typed" style="--t: 1.075s">p</span><span class="typed" style="--t: 1.100s">y</span><span class="typed" style="--t: 1.125s">t</span><span class="typed" style="--t: 1.150s">o</span><span class="typed" style="--t: 1.175s">r</span><span class="typed" style="--t: 1.200s">c</span><span class="typed" style="--t: 1.225s">h</span><span class="typed" style="--t: 1.250s">-</span><span class="typed" style="--t: 1.275s">a</span><span class="typed" style="--t: 1.300s">r</span><span class="typed" style="--t: 1.325s">m</span><span class="typed" style="--t: 1.350s">a</span><span class="typed" style="--t: 1.375s">d</span><span class="typed" style="--t: 1.400s">i</span><span class="typed" style="--t: 1.425s">l</span><span class="typed" style="--t: 1.450s">l</span><span class="typed" style="--t: 1.475s">o</span><span class="typed" style="--t: 1.500s">=</span><span class="typed" style="--t: 1.525s">=</span><span class="typed" style="--t: 1.550s">1</span><span class="typed" style="--t: 1.575s">.</span><span class="typed" style="--t: 1.600s">0</span><span class="typed" style="--t: 1.625s">.</span><span class="typed" style="--t: 1.650s">4</span><span class="typed" style="--t: 1.675s"> </span><span class="typed" style="--t: 1.700s">m</span><span class="typed" style="--t: 1.725s">o</span><span class="typed" style="--t: 1.750s">l</span><span class="typed" style="--t: 1.775s">g</span><span class="typed" style="--t: 1.800s">e</span><span class="typed" style="--t: 1.825s">n</span><span class="typed" style="--t: 1.850s">i</span><span class="typed" style="--t: 1.875s">s</span><span class="typed" style="--t: 1.900s"> </span><span class="typed" style="--t: 1.925s">-</span><span class="typed" style="--t: 1.950s">-</span><span class="typed" style="--t: 1.975s">s</span><span class="typed" style="--t: 2.000s">t</span><span class="typed" style="--t: 2.025s">r</span><span class="typed" style="--t: 2.050s">e</span><span class="typed" style="--t: 2.075s">a</span><span class="typed" style="--t: 2.100s">m</span></pre>
<pre class="out" style="--t: 0.40s">Injecting tokens from armadillo-flwr-authenticate</pre>
<pre class="out" style="--t: 0.52s">Using SuperLink: molgenis (superlink.molgenis.net:9093)</pre>
<pre class="out" style="--t: 1.32s">Successfully started run 682386506130654805</pre>
<pre class="out" style="--t: 1.62s">INFO :      Starting logstream for run_id `682386506130654805`</pre>
<pre class="out" style="--t: 2.22s">INFO :      Start `flwr-serverapp` process</pre>
<pre class="out" style="--t: 3.22s">Successfully installed quickstart-pytorch-armadillo to /app/.flwr/apps/timmyjc.quickstart-pytorch-armadillo.1.0.4.c0945432.</pre>
<pre class="out" style="--t: 4.02s">INFO :      Starting FedAvg strategy:</pre>
<pre class="out" style="--t: 4.14s">INFO :          ├── Number of rounds: 1</pre>
<pre class="out" style="--t: 4.26s">INFO :          ├── ArrayRecord (0.24 MB)</pre>
<pre class="out" style="--t: 4.38s">INFO :          ├── ConfigRecord (train): {'lr': 0.01, 'project': test-flower, 'armadillo-tokens': eyIx<span class="dim">… (truncated)</span>}</pre>
<pre class="out" style="--t: 4.50s">INFO :          ├── ConfigRecord (evaluate): {'project': test-flower, 'armadillo-tokens': eyIx<span class="dim">… (truncated)</span>}</pre>
<pre class="out" style="--t: 4.62s"><span class="dim">…</span></pre>
<pre class="out" style="--t: 5.42s">INFO :      [ROUND 1/1]</pre>
<pre class="out" style="--t: 5.72s">INFO :      configure_train: Sampled 3 nodes (out of 3)</pre>
<pre class="out" style="--t: 8.72s">INFO :      aggregate_train: Received 3 results and 0 failures</pre>
<pre class="out" style="--t: 8.84s">INFO :          └──> Aggregated MetricRecord: {'train_loss': 1.1793657589912414}</pre>
<pre class="out" style="--t: 9.14s">INFO :      configure_evaluate: Sampled 3 nodes (out of 3)</pre>
<pre class="out" style="--t: 10.64s">INFO :      aggregate_evaluate: Received 3 results and 0 failures</pre>
<pre class="out" style="--t: 10.76s">INFO :          └──> Aggregated MetricRecord: {'eval_loss': 1.255734071944849, 'eval_acc': 0.5511}</pre>
<pre class="out" style="--t: 11.26s">INFO :      Strategy execution finished in 27.22s</pre>
<pre class="out" style="--t: 11.38s">INFO :      Final results:</pre>
<pre class="out" style="--t: 11.50s">INFO :          Global Arrays:</pre>
<pre class="out" style="--t: 11.62s">INFO :                  ArrayRecord (0.238 MB)</pre>
<pre class="out" style="--t: 11.74s">INFO :          Aggregated ClientApp-side Train Metrics:</pre>
<pre class="out" style="--t: 11.86s">INFO :          {1: {'train_loss': '1.1794e+00'}}</pre>
<pre class="out" style="--t: 11.98s">INFO :          Aggregated ClientApp-side Evaluate Metrics:</pre>
<pre class="out" style="--t: 12.10s">INFO :          {1: {'eval_acc': '5.5110e-01', 'eval_loss': '1.2557e+00'}}</pre>
<pre class="out" style="--t: 12.60s">Saving final model to disk...</pre>
</TerminalSession>
<div>
<div class="run-diagram" :class="{ go: $clicks >= 2 }">
<div class="superlink">SuperLink</div>
<div class="line" style="left: 130px; top: 183px; width: 60px; height: 2px;"></div>
<div class="line" style="left: 189px; top: 64px; width: 2px; height: 240px;"></div>
<div v-for="i in 3" :key="'l' + i" class="line" :style="{ left: '189px', top: `${120 * i - 57}px`, width: '51px', height: '2px' }"></div>
<div v-for="i in 3" :key="'n' + i" class="node" :style="{ top: `${120 * i - 86}px` }">
<img src="/armadillo-logo.png" />
<div class="thumb"><img src="/cifar10-dogs.png" :style="{ marginTop: `${-26.1 * (i - 1)}px` }" /></div>
</div>
<div class="hl hl-server" style="left: 3px; top: 157px; width: 134px; height: 54px;"></div>
<div v-for="i in 3" :key="'h' + i" class="hl hl-clients" :style="{ left: '233px', top: `${120 * i - 93}px`, width: '164px', height: '74px' }"></div>
</div>
</div>
</div>

---
layout: section
---

# Discussion

---
layout: content
heading: Summary
section: Discussion
---

- We extended MOLGENIS Armadillo to support Flower alongside DataSHIELD
- We adapted open-source Flower to support app whitelisting and OIDC authentication
- Data owners can now install one back-end and allow analysis via DataSHIELD or Flower
- Future plans are to extend Armadillo to also support Vantage6
- Outstanding issues: (i) differential privacy, (ii) app review

---
layout: content
heading: Differential privacy
subheading: Planned developments
section: Discussion
---

- Use built-in Flower functionality where possible
- <span style="font-family: var(--font-subtitle);">LocalDpMod</span> applies clipping to return values from node
- Enforce this either at the app review stage or within the SuperExec container

---
layout: content
heading: App review
subheading: Some ideas
section: Discussion
---

- Comprehensive literature review on attack vectors / disclosure controls
- Develop cross-platform app review protocol
- Validate AI as review tool

---
layout: content-img-right
heading: Acknowledgements
image: ./public/team-photo.jpg
imageWidth: '42'
---

- **UMCG Armadillo team:** Mariska Slofstra, Ruben Veenstra, Dick Postma, Erik Zwart, Stuart Wheater <br> and Morris Swertz
- **Flower team:** Chong Shen & Pedro Mesa
- **Funders:** EU via International Human Exposome Network (IHEN), FLEX4HEALTH (OSCARS)

<div style="display: flex; justify-content: flex-start; align-items: center; gap: 1.25rem; margin-top: 1rem;">
  <img src="./public/ihen-logo.svg" style="height: 1.75rem; width: 9.62rem; max-width: none; flex: none;" />
  <img src="./public/funder-logo.svg" style="height: 1.75rem; width: 5.72rem; max-width: none; flex: none;" />
  <img src="./public/eu-funded-logo.png" style="height: 1.75rem; width: 7.69rem; max-width: none; flex: none;" />
</div>
