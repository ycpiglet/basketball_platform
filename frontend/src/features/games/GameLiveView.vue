<script setup lang="ts">
import { useRoute } from 'vue-router';
import PlaceholderPage from '@/shared/PlaceholderPage.vue';

const route = useRoute();
const gameId = String(route.params.id ?? 'N/A');
</script>

<template>
  <PlaceholderPage
    eyebrow="Digital score sheet"
    :title="`Live Game Sheet: ${gameId}`"
    description="This route will host the Phase 1 scorekeeper workflow for live player events, fouls, corrections, and synchronized game status."
    :next-steps="[
      'Define the immutable game event schema.',
      'Add player event entry placeholders once roster data exists.',
      'Connect to backend validation and structured logging before live use.',
    ]"
  />
</template>
