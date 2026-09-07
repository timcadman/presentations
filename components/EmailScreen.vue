<script setup>
import { useNav } from '@slidev/client'

const props = defineProps({
  from: {
    type: String,
    default: 'Data Access Committee <dac@umcg.nl>',
  },
  subject: {
    type: String,
    default: 'Access approved: OncoLifeS quality-of-life study',
  },
  link: {
    type: String,
    default: '',
  },
})

const { next } = useNav()
</script>

<template>
  <div class="em-window">
    <div class="em-meta">
      <div class="em-row">
        <span class="em-key">From</span>
        <span class="em-val">{{ from }}</span>
      </div>
      <div class="em-row">
        <span class="em-key">To</span>
        <span class="em-val">data.manager@umcg.nl</span>
      </div>
      <div class="em-row">
        <span class="em-key">Subject</span>
        <span class="em-val em-subject">{{ subject }}</span>
      </div>
    </div>

    <div class="em-body">
      <p>Dear data manager,</p>
      <p>
        Morris Swertz has been approved access via the Data Access Committee for
        <strong>OncoLifeS</strong>, for a study entitled &ldquo;Predicting chemotherapy
        completion from baseline quality of life&rdquo;.
      </p>
      <p>Click this link to grant analysis access via MOLGENIS Armadillo:</p>
      <a class="em-link" href="javascript:void(0)" @click="next()">{{ link }}</a>
    </div>
  </div>
</template>

<style scoped>
.em-window {
  height: 100%;
  display: flex;
  flex-direction: column;
  min-height: 0;
  border: 1px solid #c8ced4;
  border-radius: 7px;
  overflow: hidden;
  background: #fff;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.09);
  font-family: var(--font-subtitle);
}

.em-meta {
  flex: none;
  padding: 0.9rem 1.2rem;
  background: #f6f8fa;
  border-bottom: 1px solid #e2e6ea;
}

.em-row {
  display: flex;
  gap: 0.6rem;
  font-size: 13px;
  padding: 0.15rem 0;
}

.em-key {
  flex: none;
  width: 56px;
  color: #8a929b;
}

.em-val {
  color: #2b3440;
}

.em-subject {
  font-weight: 600;
}

.em-body {
  flex: 1;
  min-height: 0;
  overflow-y: auto;
  padding: 1.1rem 1.4rem;
  font-size: 14px;
  line-height: 1.5;
  color: #2b3440;
}

.em-body p {
  margin: 0 0 0.7rem 0;
}

.em-link {
  display: block;
  margin-top: 0.4rem;
  color: var(--slidev-theme-primary);
  text-decoration: underline;
  word-break: break-all;
  cursor: pointer;
  font-size: 13px;
}

.em-link:hover {
  opacity: 0.8;
}
</style>
