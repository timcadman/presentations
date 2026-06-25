<script setup>
defineProps({
  caption: {
    type: String,
    default: 'chart pending',
  },
})
</script>

<template>
  <div class="ph-box">
    <div class="ph-inner">
      <div class="ph-icon">▦</div>
      <div class="ph-caption">chart pending: <span>{{ caption }}</span></div>
    </div>
  </div>
</template>

<style scoped>
.ph-box {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  min-height: 220px;
}
.ph-inner {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.75rem;
  width: 80%;
  padding: 2.5rem 2rem;
  border: 2px dashed var(--slidev-theme-primary);
  border-radius: 10px;
  background: repeating-linear-gradient(
    45deg,
    rgba(66, 133, 244, 0.04),
    rgba(66, 133, 244, 0.04) 10px,
    rgba(66, 133, 244, 0.08) 10px,
    rgba(66, 133, 244, 0.08) 20px
  );
}
.ph-icon {
  font-size: 34px;
  color: var(--slidev-theme-primary);
  opacity: 0.6;
}
.ph-caption {
  font-family: var(--font-subtitle);
  font-size: 15px;
  color: #777;
  text-align: center;
}
.ph-caption span {
  color: var(--slidev-theme-primary);
}
</style>
