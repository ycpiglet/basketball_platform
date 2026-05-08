<script setup lang="ts">
import PlaceholderPage from '@/shared/PlaceholderPage.vue';
</script>

<template>
  <PlaceholderPage
    eyebrow="Scoreboard"
    title="Scoreboard Control Panel"
    description="Touch-first controls for score, timer, fouls, periods, and game finalization will be designed here after the event model is defined."
    :next-steps="[
      'Define deterministic score and timer event contracts.',
      'Add permission-aware API calls through backend services.',
      'Add large tap targets and clear retry/error states for live game operation.',
    ]"
  />
</template>
