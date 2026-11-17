<script setup>
// A row of numbered steps joined by a line, with the current one filled, so a run of
// slides reads as one sequence.
//
//   <ChallengeTrail :current="2" :steps="['Harmonisation', 'Approvals', 'IT departments']" />
defineProps({
  steps: {
    type: Array,
    required: true,
  },
  current: {
    type: Number,
    required: true,
  },
})
</script>

<template>
  <div class="ct">
    <template v-for="(s, i) in steps" :key="s">
      <div v-if="i > 0" class="ct-line" :class="{ done: i < current }"></div>
      <div class="ct-step" :class="{ cur: i + 1 === current, done: i + 1 < current }">
        <span class="ct-n">{{ i + 1 }}</span>
        <span class="ct-label">{{ s }}</span>
      </div>
    </template>
  </div>
</template>

<style scoped>
.ct { display: flex; align-items: center; gap: 0.6rem; margin: 0 0 1.5rem 0; }
.ct-step { display: flex; align-items: center; gap: 0.5rem; flex: none; color: var(--c-grey); }
.ct-n {
  display: inline-flex; align-items: center; justify-content: center;
  width: 1.8rem; height: 1.8rem; border-radius: 50%; box-sizing: border-box;
  border: 2px solid var(--c-grey); font-family: var(--font-subtitle); font-size: 15px; font-weight: 600;
}
.ct-label { font-family: var(--font-subtitle); font-size: 16px; }
.ct-step.done { color: var(--c-blue); }
.ct-step.done .ct-n { border-color: var(--c-blue); }
.ct-step.cur { color: var(--c-text); font-weight: 600; }
.ct-step.cur .ct-n { background: var(--c-blue); border-color: var(--c-blue); color: #fff; }
.ct-line { flex: 1; height: 2px; background: var(--c-grey); opacity: 0.5; }
.ct-line.done { background: var(--c-blue); opacity: 1; }
</style>
