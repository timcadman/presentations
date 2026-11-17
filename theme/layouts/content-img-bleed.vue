<script setup>
import { computed } from 'vue'
import { configs } from '@slidev/client'

// Text on the left, a photo on the right that runs to the slide's right edge.
// The photo starts below the title, so it never overlaps it, and stops above the
// logo and section rail at the bottom.
const props = defineProps({
  heading: {
    type: String,
    default: '',
  },
  subheading: {
    type: String,
    default: '',
  },
  image: {
    type: String,
    default: '',
  },
  // width of the photo as a % of the whole slide (text takes the rest)
  imageWidth: {
    type: String,
    default: '50',
  },
  // run the photo to the slide's right edge; false keeps it inside the right margin
  bleed: {
    type: Boolean,
    default: true,
  },
  // CSS object-position for the crop, e.g. 'center 35%'
  imagePosition: {
    type: String,
    default: 'center',
  },
  section: {
    type: String,
    default: '',
  },
})

const base = import.meta.env.BASE_URL
const logo = configs.themeConfig?.logo ?? 'molgenis-logo.png'
const sections = configs.themeConfig?.sections || ['Background', 'Methods', 'Results', 'Conclusions']
const resolvedImage = computed(() => {
  if (!props.image) return ''
  return `${base}${props.image.replace(/^\.\/public\//, '')}`
})
// the row sits inside 5rem of side padding, so a % of the slide is a % of the row plus 10rem
const imageBasis = computed(() => `calc((100% + 10rem) * ${Number(props.imageWidth) / 100})`)
</script>

<template>
  <div class="slidev-layout content-img-bleed">
    <div class="slide-header">
      <h1>{{ heading }}</h1>
      <h2 v-if="subheading">{{ subheading }}</h2>
    </div>
    <div class="body-row">
      <div class="text-area">
        <div class="slide-body">
          <slot />
        </div>
      </div>
      <div class="image-area" :style="{ flexBasis: imageBasis, marginRight: bleed ? '-5rem' : '0' }">
        <img v-if="image" :src="resolvedImage" class="slide-image" :style="{ objectPosition: imagePosition }" />
      </div>
    </div>
    <div class="logo-bar">
      <img :src="`${base}${logo}`" class="slide-logo" />
    </div>
    <div v-if="section" class="section-rail">
      <template v-for="(s, i) in sections" :key="s">
        <span :class="{ cur: s.toLowerCase() === section.toLowerCase() }">{{ s }}</span>
        <span v-if="i < sections.length - 1" class="sep">·</span>
      </template>
    </div>
  </div>
</template>

<style scoped>
.content-img-bleed {
  display: flex;
  flex-direction: column;
  /* bottom padding clears the logo (~3.25rem) so the photo never overlaps it */
  padding: 4.5rem 5rem 3.75rem 5rem;
  height: 100%;
}

.slide-header {
  min-height: 7.25rem;
  margin-bottom: 1.5rem;
  padding-top: 0.75rem;
  position: relative;
}

.slide-header::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 33%;
  height: var(--slidev-theme-header-bar, 3px);
  background-color: var(--slidev-theme-primary);
}

.slide-header h1 {
  font-family: var(--font-title);
  font-size: 44px;
  font-weight: 400;
  color: var(--slidev-theme-heading);
  margin: 0;
  line-height: 1.2;
}

.slide-header h2 {
  font-family: var(--font-subtitle);
  font-size: 25px;
  font-weight: 400;
  color: var(--slidev-theme-heading);
  margin: 0.25rem 0 0 0;
}

.body-row {
  flex: 1;
  display: flex;
  gap: 2rem;
  min-height: 0;
}

.text-area {
  flex: 1;
  min-width: 0;
}

/* with bleed, a negative right margin (set inline) pulls the photo out through
   the padding to the slide edge */
.image-area {
  flex: 0 0 auto;
  min-width: 0;
}

.slide-image {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.slide-body :deep(ul) {
  padding-left: 1.5rem;
}

.slide-body :deep(li) {
  font-size: 18px;
  margin-bottom: 0.5rem;
  line-height: 1.5;
}

.logo-bar {
  position: absolute;
  bottom: 1rem;
  right: 1.5rem;
}

.slide-logo {
  height: 36px;
  opacity: 0.8;
}

.section-rail {
  position: absolute;
  bottom: 1.4rem;
  left: 5rem;
  display: flex;
  align-items: center;
  gap: 0.4rem;
  font-family: var(--font-subtitle);
  font-size: 12px;
  letter-spacing: 0.01em;
  color: #9aa4b0;
}
.section-rail .cur {
  color: var(--slidev-theme-primary);
  font-weight: 600;
}
.section-rail .sep {
  opacity: 0.5;
}
</style>
