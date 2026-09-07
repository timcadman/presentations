<script setup>
import { useSlideContext } from '@slidev/client'

defineProps({
  requester: {
    type: String,
    default: 'morris.swertz@umcg.nl',
  },
  table: {
    type: String,
    default: 'uncan-connect/data/core.parquet',
  },
  project: {
    type: String,
    default: 'project-1',
  },
  variables: {
    type: Array,
    default: () => [
      'ql2_baseline',
      'chemo_modification_reason',
      'age_at_diagnosis',
      'figo_stage',
      'charlson_score',
    ],
  },
})

const { $clicks } = useSlideContext()
</script>

<template>
  <div class="as-window">
    <div class="as-titlebar">
      <span class="as-dot as-dot-r"></span>
      <span class="as-dot as-dot-y"></span>
      <span class="as-dot as-dot-g"></span>
      <div class="as-addressbar">
        <span v-if="$clicks < 3">localhost:8081/#/r/{{ project }}/{{ requester }}/&hellip;</span>
        <span v-else>localhost:8081/#/projects/{{ project }}</span>
      </div>
    </div>

    <div class="as-body">
      <!-- Step 0-2: access request page -->
      <div v-show="$clicks < 3" class="as-request">
        <h1 class="as-h1">Access request</h1>

        <div class="as-row">
          <span class="as-key">Requested by</span>
          <span class="as-val">{{ requester }}</span>
        </div>
        <div class="as-row">
          <span class="as-key">Source table</span>
          <span class="as-val as-mono">{{ table }}</span>
        </div>
        <div class="as-row as-row-top">
          <span class="as-key">Variables</span>
          <ul class="as-varlist">
            <li v-for="v in variables" :key="v">{{ v }}</li>
          </ul>
        </div>

        <div class="as-actions">
          <button class="as-btn as-btn-ghost">Decline</button>
          <button class="as-btn as-btn-primary" :class="{ 'as-pressed': $clicks === 1 }">Approve</button>
        </div>

        <div v-show="$clicks >= 1" class="as-toast">
          <span v-if="$clicks === 1" class="as-dim">Creating project&hellip;</span>
          <span v-else>&#10003; Request approved &mdash; project <strong>{{ project }}</strong> created</span>
        </div>
      </div>

      <!-- Step 3: project file browser -->
      <div v-show="$clicks >= 3" class="as-explorer">
        <h1 class="as-h1">Project: {{ project }}</h1>
        <div class="as-tree">
          <div class="as-node as-node-folder">
            <span class="as-icon">&#128193;</span> data
          </div>
          <div class="as-node as-node-file as-node-indent">
            <span class="as-icon">&#128196;</span> core.parquet
            <span class="as-meta">{{ variables.length }} columns</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.as-window {
  height: 100%;
  display: flex;
  flex-direction: column;
  min-height: 0;
  border: 1px solid #c8ced4;
  border-radius: 7px;
  overflow: hidden;
  background: #fff;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.09);
}

.as-titlebar {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.35rem 0.6rem;
  background: linear-gradient(#f7f8f9, #eceff1);
  border-bottom: 1px solid #c8ced4;
  flex: none;
}

.as-dot {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  display: inline-block;
}
.as-dot-r { background: #ff5f57; }
.as-dot-y { background: #febc2e; }
.as-dot-g { background: #28c840; }

.as-addressbar {
  margin-left: 0.6rem;
  flex: 1;
  background: #fff;
  border: 1px solid #d7dce1;
  border-radius: 12px;
  padding: 0.15rem 0.75rem;
  font-family: var(--font-subtitle);
  font-size: 11px;
  color: #4a5561;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.as-body {
  flex: 1;
  min-height: 0;
  padding: 1.3rem 1.6rem;
  overflow: hidden;
}

.as-h1 {
  font-family: var(--font-title);
  font-size: 26px;
  font-weight: 400;
  color: var(--slidev-theme-primary);
  margin: 0 0 0.9rem 0;
}

.as-row {
  display: flex;
  align-items: baseline;
  gap: 0.6rem;
  padding: 0.35rem 0;
  border-bottom: 1px solid #edf0f3;
  font-family: var(--font-subtitle);
  font-size: 13px;
}

.as-row-top {
  align-items: flex-start;
}

.as-key {
  flex: none;
  width: 120px;
  color: #8a929b;
}

.as-val {
  color: #2b3440;
}

.as-mono {
  font-family: var(--font-subtitle);
}

.as-varlist {
  margin: 0;
  padding-left: 1.1rem;
  color: #2b3440;
}
.as-varlist li {
  margin-bottom: 0.15rem;
}

.as-actions {
  margin-top: 1.1rem;
  display: flex;
  gap: 0.6rem;
  justify-content: flex-end;
}

.as-btn {
  font-family: var(--font-subtitle);
  font-size: 12.5px;
  padding: 0.4rem 1.1rem;
  border-radius: 5px;
  border: 1px solid transparent;
  cursor: default;
  transition: transform 0.15s ease;
}

.as-btn-ghost {
  background: #fff;
  border-color: #d7dce1;
  color: #4a5561;
}

.as-btn-primary {
  background: var(--slidev-theme-primary);
  color: #fff;
}

.as-pressed {
  transform: scale(0.96);
}

.as-toast {
  margin-top: 0.9rem;
  font-family: var(--font-subtitle);
  font-size: 12.5px;
  color: #1e824c;
}

.as-dim {
  color: #9aa0a6;
}

.as-tree {
  font-family: var(--font-subtitle);
  font-size: 13px;
  color: #2b3440;
}

.as-node {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.4rem 0.5rem;
  border-radius: 4px;
}

.as-node-folder {
  font-weight: 600;
}

.as-node-indent {
  margin-left: 1.6rem;
  background: rgba(66, 133, 244, 0.06);
}

.as-icon {
  font-size: 14px;
}

.as-meta {
  margin-left: auto;
  color: #9aa0a6;
  font-size: 11px;
}
</style>
