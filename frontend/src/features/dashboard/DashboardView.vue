<script setup lang="ts">
import PlaceholderPage from '@/shared/PlaceholderPage.vue';
</script>

<template>
  <PlaceholderPage
    eyebrow="Dashboard"
    title="MVP Operations Dashboard"
    description="A role-aware landing area for upcoming games, team operations, notices, and scorekeeping shortcuts will be added here."
    :next-steps="[
      'Decide dashboard summaries for users, team managers, and administrators.',
      'Add loading, empty, error, and retry states when APIs are available.',
    ]"
  />
</template>
