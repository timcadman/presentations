<template>
  <div class="order-grid">
    <div class="col-heading" style="grid-column: 2; grid-row: 1;">molgenis-service-armadillo</div>
    <div class="col-heading" style="grid-column: 3; grid-row: 1;">molgenis-flwr-armadillo</div>

    <div v-click="1" class="wave" style="grid-column: 1; grid-row: 2;">1</div>
    <div v-click="1" class="cell" style="grid-column: 2; grid-row: 2;">
      <a class="pr-box armadillo" href="https://github.com/molgenis/molgenis-service-armadillo/tree/feat/%232053-ui-for-containers" target="_blank">feat #2053 — container UI<span class="pr-src">closed PR #933, 82 commits behind: revive first</span></a>
      <a class="pr-box armadillo" href="https://github.com/molgenis/molgenis-service-armadillo/pull/985" target="_blank">PR #985 — container classes &amp; Docker service<span class="pr-src">everything Armadillo-side stacks on this</span></a>
    </div>
    <div v-click="1" class="cell" style="grid-column: 3; grid-row: 2;">
      <a class="pr-box py" href="https://github.com/molgenis/molgenis-flwr-armadillo/pull/5" target="_blank">PR #5 — auth CLI &amp; token routing<span class="pr-src">everything else Python-side stacks on this</span></a>
    </div>

    <div v-click="2" class="wave" style="grid-column: 1; grid-row: 3;">2</div>
    <div v-click="2" class="cell" style="grid-column: 2; grid-row: 3;">
      <a class="pr-box armadillo" href="https://github.com/molgenis/molgenis-service-armadillo/pull/986" target="_blank">PR #986 — push-data endpoint<span class="pr-src">stacked on #985</span></a>
    </div>
    <div v-click="2" class="cell" style="grid-column: 3; grid-row: 3;">
      <a class="pr-box py" href="https://github.com/molgenis/molgenis-flwr-armadillo/pull/10" target="_blank">PR #10 — app load data helper<span class="pr-src">stacked on #5; client of #986</span></a>
    </div>

    <div v-click="3" class="wave" style="grid-column: 1; grid-row: 4;">3</div>
    <div v-click="3" class="cell" style="grid-column: 2; grid-row: 4;">
      <a class="pr-box armadillo" href="https://github.com/molgenis/molgenis-service-armadillo/pull/1066" target="_blank">PR #1066 — whitelist config &amp; endpoint<span class="pr-src">stacked on #986</span></a>
    </div>
    <div v-click="3" class="cell" style="grid-column: 3; grid-row: 4;">
      <a class="pr-box py" href="https://github.com/molgenis/molgenis-flwr-armadillo/pull/11" target="_blank">PR #11 — custom superexec image<span class="pr-src">independent; enforces #1066's whitelist</span></a>
      <a class="pr-box py" href="https://github.com/molgenis/molgenis-flwr-armadillo/pull/12" target="_blank">PR #12 — approve-app CLI<span class="pr-src">stacked on #5; client of #1066</span></a>
    </div>

    <div v-click="4" class="wave" style="grid-column: 1; grid-row: 5;">4</div>
    <div v-click="4" class="cell" style="grid-column: 3; grid-row: 5;">
      <a class="pr-box py" href="https://github.com/molgenis/molgenis-flwr-armadillo/pull/6" target="_blank">PR #6 — API helpers &amp; resources CLI<span class="pr-src">stacked on #5</span></a>
    </div>

    <div v-click="5" class="wave" style="grid-column: 1; grid-row: 6;">then</div>
    <div v-click="5" class="cell" style="grid-column: 2; grid-row: 6;">
      <div class="pr-box armadillo pending">Armadillo docs<span class="pr-src">to be done</span></div>
    </div>
    <div v-click="5" class="cell" style="grid-column: 3; grid-row: 6;">
      <a class="pr-box py pending" href="https://github.com/molgenis/molgenis-flwr-armadillo/pull/4" target="_blank">PR #4 — example app<span class="pr-src">rebased onto #10, imports the package</span></a>
      <a class="pr-box py pending" href="https://github.com/molgenis/molgenis-flwr-armadillo/tree/feat/dp" target="_blank">feat — DP wrappers<span class="pr-src">feat/dp, unfinished</span></a>
      <div class="pr-box py pending">Python docs<span class="pr-src">to be done</span></div>
    </div>
  </div>
</template>

<style scoped>
.order-grid {
  display: grid;
  grid-template-columns: 3rem 1fr 1fr;
  grid-template-rows: auto repeat(5, auto);
  row-gap: 0.6rem;
  column-gap: 0.8rem;
  align-items: stretch;
  height: 100%;
  align-content: start;
}

.col-heading {
  font-family: var(--font-subtitle);
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: #9AA0A6;
}

.wave {
  font-family: var(--font-subtitle);
  font-size: 18px;
  font-weight: 600;
  color: #9AA0A6;
  display: flex;
  align-items: center;
  transition: opacity 0.4s ease, filter 0.4s ease;
}

.cell {
  display: flex;
  gap: 0.35rem;
  transition: opacity 0.4s ease, filter 0.4s ease;
}
.cell > .pr-box {
  flex: 1 1 0;
  min-width: 0;
}

.pr-box {
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 4rem;
  box-sizing: border-box;
  overflow: hidden;
  border-radius: 8px;
  border: 2px solid #9AA0A6;
  padding: 0.3rem 0.6rem;
  font-size: 11px;
  font-weight: 600;
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
.pr-src {
  font-size: 9px;
  font-weight: 400;
  color: #9AA0A6;
  margin-top: 0.1rem;
}

.wave.slidev-vclick-hidden,
.cell.slidev-vclick-hidden {
  opacity: 0.28 !important;
  filter: grayscale(85%);
  pointer-events: none;
}
</style>
