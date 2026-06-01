<template>
  <div style="display: flex; align-items: flex-start; justify-content: flex-start; gap: 2rem; margin-top: 2rem; position: relative;">

    <!-- Local data (visually left, appears 2nd with arrows) -->
    <div v-click="2" style="text-align: left;">
      <p style="font-weight: 700; color: var(--slidev-theme-primary); margin-bottom: 0.5rem;">Local data</p>
      <div style="display: flex; flex-direction: column; gap: 0.75rem;">
        <div style="display: flex; align-items: center; gap: 0.5rem;"><img src="/icon-database.png" style="height: 40px;" /> <span style="font-size: 14px;">Cohort A</span></div>
        <div style="display: flex; align-items: center; gap: 0.5rem;"><img src="/icon-database.png" style="height: 40px;" /> <span style="font-size: 14px;">Cohort B</span></div>
        <div style="display: flex; align-items: center; gap: 0.5rem;"><img src="/icon-database.png" style="height: 40px;" /> <span style="font-size: 14px;">Cohort C</span></div>
      </div>
      <p v-click-hide="3" style="font-size: 12px; color: #888; margin-top: 0.5rem;">Upload data</p>
    </div>

    <!-- Arrows (appears 2nd, stays) -->
    <div v-click="2" style="display: flex; flex-direction: column; align-items: center; padding-top: 2.2rem; gap: 0.75rem;">
      <div style="font-size: 1.5rem; color: var(--slidev-theme-primary); height: 40px; display: flex; align-items: center;">→</div>
      <div style="font-size: 1.5rem; color: var(--slidev-theme-primary); height: 40px; display: flex; align-items: center;">→</div>
      <div style="font-size: 1.5rem; color: var(--slidev-theme-primary); height: 40px; display: flex; align-items: center;">→</div>
    </div>

    <!-- Local servers (visually right, appears 1st) -->
    <div v-click="1" style="text-align: left;">
      <p style="font-weight: 700; color: var(--slidev-theme-primary); margin-bottom: 0.5rem;">Local servers</p>
      <div style="display: flex; flex-direction: column; gap: 0.75rem;">
        <div style="display: flex; align-items: center; gap: 0.5rem;"><img src="/icon-server.png" style="height: 40px;" /> <span style="font-size: 14px;">Armadillo/Opal A</span></div>
        <div style="display: flex; align-items: center; gap: 0.5rem;"><img src="/icon-server.png" style="height: 40px;" /> <span style="font-size: 14px;">Armadillo/Opal B</span></div>
        <div style="display: flex; align-items: center; gap: 0.5rem;"><img src="/icon-server.png" style="height: 40px;" /> <span style="font-size: 14px;">Armadillo/Opal C</span></div>
      </div>
      <p v-click-hide="2" style="font-size: 12px; color: #888; margin-top: 0.5rem;">Setup server</p>
    </div>

    <!-- Animated arrows: commands with A, statistics with C -->
    <div v-click="5" style="display: flex; flex-direction: column; align-items: center; align-self: center; margin-top: 1rem; width: 120px;">
      <div style="text-align: center; height: 40px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
        <p style="font-size: 12px; color: #888; margin: 0;">Analysis commands</p>
        <div class="arrow-left" style="font-size: 1.5rem; color: var(--slidev-theme-primary); line-height: 1;">←</div>
      </div>
      <div style="height: 10px;"></div>
      <div style="text-align: center; height: 40px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
        <div class="arrow-right" style="font-size: 1.5rem; color: var(--slidev-theme-primary); line-height: 1;">→</div>
        <p style="font-size: 12px; color: #888; margin: 0;">Summary statistics</p>
      </div>
    </div>

    <!-- Researcher -->
    <div v-click="3" style="text-align: center; min-width: 80px;">
      <p style="font-weight: 700; color: var(--slidev-theme-primary); margin-bottom: 0.5rem;">Researcher</p>
      <div style="height: calc(40px + 0.75rem - 10px);"></div>
      <img src="/icon-researcher.png" style="height: 60px; display: block; margin: 0 auto;" />
      <div style="height: calc(0.75rem + 40px - 60px + 0.75rem);"></div>
      <div style="display: flex; align-items: center; justify-content: center; gap: 0.4rem;">
        <img src="/icon-rstudio.png" style="height: 16px;" />
        <img src="/icon-datashield.png" style="height: 16px;" />
      </div>
    </div>

    <!-- Applies for access + Access granted -->
    <div v-click="4" style="position: absolute; bottom: -55px; left: 5%; right: 33%; height: 50px;">
      <div style="position: absolute; right: 0; top: 0; width: 2px; height: 100%; border-right: 2px dashed #4285F4;"></div>
      <div style="position: absolute; bottom: 0; left: 0; right: 0; height: 2px; border-bottom: 2px dashed #4285F4;"></div>
      <div style="position: absolute; left: 0; top: 0; width: 2px; height: 100%; border-left: 2px dashed #4285F4;"></div>
      <div class="access-dot" style="position: absolute; width: 8px; height: 8px; background: #4285F4; border-radius: 50%;"></div>
      <p class="access-label" style="position: absolute; bottom: -18px; left: 50%; transform: translateX(-50%); font-size: 12px; color: #888; white-space: nowrap;">Applies for access</p>
      <p class="granted-label" style="position: absolute; bottom: -18px; left: 50%; transform: translateX(-50%); font-size: 12px; color: #888; white-space: nowrap; opacity: 0;">Access granted</p>
    </div>

  </div>
</template>

<style scoped>
.access-dot {
  animation: accessRoundTrip 6s linear forwards, hideDot 0.1s linear 6s forwards;
  animation-play-state: paused;
}
:deep(.slidev-vclick-target:not(.slidev-vclick-hidden)) .access-dot,
.slidev-vclick-target:not(.slidev-vclick-hidden) .access-dot {
  animation-play-state: running;
}
@keyframes accessRoundTrip {
  0%    { left: calc(100% - 4px); top: -4px; }
  5%    { left: calc(100% - 4px); top: 42px; }
  45%   { left: -4px; top: 42px; }
  50%   { left: -4px; top: -4px; }
  55%   { left: -4px; top: 42px; }
  95%   { left: calc(100% - 4px); top: 42px; }
  100%  { left: calc(100% - 4px); top: -4px; }
}
@keyframes hideDot {
  to { opacity: 0; }
}

.access-label {
  animation: hideAtHalf 6s step-end forwards;
  animation-play-state: paused;
}
:deep(.slidev-vclick-target:not(.slidev-vclick-hidden)) .access-label,
.slidev-vclick-target:not(.slidev-vclick-hidden) .access-label {
  animation-play-state: running;
}
@keyframes hideAtHalf {
  0%   { opacity: 1; }
  50%  { opacity: 0; }
  100% { opacity: 0; }
}

.granted-label {
  animation: showAtHalf 6s step-end forwards;
  animation-play-state: paused;
}
:deep(.slidev-vclick-target:not(.slidev-vclick-hidden)) .granted-label,
.slidev-vclick-target:not(.slidev-vclick-hidden) .granted-label {
  animation-play-state: running;
}
@keyframes showAtHalf {
  0%   { opacity: 0; }
  50%  { opacity: 1; }
  100% { opacity: 1; }
}

.arrow-left {
  animation: moveLeft 2.5s ease-in-out infinite;
  animation-play-state: paused;
}
:deep(.slidev-vclick-target:not(.slidev-vclick-hidden)) .arrow-left,
.slidev-vclick-target:not(.slidev-vclick-hidden) .arrow-left {
  animation-play-state: running;
}
.arrow-right {
  animation: moveRight 2.5s ease-in-out infinite;
  animation-play-state: paused;
}
:deep(.slidev-vclick-target:not(.slidev-vclick-hidden)) .arrow-right,
.slidev-vclick-target:not(.slidev-vclick-hidden) .arrow-right {
  animation-play-state: running;
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
