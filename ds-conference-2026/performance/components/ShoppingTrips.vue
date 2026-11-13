<script setup>
// One lane: home (house, left) <-> supermarket (right). On `startAt` click the
// shopper makes one trip per item; on the next click the lane is replaced by a
// single trip for everything. Every round trip takes `tripSeconds`, so only the
// number of trips differs. The trolley faces its direction of travel.
import { computed, ref, watch, onUnmounted } from 'vue'

const props = defineProps({
  clicks: { type: Number, default: 0 },
  startAt: { type: Number, default: 1 },
  items: { type: Number, default: 4 },
  tripSeconds: { type: Number, default: 3.2 },
  note: { type: String, default: '' },
  noteAfter: { type: String, default: '' },
  // 'both' swaps before -> after on the next click; 'before' / 'after' show one only
  show: { type: String, default: 'both' },
  walkMinutes: { type: Number, default: 10 },
  shopMinutes: { type: Number, default: 5 },
})

const base = import.meta.env.BASE_URL
const showAfter = computed(() =>
  props.show === 'after' || (props.show === 'both' && props.clicks >= props.startAt + 1))
const lane = computed(() => showAfter.value
  ? { key: 'after', label: 'Everything in one trip', trips: 1 }
  : { key: 'before', label: 'Separate trips', trips: props.items })
const running = computed(() => props.clicks >= props.startAt)

// Simulated clock: each round trip costs walkMinutes + shopMinutes. It reads
// the trolley animation's own elapsed time, so the two cannot drift apart
// when the browser starts or pauses the animation at a different moment.
const walker = ref(null)
const minutes = ref(0)
let frame = null
const stopClock = () => { if (frame) cancelAnimationFrame(frame); frame = null }
const startClock = () => {
  stopClock()
  minutes.value = 0
  if (!running.value) return
  const perTrip = props.walkMinutes + props.shopMinutes
  const total = lane.value.trips * perTrip
  const tick = () => {
    const animation = walker.value?.getAnimations()[0]
    const trips = (animation?.currentTime ?? 0) / 1000 / props.tripSeconds
    minutes.value = Math.min(total, Math.floor(trips * perTrip))
    if (minutes.value < total) frame = requestAnimationFrame(tick)
  }
  frame = requestAnimationFrame(tick)
}
watch(() => [running.value, lane.value.key], startClock, { immediate: true })
onUnmounted(stopClock)
</script>

<template>
  <div class="st-wrap">
    <div class="st-lane" :class="`st-${lane.key}`">
      <div class="st-head">
        <div class="st-label">{{ lane.label }}</div>
        <div class="st-clock">⏱ {{ minutes }} min</div>
      </div>
      <div class="st-row">
        <img :src="`${base}house.jpg`" class="st-end" />
        <div class="st-road">
          <img
            ref="walker"
            :key="lane.key"
            :src="`${base}trolley.jpg`"
            class="st-walker"
            :class="{ go: running }"
            :style="{ animationDuration: tripSeconds + 's', animationIterationCount: lane.trips }"
          />
        </div>
        <img :src="`${base}supermarket.jpg`" class="st-end" />
      </div>
      <div
        :key="lane.key"
        class="st-count"
        :class="{ go: running }"
        :style="{ animationDelay: lane.trips * tripSeconds + 's' }"
      >
        {{ lane.trips }} {{ lane.trips === 1 ? 'trip' : 'trips' }}
      </div>
    </div>
    <div class="st-note">{{ lane.key === 'after' && noteAfter ? noteAfter : note }}</div>
  </div>
</template>

<style scoped>
.st-wrap {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  padding-top: 2rem;
}

.st-lane { display: flex; flex-direction: column; gap: 0.3rem; transition: opacity 0.3s; }

.st-head { display: flex; justify-content: space-between; align-items: baseline; }

.st-clock {
  font-family: var(--font-subtitle);
  font-size: 18px;
  font-weight: 600;
  color: var(--slidev-theme-primary);
  font-variant-numeric: tabular-nums;
}

.st-label {
  font-family: var(--font-subtitle);
  font-size: 14px;
  color: var(--slidev-theme-text);
}

.st-row { display: flex; align-items: center; gap: 0.75rem; }

.st-end {
  width: 4.5rem;
  height: 4.5rem;
  object-fit: cover;
  border-radius: 8px;
  flex-shrink: 0;
}

.st-road {
  position: relative;
  flex: 1;
  height: 4px;
  background: #e5e5e5;
  border-radius: 2px;
}

.st-walker {
  position: absolute;
  top: 50%;
  left: 0;
  width: 36px;
  height: 36px;
  margin-top: -30px;
  object-fit: contain;
  mix-blend-mode: multiply;
}

.st-walker.go {
  animation-name: st-trip;
  animation-timing-function: linear;
  animation-fill-mode: forwards;
}

@keyframes st-trip {
  0%    { left: 0;                 transform: scaleX(1); }
  49.9% { left: calc(100% - 36px); transform: scaleX(1); }
  50%   { left: calc(100% - 36px); transform: scaleX(-1); }
  100%  { left: 0;                 transform: scaleX(-1); }
}

.st-count {
  align-self: center;
  font-family: var(--font-subtitle);
  font-size: 14px;
  font-weight: 600;
  opacity: 0;
}
.st-count.go {
  animation-name: st-fade;
  animation-duration: 0.3s;
  animation-fill-mode: forwards;
}
@keyframes st-fade { to { opacity: 1; } }
.st-before .st-count { color: #999; }
.st-after .st-count { color: var(--slidev-theme-primary); }

.st-note {
  text-align: center;
  font-family: var(--font-body);
  font-size: 14px;
  color: #777;
  line-height: 1.4;
}
</style>
