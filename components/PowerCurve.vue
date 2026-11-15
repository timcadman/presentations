<template>
<!--
  Power to detect an association with PM10 as cohorts are pooled,
  Cadman et al. (2024) Environ Int 185:108453.
-->
  <svg viewBox="0 22 720 308" preserveAspectRatio="xMinYMin meet" role="img" aria-label="Power to detect an association with PM10 rises as cohorts are added">
    <line x1="90" y1="30" x2="690" y2="30" stroke="#eee" />
    <line x1="90" y1="90" x2="690" y2="90" stroke="#eee" />
    <line x1="90" y1="150" x2="690" y2="150" stroke="#eee" />
    <line x1="90" y1="210" x2="690" y2="210" stroke="#eee" />
    <line x1="90" y1="78" x2="690" y2="78" stroke="#9AA0A6" stroke-width="1.5" stroke-dasharray="6 5" />
    <text style="font-size: 14px" x="690" y="72" fill="#9AA0A6" text-anchor="end">80% power</text>

    <line x1="90" y1="30" x2="90" y2="270" stroke="#999" stroke-width="1.5" />
    <line x1="90" y1="270" x2="690" y2="270" stroke="#999" stroke-width="1.5" />
    <text style="font-size: 14px" x="82" y="274" fill="#666" text-anchor="end">0%</text>
    <text style="font-size: 14px" x="82" y="214" fill="#666" text-anchor="end">25%</text>
    <text style="font-size: 14px" x="82" y="154" fill="#666" text-anchor="end">50%</text>
    <text style="font-size: 14px" x="82" y="94" fill="#666" text-anchor="end">75%</text>
    <text style="font-size: 14px" x="82" y="34" fill="#666" text-anchor="end">100%</text>
    <text style="font-size: 14px" x="90" y="288" fill="#666" text-anchor="middle">0</text>
    <text style="font-size: 14px" x="277.5" y="288" fill="#666" text-anchor="middle">10,000</text>
    <text style="font-size: 14px" x="465" y="288" fill="#666" text-anchor="middle">20,000</text>
    <text style="font-size: 14px" x="652.5" y="288" fill="#666" text-anchor="middle">30,000</text>
    <text style="font-size: 16px" x="390" y="312" fill="#555" text-anchor="middle">Cumulative sample size</text>
    <text style="font-size: 16px" x="0" y="0" fill="#555" text-anchor="middle" transform="translate(30,150) rotate(-90)">Power (OR 1.10 per IQR PM₁₀)</text>

    <g>
      <circle cx="112.1" cy="249.8" r="5" fill="#4285F4" />
      <text style="font-size: 15px" x="124" y="262" fill="#333">One cohort</text>
    </g>
    <g v-click>
      <polyline points="112.1,249.8 117.6,240.7 135.2,214.1 162.2,186.7 219.4,150.5" fill="none" stroke="#4285F4" stroke-width="3" />
      <circle cx="117.6" cy="240.7" r="5" fill="#4285F4" />
      <circle cx="135.2" cy="214.1" r="5" fill="#4285F4" />
      <circle cx="162.2" cy="186.7" r="5" fill="#4285F4" />
      <circle cx="219.4" cy="150.5" r="5" fill="#4285F4" />
      <text style="font-size: 15px" x="230" y="166" fill="#333">Five cohorts</text>
    </g>
    <g v-click>
      <polyline points="219.4,150.5 238.1,116.2 372.4,62.2" fill="none" stroke="#4285F4" stroke-width="3" />
      <circle cx="238.1" cy="116.2" r="5" fill="#4285F4" />
      <circle cx="372.4" cy="62.2" r="5" fill="#4285F4" />
      <text style="font-size: 15px" x="362" y="52" fill="#333" text-anchor="end">Seven cohorts</text>
    </g>
    <g v-click>
      <polyline points="372.4,62.2 430,48 493.5,39.6 551,34 608,31.4 666.8,30" fill="none" stroke="#4285F4" stroke-width="3" />
      <circle cx="430" cy="48" r="5" fill="#4285F4" />
      <circle cx="493.5" cy="39.6" r="5" fill="#4285F4" />
      <circle cx="551" cy="34" r="5" fill="#4285F4" />
      <circle cx="608" cy="31.4" r="5" fill="#4285F4" />
      <circle cx="666.8" cy="30" r="5" fill="#4285F4" />
      <text style="font-size: 15px" x="670" y="52" fill="#333" text-anchor="end">Twelve cohorts</text>
    </g>
  </svg>
</template>
