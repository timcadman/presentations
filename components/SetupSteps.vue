<script setup>
// The whole self-hosted Armadillo setup on one slide: four numbered steps across,
// each revealed on its own click. The long version is
// library/infrastructure/armadillo-setup.md.
//
//   <SetupSteps />
//   <SetupSteps :steps="[...]" />
defineProps({
  steps: {
    type: Array,
    default: () => [
      {
        name: 'Prepare',
        points: ['Ubuntu LTS server or VM', '8–32 GB memory, 4–8 cores', 'Java 21 and Docker', 'A domain name'],
      },
      {
        name: 'Install',
        points: ['Run <code>armadillo-setup.sh</code>', 'Installs as a systemd service', 'Listening on port 8080'],
      },
      {
        name: 'Secure',
        points: ['Nginx in front, with SSL', 'Register the domain for OIDC', 'Firewall to known addresses'],
      },
      {
        name: 'Run',
        points: ['<code>systemctl</code> to start and stop', 'Back up data and config', 'Update at each release'],
      },
    ],
  },
})
</script>

<template>
  <ol class="steps">
    <li v-for="(s, i) in steps" :key="s.name" v-click class="step">
      <span class="step-n">{{ i + 1 }}</span>
      <h3>{{ s.name }}</h3>
      <ul>
        <li v-for="p in s.points" :key="p" v-html="p"></li>
      </ul>
    </li>
  </ol>
</template>
