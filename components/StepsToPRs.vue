<template>
  <div class="map-grid">
    <div class="col-heading" style="grid-column: 1; grid-row: 1;">Step</div>
    <div class="col-heading" style="grid-column: 3; grid-row: 1;">Implemented by</div>

    <div v-click="1" class="step dm" style="grid-column: 1; grid-row: 2;">Install supernode &amp; superexec containers</div>
    <div v-click="2" class="step dm" style="grid-column: 1; grid-row: 4;">Review &amp; whitelist app</div>
    <div v-click="3" class="step res" style="grid-column: 1; grid-row: 6;">Fetch access token &amp; run app</div>
    <div v-click="4" class="step res" style="grid-column: 1; grid-row: 8;">Push data into container</div>
    <div v-click="5" class="step dm" style="grid-column: 1; grid-row: 10;">Data manager tools</div>
    <div v-click="6" class="step res" style="grid-column: 1; grid-row: 12;">Differential privacy</div>
    <div v-click="7" class="step dm" style="grid-column: 1; grid-row: 14;">Documentation</div>
    <div v-click="8" class="step dm" style="grid-column: 1; grid-row: 16;">End-to-end release test</div>

    <div v-click="1" class="h-connector" style="grid-column: 2; grid-row: 2;">
      <span class="h-line"></span><span class="h-arrowhead right"></span>
    </div>
    <div v-click="2" class="h-connector" style="grid-column: 2; grid-row: 4;">
      <span class="h-line"></span><span class="h-arrowhead right"></span>
    </div>
    <div v-click="3" class="h-connector" style="grid-column: 2; grid-row: 6;">
      <span class="h-line"></span><span class="h-arrowhead right"></span>
    </div>
    <div v-click="4" class="h-connector" style="grid-column: 2; grid-row: 8;">
      <span class="h-line"></span><span class="h-arrowhead right"></span>
    </div>
    <div v-click="5" class="h-connector" style="grid-column: 2; grid-row: 10;">
      <span class="h-line"></span><span class="h-arrowhead right"></span>
    </div>
    <div v-click="6" class="h-connector" style="grid-column: 2; grid-row: 12;">
      <span class="h-line"></span><span class="h-arrowhead right"></span>
    </div>
    <div v-click="7" class="h-connector" style="grid-column: 2; grid-row: 14;">
      <span class="h-line"></span><span class="h-arrowhead right"></span>
    </div>
    <div v-click="8" class="h-connector" style="grid-column: 2; grid-row: 16;">
      <span class="h-line"></span><span class="h-arrowhead right"></span>
    </div>

    <div v-click="1" class="pr-stack" style="grid-column: 3; grid-row: 2;">
      <a class="pr-box armadillo" href="https://github.com/molgenis/molgenis-service-armadillo/pull/985" target="_blank"><span class="pr-title">PR #985 — Flower container classes &amp; Docker service integration <span class="pr-ready" title="Ready for review">&#10003;</span></span><span class="pr-src">molgenis-service-armadillo</span></a>
      <a class="pr-box armadillo" href="https://github.com/molgenis/molgenis-service-armadillo/tree/feat/%232053-ui-for-containers" target="_blank">feat #2053 — container UI<span class="pr-src">feat/#2053-ui-for-containers, molgenis-service-armadillo</span></a>
    </div>
    <div v-click="2" class="pr-stack" style="grid-column: 3; grid-row: 4;">
      <a class="pr-box armadillo" href="https://github.com/molgenis/molgenis-service-armadillo/pull/1066" target="_blank"><span class="pr-title">PR #1066 — whitelist config &amp; endpoint <span class="pr-ready" title="Ready for review">&#10003;</span></span><span class="pr-src">molgenis-service-armadillo</span></a>
      <a class="pr-box py" href="https://github.com/molgenis/molgenis-flwr-armadillo/pull/12" target="_blank">PR #12 — approve-app CLI (download, review, whitelist)<span class="pr-src">molgenis-flwr-armadillo</span></a>
      <a class="pr-box py" href="https://github.com/molgenis/molgenis-flwr-armadillo/pull/11" target="_blank">PR #11 — custom superexec image to check app against whitelist<span class="pr-src">molgenis-flwr-armadillo</span></a>
    </div>
    <div v-click="3" class="pr-stack" style="grid-column: 3; grid-row: 6;">
      <a class="pr-box py" href="https://github.com/molgenis/molgenis-flwr-armadillo/pull/5" target="_blank">PR #5 — Python auth CLI &amp; token routing<span class="pr-src">molgenis-flwr-armadillo</span></a>
    </div>
    <div v-click="4" class="pr-stack" style="grid-column: 3; grid-row: 8;">
      <a class="pr-box armadillo" href="https://github.com/molgenis/molgenis-service-armadillo/pull/986" target="_blank"><span class="pr-title">PR #986 — Flower push-data-to-container endpoint <span class="pr-ready" title="Ready for review">&#10003;</span></span><span class="pr-src">molgenis-service-armadillo</span></a>
      <a class="pr-box py" href="https://github.com/molgenis/molgenis-flwr-armadillo/pull/10" target="_blank">PR #10 — app load data helper<span class="pr-src">molgenis-flwr-armadillo</span></a>
    </div>
    <div v-click="5" class="pr-stack" style="grid-column: 3; grid-row: 10;">
      <a class="pr-box py" href="https://github.com/molgenis/molgenis-flwr-armadillo/pull/6" target="_blank">PR #6 — Armadillo API helpers &amp; resources CLI<span class="pr-src">molgenis-flwr-armadillo</span></a>
    </div>
    <div v-click="6" class="pr-stack" style="grid-column: 3; grid-row: 12;">
      <a class="pr-box py pending" href="https://github.com/molgenis/molgenis-flwr-armadillo/tree/feat/dp" target="_blank">feat — DP wrappers<span class="pr-src">feat/dp, molgenis-flwr-armadillo (unfinished)</span></a>
    </div>
    <div v-click="7" class="pr-stack" style="grid-column: 3; grid-row: 14;">
      <div class="pr-box armadillo pending">Armadillo docs<span class="pr-src">molgenis-service-armadillo (to be done)</span></div>
      <div class="pr-box py pending">Python docs<span class="pr-src">molgenis-flwr-armadillo (to be done)</span></div>
    </div>
    <div v-click="8" class="pr-stack" style="grid-column: 3; grid-row: 16;">
      <a class="pr-box py" href="https://github.com/molgenis/molgenis-flwr-armadillo/tree/test/fab-whitelist-staging" target="_blank">Release test branch<span class="pr-src">test/fab-whitelist-staging, molgenis-flwr-armadillo</span></a>
      <div class="pr-box py pending">Python release<span class="pr-src">molgenis-flwr-armadillo (PR pending)</span></div>
    </div>
  </div>
</template>

<style scoped>
.map-grid {
  display: grid;
  grid-template-columns: 150px 40px 1fr;
  /* same fit-to-height trick as AppStoreFlow: connector rows are 1fr so the
     diagram always fills height:100% instead of overflowing the slide. */
  grid-template-rows: auto auto minmax(4px, 1fr) auto minmax(4px, 1fr) auto minmax(4px, 1fr) auto minmax(4px, 1fr) auto minmax(4px, 1fr) auto minmax(4px, 1fr) auto minmax(4px, 1fr) auto;
  row-gap: 0;
  column-gap: 0;
  align-items: center;
  height: 100%;
}

.col-heading {
  font-family: var(--font-subtitle);
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: #9AA0A6;
  margin-bottom: 0.5rem;
}

.step {
  border-radius: 8px;
  border: 2px solid;
  padding: 0.3rem 0.6rem;
  font-size: 12px;
  font-weight: 500;
  line-height: 1.3;
  height: 2.5rem;
  box-sizing: border-box;
  display: flex;
  align-items: center;
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

.h-connector {
  display: flex;
  align-items: center;
  height: 2px;
  transition: opacity 0.4s ease, filter 0.4s ease;
}
.h-line {
  flex: 1;
  height: 2px;
  background: #9AA0A6;
}
.h-arrowhead {
  width: 0;
  height: 0;
  border-top: 6px solid transparent;
  border-bottom: 6px solid transparent;
  flex: none;
}
.h-arrowhead.right { border-left: 9px solid #9AA0A6; }

/* All PRs for one step share a single row; text wraps inside the boxes. */
.pr-stack {
  display: flex;
  gap: 0.35rem;
  transition: opacity 0.4s ease, filter 0.4s ease;
}
.pr-stack > .pr-box {
  flex: 1 1 0;
  min-width: 0;
}
.pr-stack > .pr-box:only-child {
  flex: 0 0 50%;
}

.pr-box {
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 2.5rem;
  box-sizing: border-box;
  overflow: hidden;
  border-radius: 8px;
  border: 2px solid #9AA0A6;
  background: rgba(154, 160, 166, 0.08);
  padding: 0.25rem 0.5rem;
  font-size: 10px;
  font-weight: 600;
  color: #0097A7;
  text-decoration: none;
  line-height: 1.3;
}
.pr-box.py {
  border-color: #E6B96A;
  background: rgba(230, 185, 106, 0.12);
  color: #B9852A;
}
.pr-box.armadillo {
  border-color: #4285F4;
  background: rgba(66, 133, 244, 0.06);
  color: #4285F4;
}
.pr-box.pending {
  border-style: dashed;
}
/* Repo is carried by the box colour; the source line doesn't fit eight rows. */
.pr-src {
  display: none;
}
.pr-title {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 0.3rem;
}
.pr-ready {
  color: #0097A7;
  font-weight: 700;
  flex: none;
}

/* Reveal-in-place, same values as AppStoreFlow/fq-card. */
.step.slidev-vclick-hidden,
.h-connector.slidev-vclick-hidden,
.pr-stack.slidev-vclick-hidden {
  opacity: 0.28 !important;
  filter: grayscale(85%);
  pointer-events: none;
}
</style>
