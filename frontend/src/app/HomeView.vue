<script setup lang="ts">
import { ROUTE_PATHS } from '@/routes/route-constants';
import { setDevRole } from '@/shared/auth/session';
import { roles, type Role } from '@/shared/types/roles';

function chooseRole(role: Role): void {
  setDevRole(role);
  window.location.reload();
}
</script>

<template>
  <main class="page-shell">
    <section class="hero-card">
      <p class="eyebrow">Phase 1 MVP frontend shell</p>
      <h1>Amateur Basketball Platform</h1>
      <p>
        Placeholder pages are ready for the scoreboard, digital score sheet, result view,
        dashboard, and CRUD foundations. Business logic, production authentication,
        payments, credits, gym rental, and hardware control are intentionally excluded.
      </p>
    </section>

    <section class="grid-panel" aria-labelledby="routes-heading">
      <h2 id="routes-heading">Phase 1 route placeholders</h2>
      <RouterLink :to="ROUTE_PATHS.dashboard">Dashboard</RouterLink>
      <RouterLink :to="ROUTE_PATHS.scoreboardControl">Scoreboard control</RouterLink>
      <RouterLink :to="ROUTE_PATHS.scoreboardDisplay">Public scoreboard display</RouterLink>
      <RouterLink to="/games/demo-game/live">Live digital score sheet</RouterLink>
      <RouterLink to="/games/demo-game/result">Game result and box score</RouterLink>
      <RouterLink :to="ROUTE_PATHS.teams">Teams</RouterLink>
      <RouterLink :to="ROUTE_PATHS.players">Players</RouterLink>
      <RouterLink :to="ROUTE_PATHS.leagues">Leagues</RouterLink>
      <RouterLink :to="ROUTE_PATHS.tournaments">Tournaments</RouterLink>
    </section>

    <section class="grid-panel" aria-labelledby="role-heading">
      <h2 id="role-heading">Development-only route guard helper</h2>
      <p>
        This is not production authentication. It only helps exercise placeholder route guards
        until backend authentication and authorization are designed.
      </p>
      <div class="button-row">
        <button v-for="role in roles" :key="role" type="button" @click="chooseRole(role)">
          Use {{ role }}
        </button>
      </div>
    </section>
  </main>
</template>
