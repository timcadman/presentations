<script setup>
defineProps({
  submitLabel: { type: String, default: 'Submit' },
  submitDesc: { type: String, default: '' },
  finalLabel: { type: String, default: 'Fetch' },
  finalDesc: { type: String, default: '' },
})
</script>

<template>
  <div class="wrap">
    <div class="flow">
      <div class="node submit"><b>{{ submitLabel }}</b><small>{{ submitDesc }}</small></div>
      <span class="arrow">→</span>

      <div class="branch">
        <svg class="loopsvg" viewBox="0 0 34 100" preserveAspectRatio="none">
          <path d="M 27 4 C -6 4, -6 96, 27 96" fill="none" stroke="#0097a7" stroke-width="2.5" />
          <polygon points="27,102 20,90 34,90" fill="#0097a7" />
        </svg>
        <div class="pollcol">
          <div class="node poll"><b>Poll</b><small>GET /lastcommand</small></div>
          <div class="caption">PENDING / IN_PROGRESS</div>
          <div class="node sleep"><b>Sleep</b><small>50ms</small></div>
        </div>
        <svg class="loopsvg" viewBox="0 0 34 100" preserveAspectRatio="none">
          <path d="M 7 96 C 40 96, 40 4, 7 4" fill="none" stroke="#0097a7" stroke-width="2.5" />
          <polygon points="7,-2 0,10 14,10" fill="#0097a7" />
        </svg>
      </div>

      <div class="donewrap">
        <span class="donecap">COMPLETED<br />or FAILED</span>
        <span class="arrow">→</span>
      </div>

      <div class="node final"><b>{{ finalLabel }}</b><small>{{ finalDesc }}</small></div>
    </div>
  </div>
</template>

<style scoped>
.wrap { margin-top: 1.8rem; }
.flow {
  display: flex;
  align-items: center;
  gap: 0.4rem;
}
.node {
  padding: 0.75rem 0.75rem;
  border-radius: 8px;
  text-align: center;
  color: #fff;
  box-shadow: 0 1px 5px rgba(0, 0, 0, 0.13);
  min-width: 6.5rem;
}
.node b {
  display: block;
  font-family: var(--font-subtitle);
  font-size: 0.85rem;
}
.node small {
  display: block;
  font-size: 0.65rem;
  opacity: 0.9;
  margin-top: 0.25rem;
  line-height: 1.3;
}
.submit { background: #1e3a5f; }
.poll, .sleep { background: #0097a7; }
.final { background: #e6b96a; color: #5c4410; }
.arrow { color: #9aa4b0; font-size: 1.2rem; }

.branch {
  display: flex;
  align-items: stretch;
  gap: 0.2rem;
}
.loopsvg {
  width: 1.9rem;
  height: auto;
  align-self: stretch;
  overflow: visible;
}
.pollcol {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.35rem;
}
.caption {
  font-size: 0.6rem;
  color: #0097a7;
  font-family: var(--font-subtitle);
  letter-spacing: 0.01em;
  text-align: center;
  white-space: nowrap;
}
.donewrap {
  display: flex;
  flex-direction: column;
  align-items: center;
  font-size: 0.6rem;
  color: #b9852a;
  font-family: var(--font-subtitle);
  gap: 0.15rem;
  line-height: 1.15;
}
</style>
