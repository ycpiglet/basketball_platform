<script setup lang="ts">
defineProps<{
  entityName: string;
}>();
</script>

<template>
  <main class="page-shell">
    <section class="hero-card">
      <p class="eyebrow">CRUD foundation</p>
      <h1>{{ entityName }}</h1>
      <p>Search, filters, pagination, validation, and permission-aware API integration will be added here.</p>
    </section>
  </main>
</template>
