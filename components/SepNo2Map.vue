<template>
<!--
  Pregnancy NO2 in high- vs lower-SEP areas by city, Robinson et al. (2018)
  Environ Health Perspect 126(7):077005. Three registered layers so the
  slide can reveal the two directions on click. Paths are root-absolute
  because a component cannot resolve a deck-relative one: the consuming deck
  needs ihen_ses_no2_map_{base,lower,higher}.png in its own public/.
-->
  <div style="position: relative; align-self: stretch; width: 100%; height: 100%;">
    <img src="/ihen_ses_no2_map_base.png" style="position: absolute; inset: 0; width: 100%; height: 100%; object-position: left top;" />
    <img v-click src="/ihen_ses_no2_map_lower.png" style="position: absolute; inset: 0; width: 100%; height: 100%; object-position: left top;" />
    <img v-click src="/ihen_ses_no2_map_higher.png" style="position: absolute; inset: 0; width: 100%; height: 100%; object-position: left top;" />
  </div>
</template>
