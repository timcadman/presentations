<template>
  <div class="slidev-layout section">
    <div class="section-content">
      <slot />
    </div>
  </div>
</template>

<style scoped>
.section {
  background-color: #F7D38C;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 4rem 5rem;
  height: 100%;
}

.section-content {
  text-align: center;
  width: 100%;
}

.section :deep(h1) {
  font-family: var(--font-title);
  font-size: 55px;
  font-weight: 400;
  color: var(--slidev-theme-primary);
  margin-bottom: 0.5rem;
  line-height: 1.2;
}

.section :deep(p) {
  font-family: var(--font-subtitle);
  font-size: 25px;
  color: var(--slidev-theme-primary);
  font-weight: 400;
}
</style>
