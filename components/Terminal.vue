<script setup>
import { onUnmounted, ref, watch } from 'vue'
import { useSlideContext } from '@slidev/client'

const props = defineProps({
  title: {
    type: String,
    default: 'claude',
  },
  text: {
    type: String,
    default: '',
  },
  charMs: {
    type: Number,
    default: 55,
  },
  startDelay: {
    type: Number,
    default: 300,
  },
  startAtClick: {
    type: Number,
    default: 1,
  },
})

const { $clicks } = useSlideContext()
const shown = ref('')
let timer = null
let started = false

function startTyping() {
  if (started) return
  started = true
  let i = 0
  const tick = () => {
    i += 1
    shown.value = props.text.slice(0, i)
    if (i < props.text.length) timer = setTimeout(tick, props.charMs)
  }
  timer = setTimeout(tick, props.startDelay)
}

watch(
  () => $clicks.value,
  (clicks, prevClicks) => {
    if (clicks < props.startAtClick) return
    // already past the trigger click on mount (e.g. navigating back in) — show it straight away
    if (prevClicks === undefined) {
      started = true
      shown.value = props.text
      return
    }
    startTyping()
  },
  { immediate: true }
)

onUnmounted(() => {
  if (timer) clearTimeout(timer)
})
</script>

<template>
  <div class="tm-window">
    <div class="tm-titlebar">
      <span class="tm-dot tm-dot-r"></span>
      <span class="tm-dot tm-dot-y"></span>
      <span class="tm-dot tm-dot-g"></span>
      <span class="tm-title">{{ title }}</span>
    </div>
    <div class="tm-body">
      <span class="tm-prompt">$</span>
      <pre class="tm-text">{{ shown }}<span class="tm-cursor"></span></pre>
    </div>
  </div>
</template>

<style scoped>
.tm-window {
  height: 100%;
  display: flex;
  flex-direction: column;
  min-height: 0;
  border-radius: 7px;
  overflow: hidden;
  background: #1e2530;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.25);
}

.tm-titlebar {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.4rem 0.7rem;
  background: #171c24;
  flex: none;
}

.tm-dot { width: 9px; height: 9px; border-radius: 50%; display: inline-block; }
.tm-dot-r { background: #ff5f57; }
.tm-dot-y { background: #febc2e; }
.tm-dot-g { background: #28c840; }

.tm-title {
  margin-left: auto;
  margin-right: auto;
  font-family: var(--font-subtitle);
  font-size: 11px;
  color: #8a96a6;
}

.tm-body {
  flex: 1;
  min-height: 0;
  overflow: hidden;
  padding: 1.1rem 1.4rem;
  display: flex;
  gap: 0.6rem;
}

.tm-prompt {
  flex: none;
  font-family: var(--font-subtitle);
  font-size: 11px;
  font-weight: 700;
  color: var(--slidev-theme-primary);
}

.tm-text {
  margin: 0;
  flex: 1;
  min-width: 0;
  font-family: var(--font-subtitle);
  font-size: 11px;
  line-height: 1.6;
  color: #d7dde5;
  white-space: pre-wrap;
  word-break: break-word;
}

.tm-cursor {
  display: inline-block;
  width: 0.55em;
  height: 1em;
  background: var(--slidev-theme-primary);
  vertical-align: text-bottom;
  animation: tm-blink 1s step-end infinite;
}

@keyframes tm-blink {
  0%, 50% { opacity: 1; }
  50.01%, 100% { opacity: 0; }
}
</style>
