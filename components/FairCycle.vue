<script setup>
import { computed, useId } from 'vue'

const props = defineProps({
  // 0 shows the whole cycle; 1-4 highlights F, A, I or R and dims the rest.
  // Pass $clicks to step through them.
  focus: {
    type: Number,
    default: 0,
  },
})

// every instance needs its own marker id: all slides share one DOM, so a fixed
// id would leave the second diagram pointing at a def that unmounts with the first
const arrow = `fair-arrow-${useId()}`

const BOXES = [
  { key: 'f', letter: 'F', label: 'Findable' },
  { key: 'a', letter: 'A', label: 'Accessible' },
  { key: 'i', letter: 'I', label: 'Interoperable' },
  { key: 'r', letter: 'R', label: 'Reusable' },
]

const boxes = computed(() => BOXES.map((b, i) => ({
  ...b,
  dim: props.focus > 0 && props.focus !== i + 1,
})))
</script>

<template>
  <div class="fair-diagram">
    <svg class="fair-arrows" viewBox="30 30 420 360" preserveAspectRatio="none"
         role="img" aria-label="FAIR cycle: Findable, Accessible, Interoperable, Reusable">
      <defs>
        <marker :id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7"
                orient="auto-start-reverse">
          <path d="M0,0 L10,5 L0,10 z" fill="#9AA0A6" />
        </marker>
      </defs>
      <g fill="none" stroke="#9AA0A6" stroke-width="3" :marker-end="`url(#${arrow})`">
        <path d="M185.2,97.7 A125,125 0 0 1 294.8,97.7" />
        <path d="M352.3,155.2 A125,125 0 0 1 352.3,264.8" />
        <path d="M294.8,322.3 A125,125 0 0 1 185.2,322.3" />
        <path d="M127.7,264.8 A125,125 0 0 1 127.7,155.2" />
      </g>
    </svg>
    <div v-for="b in boxes" :key="b.key" class="fair-box" :class="[b.key, { dim: b.dim }]">
      <span class="l">{{ b.letter }}</span>
      <span class="n">{{ b.label }}</span>
    </div>
  </div>
</template>
