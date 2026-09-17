<script setup>
import Layout from '../../theme/layouts/content-two-images.vue'
</script>

<template>
  <Layout v-bind="$attrs">
    <template v-for="(_, name) in $slots" #[name]="slotProps">
      <slot :name="name" v-bind="slotProps" />
    </template>
  </Layout>
</template>
