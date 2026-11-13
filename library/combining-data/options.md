---
layout: content
heading: Analysing multiple datasets
subheading: How
clicks: 3
---

<style>
.approach-card { height: 4.8rem; box-sizing: border-box; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; }
.approach-card h3 { margin: 0; font-size: 1rem; }
</style>

<div style="display: flex; gap: 2rem; align-items: stretch;">
  <div style="flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 0.7rem;">
    <div class="tint-card approach-card" style="--c: #4285F4;" :class="$clicks < 1 ? 'active' : 'dimmed'">
      <h3>Move data to one location</h3>
    </div>
    <div class="tint-card approach-card" style="--c: #E6B96A; --h: #B9852A; --t: #333333;" :class="$clicks === 1 ? 'active' : 'dimmed'">
      <h3>Share script, meta-analysis</h3>
    </div>
    <div class="tint-card approach-card" style="--c: #0097A7;" :class="$clicks >= 2 ? 'active' : 'dimmed'">
      <h3>Federated Analysis</h3>
      <p v-show="$clicks >= 3" style="margin: 0.4rem 0 0 0; font-size: 13px;">"Remote analysis without data transfer"</p>
    </div>
  </div>
  <div style="flex: 1; display: flex; align-items: center; justify-content: center;">
  <div style="width: 300px; height: 208px; margin: 0 auto; position: relative;">
  <div v-show="$clicks === 0" style="position: absolute; inset: 0;">
  <svg viewBox="0 0 300 208" style="position: absolute; inset: 0; width: 100%; height: 100%;">
  <defs>
  <marker id="cd-arrow-1" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
  <path d="M0,0 L10,5 L0,10 z" fill="#4285F4" />
  </marker>
  </defs>
  <line x1="100" y1="41.5" x2="170.44" y2="94.85" stroke="#4285F4" stroke-width="2" marker-end="url(#cd-arrow-1)" />
  <line x1="100" y1="102.1" x2="168" y2="102.1" stroke="#4285F4" stroke-width="2" marker-end="url(#cd-arrow-1)" />
  <line x1="100" y1="162.7" x2="170.44" y2="109.35" stroke="#4285F4" stroke-width="2" marker-end="url(#cd-arrow-1)" />
  </svg>
  <div style="position: absolute; left: 0; top: 20px; width: 100px; height: 43px; display: flex; align-items: center; justify-content: flex-end; gap: 0.5rem;">
  <span style="font-size: 13px;">Site A</span>
  <img src="../assets/icon-database.png" style="height: 43px;" />
  </div>
  <div style="position: absolute; left: 0; top: 80.6px; width: 100px; height: 43px; display: flex; align-items: center; justify-content: flex-end; gap: 0.5rem;">
  <span style="font-size: 13px;">Site B</span>
  <img src="../assets/icon-database.png" style="height: 43px;" />
  </div>
  <div style="position: absolute; left: 0; top: 141.2px; width: 100px; height: 43px; display: flex; align-items: center; justify-content: flex-end; gap: 0.5rem;">
  <span style="font-size: 13px;">Site C</span>
  <img src="../assets/icon-database.png" style="height: 43px;" />
  </div>
  <img src="../assets/icon-researcher.png" style="position: absolute; left: 190px; top: 69.1px; height: 66px;" />
  <!-- No laptop icon asset exists in this deck, so drawn in CSS: a screen
       (bordered rectangle) over a base (filled bar), same 43px height as the
       site icons, centred on the same y as the researcher/site-B row. -->
  <div style="position: absolute; left: 245px; top: 80.6px; width: 48px; height: 43px;">
  <div style="width: 42px; height: 33px; margin: 0 3px; border: 2.5px solid #333; border-radius: 3px; box-sizing: border-box;"></div>
  <div style="width: 48px; height: 7px; background: #333; border-radius: 0 0 3px 3px; margin-top: 3px;"></div>
  </div>
  </div>
  <div v-show="$clicks === 1" style="position: absolute; inset: 0;">
  <svg viewBox="0 0 300 208" style="position: absolute; inset: 0; width: 100%; height: 100%;">
  <defs>
  <marker id="cd-arrow-2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
  <path d="M0,0 L10,5 L0,10 z" fill="#4285F4" />
  </marker>
  <marker id="cd-arrow-2-gold" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
  <path d="M0,0 L10,5 L0,10 z" fill="#E6B96A" />
  </marker>
  </defs>
  <!-- Script out: researcher to each site -->
  <line x1="170.44" y1="94.85" x2="100" y2="41.5" stroke="#4285F4" stroke-width="2" marker-end="url(#cd-arrow-2)" />
  <line x1="168" y1="102.1" x2="100" y2="102.1" stroke="#4285F4" stroke-width="2" marker-end="url(#cd-arrow-2)" />
  <line x1="170.44" y1="109.35" x2="100" y2="162.7" stroke="#4285F4" stroke-width="2" marker-end="url(#cd-arrow-2)" />
  <!-- Combined results back: one arc from the site cluster to the researcher,
       routed below the outbound lines so it doesn't cross them. Gold, to
       stand out from the (blue) outbound script lines. -->
  <path d="M 60,184 C 60,205 207,205 207,135" stroke="#E6B96A" stroke-width="2" fill="none" marker-end="url(#cd-arrow-2-gold)" />
  </svg>
  <div style="position: absolute; left: 0; top: 20px; width: 100px; height: 43px; display: flex; align-items: center; justify-content: flex-end; gap: 0.5rem;">
  <span style="font-size: 13px;">Site A</span>
  <img src="../assets/icon-database.png" style="height: 43px;" />
  </div>
  <div style="position: absolute; left: 0; top: 80.6px; width: 100px; height: 43px; display: flex; align-items: center; justify-content: flex-end; gap: 0.5rem;">
  <span style="font-size: 13px;">Site B</span>
  <img src="../assets/icon-database.png" style="height: 43px;" />
  </div>
  <div style="position: absolute; left: 0; top: 141.2px; width: 100px; height: 43px; display: flex; align-items: center; justify-content: flex-end; gap: 0.5rem;">
  <span style="font-size: 13px;">Site C</span>
  <img src="../assets/icon-database.png" style="height: 43px;" />
  </div>
  <img src="../assets/icon-researcher.png" style="position: absolute; left: 190px; top: 69.1px; height: 66px;" />
  <div style="position: absolute; left: 132.5px; top: 61.8px; width: 15px; height: 20px; border: 1.5px solid #4285F4; border-radius: 2px; background: white; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px;">
  <div style="width: 9px; height: 1px; background: #4285F4;"></div>
  <div style="width: 9px; height: 1px; background: #4285F4;"></div>
  </div>
  <div style="position: absolute; left: 132.5px; top: 92.1px; width: 15px; height: 20px; border: 1.5px solid #4285F4; border-radius: 2px; background: white; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px;">
  <div style="width: 9px; height: 1px; background: #4285F4;"></div>
  <div style="width: 9px; height: 1px; background: #4285F4;"></div>
  </div>
  <div style="position: absolute; left: 132.5px; top: 122.4px; width: 15px; height: 20px; border: 1.5px solid #4285F4; border-radius: 2px; background: white; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px;">
  <div style="width: 9px; height: 1px; background: #4285F4;"></div>
  <div style="width: 9px; height: 1px; background: #4285F4;"></div>
  </div>
  <!-- Stacked-documents icon on the return arc: combined/aggregated results
       from all sites (as opposed to the single script paper on the way out). -->
  <div style="position: absolute; left: 123px; top: 180.6px; width: 21px; height: 26px;">
  <div style="position: absolute; left: 6px; top: 6px; width: 15px; height: 20px; border: 1.5px solid #E6B96A; border-radius: 2px; background: white;"></div>
  <div style="position: absolute; left: 3px; top: 3px; width: 15px; height: 20px; border: 1.5px solid #E6B96A; border-radius: 2px; background: white;"></div>
  <div style="position: absolute; left: 0; top: 0; width: 15px; height: 20px; border: 1.5px solid #E6B96A; border-radius: 2px; background: white; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px;">
  <div style="width: 9px; height: 1px; background: #E6B96A;"></div>
  <div style="width: 9px; height: 1px; background: #E6B96A;"></div>
  </div>
  </div>
  </div>
  <div v-show="$clicks >= 2" style="position: absolute; inset: 0;">
  <svg viewBox="0 0 300 208" style="position: absolute; inset: 0; width: 100%; height: 100%;">
  <defs>
  <marker id="cd-arrow-3" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
  <path d="M0,0 L10,5 L0,10 z" fill="#4285F4" />
  </marker>
  <marker id="cd-arrow-3-gold" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
  <path d="M0,0 L10,5 L0,10 z" fill="#E6B96A" />
  </marker>
  </defs>
  <!-- Same blue lines/coordinates as diagram 1 (data->researcher), but
       pointing researcher->data (marker-start, not marker-end) — federated
       analysis sends commands to the data, not the other way round. -->
  <line x1="100" y1="41.5" x2="170.44" y2="94.85" stroke="#4285F4" stroke-width="2" marker-start="url(#cd-arrow-3)" />
  <line x1="100" y1="102.1" x2="168" y2="102.1" stroke="#4285F4" stroke-width="2" marker-start="url(#cd-arrow-3)" />
  <line x1="100" y1="162.7" x2="170.44" y2="109.35" stroke="#4285F4" stroke-width="2" marker-start="url(#cd-arrow-3)" />
  <!-- Same gold return arc as diagram 2, same path/endpoint (researcher is
       back at its usual position here), just with a code glyph on it
       instead of the stacked-documents icon. -->
  <path d="M 60,184 C 60,205 207,205 207,135" stroke="#E6B96A" stroke-width="2" fill="none" marker-end="url(#cd-arrow-3-gold)" />
  </svg>
  <div style="position: absolute; left: 0; top: 20px; width: 100px; height: 43px; display: flex; align-items: center; justify-content: flex-end; gap: 0.5rem;">
  <span style="font-size: 13px;">Site A</span>
  <img src="../assets/icon-database.png" style="height: 43px;" />
  </div>
  <div style="position: absolute; left: 0; top: 80.6px; width: 100px; height: 43px; display: flex; align-items: center; justify-content: flex-end; gap: 0.5rem;">
  <span style="font-size: 13px;">Site B</span>
  <img src="../assets/icon-database.png" style="height: 43px;" />
  </div>
  <div style="position: absolute; left: 0; top: 141.2px; width: 100px; height: 43px; display: flex; align-items: center; justify-content: flex-end; gap: 0.5rem;">
  <span style="font-size: 13px;">Site C</span>
  <img src="../assets/icon-database.png" style="height: 43px;" />
  </div>
  <!-- Code glyphs sit above each line's midpoint (instead of the paper/script
       icon — federated analysis runs code interactively rather than passing
       documents), and a larger one above the return arc, replacing diagram 2's
       stacked-documents icon. Line A/B/C midpoints are (140,71.8)/(140,102.1)/(140,132.4). -->
  <div style="position: absolute; left: 132.5px; top: 61.8px; width: 15px; height: 20px; border: 1.5px solid #4285F4; border-radius: 2px; background: white; display: flex; align-items: center; justify-content: center;">
  <span style="font-size: 8px; font-weight: 700; color: #4285F4; line-height: 1;">&lt;/&gt;</span>
  </div>
  <div style="position: absolute; left: 132.5px; top: 92.1px; width: 15px; height: 20px; border: 1.5px solid #4285F4; border-radius: 2px; background: white; display: flex; align-items: center; justify-content: center;">
  <span style="font-size: 8px; font-weight: 700; color: #4285F4; line-height: 1;">&lt;/&gt;</span>
  </div>
  <div style="position: absolute; left: 132.5px; top: 122.4px; width: 15px; height: 20px; border: 1.5px solid #4285F4; border-radius: 2px; background: white; display: flex; align-items: center; justify-content: center;">
  <span style="font-size: 8px; font-weight: 700; color: #4285F4; line-height: 1;">&lt;/&gt;</span>
  </div>
  <div style="position: absolute; left: 123px; top: 180.6px; width: 15px; height: 20px; border: 1.5px solid #E6B96A; border-radius: 2px; background: white; display: flex; align-items: center; justify-content: center;">
  <span style="font-size: 10px; font-weight: 700; color: #E6B96A; line-height: 1;">&lt;/&gt;</span>
  </div>
  <!-- Researcher back in its usual position (lines above terminate here);
       computer symbol to its right, representing the analysis platform they
       run federated queries from. -->
  <img src="../assets/icon-researcher.png" style="position: absolute; left: 190px; top: 69.1px; height: 66px;" />
  <!-- No laptop icon asset exists in this deck, so drawn in CSS: a screen
       (bordered rectangle) over a base (filled bar), same 43px height as the
       site icons, centred on the same y as the researcher/site-B row. -->
  <div style="position: absolute; left: 245px; top: 80.6px; width: 48px; height: 43px;">
  <div style="width: 42px; height: 33px; margin: 0 3px; border: 2.5px solid #333; border-radius: 3px; box-sizing: border-box;"></div>
  <div style="width: 48px; height: 7px; background: #333; border-radius: 0 0 3px 3px; margin-top: 3px;"></div>
  </div>
  </div>
</div>
</div>
</div>

---
layout: content
heading: Analysing multiple datasets
subheading: "Option 1: Data transfer"
transition: slide-up
---

<div style="display: flex; gap: 2rem; align-items: flex-start;">
  <div style="flex: 1; display: flex; align-items: center; justify-content: center;">
  <div style="width: 300px; height: 208px; margin: 0 auto; position: relative;">
  <svg viewBox="0 0 300 208" style="position: absolute; inset: 0; width: 100%; height: 100%;">
  <defs>
  <marker id="cd-arrow-o1" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
  <path d="M0,0 L10,5 L0,10 z" fill="#4285F4" />
  </marker>
  </defs>
  <line x1="100" y1="41.5" x2="170.44" y2="94.85" stroke="#4285F4" stroke-width="2" marker-end="url(#cd-arrow-o1)" />
  <line x1="100" y1="102.1" x2="168" y2="102.1" stroke="#4285F4" stroke-width="2" marker-end="url(#cd-arrow-o1)" />
  <line x1="100" y1="162.7" x2="170.44" y2="109.35" stroke="#4285F4" stroke-width="2" marker-end="url(#cd-arrow-o1)" />
  </svg>
  <div style="position: absolute; left: 0; top: 20px; width: 100px; height: 43px; display: flex; align-items: center; justify-content: flex-end; gap: 0.5rem;">
  <span style="font-size: 13px;">Site A</span>
  <img src="../assets/icon-database.png" style="height: 43px;" />
  </div>
  <div style="position: absolute; left: 0; top: 80.6px; width: 100px; height: 43px; display: flex; align-items: center; justify-content: flex-end; gap: 0.5rem;">
  <span style="font-size: 13px;">Site B</span>
  <img src="../assets/icon-database.png" style="height: 43px;" />
  </div>
  <div style="position: absolute; left: 0; top: 141.2px; width: 100px; height: 43px; display: flex; align-items: center; justify-content: flex-end; gap: 0.5rem;">
  <span style="font-size: 13px;">Site C</span>
  <img src="../assets/icon-database.png" style="height: 43px;" />
  </div>
  <img src="../assets/icon-researcher.png" style="position: absolute; left: 190px; top: 69.1px; height: 66px;" />
  <!-- No laptop icon asset exists in this deck, so drawn in CSS: a screen
       (bordered rectangle) over a base (filled bar), same 43px height as the
       site icons, centred on the same y as the researcher/site-B row. -->
  <div style="position: absolute; left: 245px; top: 80.6px; width: 48px; height: 43px;">
  <div style="width: 42px; height: 33px; margin: 0 3px; border: 2.5px solid #333; border-radius: 3px; box-sizing: border-box;"></div>
  <div style="width: 48px; height: 7px; background: #333; border-radius: 0 0 3px 3px; margin-top: 3px;"></div>
  </div>
  </div>
  </div>
  <div style="flex: 1;">
    <ul style="padding-left: 1.5rem; margin: 0;">
      <li style="font-size: 18px; margin-bottom: 0.5rem; line-height: 1.5;"><strong>Strategy:</strong> Transfer to one location</li>
      <li style="font-size: 18px; margin-bottom: 0.5rem; line-height: 1.5;"><strong>Pros:</strong> One researcher conducts all analyses</li>
      <li style="font-size: 18px; margin-bottom: 0.5rem; line-height: 1.5;"><strong>Cons:</strong>
        <ul style="padding-left: 1.5rem; margin: 0.3rem 0 0 0;">
          <li style="font-size: 18px; margin-bottom: 0.3rem; line-height: 1.5;">Ethico-legal restrictions</li>
          <li style="font-size: 18px; margin-bottom: 0.3rem; line-height: 1.5;">Data owners lose control of data</li>
          <li style="font-size: 18px; margin-bottom: 0.3rem; line-height: 1.5;">Storage demands (e.g. omics)</li>
        </ul>
      </li>
    </ul>
  </div>
</div>

---
layout: content
heading: Analysing multiple datasets
subheading: "Option 2: Share script, meta-analysis"
transition: slide-up
---

<div style="display: flex; gap: 2rem; align-items: flex-start;">
  <div style="flex: 1; display: flex; align-items: center; justify-content: center;">
  <div style="width: 300px; height: 208px; margin: 0 auto; position: relative;">
  <svg viewBox="0 0 300 208" style="position: absolute; inset: 0; width: 100%; height: 100%;">
  <defs>
  <marker id="cd-arrow-o2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
  <path d="M0,0 L10,5 L0,10 z" fill="#4285F4" />
  </marker>
  <marker id="cd-arrow-o2-gold" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
  <path d="M0,0 L10,5 L0,10 z" fill="#E6B96A" />
  </marker>
  </defs>
  <line x1="170.44" y1="94.85" x2="100" y2="41.5" stroke="#4285F4" stroke-width="2" marker-end="url(#cd-arrow-o2)" />
  <line x1="168" y1="102.1" x2="100" y2="102.1" stroke="#4285F4" stroke-width="2" marker-end="url(#cd-arrow-o2)" />
  <line x1="170.44" y1="109.35" x2="100" y2="162.7" stroke="#4285F4" stroke-width="2" marker-end="url(#cd-arrow-o2)" />
  <path d="M 60,184 C 60,205 207,205 207,135" stroke="#E6B96A" stroke-width="2" fill="none" marker-end="url(#cd-arrow-o2-gold)" />
  </svg>
  <div style="position: absolute; left: 0; top: 20px; width: 100px; height: 43px; display: flex; align-items: center; justify-content: flex-end; gap: 0.5rem;">
  <span style="font-size: 13px;">Site A</span>
  <img src="../assets/icon-database.png" style="height: 43px;" />
  </div>
  <div style="position: absolute; left: 0; top: 80.6px; width: 100px; height: 43px; display: flex; align-items: center; justify-content: flex-end; gap: 0.5rem;">
  <span style="font-size: 13px;">Site B</span>
  <img src="../assets/icon-database.png" style="height: 43px;" />
  </div>
  <div style="position: absolute; left: 0; top: 141.2px; width: 100px; height: 43px; display: flex; align-items: center; justify-content: flex-end; gap: 0.5rem;">
  <span style="font-size: 13px;">Site C</span>
  <img src="../assets/icon-database.png" style="height: 43px;" />
  </div>
  <img src="../assets/icon-researcher.png" style="position: absolute; left: 190px; top: 69.1px; height: 66px;" />
  <div style="position: absolute; left: 132.5px; top: 61.8px; width: 15px; height: 20px; border: 1.5px solid #4285F4; border-radius: 2px; background: white; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px;">
  <div style="width: 9px; height: 1px; background: #4285F4;"></div>
  <div style="width: 9px; height: 1px; background: #4285F4;"></div>
  </div>
  <div style="position: absolute; left: 132.5px; top: 92.1px; width: 15px; height: 20px; border: 1.5px solid #4285F4; border-radius: 2px; background: white; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px;">
  <div style="width: 9px; height: 1px; background: #4285F4;"></div>
  <div style="width: 9px; height: 1px; background: #4285F4;"></div>
  </div>
  <div style="position: absolute; left: 132.5px; top: 122.4px; width: 15px; height: 20px; border: 1.5px solid #4285F4; border-radius: 2px; background: white; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px;">
  <div style="width: 9px; height: 1px; background: #4285F4;"></div>
  <div style="width: 9px; height: 1px; background: #4285F4;"></div>
  </div>
  <div style="position: absolute; left: 123px; top: 180.6px; width: 21px; height: 26px;">
  <div style="position: absolute; left: 6px; top: 6px; width: 15px; height: 20px; border: 1.5px solid #E6B96A; border-radius: 2px; background: white;"></div>
  <div style="position: absolute; left: 3px; top: 3px; width: 15px; height: 20px; border: 1.5px solid #E6B96A; border-radius: 2px; background: white;"></div>
  <div style="position: absolute; left: 0; top: 0; width: 15px; height: 20px; border: 1.5px solid #E6B96A; border-radius: 2px; background: white; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px;">
  <div style="width: 9px; height: 1px; background: #E6B96A;"></div>
  <div style="width: 9px; height: 1px; background: #E6B96A;"></div>
  </div>
  </div>
  </div>
  </div>
  <div style="flex: 1;">
    <ul style="padding-left: 1.5rem; margin: 0;">
      <li style="font-size: 18px; margin-bottom: 0.5rem; line-height: 1.5;"><strong>Strategy:</strong> Send analysis script to each site; combine returned results</li>
      <li style="font-size: 18px; margin-bottom: 0.5rem; line-height: 1.5;"><strong>Pros:</strong> No sharing of data</li>
      <li style="font-size: 18px; margin-bottom: 0.5rem; line-height: 1.5;"><strong>Cons:</strong>
        <ul style="padding-left: 1.5rem; margin: 0.3rem 0 0 0;">
          <li style="font-size: 18px; margin-bottom: 0.3rem; line-height: 1.5;">Inefficient</li>
          <li style="font-size: 18px; margin-bottom: 0.3rem; line-height: 1.5;">Limited to two-stage methods</li>
        </ul>
      </li>
    </ul>
  </div>
</div>

---
layout: content
heading: Analysing multiple datasets
subheading: "Option 3: Federated analysis"
transition: slide-up
---

<div style="display: flex; gap: 2rem; align-items: flex-start;">
  <div style="flex: 1; display: flex; align-items: center; justify-content: center;">
  <div style="width: 300px; height: 208px; margin: 0 auto; position: relative;">
  <svg viewBox="0 0 300 208" style="position: absolute; inset: 0; width: 100%; height: 100%;">
  <defs>
  <marker id="cd-arrow-o3" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
  <path d="M0,0 L10,5 L0,10 z" fill="#4285F4" />
  </marker>
  <marker id="cd-arrow-o3-gold" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
  <path d="M0,0 L10,5 L0,10 z" fill="#E6B96A" />
  </marker>
  </defs>
  <line x1="100" y1="41.5" x2="170.44" y2="94.85" stroke="#4285F4" stroke-width="2" marker-start="url(#cd-arrow-o3)" />
  <line x1="100" y1="102.1" x2="168" y2="102.1" stroke="#4285F4" stroke-width="2" marker-start="url(#cd-arrow-o3)" />
  <line x1="100" y1="162.7" x2="170.44" y2="109.35" stroke="#4285F4" stroke-width="2" marker-start="url(#cd-arrow-o3)" />
  <path d="M 60,184 C 60,205 207,205 207,135" stroke="#E6B96A" stroke-width="2" fill="none" marker-end="url(#cd-arrow-o3-gold)" />
  </svg>
  <div style="position: absolute; left: 0; top: 20px; width: 100px; height: 43px; display: flex; align-items: center; justify-content: flex-end; gap: 0.5rem;">
  <span style="font-size: 13px;">Site A</span>
  <img src="../assets/icon-database.png" style="height: 43px;" />
  </div>
  <div style="position: absolute; left: 0; top: 80.6px; width: 100px; height: 43px; display: flex; align-items: center; justify-content: flex-end; gap: 0.5rem;">
  <span style="font-size: 13px;">Site B</span>
  <img src="../assets/icon-database.png" style="height: 43px;" />
  </div>
  <div style="position: absolute; left: 0; top: 141.2px; width: 100px; height: 43px; display: flex; align-items: center; justify-content: flex-end; gap: 0.5rem;">
  <span style="font-size: 13px;">Site C</span>
  <img src="../assets/icon-database.png" style="height: 43px;" />
  </div>
  <div style="position: absolute; left: 132.5px; top: 61.8px; width: 15px; height: 20px; border: 1.5px solid #4285F4; border-radius: 2px; background: white; display: flex; align-items: center; justify-content: center;">
  <span style="font-size: 8px; font-weight: 700; color: #4285F4; line-height: 1;">&lt;/&gt;</span>
  </div>
  <div style="position: absolute; left: 132.5px; top: 92.1px; width: 15px; height: 20px; border: 1.5px solid #4285F4; border-radius: 2px; background: white; display: flex; align-items: center; justify-content: center;">
  <span style="font-size: 8px; font-weight: 700; color: #4285F4; line-height: 1;">&lt;/&gt;</span>
  </div>
  <div style="position: absolute; left: 132.5px; top: 122.4px; width: 15px; height: 20px; border: 1.5px solid #4285F4; border-radius: 2px; background: white; display: flex; align-items: center; justify-content: center;">
  <span style="font-size: 8px; font-weight: 700; color: #4285F4; line-height: 1;">&lt;/&gt;</span>
  </div>
  <div style="position: absolute; left: 123px; top: 180.6px; width: 15px; height: 20px; border: 1.5px solid #E6B96A; border-radius: 2px; background: white; display: flex; align-items: center; justify-content: center;">
  <span style="font-size: 10px; font-weight: 700; color: #E6B96A; line-height: 1;">&lt;/&gt;</span>
  </div>
  <img src="../assets/icon-researcher.png" style="position: absolute; left: 190px; top: 69.1px; height: 66px;" />
  <div style="position: absolute; left: 245px; top: 80.6px; width: 48px; height: 43px;">
  <div style="width: 42px; height: 33px; margin: 0 3px; border: 2.5px solid #333; border-radius: 3px; box-sizing: border-box;"></div>
  <div style="width: 48px; height: 7px; background: #333; border-radius: 0 0 3px 3px; margin-top: 3px;"></div>
  </div>
  </div>
  </div>
  <div style="flex: 1;">
    <ul style="padding-left: 1.5rem; margin: 0;">
      <li style="font-size: 18px; margin-bottom: 0.5rem; line-height: 1.5;"><strong>Strategy:</strong> Send analysis code to the data; only aggregate results return</li>
      <li style="font-size: 18px; margin-bottom: 0.5rem; line-height: 1.5;"><strong>Pros:</strong> Data never leaves its location; owners keep control and access rights</li>
      <li style="font-size: 18px; margin-bottom: 0.5rem; line-height: 1.5;"><strong>Cons:</strong>
        <ul style="padding-left: 1.5rem; margin: 0.3rem 0 0 0;">
          <li style="font-size: 18px; margin-bottom: 0.3rem; line-height: 1.5;">Needs common infrastructure</li>
          <li style="font-size: 18px; margin-bottom: 0.3rem; line-height: 1.5;">Fewer analysis options than pooling</li>
        </ul>
      </li>
    </ul>
  </div>
</div>


---
layout: content
heading: Analysing multiple datasets
subheading: Comparing the options
---

| | Data transfer | Share script | Federated analysis |
|---|:-:|:-:|:-:|
| Data stays at source | <carbon-close style="color: #D9534F" /> | <carbon-checkmark style="color: #0097A7" /> | <carbon-checkmark style="color: #0097A7" /> |
| Data owners keep control | <carbon-close style="color: #D9534F" /> | <carbon-checkmark style="color: #0097A7" /> | <carbon-checkmark style="color: #0097A7" /> |
| One pooled analysis | <carbon-checkmark style="color: #0097A7" /> | <carbon-close style="color: #D9534F" /> two-stage only | <carbon-checkmark style="color: #0097A7" /> |
| No shared infrastructure needed | <carbon-checkmark style="color: #0097A7" /> | <carbon-checkmark style="color: #0097A7" /> | <carbon-close style="color: #D9534F" /> |
| Full range of analysis methods | <carbon-checkmark style="color: #0097A7" /> | <carbon-close style="color: #D9534F" /> | <carbon-subtract style="color: #B9852A" /> fewer than pooling |
