<template>
  <div style="position: relative; display: inline-flex; align-items: center; gap: 2rem; margin-top: 1rem;">

    <!-- Local data -->
    <div style="text-align: left;">
      <p style="font-weight: 700; color: var(--slidev-theme-primary); margin-bottom: 0.5rem;">Local data</p>
      <div style="display: flex; flex-direction: column; gap: 0.75rem;">
        <div style="display: flex; align-items: center; gap: 0.5rem;"><img src="/icon-database.png" style="height: 40px;" /> <span style="font-size: 14px;">Cohort A</span></div>
        <div style="display: flex; align-items: center; gap: 0.5rem;"><img src="/icon-database.png" style="height: 40px;" /> <span style="font-size: 14px;">Cohort B</span></div>
        <div style="display: flex; align-items: center; gap: 0.5rem;"><img src="/icon-database.png" style="height: 40px;" /> <span style="font-size: 14px;">Cohort C</span></div>
      </div>
    </div>

    <!-- Arrows -->
    <div style="display: flex; flex-direction: column; align-items: center; padding-top: 2.2rem; gap: 0.75rem;">
      <div style="font-size: 1.5rem; color: var(--slidev-theme-primary); height: 40px; display: flex; align-items: center;">→</div>
      <div style="font-size: 1.5rem; color: var(--slidev-theme-primary); height: 40px; display: flex; align-items: center;">→</div>
      <div style="font-size: 1.5rem; color: var(--slidev-theme-primary); height: 40px; display: flex; align-items: center;">→</div>
    </div>

    <!-- Local servers -->
    <div style="text-align: left;">
      <p style="font-weight: 700; color: var(--slidev-theme-primary); margin-bottom: 0.5rem;">Local servers</p>
      <div style="display: flex; flex-direction: column; gap: 0.75rem;">
        <div style="display: flex; align-items: center; gap: 0.5rem;"><img src="/icon-server.png" style="height: 40px;" /> <span style="font-size: 14px;">Armadillo/Opal A</span></div>
        <div style="display: flex; align-items: center; gap: 0.5rem;"><img src="/icon-server.png" style="height: 40px;" /> <span style="font-size: 14px;">Armadillo/Opal B</span></div>
        <div style="display: flex; align-items: center; gap: 0.5rem;"><img src="/icon-server.png" style="height: 40px;" /> <span style="font-size: 14px;">Armadillo/Opal C</span></div>
      </div>
    </div>

    <!-- Animated commands / statistics -->
    <div style="display: flex; flex-direction: column; align-items: center; align-self: center; width: 130px;">
      <div style="text-align: center;">
        <p style="font-size: 12px; color: #888; margin: 0;">Analysis commands</p>
        <div class="arrow-left" style="font-size: 1.5rem; color: var(--slidev-theme-primary); line-height: 1;">←</div>
      </div>
      <div style="height: 10px;"></div>
      <div style="text-align: center;">
        <div class="arrow-right" style="font-size: 1.5rem; color: var(--slidev-theme-primary); line-height: 1;">→</div>
        <p style="font-size: 12px; color: #888; margin: 0;">Summary statistics</p>
      </div>
    </div>

    <!-- Researcher -->
    <div style="text-align: center; min-width: 80px;">
      <p style="font-weight: 700; color: var(--slidev-theme-primary); margin-bottom: 0.5rem;">Researcher</p>
      <img src="/icon-researcher.png" style="height: 60px; display: block; margin: 0 auto;" />
      <div style="display: flex; align-items: center; justify-content: center; gap: 0.4rem; margin-top: 0.5rem;">
        <img src="/icon-rstudio.png" style="height: 16px;" />
        <img src="/icon-datashield.png" style="height: 16px;" />
      </div>
    </div>

    <!-- Access path (static) -->
    <div style="position: absolute; bottom: -48px; left: 4%; right: 6%; height: 42px;">
      <div style="position: absolute; right: 0; top: 0; width: 2px; height: 100%; border-right: 2px dashed #4285F4;"></div>
      <div style="position: absolute; bottom: 0; left: 0; right: 0; height: 2px; border-bottom: 2px dashed #4285F4;"></div>
      <div style="position: absolute; left: 0; top: 0; width: 2px; height: 100%; border-left: 2px dashed #4285F4;"></div>
      <p style="position: absolute; bottom: -20px; left: 50%; transform: translateX(-50%); font-size: 12px; color: #888; white-space: nowrap; margin: 0;">Access granted to researcher</p>
    </div>

  </div>
</template>

<style scoped>
.arrow-left {
  animation: moveLeft 2.5s ease-in-out infinite;
}
.arrow-right {
  animation: moveRight 2.5s ease-in-out infinite;
}
@keyframes moveLeft {
  0% { transform: translateX(40px); opacity: 0; }
  10% { opacity: 1; }
  40% { opacity: 1; }
  50% { transform: translateX(-40px); opacity: 0; }
  100% { opacity: 0; }
}
@keyframes moveRight {
  0% { opacity: 0; }
  50% { transform: translateX(-40px); opacity: 0; }
  60% { opacity: 1; }
  90% { opacity: 1; }
  100% { transform: translateX(40px); opacity: 0; }
}
</style>
