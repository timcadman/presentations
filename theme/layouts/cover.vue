<template>
  <div class="slidev-layout cover">
    <div class="cover-content">
      <slot />
    </div>
  </div>
</template>

<style scoped>
.cover {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 4rem 5rem;
  height: 100%;
}

.cover-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.cover :deep(h1) {
  font-family: var(--font-title);
  font-size: 55px;
  font-weight: 400;
  margin-bottom: 0.5rem;
  line-height: 1.2;
}

.cover :deep(p:first-of-type:not(.author-info p)) {
  font-family: var(--font-subtitle);
  font-size: 25px;
  color: var(--slidev-theme-primary);
  margin-bottom: 2rem;
}

.cover :deep(.author-info) {
  margin-top: 1.5rem;
  border-top: 2px solid #ccc;
  padding-top: 1rem;
}

.cover :deep(.author-info p) {
  margin: 0.1rem 0;
  font-size: 1rem;
  color: #333;
}

.cover :deep(.title-logos) {
  position: absolute;
  bottom: 3rem;
  left: 5rem;
  display: flex;
  align-items: center;
  gap: 2rem;
}

.cover :deep(.logo-umcg) {
  height: 28px;
}

.cover :deep(.logo-molgenis) {
  height: 40px;
}
</style>
