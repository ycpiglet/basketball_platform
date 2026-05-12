<script setup lang="ts">
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import { ROUTE_PATHS } from '@/routes/route-constants';

const route = useRoute();
const isPublicDisplay = computed(() => route.meta.publicDisplay === true);

const navItems = [
  { label: '대시보드', to: ROUTE_PATHS.dashboard },
  { label: '컨트롤', to: ROUTE_PATHS.scoreboardControl },
  { label: '기록지', to: '/games/demo-game/live' },
  { label: '결과', to: '/games/demo-game/result' },
  { label: '팀', to: ROUTE_PATHS.teams },
  { label: '선수', to: ROUTE_PATHS.players },
  { label: '리그', to: ROUTE_PATHS.leagues },
  { label: '대회', to: ROUTE_PATHS.tournaments },
] as const;

const globalItems = [
  { label: '파일럿 홈', to: ROUTE_PATHS.home },
  { label: 'TV 표시', to: ROUTE_PATHS.scoreboardDisplay },
  { label: '운영 대시보드', to: ROUTE_PATHS.dashboard },
] as const;
</script>

<template>
  <RouterView v-if="isPublicDisplay" />

  <div
    v-else
    class="app-layout"
  >
    <header class="global-nav">
      <div class="global-nav-inner">
        <RouterLink
          class="brand-link"
          :to="ROUTE_PATHS.home"
          aria-label="Go to home"
        >
          <span
            class="brand-mark"
            aria-hidden="true"
          >B</span>
          <span>Basketball Ops</span>
        </RouterLink>

        <nav
          class="global-links"
          aria-label="Primary routes"
        >
          <RouterLink
            v-for="item in globalItems"
            :key="item.to"
            :to="item.to"
          >
            {{ item.label }}
          </RouterLink>
        </nav>
      </div>
    </header>

    <div class="sub-nav">
      <div class="sub-nav-inner">
        <p class="sub-title">
          아마추어 농구 필드 파일럿
        </p>
        <nav
          class="nav-scroll"
          aria-label="Phase 1 MVP routes"
        >
          <RouterLink
            v-for="item in navItems"
            :key="item.to"
            class="nav-pill"
            :to="item.to"
          >
            {{ item.label }}
          </RouterLink>
        </nav>
      </div>
    </div>

    <RouterView />
  </div>
</template>
