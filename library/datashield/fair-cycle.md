---
layout: content
heading: FAIR data
subheading: The research cycle
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
  <li v-click><span class="chips"><span class="chip f">F</span></span>Catalogue</li>
  <li v-click><span class="chips"><span class="chip i">I</span><span class="chip r">R</span></span>Exposome tools</li>
  <li v-click><span class="chips"><span class="chip a">A</span><span class="chip r">R</span></span>DataSHIELD</li>
</ul>
</div>
