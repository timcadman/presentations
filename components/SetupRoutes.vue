<script setup>
import { computed } from 'vue'

// The ways to get an Armadillo node, side by side. Each route appears on its own
// click, so the choice can be talked through one at a time. SURF is only open to
// Dutch consortia, so it is off unless asked for.
//
//   <SetupRoutes />
//   <SetupRoutes surf />
//   <SetupRoutes :routes="[...]" />
const props = defineProps({
  surf: {
    type: Boolean,
    default: false,
  },
  routes: {
    type: Array,
    default: () => [
      {
        name: 'Run it yourself',
        lead: 'Install Armadillo on your own server or VM',
        points: ['Ubuntu LTS, Java 21, Docker', 'A domain and SSL certificate', 'Installed by one script'],
        colour: 'var(--c-blue)',
      },
      {
        name: 'We run it for you',
        lead: 'MOLGENIS hosts Armadillo on the UMCG Azure cloud',
        points: ['Set up and maintained by the team', 'Only you can see the data', 'support@molgenis.org'],
        colour: 'var(--c-teal)',
      },
    ],
  },
  surfRoute: {
    type: Object,
    default: () => ({
      name: 'SURF',
      lead: 'Hosted on Dutch national research infrastructure',
      points: ['For Dutch consortia already using SURF'],
      colour: 'var(--c-purple)',
    }),
  },
})

const shown = computed(() => (props.surf ? [...props.routes, props.surfRoute] : props.routes))
</script>

<template>
  <div class="routes" :style="{ '--n': shown.length }">
    <div v-for="(r, i) in shown" :key="r.name" v-click class="route" :style="{ '--c': r.colour }">
      <span class="route-n">{{ i + 1 }}</span>
      <h3>{{ r.name }}</h3>
      <p class="route-lead">{{ r.lead }}</p>
      <ul>
        <li v-for="p in r.points" :key="p">{{ p }}</li>
      </ul>
    </div>
  </div>
</template>
