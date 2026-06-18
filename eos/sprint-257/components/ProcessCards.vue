<script setup>
import { computed } from 'vue'

const props = defineProps({
  // [{ steps: [{title, desc}], loop?: true, label?: string }]
  // Each group renders as one row of cards. A `loop` group is highlighted and
  // gets a "repeat" return arrow beneath it.
  groups: {
    type: Array,
    required: true,
  },
  // Current Slidev click count; pass `:clicks="$clicks"`. Cards reveal one per
  // click (card 1 shown immediately). Defaults high so all show when unused.
  clicks: {
    type: Number,
    default: 9999,
  },
})

// Flatten to assign a continuous 1-based number across all groups.
const numberedGroups = computed(() => {
  let n = 0
  return props.groups.map((g) => ({
    ...g,
    steps: g.steps.map((s) => ({ ...s, n: ++n })),
  }))
})

function shown(n) {
  return props.clicks >= n - 1
}
</script>

<template>
  <div class="pc-flow">
    <div
      v-for="(group, g) in numberedGroups"
      :key="g"
      class="pc-group"
      :class="{ 'pc-group-loop': group.loop }"
    >
      <div class="pc-row">
        <template v-for="(step, i) in group.steps" :key="i">
          <div v-if="i > 0" class="pc-conn" :class="{ 'pc-hidden': !shown(step.n) }">
            <span class="pc-arrow">→</span>
          </div>
          <div class="pc-card" :class="{ 'pc-hidden': !shown(step.n) }">
            <div class="pc-num">{{ step.n }}</div>
            <div class="pc-body">
              <h3>{{ step.title }}</h3>
              <p v-if="step.desc">{{ step.desc }}</p>
            </div>
          </div>
        </template>
      </div>

      <div
        v-if="group.loop"
        class="pc-return"
        :class="{ 'pc-hidden': !shown(group.steps[group.steps.length - 1].n) }"
      >
        <span class="pc-return-arrow" />
        <div class="pc-return-curve" />
        <span class="pc-return-text">⟲ {{ group.label || 'iterate' }}</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.pc-flow {
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
  margin-top: 0.3rem;
}

.pc-group-loop {
  padding: 0 1.5rem;
}

.pc-row {
  display: flex;
  align-items: stretch;
  justify-content: center;
  gap: 0.45rem;
}

.pc-card {
  flex: 1;
  display: flex;
  align-items: flex-start;
  gap: 0.55rem;
  border: 2px solid #ddd;
  border-left: 5px solid var(--slidev-theme-primary);
  border-radius: 10px;
  padding: 0.5rem 0.7rem;
  background: rgba(66, 133, 244, 0.05);
  transition: opacity 0.35s ease;
}

.pc-group-loop .pc-card {
  border-color: #e6b96a;
  border-left-color: #e6b96a;
  background: rgba(247, 211, 140, 0.22);
}

.pc-num {
  flex: none;
  width: 1.5rem;
  height: 1.5rem;
  border-radius: 50%;
  background: var(--slidev-theme-primary);
  color: #fff;
  font-family: var(--font-title);
  font-size: 0.95rem;
  line-height: 1.5rem;
  text-align: center;
}

.pc-group-loop .pc-num {
  background: #e6b96a;
}

.pc-body h3 {
  margin: 0 0 0.15rem 0;
  font-family: var(--font-subtitle);
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--slidev-theme-primary);
}

.pc-group-loop .pc-body h3 {
  color: #b9852a;
}

.pc-body p {
  margin: 0;
  font-size: 0.72rem;
  line-height: 1.3;
  color: #444;
}

.pc-conn {
  flex: none;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 1.4rem;
  transition: opacity 0.35s ease;
}

.pc-arrow {
  font-family: var(--font-title);
  font-size: 1.3rem;
  color: #bbb;
}

/* circular return loop under a loop group: flows from the last card back up
   into the first, forming a cycle */
.pc-return {
  position: relative;
  height: 1.6rem;
  /* inset so the legs meet the centres of the first and last loop cards;
     top margin leaves a gap so the arrowhead sits below the cards */
  margin: 0.6rem 16.5% 0.2rem;
  transition: opacity 0.35s ease;
}

.pc-return-curve {
  height: 100%;
  border: 2px dashed #e6b96a;
  border-top: none;
  border-radius: 0 0 22px 22px;
}

/* up-pointing arrowhead at the left end, returning into the first card */
.pc-return-arrow {
  position: absolute;
  left: -6px;
  top: -6px;
  width: 0;
  height: 0;
  border-left: 6px solid transparent;
  border-right: 6px solid transparent;
  border-bottom: 9px solid #e6b96a;
}

.pc-return-text {
  position: absolute;
  left: 50%;
  bottom: -0.6rem;
  transform: translateX(-50%);
  background: #fff;
  padding: 0 0.5rem;
  font-family: var(--font-subtitle);
  font-size: 0.8rem;
  font-weight: 600;
  color: #b9852a;
  white-space: nowrap;
}

.pc-hidden {
  opacity: 0;
}
</style>
