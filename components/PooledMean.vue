<script setup>
import { ref, computed } from 'vue'

// Live pooled mean for the group exercise: add a row per group during the talk,
// type each group's mean and N, and the weighted mean updates as you type.
const rows = ref([
  { mean: null, n: null },
  { mean: null, n: null },
])

const filled = computed(() => rows.value.filter(r => Number(r.n) > 0 && r.mean !== null && r.mean !== ''))
const totalN = computed(() => filled.value.reduce((a, r) => a + Number(r.n), 0))
const pooled = computed(() => {
  if (!filled.value.length) return null
  return filled.value.reduce((a, r) => a + Number(r.mean) * Number(r.n), 0) / totalN.value
})
</script>

<template>
  <div class="pm">
    <div class="pm-left">
      <slot />
      <p class="pm-result">
        Pooled mean
        <strong>{{ pooled === null ? '—' : pooled.toFixed(1) }}</strong>
        <span v-if="totalN">cm over N = {{ totalN }}</span>
      </p>
    </div>

    <div class="pm-right">
    <table class="pm-table">
      <thead>
        <tr><th>Group</th><th>Mean (cm)</th><th>N</th></tr>
      </thead>
      <tbody>
        <tr v-for="(r, i) in rows" :key="i">
          <td>{{ i + 1 }}</td>
          <td><input v-model="r.mean" type="number" placeholder="—" /></td>
          <td><input v-model="r.n" type="number" placeholder="—" /></td>
        </tr>
      </tbody>
    </table>

    <div class="pm-actions">
      <button @click="rows.push({ mean: null, n: null })">+ group</button>
      <button v-if="rows.length > 1" @click="rows.pop()">− group</button>
    </div>

    </div>
  </div>
</template>
