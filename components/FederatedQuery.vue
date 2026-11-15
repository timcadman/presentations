<script setup>
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'
import { WINDOWS, CITIES } from './map-windows.js'

// A researcher querying several cohort sites: the analysis code goes out, the
// aggregate results come back. Builds on clicks — 1 code out, 2 results back.
//
//   <FederatedQuery />
//   <FederatedQuery map="europe" :cities="['Utrecht', 'Kaunas:left']" researcher="Bristol" />
//
// A city is a name from CITIES in map-windows.js, optionally "Name:side" to place
// its label (left, right, below) clear of its neighbours.
const props = defineProps({
  map: {
    type: String,
    default: 'world',
  },
  cities: {
    type: Array,
    default: () => ['Utrecht:left', 'Barcelona:below', 'Kampala:right', 'New York:left', 'Lima:right'],
  },
  researcher: {
    type: String,
    default: 'New Delhi',
  },
})

const win = computed(() => WINDOWS[props.map] ?? WINDOWS.world)
const px = lon => ((lon - win.value.lon[0]) / (win.value.lon[1] - win.value.lon[0])) * 100
const py = lat => ((win.value.lat[1] - lat) / (win.value.lat[1] - win.value.lat[0])) * 100

function place(entry, fallbackSide) {
  const [name, side] = entry.split(':')
  const at = CITIES[name]
  if (!at) throw new Error(`FederatedQuery: unknown city "${name}" — add it to map-windows.js`)
  return { name, side: side || fallbackSide, x: px(at[0]), y: py(at[1]) }
}

const { $clicks } = useSlideContext()

const nodes = computed(() => props.cities.map(c => place(c, 'right')))
const me = computed(() => place(props.researcher, 'below'))
const ratio = computed(() => `${win.value.size[0]} / ${win.value.size[1]}`)

// a shallow arc each way, so the outbound and return paths stay apart
function arc(n, lift) {
  const m = me.value
  return `M ${m.x} ${m.y} Q ${(m.x + n.x) / 2} ${(m.y + n.y) / 2 - lift} ${n.x} ${n.y}`
}

const showOut = computed(() => $clicks.value >= 2)
const showBack = computed(() => $clicks.value >= 3)
</script>

<template>
  <div class="fq-map" :style="{ aspectRatio: ratio }">
    <img :src="win.file" class="fq-base" />

    <svg class="fq-overlay" viewBox="0 0 100 100" preserveAspectRatio="none">
      <g v-if="showOut">
        <path v-for="n in nodes" :key="`o${n.name}`" :d="arc(n, 5)"
              fill="none" stroke="#119DA1" stroke-width="0.6"
              vector-effect="non-scaling-stroke" stroke-dasharray="2 1.5" />
      </g>
      <g v-if="showBack">
        <path v-for="n in nodes" :key="`b${n.name}`" :d="arc(n, -5)"
              fill="none" stroke="#E2A517" stroke-width="0.6"
              vector-effect="non-scaling-stroke" />
      </g>
    </svg>

    <div v-for="n in nodes" :key="n.name" class="fq-node" :class="n.side"
         :style="{ left: n.x + '%', top: n.y + '%' }">
      <span class="fq-dot"></span>
      <span class="fq-name">{{ n.name }}</span>
    </div>

    <div class="fq-key">
      <div v-if="showOut"><span class="k out"></span>Analysis code</div>
      <div v-if="showBack"><span class="k back"></span>Aggregate results</div>
    </div>

    <div class="fq-me" :style="{ left: me.x + '%', top: me.y + '%' }">
      <img src="/icon-researcher.png" />
      <span>Researcher</span>
    </div>
  </div>
</template>
