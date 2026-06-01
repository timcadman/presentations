<script setup>
defineProps({
  heading: {
    type: String,
    default: '',
  },
  subheading: {
    type: String,
    default: '',
  },
  image: {
    type: String,
    default: '',
  },
})
</script>

<template>
  <div class="slidev-layout content-img-left">
    <div class="image-area">
      <img v-if="image" :src="image" class="slide-image" />
    </div>
    <div class="text-area">
      <div class="slide-header">
        <h1>{{ heading }}</h1>
        <h2 v-if="subheading">{{ subheading }}</h2>
      </div>
      <div class="slide-body">
        <slot />
      </div>
      <div class="logo-bar">
        <img src="/molgenis-logo.png" class="slide-logo" />
      </div>
    </div>
  </div>
</template>

<style scoped>
.content-img-left {
  display: flex;
  height: 100%;
}

.image-area {
  width: 40%;
  height: 100%;
  overflow: hidden;
}

.slide-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.text-area {
  width: 55%;
  padding: 4.5rem 5rem 2rem 3rem;
  margin-left: auto;
  display: flex;
  flex-direction: column;
}

.slide-header {
  margin-bottom: 1.5rem;
  padding-top: 0.75rem;
  position: relative;
}

.slide-header::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 60%;
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

.slide-header h2 {
  font-family: var(--font-subtitle);
  font-size: 25px;
  font-weight: 400;
  color: var(--slidev-theme-primary);
  margin: 0.25rem 0 0 0;
}

.slide-body {
  flex: 1;
}

.slide-body :deep(ul) {
  padding-left: 1.5rem;
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
