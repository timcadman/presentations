// The eight cohorts pooled in Garcia-Aymerich et al. (2025) Lancet Respir Med
// 13:611-22, figure 1: participants, and the first and last age each observed.
// Colours are the repaired palette in COLOURS.md. Shared by CohortCoverage.vue
// and FevTrajectory.vue so the two figures cannot drift apart.
export const COHORTS = [
  { name: 'INMA', n: 904, first: 4, last: 18, colour: '#5D408A' },
  { name: 'TAHS', n: 2987, first: 6, last: 55, colour: '#DA594A' },
  { name: 'BAMSE', n: 1999, first: 7, last: 24, colour: '#E2A517' },
  { name: 'PIAMA', n: 869, first: 7, last: 17, colour: '#02529B' },
  { name: 'ALSPAC', n: 3566, first: 8, last: 26, colour: '#119DA1' },
  { name: 'VlaVla', n: 4750, first: 14, last: 80, colour: '#4285F4' },
  { name: 'SAPALDIA', n: 6593, first: 17, last: 80, colour: '#BA8118' },
  { name: 'ECRHS', n: 8770, first: 19, last: 67, colour: '#40A2C7' },
]

// age 0 at x=160, 6.75px per year, so 0-80 still ends at x=700. Shared by both
// Example 3 figures, which is what keeps their x axes aligned slide to slide.
export const X = age => 160 + 6.75 * age

// bar thickness carries participant count; sqrt keeps area roughly proportional
export const thickness = n => 6 + (Math.sqrt(n) - 29.5) / 64.1 * 14
