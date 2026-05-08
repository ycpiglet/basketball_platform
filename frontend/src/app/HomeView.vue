<script setup lang="ts">
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
      <p class="eyebrow">Phase 1 MVP skeleton</p>
      <h1>Amateur Basketball Platform</h1>
      <p>
        Start with reliable field operation: scoreboard control, public display,
        digital scorekeeping, CRUD foundations, RBAC, logging, and tests.
      </p>
    </section>

    <section class="grid-panel" aria-labelledby="routes-heading">
      <h2 id="routes-heading">MVP route foundations</h2>
      <RouterLink to="/games/demo-game/control">Scoreboard control</RouterLink>
      <RouterLink to="/games/demo-game/display">Public display</RouterLink>
      <RouterLink to="/games/demo-game/record">Digital score sheet</RouterLink>
      <RouterLink to="/teams">Teams</RouterLink>
      <RouterLink to="/players">Players</RouterLink>
      <RouterLink to="/leagues">Leagues</RouterLink>
      <RouterLink to="/tournaments">Tournaments</RouterLink>
    </section>

    <section class="grid-panel" aria-labelledby="role-heading">
      <h2 id="role-heading">Development-only role switcher</h2>
      <p>
        This is not production authentication. It exists only to exercise router guard behavior
        until backend auth is designed.
      </p>
      <div class="button-row">
        <button v-for="role in roles" :key="role" type="button" @click="chooseRole(role)">
          Use {{ role }}
        </button>
      </div>
    </section>
  </main>
</template>
