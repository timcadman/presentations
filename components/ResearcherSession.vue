<script setup>
import { computed, reactive, watch } from 'vue'
import Ql2Histograms from './Ql2Histograms.vue'
import ChemoTable from './ChemoTable.vue'
import ForestPlot from './ForestPlot.vue'
import { useSlideContext } from '@slidev/client'

const props = defineProps({
  fileName: {
    type: String,
    default: 'uncan_demo.R',
  },
  startAt: {
    type: Number,
    default: 1,
  },
  endAt: {
    type: Number,
    default: 0,
  },
  alwaysShow: {
    type: Boolean,
    default: false,
  },
  leadingPrompt: {
    type: Boolean,
    default: false,
  },
  steps: {
    type: Array,
    default: () => [
      {
        code: 'login_details <- <span class="fn">list</span>(\n  <span class="arg">server</span> = <span class="fn">c</span>(<span class="str">"server_1"</span>, <span class="str">"server_2"</span>, <span class="str">"server_3"</span>),\n  <span class="arg">url</span> = <span class="fn">c</span>(\n    <span class="str">"http://localhost:8080"</span>,\n    <span class="str">"http://localhost:8081"</span>,\n    <span class="str">"http://localhost:8082"</span>))',
        output: '',
      },
      {
        code: 'credentials <- <span class="fn">map</span>(\n  login_details$url,\n  <span class="fn">armadillo.get_credentials</span>)',
        output: '[1] <span class="str">"We\'re opening a browser so you can log in with code PGTN-AUVD"</span>',
        promptDelay: 2,
      },
      {
        code: '',
        output: '',
      },
      {
        code: '',
        output: '',
      },
      {
        code: 'logindata <- <span class="fn">build_logindata</span>(\n  login_details,\n  <span class="arg">table</span> = <span class="str">"project-1/data/core"</span>,\n  <span class="arg">credentials</span> = credentials)',
        output: '',
      },
      {
        code: 'conns <- DSI::<span class="fn">datashield.login</span>(\n  <span class="arg">logins</span> = logindata,\n  <span class="arg">assign</span> = TRUE,\n  <span class="arg">symbol</span> = <span class="str">"data"</span>)',
        frames: [
          'Logging into the collaborating servers\n<span class="dim">  Login server_1</span> [=====>----------------]  25% / 3s',
          'Logging into the collaborating servers\n<span class="dim">  Login server_2</span> [==========>-----------]  50% / 7s',
          'Logging into the collaborating servers\n<span class="dim">  Login server_3</span> [===============>------]  75% / 10s',
          'Logging into the collaborating servers\n<span class="dim">  Logged in all servers</span> [======================] 100% /13s',
          'Logging into the collaborating servers\n<span class="dim">  Logged in all servers</span> [======================] 100% /13s\n<span class="dim">  Assigning (data &lt;- ...)</span> [=====>----------------]  25% / 2s',
          'Logging into the collaborating servers\n<span class="dim">  Logged in all servers</span> [======================] 100% /13s\n<span class="dim">  Assigning (data &lt;- ...)</span> [==========>-----------]  50% / 3s',
          'Logging into the collaborating servers\n<span class="dim">  Logged in all servers</span> [======================] 100% /13s\n<span class="dim">  Assigning (data &lt;- ...)</span> [===============>------]  75% / 5s',
          'Logging into the collaborating servers\n<span class="dim">  Logged in all servers</span> [======================] 100% /13s\n<span class="dim">  Assigned all table (data &lt;- ...)</span> [======================] 100% / 6s',
        ],
      },
      {
        code: '<span class="fn">ds.colnames</span>(<span class="str">"data"</span>)',
        output: '$server_1\n[1] "ql2_baseline"              "chemo_modification_reason" "age_at_diagnosis"\n[4] "figo_stage"                "charlson_score"\n\n$server_2\n[1] "ql2_baseline"              "chemo_modification_reason" "age_at_diagnosis"\n[4] "figo_stage"                "charlson_score"\n\n$server_3\n[1] "ql2_baseline"              "chemo_modification_reason" "age_at_diagnosis"\n[4] "figo_stage"                "charlson_score"',
      },
      {
        code: '<span class="fn">ds.histogram</span>(<span class="str">"data$ql2_baseline"</span>)',
        clear: true,
        plot: true,
        frameMs: 650,
        frames: [
          '<span class="dim">  Aggregating server_1</span> [=====>----------------]  25%',
          '<span class="dim">  Aggregating server_2</span> [==========>-----------]  50%',
          '<span class="dim">  Aggregating server_3</span> [===============>------]  75%',
          '<span class="dim">  Aggregated (histogramDS1(data$ql2_baseline,1,3,0.25))</span> [======================] 100%',
        ],
      },
      {
        code: '<span class="fn">ds.table</span>(<span class="str">"data$chemo_modification_reason"</span>)',
        table: true,
        frameMs: 650,
        frames: [
          '<span class="dim">  Aggregating server_1</span> [=====>----------------]  25%',
          '<span class="dim">  Aggregating server_2</span> [==========>-----------]  50%',
          '<span class="dim">  Aggregating server_3</span> [===============>------]  75%',
          '<span class="dim">  Aggregated (tableDS(data$chemo_modification_reason))</span> [======================] 100%',
        ],
      },
      {
        code: 'mod <- <span class="fn">ds.glmSLMA</span>(\n  modified ~ ql2_baseline + age_at_diagnosis + charlson_score,\n  <span class="arg">family</span> = <span class="str">"binomial"</span>,\n  <span class="arg">dataName</span> = <span class="str">"data"</span>)',
        clear: true,
        frameMs: 975,
        frames: [
          '<span class="dim">  Aggregating server_1</span> [=====>----------------]  25%',
          '<span class="dim">  Aggregating server_2</span> [==========>-----------]  50%',
          '<span class="dim">  Aggregating server_3</span> [===============>------]  75%',
          '<span class="dim">  Aggregated (glmSLMADS2(modified~ql2_baseline+...))</span> [======================] 100%',
        ],
        output: '<span class="dim">ql2_baseline, per study</span>\n           Estimate      SE       p\nserver_1   <span class="hl">-0.0217</span>  0.0044  <0.001\nserver_2   <span class="hl">-0.0180</span>  0.0034  <0.001\nserver_3   <span class="hl">-0.0052</span>  0.0050   0.295\n<span class="dim">-----------------------------------</span>\ncombined   <span class="hl">-0.0154</span>  0.0044  <0.001',
      },
      {
        code: '<span class="fn">ds.forestplot</span>(mod, <span class="arg">variable</span> = <span class="str">"ql2_baseline"</span>)',
        forest: true,
      },
    ],
  },
})

const shownSteps = computed(() => {
  const end = props.endAt > 0 ? props.endAt : props.steps.length
  return props.steps.slice(props.startAt - 1, end)
})

const clickPlan = computed(() => {
  let n = 0
  const plan = shownSteps.value.map((step) => {
    const cmdStep = ++n
    const outStep = (step.output || step.frames || step.plot || step.table || step.forest) ? ++n : null
    return { step, cmdStep, outStep }
  })
  // a step marked `clear` wipes the pane: everything before it stops showing
  // once its own click is reached, so the session starts fresh from there.
  return plan.map((entry, i) => {
    const next = plan.slice(i + 1).find((e) => e.step.clear)
    return { ...entry, clearedAt: next ? next.cmdStep : Number.POSITIVE_INFINITY }
  })
})

const codeLines = computed(() => {
  const rows = []
  clickPlan.value.forEach((entry, i) => {
    if (!entry.step.code) return
    if (i > 0 && !entry.step.clear) rows.push({ html: '', step: entry.cmdStep, clearedAt: entry.clearedAt })
    entry.step.code.split('\n').forEach((line) =>
      rows.push({ html: line, step: entry.cmdStep, clearedAt: entry.clearedAt })
    )
  })
  return rows
})

const { $clicks } = useSlideContext()
const frameIndex = reactive({})
const running = {}

watch(
  () => $clicks.value,
  (clicks) => {
    clickPlan.value.forEach((entry) => {
      const frames = entry.step.frames
      if (!frames || entry.outStep === null) return
      if (clicks < entry.outStep) {
        frameIndex[entry.cmdStep] = 0
        running[entry.cmdStep] = false
        return
      }
      if (running[entry.cmdStep]) return
      running[entry.cmdStep] = true
      frameIndex[entry.cmdStep] = 0
      const tick = () => {
        if (frameIndex[entry.cmdStep] < frames.length - 1) {
          frameIndex[entry.cmdStep] += 1
          setTimeout(tick, entry.step.frameMs || 840)
        }
      }
      setTimeout(tick, (entry.step.frameMs || 840) + 400)
    })
  },
  { immediate: true }
)

const consoleEntries = computed(() =>
  clickPlan.value.map((entry) => ({
    cmdStep: entry.cmdStep,
    outStep: entry.outStep,
    clearedAt: entry.clearedAt,
    cmd: entry.step.code.split('\n').map((l, k) => ({ prompt: k === 0 ? '>' : '+', html: l })),
    output: (() => {
      const f = entry.step.frames
      if (!f) return entry.step.output
      const i = Math.min(frameIndex[entry.cmdStep] ?? 0, f.length - 1)
      if (i >= f.length - 1 && entry.step.output) return entry.step.output
      return f[i]
    })(),
    plot: entry.step.plot === true,
    table: entry.step.table === true,
    promptStep: entry.outStep !== null ? entry.outStep + (entry.step.promptDelay || 0) : null,
    forest: entry.step.forest === true,
    done: entry.step.frames
      ? (frameIndex[entry.cmdStep] ?? 0) >= entry.step.frames.length - 1
      : true,
  }))
)
</script>

<template>
  <div class="rs-window">
    <div class="rs-titlebar">
      <span class="rs-dot rs-dot-r"></span>
      <span class="rs-dot rs-dot-y"></span>
      <span class="rs-dot rs-dot-g"></span>
      <span class="rs-title">RStudio &mdash; UNCAN demo</span>
    </div>

    <div class="rs-panes">
      <div class="rs-pane">
        <div class="rs-tabbar"><span class="rs-tab rs-tab-active">{{ fileName }}</span></div>
        <div class="rs-body rs-editor">
          <div v-for="(row, i) in codeLines" :key="i" v-show="alwaysShow || ($clicks >= row.step && $clicks < row.clearedAt)" class="rs-row">
            <span class="rs-gutter">{{ i + 1 }}</span>
            <span class="rs-code" v-html="row.html || '&nbsp;'"></span>
          </div>
        </div>
      </div>

      <div class="rs-pane">
        <div class="rs-tabbar"><span class="rs-tab rs-tab-active">Console</span></div>
        <div class="rs-body rs-console">
          <div v-if="leadingPrompt" class="rs-cmdline"><span class="rs-prompt">&gt;</span></div>
          <div v-for="entry in consoleEntries" :key="entry.cmdStep" class="rs-entry">
            <div v-if="entry.forest" v-show="alwaysShow || ($clicks >= entry.outStep && $clicks < entry.clearedAt)">
              <ForestPlot />
              <div class="rs-cmdline"><span class="rs-prompt">&gt;</span></div>
            </div>
            <div v-else-if="entry.table" v-show="alwaysShow || ($clicks >= entry.outStep && $clicks < entry.clearedAt)">
              <pre v-if="entry.output && !entry.done" class="rs-out" v-html="entry.output"></pre>
              <ChemoTable v-if="entry.done" />
              <div v-if="entry.done" v-show="$clicks >= entry.promptStep" class="rs-cmdline"><span class="rs-prompt">&gt;</span></div>
            </div>
            <div v-else-if="entry.plot" v-show="alwaysShow || ($clicks >= entry.outStep && $clicks < entry.clearedAt)">
              <pre v-if="entry.output && !entry.done" class="rs-out" v-html="entry.output"></pre>
              <Ql2Histograms v-if="entry.done" />
              <div v-if="entry.done" v-show="$clicks >= entry.promptStep" class="rs-cmdline"><span class="rs-prompt">&gt;</span></div>
            </div>
            <div v-else-if="entry.output" v-show="alwaysShow || ($clicks >= entry.outStep && $clicks < entry.clearedAt)">
              <pre class="rs-out" v-html="entry.output"></pre>
              <div v-if="entry.done" v-show="$clicks >= entry.promptStep" class="rs-cmdline"><span class="rs-prompt">&gt;</span></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.rs-window {
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

.rs-titlebar {
  display: flex;
  align-items: center;
  gap: 0.35rem;
  padding: 0.3rem 0.6rem;
  background: linear-gradient(#f7f8f9, #eceff1);
  border-bottom: 1px solid #c8ced4;
  flex: none;
}

.rs-dot { width: 9px; height: 9px; border-radius: 50%; display: inline-block; }
.rs-dot-r { background: #ff5f57; }
.rs-dot-y { background: #febc2e; }
.rs-dot-g { background: #28c840; }

.rs-title {
  margin-left: auto;
  margin-right: auto;
  font-family: var(--font-subtitle);
  font-size: 10px;
  color: #6b7480;
}

.rs-panes {
  display: grid;
  grid-template-columns: 0.82fr 1.18fr;
  flex: 1;
  min-height: 0;
}

.rs-pane {
  display: flex;
  flex-direction: column;
  min-height: 0;
  min-width: 0;
}

.rs-pane + .rs-pane { border-left: 1px solid #d7dce1; }

.rs-tabbar {
  flex: none;
  background: #eef1f4;
  border-bottom: 1px solid #d7dce1;
  padding: 0 0.35rem;
}

.rs-tab {
  display: inline-block;
  font-family: var(--font-subtitle);
  font-size: 10px;
  color: #4a5561;
  padding: 0.28rem 0.6rem;
}

.rs-tab-active {
  background: #fff;
  border: 1px solid #d7dce1;
  border-bottom: 1px solid #fff;
  border-radius: 3px 3px 0 0;
  margin-bottom: -1px;
  color: #1f2933;
}

.rs-body {
  flex: 1;
  min-height: 0;
  overflow: hidden;
  padding: 0.3rem 0 0.3rem 0;
  background: #fff;
}

.rs-console .rs-out,
.rs-console .rs-prompt {
  font-size: 9px;
  line-height: 1.45;
}

.rs-console {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  padding-left: 0.45rem;
  padding-right: 0.25rem;
}

.rs-row { display: flex; align-items: baseline; }

@keyframes rs-in {
  from { opacity: 0; }
  to   { opacity: 1; }
}

.rs-row {
  animation: rs-in 0.25s ease 0.12s both;
}

.rs-entry > * {
  animation: rs-in 0.25s ease 0.4s both;
}

.rs-gutter {
  flex: none;
  width: 2rem;
  text-align: right;
  padding-right: 0.55rem;
  margin-right: 0.5rem;
  border-right: 1px solid #edf0f3;
  font-family: var(--font-subtitle);
  font-size: 8.5px;
  color: #b3bcc5;
  user-select: none;
}

.rs-code,
.rs-out,
.rs-prompt {
  font-family: var(--font-subtitle);
  font-size: 9px;
  line-height: 1.45;
  white-space: pre-wrap;
  word-break: break-word;
}

.rs-code { color: #1f2933; }

.rs-entry + .rs-entry { margin-top: 0.75rem; }

.rs-cmdline { display: flex; align-items: baseline; }

.rs-prompt {
  flex: none;
  color: #4285F4;
  font-weight: 700;
  width: 0.9rem;
}

.rs-out {
  margin: 0;
  color: #3d4852;
}

:deep(.fn) { color: #4285F4; }
:deep(.str) { color: #B9852A; }
:deep(.arg) { color: #6A4C93; }
:deep(.hl) { color: #B9852A; font-weight: 700; }
:deep(.dim) { color: #9AA0A6; }
</style>
