<script setup>
import ResearcherSession from './ResearcherSession.vue'
import ExwasPlot from './ExwasPlot.vue'

defineProps({
  height: {
    type: String,
    default: '17rem',
  },
  fileName: {
    type: String,
    default: 'exposome_analysis.R',
  },
  title: {
    type: String,
    default: 'RStudio — DataSHIELD',
  },
  wd: {
    type: String,
    default: '~/exposome/',
  },
  alwaysShow: {
    type: Boolean,
    default: true,
  },
  startAt: {
    type: Number,
    default: 1,
  },
  endAt: {
    type: Number,
    default: 0,
  },
})

// A still of a federated exposome session: one ExWAS model fitted across the
// servers and its plot. Shown whole by default — it is a picture of the
// platform, not a walkthrough.
const steps = [
  {
    code: 'ewas <- <span class="fn">ds.exwas</span>(\n  depression ~ sex + age,\n  <span class="arg">Set</span> = <span class="str">"exp"</span>,\n  <span class="arg">family</span> = <span class="str">"binomial"</span>)',
    output: '<span class="dim">exposure</span>      Estimate      SE       p\npm25           <span class="hl">0.182</span>   0.041  &lt;0.001\nno2            <span class="hl">0.134</span>   0.038  &lt;0.001\nndvi_300m     <span class="hl">-0.097</span>   0.035   0.006',
  },
  {
    code: '<span class="fn">ds.plotExwas</span>(ewas)',
    plot: true,
  },
]
</script>

<template>
  <div class="xs-frame" :style="{ height }">
    <ResearcherSession
      :steps="steps"
      :file-name="fileName"
      :title="title"
      :wd="wd"
      :always-show="alwaysShow"
      :plot-component="ExwasPlot"
      :start-at="startAt"
      :end-at="endAt"
    />
  </div>
</template>

<style scoped>
.xs-frame {
  min-height: 0;
}

/* the console pane is short, so cap the plot rather than let it spill */
.xs-frame :deep(.rs-console svg) {
  width: 100%;
  max-height: 5.5rem;
}
</style>
