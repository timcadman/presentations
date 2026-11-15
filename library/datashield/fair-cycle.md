---
layout: content
heading: FAIR data
subheading: The research cycle
transition: none
---


<div class="fair-wrap">
<div class="fair-diagram">
<svg class="fair-arrows" viewBox="0 0 480 420" preserveAspectRatio="none" role="img" aria-label="FAIR cycle: Findable, Accessible, Interoperable, Reusable">
  <defs>
    <marker id="fair-arrow-a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#9AA0A6" />
    </marker>
  </defs>
  <g fill="none" stroke="#9AA0A6" stroke-width="3" marker-end="url(#fair-arrow-a)">
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
transition: slide-up
---

<div class="fair-wrap">
<div class="fair-diagram">
<svg class="fair-arrows" viewBox="0 0 480 420" preserveAspectRatio="none" role="img" aria-label="FAIR cycle: Findable, Accessible, Interoperable, Reusable">
  <defs>
    <marker id="fair-arrow-b" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#9AA0A6" />
    </marker>
  </defs>
  <g fill="none" stroke="#9AA0A6" stroke-width="3" marker-end="url(#fair-arrow-b)">
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
<li v-click><b>Reusable</b> — documented and available for re-analysis</li>
</ul>
</div>
