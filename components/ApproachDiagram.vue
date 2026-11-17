<script>
let counter = 0
</script>

<script setup>
import iconDatabase from '../library/assets/icon-database.png'
import iconResearcher from '../library/assets/icon-researcher.png'

// One option for analysing multiple datasets, drawn as three sites and a researcher.
//
//   <ApproachDiagram kind="federated" />
//
// kind: transfer | script | published | federated
defineProps({
  kind: {
    type: String,
    required: true,
  },
})

const id = `ad-${counter++}`
const sites = [
  { label: 'Site A', top: '20px' },
  { label: 'Site B', top: '80.6px' },
  { label: 'Site C', top: '141.2px' },
]
const midTops = ['61.8px', '92.1px', '122.4px']
</script>

<template>
  <div class="ad">
    <svg viewBox="0 0 300 208" class="ad-svg">
      <defs>
        <marker :id="`${id}-blue`" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
          <path d="M0,0 L10,5 L0,10 z" fill="#4285F4" />
        </marker>
        <marker :id="`${id}-gold`" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
          <path d="M0,0 L10,5 L0,10 z" fill="#E6B96A" />
        </marker>
      </defs>
      <template v-if="kind === 'transfer'">
        <line x1="100" y1="41.5" x2="170.44" y2="94.85" stroke="#4285F4" stroke-width="2" :marker-end="`url(#${id}-blue)`" />
        <line x1="100" y1="102.1" x2="168" y2="102.1" stroke="#4285F4" stroke-width="2" :marker-end="`url(#${id}-blue)`" />
        <line x1="100" y1="162.7" x2="170.44" y2="109.35" stroke="#4285F4" stroke-width="2" :marker-end="`url(#${id}-blue)`" />
      </template>
      <template v-else-if="kind === 'published'">
        <line x1="100" y1="41.5" x2="120" y2="87" stroke="#E6B96A" stroke-width="2" :marker-end="`url(#${id}-gold)`" />
        <line x1="100" y1="102.1" x2="120" y2="102.1" stroke="#E6B96A" stroke-width="2" :marker-end="`url(#${id}-gold)`" />
        <line x1="100" y1="162.7" x2="120" y2="117" stroke="#E6B96A" stroke-width="2" :marker-end="`url(#${id}-gold)`" />
        <line x1="170" y1="102.1" x2="186" y2="102.1" stroke="#E6B96A" stroke-width="2" :marker-end="`url(#${id}-gold)`" />
      </template>
      <template v-else-if="kind === 'script'">
        <line x1="170.44" y1="94.85" x2="100" y2="41.5" stroke="#4285F4" stroke-width="2" :marker-end="`url(#${id}-blue)`" />
        <line x1="168" y1="102.1" x2="100" y2="102.1" stroke="#4285F4" stroke-width="2" :marker-end="`url(#${id}-blue)`" />
        <line x1="170.44" y1="109.35" x2="100" y2="162.7" stroke="#4285F4" stroke-width="2" :marker-end="`url(#${id}-blue)`" />
        <path d="M 60,184 C 60,205 207,205 207,135" stroke="#E6B96A" stroke-width="2" fill="none" :marker-end="`url(#${id}-gold)`" />
      </template>
      <template v-else-if="kind === 'federated'">
        <line x1="100" y1="41.5" x2="170.44" y2="94.85" stroke="#4285F4" stroke-width="2" :marker-start="`url(#${id}-blue)`" />
        <line x1="100" y1="102.1" x2="168" y2="102.1" stroke="#4285F4" stroke-width="2" :marker-start="`url(#${id}-blue)`" />
        <line x1="100" y1="162.7" x2="170.44" y2="109.35" stroke="#4285F4" stroke-width="2" :marker-start="`url(#${id}-blue)`" />
        <path d="M 60,184 C 60,205 207,205 207,135" stroke="#E6B96A" stroke-width="2" fill="none" :marker-end="`url(#${id}-gold)`" />
      </template>
    </svg>

    <div v-for="s in sites" :key="s.label" class="ad-site" :style="{ top: s.top }">
      <span>{{ s.label }}</span>
      <img :src="iconDatabase" style="height: 43px;" />
    </div>

    <template v-if="kind === 'script'">
      <div v-for="t in midTops" :key="t" class="ad-paper blue" :style="{ top: t }">
        <div class="line"></div>
        <div class="line"></div>
      </div>
      <div class="ad-stack">
        <div class="sheet" style="left: 6px; top: 6px;"></div>
        <div class="sheet" style="left: 3px; top: 3px;"></div>
        <div class="sheet front">
          <div class="line"></div>
          <div class="line"></div>
        </div>
      </div>
    </template>
    <template v-else-if="kind === 'published'">
      <svg viewBox="0 0 44 52" class="ad-repo">
        <rect x="1" y="1" width="42" height="50" rx="4" fill="white" stroke="#B9852A" stroke-width="2" />
        <line x1="22" y1="7" x2="22" y2="45" stroke="#9AA0A6" stroke-width="1" stroke-dasharray="2 2" />
        <line x1="10" y1="13" x2="30" y2="13" stroke="#B9852A" stroke-width="1.5" />
        <rect x="17" y="11" width="4" height="4" fill="#B9852A" />
        <line x1="14" y1="23" x2="36" y2="23" stroke="#B9852A" stroke-width="1.5" />
        <rect x="23" y="21" width="4" height="4" fill="#B9852A" />
        <line x1="8" y1="33" x2="28" y2="33" stroke="#B9852A" stroke-width="1.5" />
        <rect x="14" y="31" width="4" height="4" fill="#B9852A" />
        <polygon points="14,42 21,39 28,42 21,45" fill="#B9852A" />
      </svg>
      <span class="ad-repo-label">Repository</span>
    </template>
    <template v-else-if="kind === 'federated'">
      <div v-for="t in midTops" :key="t" class="ad-code" :style="{ top: t }">&lt;/&gt;</div>
      <div class="ad-code arc">&lt;/&gt;</div>
    </template>

    <img :src="iconResearcher" class="ad-researcher" />

    <div v-if="kind !== 'script'" class="ad-laptop">
      <div class="screen"></div>
      <div class="base"></div>
    </div>
  </div>
</template>

<style scoped>
.ad { width: 300px; height: 208px; margin: 0 auto; position: relative; }
.ad-svg { position: absolute; inset: 0; width: 100%; height: 100%; }
.ad-site { position: absolute; left: 0; width: 100px; height: 43px; display: flex; align-items: center; justify-content: flex-end; gap: 0.5rem; }
.ad-site span { font-size: 13px; }
.ad-repo { position: absolute; left: 129px; top: 83px; width: 32px; height: 38px; color: #B9852A; }
.ad-repo-label { position: absolute; left: 100px; width: 90px; top: 150px; text-align: center; font-size: 13px; }
.ad-researcher { position: absolute; left: 190px; top: 69.1px; height: 66px; }
.ad-laptop { position: absolute; left: 245px; top: 80.6px; width: 48px; height: 43px; }
.ad-laptop .screen { width: 42px; height: 33px; margin: 0 3px; border: 2.5px solid #333; border-radius: 3px; box-sizing: border-box; }
.ad-laptop .base { width: 48px; height: 7px; background: #333; border-radius: 0 0 3px 3px; margin-top: 3px; }

.ad-paper { position: absolute; left: 132.5px; width: 15px; height: 20px; border: 1.5px solid; border-radius: 2px; background: white; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px; }
.ad-paper.blue { border-color: #4285F4; }
.ad-paper.gold { border-color: #E6B96A; }
.ad-paper.blue .line { background: #4285F4; }
.ad-paper.gold .line { background: #E6B96A; }
.ad-paper .line { width: 9px; height: 1px; }

.ad-stack { position: absolute; left: 123px; top: 180.6px; width: 21px; height: 26px; }
.ad-stack .sheet { position: absolute; width: 15px; height: 20px; border: 1.5px solid #E6B96A; border-radius: 2px; background: white; }
.ad-stack .front { left: 0; top: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px; }
.ad-stack .line { width: 9px; height: 1px; background: #E6B96A; }

.ad-code { position: absolute; left: 132.5px; width: 15px; height: 20px; border: 1.5px solid #4285F4; border-radius: 2px; background: white; display: flex; align-items: center; justify-content: center; font-size: 8px; font-weight: 700; color: #4285F4; line-height: 1; }
.ad-code.arc { left: 123px; top: 180.6px; border-color: #E6B96A; color: #E6B96A; font-size: 10px; }
</style>
