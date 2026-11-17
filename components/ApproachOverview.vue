<script setup>
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'
import ApproachDiagram from './ApproachDiagram.vue'

// The overview of options for analysing multiple datasets: one card per option,
// each highlighted in turn on a click with its diagram beside it.
//
//   <ApproachOverview />
//
// The options come from `approaches` in the slide frontmatter (set on the deck's
// `src:` entry), in display order. The slide also needs `clicks` set to the
// number of options.
const CARDS = {
  transfer: { title: 'Move data to one location', style: '--c: #4285F4;' },
  script: { title: 'Share script, meta-analysis', style: '--c: #E6B96A; --h: #B9852A; --t: #333333;' },
  published: { title: 'Publish summary data', style: '--c: #6A4C93;' },
  federated: { title: 'Federated Analysis', style: '--c: #0097A7;', tagline: '"Remote analysis without data transfer"' },
}

const { $clicks, $frontmatter } = useSlideContext()

const kinds = computed(() => $frontmatter?.approaches ?? ['transfer', 'script', 'federated'])

// first option is lit before any click, the last from its click onwards
function lit(i) {
  const last = kinds.value.length - 1
  if (i === 0) return $clicks.value < 1
  if (i === last) return $clicks.value >= i
  return $clicks.value === i
}
function shown(i) {
  const last = kinds.value.length - 1
  if (i === 0) return $clicks.value === 0
  if (i === last) return $clicks.value >= i
  return $clicks.value === i
}
</script>

<template>
  <div style="display: flex; gap: 2rem; align-items: stretch;">
    <div style="flex: 1; display: flex; flex-direction: column; justify-content: center;" :style="{ gap: kinds.length > 3 ? '0.5rem' : '0.7rem' }">
      <div v-for="(k, i) in kinds" :key="k" class="tint-card approach-card" :style="[CARDS[k].style, kinds.length > 3 ? 'height: 3.6rem;' : '']" :class="lit(i) ? 'active' : 'dimmed'">
        <h3>{{ CARDS[k].title }}</h3>
        <p v-if="CARDS[k].tagline" v-show="$clicks >= kinds.length" style="margin: 0.4rem 0 0 0; font-size: 13px;">{{ CARDS[k].tagline }}</p>
      </div>
    </div>
    <div style="flex: 1; display: flex; align-items: center; justify-content: center;">
      <div style="width: 300px; height: 208px; margin: 0 auto; position: relative;">
        <div v-for="(k, i) in kinds" :key="k" style="position: absolute; inset: 0;" :style="{ opacity: shown(i) ? 1 : 0 }">
          <ApproachDiagram :kind="k" />
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.approach-card { height: 4.8rem; box-sizing: border-box; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; }
.approach-card h3 { margin: 0; font-size: 1rem; }
</style>
