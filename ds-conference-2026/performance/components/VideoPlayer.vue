<script setup>
import { computed, onBeforeUnmount, ref } from 'vue'

const props = defineProps({
  src: {
    type: String,
    required: true,
  },
  autoplay: {
    type: Boolean,
    default: false,
  },
  hideButton: {
    type: Boolean,
    default: false,
  },
  // seconds into the clip at which the stopwatch starts and stops;
  // the stopwatch is only shown when timerEnd is set
  timerStart: {
    type: Number,
    default: 0,
  },
  timerEnd: {
    type: Number,
    default: null,
  },
})

const video = ref(null)
const playing = ref(props.autoplay)
const currentTime = ref(0)
let frameRequest = null

const elapsedSeconds = computed(() => {
  const elapsed = Math.min(currentTime.value, props.timerEnd) - props.timerStart
  return Math.max(elapsed, 0).toFixed(1)
})

function toggle() {
  if (!video.value) return
  if (video.value.paused) {
    video.value.play()
  } else {
    video.value.pause()
  }
}

// timeupdate only fires a few times a second, too coarse for a tenths display
function followPlayback() {
  if (!video.value) return
  currentTime.value = video.value.currentTime
  frameRequest = requestAnimationFrame(followPlayback)
}

function startFollowing() {
  playing.value = true
  followPlayback()
}

function stopFollowing() {
  playing.value = false
  cancelAnimationFrame(frameRequest)
  if (video.value) currentTime.value = video.value.currentTime
}

onBeforeUnmount(() => cancelAnimationFrame(frameRequest))
</script>

<template>
  <div class="vp-wrap" @click="toggle">
    <video
      ref="video"
      :src="src"
      :autoplay="autoplay"
      muted
      playsinline
      class="vp-video"
      @play="startFollowing"
      @pause="stopFollowing"
    ></video>
    <div v-if="timerEnd !== null" class="vp-timer">{{ elapsedSeconds }} s</div>
    <div v-show="!playing && !hideButton" class="vp-button">
      <svg viewBox="0 0 24 24" width="28" height="28" fill="#fff">
        <path d="M8 5v14l11-7z" />
      </svg>
    </div>
  </div>
</template>

<style scoped>
.vp-wrap {
  position: absolute;
  inset: 0;
  background: transparent;
  cursor: pointer;
}

.vp-video {
  width: 100%;
  height: 100%;
  object-fit: contain;
  background: transparent;
}

.vp-timer {
  position: absolute;
  right: 0.5rem;
  bottom: 0.5rem;
  padding: 0.1rem 0.6rem;
  border-radius: 6px;
  background: rgba(0, 0, 0, 0.7);
  color: #fff;
  font-family: var(--font-subtitle);
  font-size: 22px;
  font-weight: 600;
  font-variant-numeric: tabular-nums;
}

.vp-button {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  pointer-events: none;
}

.vp-button svg {
  filter: drop-shadow(0 2px 6px rgba(0, 0, 0, 0.5));
}

.vp-button::before {
  content: '';
  position: absolute;
  width: 72px;
  height: 72px;
  border-radius: 50%;
  background: rgba(0, 0, 0, 0.45);
}
</style>
