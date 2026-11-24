<script setup>
// A timeline of numbered steps, vertical by default or a row with `horizontal`.
// Each step is done (blue), current (gold) or todo (grey).
//
//   <Timeline :items="[
//     { text: 'Test environment installed', status: 'done' },
//     { text: 'Awaiting approvals', status: 'current' },
//     { text: 'Analysis', status: 'todo' },
//   ]" />
//   <Timeline horizontal :items="[...]" />
defineProps({
  items: {
    type: Array,
    required: true,
  },
  horizontal: {
    type: Boolean,
    default: false,
  },
})
</script>

<template>
  <ol class="tl" :class="{ h: horizontal }" :style="horizontal ? { gridTemplateColumns: `repeat(${items.length}, 1fr)` } : {}">
    <li v-for="(item, i) in items" :key="item.text" :class="item.status || 'todo'">
      <span class="tl-n">{{ i + 1 }}</span>
      {{ item.text }}
    </li>
  </ol>
</template>

<style scoped>
.tl { list-style: none; margin: 0; padding: 0; position: relative; }
.tl::before { content: ''; position: absolute; left: 0.9rem; top: 0.9rem; bottom: 0.9rem; width: 2px; background: #e4e4e4; }
.tl li { position: relative; display: flex; align-items: center; gap: 1rem; margin-bottom: 0.9rem; font-size: 18px; color: var(--c-grey); }
.tl-n { position: relative; display: inline-flex; align-items: center; justify-content: center; flex: none; width: 1.8rem; height: 1.8rem; box-sizing: border-box; border-radius: 50%; border: 2px solid var(--c-grey); background: #fff; font-family: var(--font-subtitle); font-size: 15px; font-weight: 600; }
.tl li.done { color: var(--c-text); }
.tl li.done .tl-n { background: var(--c-blue); border-color: var(--c-blue); color: #fff; }
.tl li.current { color: var(--c-text); font-weight: 600; }
.tl li.current .tl-n { background: var(--c-gold-dark); border-color: var(--c-gold-dark); color: #fff; }
.tl.h { display: grid; }
.tl.h::before { left: 0.9rem; right: 0.9rem; top: 0.9rem; bottom: auto; width: auto; height: 2px; }
.tl.h li { flex-direction: column; align-items: flex-start; gap: 0.6rem; margin-bottom: 0; padding-right: 0.8rem; font-size: 15px; line-height: 1.3; }
</style>
