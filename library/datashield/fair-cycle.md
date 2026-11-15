---
layout: content
heading: FAIR data
subheading: The research cycle
---

<style>
.fair-wrap { display: flex; align-items: center; justify-content: flex-start; gap: 3rem; height: 100%; min-height: 0; }

/* The four boxes are HTML, not SVG text: an SVG font-size attribute has zero
   specificity and loses to the deck's own rules, which rendered them ~3x too
   big. Only the arrows stay as SVG. The box geometry is a percentage of the
   original 480x420 drawing, so the arcs still line up. */
.fair-diagram { position: relative; flex: 0 0 48%; margin-right: auto; aspect-ratio: 480 / 420; max-height: 100%; }
.fair-arrows { position: absolute; inset: 0; width: 100%; height: 100%; }
.fair-box {
  position: absolute; width: 29.2%; height: 26.2%; border-radius: 8px;
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  color: #fff; line-height: 1;
}
.fair-box .l { font-size: 34px; font-weight: 700; }
.fair-box { transition: opacity 0.35s ease, filter 0.35s ease; }
/* same focus treatment as FocusCards.vue: the active box keeps its colour,
   the rest recede */
.fair-box.dim { opacity: 0.28; filter: grayscale(85%); }
.fair-notes { list-style: none; padding: 0 !important; margin: 0; }
.fair-notes li { font-size: 20px !important; margin-bottom: 1.1rem !important; line-height: 1.4; }
.fair-notes b { font-weight: 700; }
.fair-box .n { font-size: 12px; margin-top: 0.25rem; }
.fair-box.f { left: 6.25%; top: 7.1%; background: #4285F4; }
.fair-box.a { right: 6.25%; top: 7.1%; background: #E2A517; color: #333333; }
.fair-box.i { right: 6.25%; bottom: 7.1%; background: #119DA1; }
.fair-box.r { left: 6.25%; bottom: 7.1%; background: #5D408A; }

.fair-links { list-style: none; padding: 0 !important; margin: 0; }
.fair-links li { display: flex; align-items: center; gap: 0.75rem; font-size: 22px !important; margin-bottom: 1.25rem !important; }
.chips { display: flex; gap: 0.3rem; min-width: 6.9rem; }
.chip { width: 2.1rem; height: 2.1rem; border-radius: 6px; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 18px; color: #fff; }
.chip.f { background: #4285F4; }
.chip.a { background: #E2A517; color: #333333; }
.chip.i { background: #119DA1; }
.chip.r { background: #5D408A; }
</style>

<div class="fair-wrap">
<div class="fair-diagram">
<svg class="fair-arrows" viewBox="0 0 480 420" preserveAspectRatio="none" role="img" aria-label="FAIR cycle: Findable, Accessible, Interoperable, Reusable">
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
</svg>
<div class="fair-box f"><span class="l">F</span><span class="n">Findable</span></div>
<div class="fair-box a"><span class="l">A</span><span class="n">Accessible</span></div>
<div class="fair-box i"><span class="l">I</span><span class="n">Interoperable</span></div>
<div class="fair-box r"><span class="l">R</span><span class="n">Reusable</span></div>
</div>
</div>

---
layout: content
heading: FAIR data
subheading: The research cycle
---

<div class="fair-wrap">
<div class="fair-diagram">
<svg class="fair-arrows" viewBox="0 0 480 420" preserveAspectRatio="none" role="img" aria-label="FAIR cycle: Findable, Accessible, Interoperable, Reusable">
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
</svg>
<div class="fair-box f" :class="{ dim: $clicks > 0 && $clicks !== 1 }"><span class="l">F</span><span class="n">Findable</span></div>
<div class="fair-box a" :class="{ dim: $clicks > 0 && $clicks !== 2 }"><span class="l">A</span><span class="n">Accessible</span></div>
<div class="fair-box i" :class="{ dim: $clicks > 0 && $clicks !== 3 }"><span class="l">I</span><span class="n">Interoperable</span></div>
<div class="fair-box r" :class="{ dim: $clicks > 0 && $clicks !== 4 }"><span class="l">R</span><span class="n">Reusable</span></div>
</div>

<ul class="fair-notes">
<li v-click><b>Findable</b> — described with rich metadata and registered in a catalogue others can search</li>
<li v-click><b>Accessible</b> — retrievable by anyone with permission, over a standard protocol</li>
<li v-click><b>Interoperable</b> — shared vocabularies and formats, so datasets can be combined</li>
<li v-click><b>Reusable</b> — documented and licensed well enough to be used again</li>
</ul>
</div>

---
layout: content
heading: FAIR data
subheading: Where our tools fit
---

<ul class="fair-links">
  <li v-click><span class="chips"><span class="chip f">F</span><span class="chip a">A</span><span class="chip r">R</span></span>Catalogue</li>
  <li v-click><span class="chips"><span class="chip i">I</span><span class="chip r">R</span></span>Exposome tools</li>
  <li v-click><span class="chips"><span class="chip a">A</span><span class="chip r">R</span></span>DataSHIELD</li>
</ul>
