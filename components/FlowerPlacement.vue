<script setup>
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'

const props = defineProps({
  // click on which Flower moves out of Rock into its own container
  standaloneAt: {
    type: Number,
    default: 1,
  },
  // enlarges or shrinks the whole diagram in proportion
  scale: {
    type: Number,
    default: 1,
  },
})

const { $clicks } = useSlideContext()
const isStandalone = computed(() => $clicks.value >= props.standaloneAt)
</script>

<template>
  <div class="fp-stage" :class="{ 'fp-standalone': isStandalone }" :style="{ zoom: scale }">

    <div class="fp-server">
      <div class="fp-server-label">
        <span :class="{ 'fp-on': !isStandalone }">Opal / Armadillo</span>
        <span :class="{ 'fp-on': isStandalone }">Armadillo</span>
      </div>

      <!-- Flower is a sibling of Rock in the markup, only drawn over it before
           the first click, so one element can slide from inside to alongside. -->
      <div class="fp-box fp-rock">
        <DockerIcon class="fp-container-icon" :height="20" />
        <p class="fp-title">Rock</p>
        <p class="fp-sub">DataSHIELD</p>
      </div>
      <div class="fp-box fp-flower">
        <DockerIcon class="fp-container-icon" :height="20" />
        <p class="fp-title">Flower</p>
        <p class="fp-sub">Federated learning</p>
      </div>
    </div>

  </div>
</template>

<style scoped>
.fp-stage {
  position: relative;
  width: 350px;
  height: 204px;
  margin: 0;
}
.fp-stage p {
  margin: 0;
}

.fp-server {
  position: absolute;
  top: 0;
  left: 0;
  width: 350px;
  height: 200px;
  border: 2px solid var(--slidev-theme-primary);
  border-radius: 12px;
  background: color-mix(in srgb, var(--slidev-theme-primary) 8%, white);
}
.fp-server-label span {
  position: absolute;
  top: 12px;
  left: 16px;
  font-weight: 700;
  font-size: 15px;
  color: var(--slidev-theme-primary);
  opacity: 0;
  transition: opacity 0.5s ease;
}
.fp-server-label span.fp-on {
  opacity: 1;
}

.fp-box {
  position: absolute;
  box-sizing: border-box;
  padding: 10px 14px;
  border: 2px solid;
  border-radius: 10px;
  transition: left 0.7s ease, top 0.7s ease, width 0.7s ease, height 0.7s ease, opacity 0.5s ease;
}
.fp-title {
  font-weight: 700;
  font-size: 15px;
  line-height: 1.3;
}
.fp-sub {
  font-size: 12px;
  line-height: 1.3;
  color: var(--slidev-theme-text);
}

/* The whale marks a box as its own Docker container. Flower only gets one
   once it has moved out of Rock. */
.fp-container-icon {
  position: absolute;
  top: 9px;
  right: 12px;
  color: #1E3A5F;
  transition: opacity 0.5s ease;
}
.fp-flower .fp-container-icon {
  opacity: 0;
}
.fp-standalone .fp-flower .fp-container-icon {
  opacity: 1;
  transition-delay: 0.5s;
}

.fp-rock {
  left: 14px;
  top: 44px;
  width: 322px;
  height: 136px;
  border-color: #E35000;
  background: color-mix(in srgb, #E35000 10%, white);
}
.fp-rock .fp-title {
  color: #E35000;
}
.fp-standalone .fp-rock {
  width: 154px;
}

.fp-flower {
  left: 172px;
  top: 80px;
  width: 150px;
  height: 84px;
  border-color: #FDAE00;
  background: #FFEFCC;
}
.fp-flower .fp-title {
  color: #B9852A;
}
.fp-standalone .fp-flower {
  left: 182px;
  top: 44px;
  width: 154px;
  height: 136px;
}
</style>
