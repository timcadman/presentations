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
  // only the nodes of one project, by its name in data/datashield_nodes.csv (LifeCycle, Athlete, ...)
  project: {
    type: String,
    default: '',
  },
  // with the key below or none, cap the map to this height, e.g. '22rem'; full width otherwise
  height: {
    type: String,
    default: '',
  },
  // where the key goes: beside the map, below it, or none
  legend: {
    type: String,
    default: 'side',
  },
  // on the first click, zoom in: [west, east, south, north] in degrees, or 'auto' to fit the project's nodes
  zoom: {
    type: [Array, String],
    default: null,
  },
  // an earlier project this one builds on: its nodes show first, the project's own on the first click
  buildsOn: {
    type: String,
    default: '',
  },
  buildsOnColour: {
    type: String,
    default: 'var(--c-blue)',
  },
  // colour of the project's nodes, live and planned alike
  colour: {
    type: String,
    default: 'var(--c-blue)',
  },
  // everything at once: live nodes in one colour, planned in another, no clicks
  simple: {
    type: Boolean,
    default: false,
  },
  // closing point, on the click after both groups
  note: {
    type: String,
    default: 'All analysable with DataSHIELD, subject to access arrangements',
  },
})

const win = computed(() => WINDOWS[props.map] ?? WINDOWS.world)
const px = lon => ((lon - win.value.lon[0]) / (win.value.lon[1] - win.value.lon[0])) * 100
const py = lat => ((win.value.lat[1] - lat) / (win.value.lat[1] - win.value.lat[0])) * 100

const inWindow = n =>
  n.lon >= win.value.lon[0] && n.lon <= win.value.lon[1] &&
  n.lat >= win.value.lat[0] && n.lat <= win.value.lat[1]

// the example slides give every map the same full-width box, whatever the base map's shape
const fixedBox = computed(() => props.legend === 'below' || props.legend === 'none')
const baseRatio = computed(() => win.value.size[0] / win.value.size[1])
const boxRatio = computed(() => (fixedBox.value ? Math.max(WINDOWS.world.size[0] / WINDOWS.world.size[1], baseRatio.value) : baseRatio.value))

// widen a box to the shape of the display box and keep it inside the map, so the zoom is uniform
function frame([x0, x1, y0, y1]) {
  const w = win.value
  const DX = w.lon[1] - w.lon[0]
  const DY = w.lat[1] - w.lat[0]
  const k = boxRatio.value / baseRatio.value
  let fx = (x1 - x0) / DX
  let fy = (y1 - y0) / DY
  if (fx / fy < k) fx = fy * k
  else fy = fx / k
  if (fx > 1) { fx = 1; fy = 1 / k }
  if (fy > 1) { fy = 1; fx = Math.min(k, 1) }
  const dx = fx * DX
  const dy = fy * DY
  const at = (c, d, lo, hi) => Math.min(Math.max(c - d / 2, lo), hi - d)
  const a = at((x0 + x1) / 2, dx, w.lon[0], w.lon[1])
  const b = at((y0 + y1) / 2, dy, w.lat[0], w.lat[1])
  return [a, a + dx, b, b + dy]
}

// the box around the project's nodes, padded
function fitBox() {
  const w = win.value
  const earlier = props.buildsOn ? NODES.filter(n => n.projects.includes(props.buildsOn)) : []
  const pts = [...pool.value, ...earlier].filter(inWindow)
  if (!pts.length) return null
  const side = (lo, hi, min) => {
    const pad = Math.max((hi - lo) * 0.2, 2)
    const mid = (lo + hi) / 2
    const half = Math.max((hi - lo) / 2 + pad, min / 2)
    return [mid - half, mid + half]
  }
  const lons = pts.map(n => n.lon)
  const lats = pts.map(n => n.lat)
  return frame([...side(Math.min(...lons), Math.max(...lons), 12), ...side(Math.min(...lats), Math.max(...lats), 8)])
}
const zoomBox = computed(() => {
  if (!props.zoom) return null
  return props.zoom === 'auto' ? fitBox() : frame(props.zoom)
})

// the map starts whole and eases in on the box at the first click
const zoomed = computed(() => !!zoomBox.value && $clicks.value >= 1)
const scale = computed(() => (zoomBox.value
  ? (win.value.lon[1] - win.value.lon[0]) / (zoomBox.value[1] - zoomBox.value[0])
  : 1))
const zoomStyle = computed(() => {
  const layer = fixedBox.value && boxRatio.value > baseRatio.value
    ? { top: `${(-(boxRatio.value / baseRatio.value - 1) / 2) * 100}%`, bottom: 'auto', height: `${(boxRatio.value / baseRatio.value) * 100}%` }
    : {}
  if (!zoomBox.value) return layer
  const w = win.value
  const fx = (zoomBox.value[0] - w.lon[0]) / (w.lon[1] - w.lon[0])
  const fy = (w.lat[1] - zoomBox.value[3]) / (w.lat[1] - w.lat[0])
  const ty = ((1 - baseRatio.value / boxRatio.value) / 2 - scale.value * fy) * 100
  return {
    ...layer,
    transform: zoomed.value ? `translate(${-fx * scale.value * 100}%, ${ty}%) scale(${scale.value})` : 'none',
    transition: 'transform 1.4s ease',
  }
})
// keep the dots the same size on screen while the map scales under them
const dotScale = computed(() => (zoomBox.value
  ? { transform: zoomed.value ? `scale(${1 / scale.value})` : 'none', transition: 'transform 1.4s ease' }
  : {}))

const pool = computed(() => (props.project ? NODES.filter(n => n.projects.includes(props.project)) : NODES))
const shown = computed(() => pool.value.filter(inWindow))

const isExposome = n => n.projects.some(p => EXPOSOME.includes(p))

// nodes in the same city share coordinates; in the single-colour maps a small ring keeps each visible
const sameSpot = n => `${n.lon},${n.lat}`
const crowd = computed(() => {
  const spots = {}
  for (const n of NODES) (spots[sameSpot(n)] ||= []).push(n)
  return spots
})
function place(n) {
  let { lon, lat } = n
  const mates = props.simple ? crowd.value[sameSpot(n)] : null
  if (mates && mates.length > 1) {
    const a = (2 * Math.PI * mates.indexOf(n)) / mates.length
    lon += 0.5 * Math.cos(a)
    lat += 0.5 * Math.sin(a)
  }
  return { ...n, x: px(lon), y: py(lat) }
}

const groups = computed(() => {
  const live = shown.value.filter(n => n.status === 'live')
  const exp = live.filter(isExposome)
  const rest = live.filter(n => !isExposome(n))
  const soon = props.planned ? shown.value.filter(n => n.status !== 'live') : []
  if (props.simple && props.project) {
    const inBase = n => !!props.buildsOn && n.projects.includes(props.buildsOn)
    const base = NODES.filter(inWindow).filter(inBase)
    const own = shown.value.filter(n => !inBase(n))
    const others = NODES.filter(inWindow).filter(n => !n.projects.includes(props.project) && !inBase(n))
    const planned = pool.value.filter(n => n.status !== 'live').length
    return [
      { key: 'others', colour: 'var(--c-grey)', pale: true, at: 0, nodes: others.map(place),
        text: 'Other nodes' },
      ...(base.length
        ? [{ key: 'base', colour: props.buildsOnColour, at: 0, nodes: base.map(place),
             text: `${props.buildsOn} nodes` }]
        : []),
      { key: 'project', colour: props.colour, at: base.length ? 1 : 0, nodes: own.map(place),
        text: `${pool.value.length} nodes${planned ? `, ${planned} planned` : ''}` },
    ]
  }
  if (props.simple) {
    return [
      { key: 'live', colour: 'var(--c-blue)', at: 0, nodes: live.map(place),
        text: `>${Math.floor(NODES.filter(n => n.status === 'live').length / 100) * 100} known nodes` },
      ...(soon.length
        ? [{ key: 'soon', colour: 'var(--c-gold-dark)', at: 0, nodes: soon.map(place),
             text: `${soon.length} more planned` }]
        : []),
    ]
  }
  return [
    { key: 'exposome', colour: 'var(--c-blue)', at: 1, nodes: exp.map(place),
      text: `${exp.length} birth cohorts with exposome and health data` },
    { key: 'rest', colour: 'var(--c-gold-dark)', at: 2, nodes: rest.map(place),
      text: `Estimated ${rest.length} other data sources with health data` },
    ...(soon.length
      ? [{ key: 'soon', colour: 'var(--c-purple)', at: 3, nodes: soon.map(place),
           text: `${soon.length} more planned` }]
      : []),
  ]
})

// the closing line sits one click after the last group
const noteAt = computed(() => (props.simple ? 0 : groups.value.length + 1))

const { $clicks } = useSlideContext()
const ratio = computed(() => `${boxRatio.value}`)
</script>

<template>
  <div class="nm" :style="legend === 'below' ? { flexDirection: 'column', gap: '0.6rem' } : {}">
    <div class="nm-map" :style="{ aspectRatio: ratio, overflow: zoomBox || fixedBox ? 'hidden' : undefined, ...(fixedBox ? { flex: 'none', width: height ? `min(100%, calc(${height} * ${boxRatio}))` : '100%', maxHeight: 'none' } : {}) }">
      <div class="nm-zoom" :style="zoomStyle">
        <img :src="win.file" class="nm-base" style="object-fit: fill" />
        <template v-for="g in groups" :key="g.key">
          <span v-for="(n, i) in g.nodes" v-show="$clicks >= g.at" :key="`${g.key}${i}`"
                class="nm-dot" :class="{ hollow: n.status !== 'live' && !simple }"
                :style="{ left: n.x + '%', top: n.y + '%', '--c': g.colour, opacity: g.pale ? 0.35 : 1, ...dotScale }" />
        </template>
      </div>
    </div>

    <ul v-if="legend !== 'none'" class="nm-side" :class="{ below: legend === 'below' }" :style="legend === 'below' ? { flex: 'none', display: 'flex', flexWrap: 'wrap', columnGap: '1.5rem' } : {}">
      <li v-for="g in groups" v-show="$clicks >= g.at" :key="g.key"
          :style="{ '--c': g.colour }">{{ g.text }}</li>
      <li v-if="note" v-show="$clicks >= noteAt" class="nm-note"
          :style="{ '--c': 'var(--c-text)' }">{{ note }}</li>
    </ul>
  </div>
</template>

<style>
.slidev-layout .nm-zoom { position: absolute; inset: 0; transform-origin: 0 0; }
.slidev-layout .nm-side.below li { font-size: 14px; margin-bottom: 0; line-height: 1.3; }
</style>
