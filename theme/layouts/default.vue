<script setup>
const base = import.meta.env.BASE_URL
</script>

<template>
  <div class="slidev-layout default">
    <div class="default-content">
      <slot />
    </div>
    <div class="logo-bar">
      <img :src="`${base}molgenis-logo.png`" class="slide-logo" />
    </div>
  </div>
</template>

<style scoped>
.default {
  padding: 2.5rem 3rem;
  display: flex;
  flex-direction: column;
  height: 100%;
}

.default-content {
  flex: 1;
}

.logo-bar {
  display: flex;
  justify-content: flex-end;
  align-items: flex-end;
}

.slide-logo {
  height: 28px;
  opacity: 0.8;
}
</style>
