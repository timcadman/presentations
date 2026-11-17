<script setup>
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'
import IconCheck from '~icons/carbon/checkmark'
import IconClose from '~icons/carbon/close'

// Comparison of the options for analysing multiple datasets, one column per option.
//
//   <ApproachTable />
//
// The options come from `approaches` in the slide frontmatter, as for ApproachOverview.
// `omit: [methods]` in the frontmatter hides the 'All analysis methods' row.
const COLUMNS = {
  transfer: 'Data transfer',
  script: 'Share script',
  published: 'Publish summaries',
  federated: 'Federated analysis',
}

// a tick per option, in the order transfer, script, published, federated
const ROWS = [
  { label: 'Data stays at source', transfer: false, script: true, published: true, federated: true },
  { label: 'Owners keep control', transfer: false, script: true, published: true, federated: true },
  { label: 'One pooled analysis', transfer: true, script: false, published: false, federated: true },
  { label: 'No extra infrastructure', transfer: true, script: true, published: true, federated: false },
  { id: 'methods', label: 'All analysis methods', transfer: true, script: false, published: false, federated: false },
  { label: 'Flexibly redo analyses', transfer: true, script: false, published: false, federated: true },
]

const { $frontmatter } = useSlideContext()
const kinds = computed(() => $frontmatter?.approaches ?? ['transfer', 'script', 'federated'])
const rows = computed(() => ROWS.filter(r => !$frontmatter?.omit?.includes(r.id)))
</script>

<template>
  <table :class="{ compact: kinds.length > 3 }">
    <thead>
      <tr>
        <th></th>
        <th v-for="k in kinds" :key="k" style="text-align: center">{{ COLUMNS[k] }}</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="row in rows" :key="row.label">
        <td>{{ row.label }}</td>
        <td v-for="k in kinds" :key="k" style="text-align: center">
          <IconCheck v-if="row[k]" style="color: #0097A7" />
          <IconClose v-else style="color: #D9534F" />
        </td>
      </tr>
    </tbody>
  </table>
</template>

<style>
.slidev-layout table.compact { margin: 0.25rem 0; }
.slidev-layout table.compact th, .slidev-layout table.compact td { white-space: nowrap; }
.slidev-layout table.compact thead th { padding-top: 0.4rem; padding-bottom: 0.4rem; }
.slidev-layout table.compact tbody td { padding-top: 0.35rem; padding-bottom: 0.35rem; }
</style>
