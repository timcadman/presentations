<script setup>
import { ref } from 'vue'

const props = defineProps({
  src: {
    type: String,
    required: true,
  },
  autoplay: {
    type: Boolean,
    default: false,
  },
})

const video = ref(null)
const playing = ref(props.autoplay)

function toggle() {
  if (!video.value) return
  if (video.value.paused) {
    video.value.play()
  } else {
    video.value.pause()
  }
}
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
      @play="playing = true"
      @pause="playing = false"
    ></video>
    <div v-show="!playing" class="vp-button">
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
  background: #000;
  cursor: pointer;
}

.vp-video {
  width: 100%;
  height: 100%;
  object-fit: contain;
  background: #000;
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
