<script setup lang="ts">
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import { ROUTE_PATHS } from '@/routes/route-constants';

const route = useRoute();
const isPublicDisplay = computed(() => route.meta.publicDisplay === true);

const navItems = [
  { label: 'Home', to: ROUTE_PATHS.home },
  { label: 'Dashboard', to: ROUTE_PATHS.dashboard },
  { label: 'Control', to: ROUTE_PATHS.scoreboardControl },
  { label: 'Display', to: ROUTE_PATHS.scoreboardDisplay },
  { label: 'Live Sheet', to: '/games/demo-game/live' },
  { label: 'Result', to: '/games/demo-game/result' },
  { label: 'Teams', to: ROUTE_PATHS.teams },
  { label: 'Players', to: ROUTE_PATHS.players },
  { label: 'Leagues', to: ROUTE_PATHS.leagues },
  { label: 'Tournaments', to: ROUTE_PATHS.tournaments },
] as const;
</script>

<template>
  <RouterView v-if="isPublicDisplay" />

  <div v-else class="app-layout">
    <header class="app-header">
      <RouterLink class="brand-link" :to="ROUTE_PATHS.home" aria-label="Go to home">
        Basketball Ops MVP
      </RouterLink>
      <nav class="primary-nav" aria-label="Phase 1 MVP routes">
        <RouterLink v-for="item in navItems" :key="item.to" :to="item.to">
          {{ item.label }}
        </RouterLink>
      </nav>
    </header>

    <RouterView />
  </div>
</template>
