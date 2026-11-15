<script setup>
defineProps({
  question: {
    type: String,
    default: '',
  },
  // optional line above the question; leave unset when the slide's subheading
  // already says it
  label: {
    type: String,
    default: '',
  },
  // optional citation, rendered small and grey at the foot of the slide
  reference: {
    type: String,
    default: '',
  },
})
</script>

<template>
  <div class="research-question">
    <div class="rq-body">
      <p class="rq-text"><template v-if="label">{{ label }}<br /></template><span class="rq-q">"{{ question }}"</span></p>
    </div>
    <p v-if="reference" class="rq-ref">{{ reference }}</p>
  </div>
</template>

<style scoped>
.research-question {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.rq-body {
  flex: 1;
  min-height: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.rq-text {
  margin: 0;
  max-width: 640px;
  text-align: center;
  font-size: 28px;
  font-weight: 500;
  line-height: 1.5;
  color: var(--slidev-theme-primary);
}

.rq-q {
  color: #9aa0a6;
}

.rq-ref {
  margin: 0;
  font-size: 12px;
  color: #9aa0a6;
}
</style>
