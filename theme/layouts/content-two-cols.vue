<script setup>
defineProps({
  heading: {
    type: String,
    default: '',
  },
  leftHeading: {
    type: String,
    default: '',
  },
  rightHeading: {
    type: String,
    default: '',
  },
  // reveal the whole right column (heading + content) on the next click
  rightReveal: {
    type: Boolean,
    default: false,
  },
})

const base = import.meta.env.BASE_URL
</script>

<template>
  <div class="slidev-layout content-two-cols">
    <div class="slide-header">
      <h1>{{ heading }}</h1>
    </div>
    <div class="cols-row">
      <div class="col">
        <div v-if="leftHeading" class="col-heading">{{ leftHeading }}</div>
        <div class="slide-body"><slot name="left" /></div>
      </div>
      <div class="col">
        <div v-if="rightReveal" v-click>
          <div v-if="rightHeading" class="col-heading">{{ rightHeading }}</div>
          <div class="slide-body"><slot name="right" /></div>
        </div>
        <template v-else>
          <div v-if="rightHeading" class="col-heading">{{ rightHeading }}</div>
          <div class="slide-body"><slot name="right" /></div>
        </template>
      </div>
    </div>
    <div class="logo-bar">
      <img :src="`${base}molgenis-logo.png`" class="slide-logo" />
    </div>
  </div>
</template>

<style scoped>
.content-two-cols {
  display: flex;
  flex-direction: column;
  padding: 4.5rem 5rem 2rem 5rem;
  height: 100%;
}

.slide-header {
  min-height: 7.25rem;
  margin-bottom: 1.5rem;
  padding-top: 0.75rem;
  position: relative;
}

.slide-header::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 33%;
  height: 3px;
  background-color: var(--slidev-theme-primary);
}

.slide-header h1 {
  font-family: var(--font-title);
  font-size: 55px;
  font-weight: 400;
  color: var(--slidev-theme-primary);
  margin: 0;
  line-height: 1.2;
}

.cols-row {
  flex: 1;
  display: flex;
  gap: 3.5rem;
  min-height: 0;
}

.col {
  flex: 1;
  min-width: 0;
}

.col-heading {
  font-family: var(--font-subtitle);
  font-size: 25px;
  font-weight: 600;
  color: var(--slidev-theme-primary);
  margin-bottom: 0.75rem;
}

.slide-body :deep(ul),
.slide-body :deep(ol) {
  padding-left: 1.5rem;
  margin: 0;
}

.slide-body :deep(li) {
  font-size: 18px;
  margin-bottom: 0.5rem;
  line-height: 1.5;
}

.logo-bar {
  position: absolute;
  bottom: 1rem;
  right: 1.5rem;
}

.slide-logo {
  height: 36px;
  opacity: 0.8;
}
</style>
