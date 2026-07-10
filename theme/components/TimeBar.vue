<script setup>
// A single horizontal bar split into labelled, colour-coded segments — a
// conceptual decomposition (no numbers). `segments` = [{ label, desc, color,
// textColor, flex }], where `flex` is each segment's relative width. Pass
// `:clicks="$clicks"` and the bar extends one segment per click (left to right);
// unrevealed segments show as an empty track.
import { computed } from 'vue'

const props = defineProps({
  segments: { type: Array, required: true },
  caption: { type: String, default: '' },
  clicks: { type: Number, default: 9999 },
  startEmpty: { type: Boolean, default: false },   // if true, click 0 shows the empty track; segments fill from click 1
})

const total = computed(() => props.segments.reduce((sum, s) => sum + (s.flex || 1), 0))
const widthPct = (s) => ((s.flex || 1) / total.value) * 100
const shown = (i) => props.clicks >= i + (props.startEmpty ? 1 : 0)
</script>

<template>
  <div class="tb">
    <div class="tb-bar">
      <div
        v-for="(s, i) in segments"
        :key="i"
        class="tb-seg"
        :class="{ 'tb-hidden': !shown(i) }"
        :style="{ width: widthPct(s) + '%', background: s.color, color: s.textColor || '#fff' }"
      >
        <b>{{ s.label }}</b>
        <small v-if="s.desc">{{ s.desc }}</small>
      </div>
    </div>
    <div v-if="caption" class="tb-cap">{{ caption }}</div>
  </div>
</template>

<style scoped>
.tb { margin-top: 1.6rem; }
.tb-bar {
  display: flex;
  border-radius: 8px;
  overflow: hidden;
  background: #eef1f6;
  box-shadow: 0 1px 5px rgba(0, 0, 0, 0.13);
}
.tb-seg {
  flex: 0 0 auto;
  min-width: 0;
  padding: 1rem 0.85rem;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 0.28rem;
  transition: opacity 0.4s ease;
}
.tb-hidden { opacity: 0; }
.tb-seg b { font-family: var(--font-subtitle); font-size: 1rem; line-height: 1.2; }
.tb-seg small { font-size: 0.8rem; opacity: 0.93; line-height: 1.25; }
.tb-cap {
  text-align: center;
  color: #6A4C93;
  font-family: var(--font-subtitle);
  font-size: 0.9rem;
  margin-top: 0.9rem;
  letter-spacing: 0.04em;
}
</style>
