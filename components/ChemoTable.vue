<script setup>
const servers = ['server_1', 'server_2', 'server_3']
const rows = [
  { label: 'not-modified', counts: [300, 490, 197] },
  { label: 'other', counts: [100, 126, 46] },
  { label: 'toxicity', counts: [100, 184, 57] },
  { label: 'NA', counts: [0, 0, 0] },
]
</script>

<template>
  <table class="kx-table">
    <thead>
      <tr>
        <th class="kx-left"></th>
        <th v-for="s in servers" :key="s" class="kx-right">{{ s }}</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(r, i) in rows" :key="i">
        <td class="kx-left">{{ r.label }}</td>
        <td v-for="(c, j) in r.counts" :key="j" class="kx-right">{{ c }}</td>
      </tr>
    </tbody>
  </table>
</template>

<style scoped>
.kx-table {
  border-collapse: collapse;
  font-family: var(--font-subtitle);
  font-size: 10px;
  color: #2b3440;
  margin: 0.35rem 0 0.2rem 0;
  min-width: 62%;
}

.kx-table thead th {
  font-weight: 700;
  border-bottom: 1px solid #c8ced4;
  padding: 0.28rem 0.75rem 0.22rem 0.4rem;
  white-space: nowrap;
}

.kx-table tbody td {
  padding: 0.2rem 0.75rem 0.2rem 0.4rem;
  border-bottom: 1px solid #e7eaee;
  white-space: nowrap;
}

.kx-table tbody tr:nth-child(odd) {
  background: #f7f8fa;
}

.kx-table tbody tr:last-child td {
  border-bottom: 1px solid #c8ced4;
}

.kx-left {
  text-align: left;
  width: 1%;
  padding-right: 1.1rem;
  white-space: nowrap;
}

.kx-right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}
</style>
