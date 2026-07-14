<script setup>
defineProps({
  heading: {
    type: String,
    default: '',
  },
})

const base = import.meta.env.BASE_URL
</script>

<template>
  <div class="slidev-layout chart-full">
    <div class="ch-header">
      <h1>{{ heading }}</h1>
    </div>
    <div class="ch-body">
      <slot />
    </div>
    <div class="logo-bar">
      <img :src="`${base}molgenis-logo.png`" class="slide-logo" />
    </div>
  </div>
</template>

<style scoped>
.chart-full {
  display: flex;
  flex-direction: column;
  /* compact padding so the chart gets the vertical space */
  /* bottom padding clears the logo (~2.75rem) so content never overlaps it */
  padding: 2.5rem 3.5rem 3rem 3.5rem;
  height: 100%;
}

.ch-header {
  position: relative;
  padding-top: 0.5rem;
  margin-bottom: 0.75rem;
}

.ch-header::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 33%;
  height: 3px;
  background-color: var(--slidev-theme-primary);
}

.ch-header h1 {
  font-family: var(--font-title);
  font-size: 40px;
  font-weight: 400;
  color: var(--slidev-theme-primary);
  margin: 0;
  line-height: 1.2;
}

.ch-body {
  flex: 1;
  min-height: 0;
}

.logo-bar {
  position: absolute;
  bottom: 0.75rem;
  right: 1.5rem;
}

.slide-logo {
  height: 32px;
  opacity: 0.8;
}
</style>
