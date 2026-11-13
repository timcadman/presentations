<script setup>
defineProps({
  beforeSteps: {
    type: Array,
    default: () => [
      'Check object exists',
      'Check object class',
      'Run operation',
      'Validate result',
    ],
  },
  afterSteps: {
    type: Array,
    default: () => ['Run operation\n(+ validation server-side)'],
  },
  // 'both' | 'before' | 'after'
  show: {
    type: String,
    default: 'both',
  },
  // 'center' | 'left' | 'right'
  align: {
    type: String,
    default: 'center',
  },
  scale: {
    type: Number,
    default: 1,
  },
})
</script>

<template>
  <div
    class="rt-wrap"
    :class="{ 'rt-solo': show !== 'both', 'rt-left': align === 'left', 'rt-right': align === 'right' }"
  >
    <div v-if="show !== 'after'" class="rt-panel" :style="{ zoom: scale }">
      <div v-if="show === 'both'" class="rt-label rt-label-before">Before</div>
      <div class="rt-diagram">
        <div class="rt-node">Client</div>
        <div class="rt-arrows">
          <div v-for="(step, i) in beforeSteps" :key="i" class="rt-trip rt-before">
            <span class="rt-step">{{ step }}</span>
            <div class="rt-arrow">
              <span class="rt-line" /><span class="rt-head rt-head-right" />
            </div>
            <div class="rt-arrow">
              <span class="rt-head rt-head-left" /><span class="rt-line" />
            </div>
          </div>
        </div>
        <div class="rt-node">Server</div>
      </div>
      <div v-if="show === 'both'" class="rt-count rt-count-before">{{ beforeSteps.length }} round trips</div>
      <div v-else class="rt-legend">
        <span><i class="rt-key rt-key-request" />Request</span>
        <span><i class="rt-key rt-key-result" />Result</span>
      </div>
    </div>

    <div v-if="show === 'both'" class="rt-arrow-between">→</div>

    <div v-if="show !== 'before'" class="rt-panel" :style="{ zoom: scale }">
      <div v-if="show === 'both'" class="rt-label rt-label-after">After</div>
      <div class="rt-diagram">
        <div class="rt-node">Client</div>
        <div class="rt-arrows">
          <div v-for="(step, i) in afterSteps" :key="i" class="rt-trip rt-after">
            <span class="rt-step">{{ step }}</span>
            <div class="rt-arrow">
              <span class="rt-line" /><span class="rt-head rt-head-right" />
            </div>
            <div class="rt-arrow">
              <span class="rt-head rt-head-left" /><span class="rt-line" />
            </div>
          </div>
        </div>
        <div class="rt-node">Server</div>
      </div>
      <div v-if="show === 'both'" class="rt-count rt-count-after">{{ afterSteps.length }} round trip</div>
      <div v-else class="rt-legend">
        <span><i class="rt-key rt-key-request" />Request</span>
        <span><i class="rt-key rt-key-result" />Result</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.rt-wrap {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 2.5rem;
  height: 100%;
}

.rt-left { justify-content: flex-start; }
.rt-left .rt-panel { align-items: flex-start; }
.rt-right { justify-content: flex-end; }
.rt-right .rt-panel { align-items: flex-end; }

.rt-panel {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
}

.rt-label {
  font-family: var(--font-subtitle);
  font-size: 18px;
  font-weight: 600;
}

.rt-label-before { color: #999; }
.rt-label-after { color: var(--slidev-theme-primary); }

.rt-diagram {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.rt-node {
  font-family: var(--font-subtitle);
  font-size: 16px;
  background: #fff;
  border: 2px solid var(--slidev-theme-primary);
  color: var(--slidev-theme-primary);
  border-radius: 8px;
  padding: 0.75rem 0.5rem;
  writing-mode: vertical-rl;
  text-orientation: mixed;
  transform: rotate(180deg);
}

.rt-arrows {
  display: flex;
  flex-direction: column;
  gap: 0.7rem;
}

.rt-trip {
  display: flex;
  flex-direction: column;
  align-items: stretch;
  width: 14rem;
}

.rt-step {
  font-family: var(--font-body);
  font-size: 12px;
  color: var(--slidev-theme-text);
  white-space: pre-line;
  text-align: center;
  margin-bottom: 0.15rem;
}

/* request (top) and response (bottom) arrows */
.rt-arrow {
  display: flex;
  align-items: center;
  height: 7px;
}

.rt-line {
  flex: 1;
  height: 2px;
}

.rt-head {
  width: 0;
  height: 0;
  border-top: 4px solid transparent;
  border-bottom: 4px solid transparent;
}

.rt-head-right { border-left-width: 7px; border-left-style: solid; }
.rt-head-left { border-right-width: 7px; border-right-style: solid; }

/* there-and-back arrows sit tight together as one round trip */
.rt-arrow + .rt-arrow { margin-top: 1px; }

/* colours */
.rt-before .rt-line { background: #bbb; }
.rt-before .rt-head-right { border-left-color: #bbb; }
.rt-before .rt-head-left { border-right-color: #bbb; }

.rt-after .rt-line { background: var(--slidev-theme-primary); }
.rt-after .rt-head-right { border-left-color: var(--slidev-theme-primary); }
.rt-after .rt-head-left { border-right-color: var(--slidev-theme-primary); }

/* standalone diagram: request and response in different colours */
.rt-solo .rt-arrow:first-of-type .rt-line { background: var(--slidev-theme-primary); }
.rt-solo .rt-head-right { border-left-color: var(--slidev-theme-primary); }
.rt-solo .rt-arrow:last-of-type .rt-line { background: var(--slidev-theme-secondary); }
.rt-solo .rt-head-left { border-right-color: var(--slidev-theme-secondary); }

.rt-legend {
  display: flex;
  gap: 1.25rem;
  margin-top: 0.5rem;
  font-family: var(--font-body);
  font-size: 13px;
  color: var(--slidev-theme-text);
}
.rt-legend span { display: flex; align-items: center; gap: 0.4rem; }
.rt-key { display: inline-block; width: 1.5rem; height: 2px; }
.rt-key-request { background: var(--slidev-theme-primary); }
.rt-key-result { background: var(--slidev-theme-secondary); }

.rt-count {
  font-family: var(--font-subtitle);
  font-size: 16px;
  font-weight: 600;
  padding: 0.25rem 0.85rem;
  border-radius: 6px;
}

.rt-count-before { color: #999; background: #f0f0f0; }
.rt-count-after { color: #fff; background: var(--slidev-theme-primary); }

.rt-arrow-between {
  font-family: var(--font-title);
  font-size: 60px;
  color: var(--slidev-theme-section-bg);
  margin-top: 1rem;
}
</style>
