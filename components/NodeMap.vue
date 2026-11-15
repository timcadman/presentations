<script setup>
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'
import { WINDOWS, CITIES } from './map-windows.js'

// The DataSHIELD network on one map, in two groups: the exposome nodes first,
// then every other node we know about. Each group appears on its own click,
// alongside its entry in the list beside the map.
//
//   <NodeMap />
//   <NodeMap map="europe" :exposome="['Utrecht', 'Barcelona:below']" :other="['Kampala']" />
//
// Cities are names from CITIES in map-windows.js, optionally "Name:side" to put
// the label (left, right, below) clear of its neighbours. Dots are drawn without
// labels when `labelled` is false — on a crowded world map the list carries the
// names instead.
const props = defineProps({
  map: {
    type: String,
    default: 'world',
  },
  exposome: {
    type: Array,
    default: () => [],
  },
  other: {
    type: Array,
    default: () => [],
  },
  exposomeLabel: {
    type: String,
    default: 'Exposome cohorts',
  },
  otherLabel: {
    type: String,
    default: 'Other DataSHIELD nodes',
  },
  exposomeNote: {
    type: String,
    default: '',
  },
  labelled: {
    type: Boolean,
    default: false,
  },
})

const win = computed(() => WINDOWS[props.map] ?? WINDOWS.world)
const px = lon => ((lon - win.value.lon[0]) / (win.value.lon[1] - win.value.lon[0])) * 100
const py = lat => ((win.value.lat[1] - lat) / (win.value.lat[1] - win.value.lat[0])) * 100

function place(entry) {
  const [name, side] = entry.split(':')
  const at = CITIES[name]
  if (!at) throw new Error(`NodeMap: unknown city "${name}" — add it to map-windows.js`)
  return { name, side: side || 'right', x: px(at[0]), y: py(at[1]) }
}

const groups = computed(() => [
  { key: 'exposome', label: props.exposomeLabel, note: props.exposomeNote, colour: 'var(--c-blue)', nodes: props.exposome.map(place), at: 1 },
  { key: 'other', label: props.otherLabel, note: '', colour: 'var(--c-teal)', nodes: props.other.map(place), at: 2 },
])

const { $clicks } = useSlideContext()
const ratio = computed(() => `${win.value.size[0]} / ${win.value.size[1]}`)
</script>

<template>
  <div class="nm">
    <div class="nm-map" :style="{ aspectRatio: ratio }">
      <img :src="win.file" class="nm-base" />
      <template v-for="g in groups" :key="g.key">
        <div v-for="n in g.nodes" v-show="$clicks >= g.at" :key="n.name"
             class="fq-node" :class="n.side"
             :style="{ left: n.x + '%', top: n.y + '%', '--c': g.colour }">
          <span class="fq-dot"></span>
          <span v-if="labelled" class="fq-name">{{ n.name }}</span>
        </div>
      </template>
    </div>

    <div class="nm-side">
      <div v-for="g in groups" v-show="$clicks >= g.at" :key="g.key" class="nm-group">
        <h3 :style="{ '--c': g.colour }">{{ g.label }}</h3>
        <p v-if="g.note" class="nm-note">{{ g.note }}</p>
        <ul class="nm-list">
          <li v-for="n in g.nodes" :key="n.name">{{ n.name }}</li>
        </ul>
      </div>
    </div>
  </div>
</template>
