<script setup>
const rows = [
  {
    gap: 'No OIDC login to nodes',
    addition: 'OIDC authentication via institutional login\nand token routing',
  },
  {
    gap: 'No per-user, per-project data access',
    addition: 'Control access to data based on roles',
  },
  {
    gap: 'App approval not open source',
    addition: 'Whitelist apps on Armadillo',
  },
]
</script>

<template>
  <div class="fg-grid">
    <div class="fg-heading" style="grid-column: 1; color: #B9852A;">Gaps to address</div>
    <div class="fg-heading" style="grid-column: 3;">What we add in Armadillo</div>

    <template v-for="(row, i) in rows" :key="row.gap">
      <div v-click="2 * i + 1" class="fg-card fg-gap" :style="{ gridRow: i + 2 }">{{ row.gap }}</div>
      <div v-click="2 * i + 2" class="fg-arrow" :style="{ gridRow: i + 2 }">
        <span class="fg-line"></span><span class="fg-arrowhead"></span>
      </div>
      <div v-click="2 * i + 2" class="fg-card fg-addition" :style="{ gridRow: i + 2 }">{{ row.addition }}</div>
    </template>
  </div>
</template>

<style scoped>
.fg-grid {
  display: grid;
  grid-template-columns: 340px 44px 380px;
  grid-template-rows: 22px;
  grid-auto-rows: 62px;
  column-gap: 10px;
  row-gap: 12px;
  justify-content: center;
  align-items: stretch;
}
.fg-heading {
  grid-row: 1;
  font-family: var(--font-subtitle);
  font-size: 15px;
  font-weight: 600;
  color: var(--slidev-theme-heading);
}
.fg-card {
  display: flex;
  align-items: center;
  padding: 0 12px;
  border-left: 5px solid;
  border-radius: 8px;
  font-size: 15px;
  line-height: 1.3;
  white-space: pre-line;
  color: var(--slidev-theme-text);
}
.fg-gap {
  grid-column: 1;
  border-left-color: #E6B96A;
  background: color-mix(in srgb, #E6B96A 14%, white);
}
.fg-addition {
  grid-column: 3;
  border-left-color: var(--slidev-theme-primary);
  background: color-mix(in srgb, var(--slidev-theme-primary) 9%, white);
}
.fg-arrow {
  grid-column: 2;
  display: flex;
  align-items: center;
}
.fg-line {
  flex: 1;
  height: 2px;
  background: var(--slidev-theme-primary);
}
.fg-arrowhead {
  width: 0;
  height: 0;
  border-top: 6px solid transparent;
  border-bottom: 6px solid transparent;
  border-left: 9px solid var(--slidev-theme-primary);
}
</style>
