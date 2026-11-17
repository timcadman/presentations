<script setup>
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'

// The "why combine data" bullets: the existing-data point, then, on a click, the benefits
// of combining sources.
//
//   <ReuseBenefits />
//
// The benefits come from `benefits` in the slide frontmatter (set on the deck's `src:` entry),
// in display order, from: contrast, power, replication, coverage, confounding. All five by default.
// `examples` sets the sources named in the first bullet; cohort studies and biobanks by default.
const ITEMS = {
  contrast: { bold: 'Exposure contrast', rest: '' },
  power: { bold: 'Statistical power', rest: '' },
  replication: { bold: 'Replication', rest: ' across different contexts' },
  coverage: { bold: 'Extended coverage', rest: ' of the lifecourse' },
  confounding: { bold: 'Different confounding structures', rest: '' },
}

const { $frontmatter } = useSlideContext()
const examples = computed(() => $frontmatter?.examples ?? 'cohort studies, biobanks')
const keys = computed(() => $frontmatter?.benefits ?? ['contrast', 'power', 'replication', 'coverage', 'confounding'])
</script>

<template>
  <ul>
    <li>Large quantities of existing data already exist (e.g. {{ examples }})</li>
  </ul>
  <div v-click>
    <ul>
      <li>
        Combining data sources allows:
        <ul>
          <li v-for="k in keys" :key="k"><strong>{{ ITEMS[k].bold }}</strong>{{ ITEMS[k].rest }}</li>
        </ul>
      </li>
    </ul>
  </div>
</template>
