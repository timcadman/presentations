<script setup>
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'

// What federated analysis is, as four tint cards. Wording merged from the
// ihen-26/federated and stage-webinar bullet slides and the uncan-demo voiceover.
const props = defineProps({
  // append a fifth card naming the software (uncan-demo uses this)
  software: {
    type: Boolean,
    default: false,
  },
})

const { $clicks } = useSlideContext()

const BASE = [
  { c: '#4285F4', title: 'Remote analysis', body: 'One model across data held at several sites' },
  { c: '#119DA1', title: 'Code travels, not data', body: 'Code is sent to the data; each site computes <strong>locally</strong>' },
  { c: '#BA8118', h: '#BA8118', title: 'Only aggregates return', body: 'Means, SDs, coefficients — <strong>never individual-level data</strong>' },
  { c: '#5D408A', title: 'Data never moves', body: 'Governance and access stay with the data holder' },
]
const EXTRA = { c: '#02529B', title: 'The software', body: '<strong>Armadillo</strong> manages data access; <strong>DataSHIELD</strong> runs the analysis' }

const cards = computed(() => (props.software ? [...BASE, EXTRA] : BASE).map((card, i) => ({
  ...card,
  style: { '--c': card.c, ...(card.h ? { '--h': card.h } : {}), ...(card.t ? { '--t': card.t } : {}) },
  active: $clicks.value === i,
  dimmed: $clicks.value !== i,
})))
</script>

<template>
  <div class="fq-grid" :class="{ five: cards.length > 4 }">
    <div v-for="(card, i) in cards" :key="i" class="tint-card"
         :style="card.style" :class="{ active: card.active, dimmed: card.dimmed }">
      <h3>{{ card.title }}</h3>
      <p v-html="card.body"></p>
    </div>
  </div>
</template>
