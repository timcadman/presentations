<template>
  <div class="flow-grid">
    <div class="lane-heading dm" style="grid-column: 1; grid-row: 1;">Data manager</div>
    <div class="lane-heading res" style="grid-column: 3; grid-row: 1;">Researcher</div>

    <div v-click="1" class="step dm" style="grid-column: 1; grid-row: 2;">Install supernode &amp; superexec containers</div>
    <div v-click="2" class="v-connector dm" style="grid-column: 1; grid-row: 3;"></div>
    <div v-click="2" class="step dm" style="grid-column: 1; grid-row: 4;">Give user permissions</div>
    <div v-click="4" class="v-connector dm" style="grid-column: 1; grid-row: 5;"></div>
    <div v-click="4" class="step dm" style="grid-column: 1; grid-row: 6;">Download app from appstore</div>
    <div v-click="5" class="v-connector dm" style="grid-column: 1; grid-row: 7;"></div>
    <div v-click="5" class="step dm" style="grid-column: 1; grid-row: 8;">Review app</div>
    <div v-click="6" class="v-connector dm" style="grid-column: 1; grid-row: 9;"></div>
    <div v-click="6" class="step dm" style="grid-column: 1; grid-row: 10;">Whitelist app</div>

    <div v-click="1" class="step res" style="grid-column: 3; grid-row: 2;">Write app</div>
    <div v-click="3" class="v-connector res" style="grid-column: 3; grid-row: 3 / 6;"></div>
    <div v-click="3" class="step res" style="grid-column: 3; grid-row: 6;">Upload app to appstore</div>
    <div v-click="7" class="v-connector res" style="grid-column: 3; grid-row: 7 / 10;"></div>
    <div v-click="7" class="step res" style="grid-column: 3; grid-row: 10;">Fetch access token</div>
    <div v-click="8" class="v-connector res" style="grid-column: 3; grid-row: 11;"></div>
    <div v-click="8" class="step res" style="grid-column: 3; grid-row: 12;">Run app</div>
    <div v-click="9" class="v-connector res" style="grid-column: 3; grid-row: 13;"></div>
    <div v-click="9" class="step res" style="grid-column: 3; grid-row: 14;">Push data into container</div>
    <div v-click="10" class="v-connector res" style="grid-column: 3; grid-row: 15;"></div>
    <div v-click="10" class="step res" style="grid-column: 3; grid-row: 16;">Return results</div>

    <div v-click="4" class="h-connector" style="grid-column: 2; grid-row: 6;">
      <span class="h-arrowhead left"></span>
      <span class="h-line"></span>
      <span class="h-label">enables</span>
      <span class="h-line"></span>
    </div>

    <div v-click="7" class="h-connector" style="grid-column: 2; grid-row: 10;">
      <span class="h-line"></span>
      <span class="h-label">enables</span>
      <span class="h-line"></span>
      <span class="h-arrowhead right"></span>
    </div>
  </div>
</template>

<style scoped>
.flow-grid {
  display: grid;
  grid-template-columns: 1fr 90px 1fr;
  /* connector rows are 1fr (not auto) so they absorb whatever space is left
     after the heading/step rows take what they need — the diagram always
     fills exactly height:100% of the slide body, never overflows it. */
  grid-template-rows: auto auto minmax(6px, 1fr) auto minmax(6px, 1fr) auto minmax(6px, 1fr) auto minmax(6px, 1fr) auto minmax(6px, 1fr) auto minmax(6px, 1fr) auto minmax(6px, 1fr) auto;
  row-gap: 0;
  column-gap: 0;
  align-items: center;
  height: 100%;
}

.lane-heading {
  font-family: var(--font-subtitle);
  font-size: 17px;
  font-weight: 600;
  text-align: center;
  margin-bottom: 0.4rem;
}
.lane-heading.dm { color: #1E3A5F; }
.lane-heading.res { color: #0097A7; }

.step {
  border-radius: 8px;
  border: 2px solid;
  padding: 0.4rem 0.8rem;
  font-size: 13px;
  font-weight: 500;
  text-align: center;
  line-height: 1.3;
  transition: opacity 0.4s ease, filter 0.4s ease;
}
.step.dm {
  border-color: #1E3A5F;
  background: rgba(30, 58, 95, 0.06);
  color: #1E3A5F;
}
.step.res {
  border-color: #0097A7;
  background: rgba(0, 151, 167, 0.06);
  color: #045863;
}

.v-connector {
  justify-self: center;
  width: 2px;
  height: 100%;
  min-height: 0.6rem;
  position: relative;
  transition: opacity 0.4s ease, filter 0.4s ease;
}
.v-connector.dm { background: #1E3A5F; }
.v-connector.res { background: #0097A7; }
.v-connector::after {
  content: '';
  position: absolute;
  left: 50%;
  bottom: -1px;
  transform: translateX(-50%);
  width: 0;
  height: 0;
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
  border-top: 7px solid currentColor;
}
.v-connector.dm::after { color: #1E3A5F; }
.v-connector.res::after { color: #0097A7; }

.h-connector {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 2px;
  position: relative;
  color: #555;
  transition: opacity 0.4s ease, filter 0.4s ease;
}
.h-line {
  flex: 1;
  height: 2px;
  background: #9AA0A6;
}
.h-label {
  font-size: 11px;
  color: #555;
  padding: 0 0.4rem;
  white-space: nowrap;
}
.h-arrowhead {
  width: 0;
  height: 0;
  border-top: 6px solid transparent;
  border-bottom: 6px solid transparent;
  flex: none;
}
.h-arrowhead.left { border-right: 9px solid #9AA0A6; }
.h-arrowhead.right { border-left: 9px solid #9AA0A6; }

/* Reveal-in-place: rows start dim/greyed (same values as fq-card in
   uncan-demo/slides.md) and clear to full colour on their click, instead of
   Slidev's default fully-hidden v-click state — two classes beats the
   library's single-class !important rule. */
.step.slidev-vclick-hidden,
.v-connector.slidev-vclick-hidden,
.h-connector.slidev-vclick-hidden {
  opacity: 0.28 !important;
  filter: grayscale(85%);
  pointer-events: none;
}
</style>
