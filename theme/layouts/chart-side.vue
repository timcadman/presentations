<script setup>
defineProps({
  heading: {
    type: String,
    default: '',
  },
  // width of the side panel as a % of the slide; chart takes the rest
  sideWidth: {
    type: String,
    default: '24',
  },
  // which side the panel sits on: 'left' | 'right'
  sidePosition: {
    type: String,
    default: 'left',
  },
})

const base = import.meta.env.BASE_URL
</script>

<template>
  <div class="slidev-layout chart-side">
    <div class="ch-header">
      <h1>{{ heading }}</h1>
    </div>
    <div class="cs-body" :style="{ flexDirection: sidePosition === 'right' ? 'row-reverse' : 'row' }">
      <div class="cs-side" :style="{ flexBasis: sideWidth + '%' }">
        <slot name="side" />
      </div>
      <div class="cs-main">
        <slot />
      </div>
    </div>
    <div class="logo-bar">
      <img :src="`${base}molgenis-logo.png`" class="slide-logo" />
    </div>
  </div>
</template>

<style scoped>
.chart-side {
  display: flex;
  flex-direction: column;
  padding: 2.5rem 3.5rem 1.25rem 3.5rem;
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

.cs-body {
  flex: 1;
  min-height: 0;
  display: flex;
  gap: 2rem;
}

.cs-side {
  flex-grow: 0;
  flex-shrink: 0;
  min-width: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.cs-main {
  flex: 1;
  min-width: 0;
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
