<script setup>
// Exposome and environment papers using DataSHIELD, from papers.datashield.org
// (keywords: Exposome, Air Pollution). `cover` is the journal's cover art in the
// deck's public/ folder; swap `papers` to show a different set.
defineProps({
  papers: {
    type: Array,
    default: () => [
      { title: 'Determinants of body mass index in early life: an exposome-wide association study', author: 'Zhao', year: 2025, journal: 'Exposome' },
      { title: 'Urban environment in pregnancy and postpartum depression', author: 'Cadman', year: 2024, journal: 'Environ Int', cover: '/journal-envint.jpg' },
      { title: 'Socioeconomic position during pregnancy and the pre-school exposome', author: 'Pizzi', year: 2024, journal: 'Soc Sci Med', cover: '/journal-socscimed.jpg' },
      { title: 'Stress and anxiety during pregnancy and length of gestation', author: 'Bergeron', year: 2024, journal: 'Eur J Epidemiol', cover: '/journal-eje.png' },
      { title: 'Residential air pollution, wheeze and shortness of breath in adults', author: 'Doiron', year: 2017, journal: 'Environ Health Perspect', cover: '/journal-ehp.jpg' },
    ],
  },
})
</script>

<template>
  <div class="papers">
    <div v-for="p in papers" :key="p.title" class="paper">
      <img v-if="p.cover" class="cover" :src="p.cover" :alt="p.journal" />
      <span v-else class="cover cover-plate">{{ p.journal }}</span>
      <div>
        <span class="t">{{ p.title }}</span>
        <span class="m">{{ p.author }} et al. ({{ p.year }}) {{ p.journal }}</span>
      </div>
    </div>
  </div>
</template>
