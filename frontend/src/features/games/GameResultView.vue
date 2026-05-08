<script setup lang="ts">
import { useRoute } from 'vue-router';
import PlaceholderPage from '@/shared/PlaceholderPage.vue';

const route = useRoute();
const gameId = String(route.params.id ?? 'N/A');
</script>

<template>
  <PlaceholderPage
    eyebrow="Game results"
    :title="`Result and Box Score: ${gameId}`"
    description="Final score, box score aggregation, publishing status, and PDF export actions will be added after game event aggregation is implemented."
    :next-steps="[
      'Build deterministic box score aggregation tests.',
      'Add manual review states for official result publishing.',
      'Add permission-aware result visibility and export actions.',
    ]"
  />
</template>
