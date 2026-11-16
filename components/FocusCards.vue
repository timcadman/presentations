<script setup>
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'

const props = defineProps({
  // [{ title, body: [lines...], color?, h?, href? }]
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

const cardStyle = (item) => ({
  ...(item.color ? { '--c': item.color } : {}),
  ...(item.h ? { '--h': item.h } : {}),
})
</script>

<template>
  <div
    class="fq-grid"
    :style="{ gridTemplateColumns: `repeat(${columns}, 1fr)`, gridTemplateRows: `repeat(${rows}, 1fr)` }"
  >
    <div
      v-for="(item, i) in items"
      :key="i"
      class="tint-card"
      :class="i === activeIndex ? 'active' : 'dimmed'"
      :style="cardStyle(item)"
    >
      <h3>{{ item.title }}</h3>
      <p v-for="(line, j) in item.body" :key="j" v-html="line"></p>
      <a v-if="item.href" :href="item.href" target="_blank" rel="noopener" class="fc-link">{{ item.href }}</a>
    </div>
  </div>
</template>

<style scoped>
.fc-link {
  font-size: 13px;
  color: var(--slidev-theme-accent);
  word-break: break-all;
}
</style>
