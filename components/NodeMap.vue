<script setup>
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'
import { WINDOWS } from './map-windows.js'
import { NODES, EXPOSOME } from './datashield-nodes.js'

// The DataSHIELD network on one map, in two groups: the exposome cohorts first,
// then every other node we know of. Each group appears on its own click, with its
// own entry in the key beside the map.
//
//   <NodeMap />
//   <NodeMap map="europe" :planned="false" />
//
// Nodes come from data/datashield_nodes.csv via data/build_nodes.py — never
// hand-written here.
const props = defineProps({
  map: {
    type: String,
    default: 'world',
  },
  // include nodes that are not live yet, drawn hollow
  planned: {
    type: Boolean,
    default: true,
  },
  // closing point, on the click after both groups
  note: {
    type: String,
    default: 'Data can be analysed using DataSHIELD, subject to access arrangements',
  },
})

const win = computed(() => WINDOWS[props.map] ?? WINDOWS.world)
const px = lon => ((lon - win.value.lon[0]) / (win.value.lon[1] - win.value.lon[0])) * 100
const py = lat => ((win.value.lat[1] - lat) / (win.value.lat[1] - win.value.lat[0])) * 100

const inWindow = n =>
  n.lon >= win.value.lon[0] && n.lon <= win.value.lon[1] &&
  n.lat >= win.value.lat[0] && n.lat <= win.value.lat[1]

const shown = computed(() =>
  NODES.filter(n => inWindow(n) && (props.planned || n.status === 'live'))
)

const isExposome = n => n.projects.some(p => EXPOSOME.includes(p))

function place(n) {
  return { ...n, x: px(n.lon), y: py(n.lat) }
}

const groups = computed(() => {
  const exp = shown.value.filter(isExposome)
  const rest = shown.value.filter(n => !isExposome(n))
  return [
    { key: 'exposome', colour: 'var(--c-blue)', at: 1, nodes: exp.map(place),
      text: `${exp.length} birth cohorts with exposome and health data` },
    { key: 'rest', colour: 'var(--c-teal)', at: 2, nodes: rest.map(place),
      text: `Estimated ${rest.length} other data sources with health data` },
  ]
})

const { $clicks } = useSlideContext()
const ratio = computed(() => `${win.value.size[0]} / ${win.value.size[1]}`)
</script>

<template>
  <div class="nm">
    <div class="nm-map" :style="{ aspectRatio: ratio }">
      <img :src="win.file" class="nm-base" />
      <template v-for="g in groups" :key="g.key">
        <span v-for="(n, i) in g.nodes" v-show="$clicks >= g.at" :key="`${g.key}${i}`"
              class="nm-dot" :class="{ planned: n.status !== 'live' }"
              :style="{ left: n.x + '%', top: n.y + '%', '--c': g.colour }" />
      </template>
    </div>

    <ul class="nm-side">
      <li v-for="g in groups" v-show="$clicks >= g.at" :key="g.key"
          :style="{ '--c': g.colour }">{{ g.text }}</li>
      <li v-if="note" v-show="$clicks >= 3" class="nm-note"
          :style="{ '--c': 'var(--c-grey)' }">{{ note }}</li>
    </ul>
  </div>
</template>
