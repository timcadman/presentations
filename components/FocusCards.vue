<script setup>
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'

const props = defineProps({
  // [{ title, body: [lines...], href? }]
  items: {
    type: Array,
    required: true,
  },
  columns: {
    type: Number,
    default: 2,
  },
})

const { $clicks } = useSlideContext()

const rows = computed(() => Math.ceil(props.items.length / props.columns))
const activeIndex = computed(() => Math.min($clicks.value, props.items.length - 1))
</script>

<template>
  <div
    class="fc-grid"
    :style="{ gridTemplateColumns: `repeat(${columns}, 1fr)`, gridTemplateRows: `repeat(${rows}, 1fr)` }"
  >
    <div
      v-for="(item, i) in items"
      :key="i"
      class="fc-card"
      :class="{ 'fc-active': i === activeIndex }"
    >
      <h3>{{ item.title }}</h3>
      <p v-for="(line, j) in item.body" :key="j" v-html="line"></p>
      <a v-if="item.href" :href="item.href" target="_blank" rel="noopener" class="fc-link">{{ item.href }}</a>
    </div>
  </div>
</template>

<style scoped>
.fc-grid {
  display: grid;
  gap: 0.7rem;
  height: 100%;
}

.fc-card {
  border: 2px solid #ddd;
  border-left: 5px solid var(--slidev-theme-primary);
  border-radius: 10px;
  padding: 0.7rem 1rem;
  background: rgba(66, 133, 244, 0.05);
  display: flex;
  flex-direction: column;
  justify-content: center;
  overflow: hidden;
  opacity: 0.28;
  filter: grayscale(85%);
  transition: opacity 0.4s ease, filter 0.4s ease, box-shadow 0.4s ease;
}

.fc-card.fc-active {
  opacity: 1;
  filter: grayscale(0%);
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.10);
}

.fc-card h3 {
  margin: 0 0 0.35rem 0;
  font-family: var(--font-subtitle);
  font-size: 1rem;
  font-weight: 600;
  color: var(--slidev-theme-primary);
}

.fc-card p {
  margin: 0 0 0.25rem 0;
  font-size: 14px;
  line-height: 1.45;
}

.fc-card p:last-child {
  margin-bottom: 0;
}

.fc-link {
  font-size: 13px;
  color: var(--slidev-theme-accent);
  word-break: break-all;
}
</style>
