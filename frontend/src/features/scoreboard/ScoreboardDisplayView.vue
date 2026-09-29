<script setup lang="ts">
import { onMounted } from 'vue';
import { pilotGame } from '@/shared/demo/pilotGame';
import { useScoreboardGame } from './useScoreboardGame';

const {
  teams,
  statusLabel,
  clockLabel,
  quarterLabel,
  isLoading,
  errorMessage,
  refresh,
  startPolling,
} = useScoreboardGame();

onMounted(() => {
  void refresh();
  startPolling();
});
</script>

<template>
  <main
    class="display-shell"
    aria-label="Public scoreboard display"
  >
    <section class="display-stage">
      <div class="display-meta">
        <span class="status-chip live">{{ pilotGame.title }}</span>
        <span class="status-chip">{{ pilotGame.venue }}</span>
        <span class="status-chip">{{ statusLabel }}</span>
      </div>

      <div
        v-if="errorMessage"
        class="display-meta"
      >
        <span class="status-chip">{{ errorMessage }}</span>
        <button
          class="btn-ghost"
          type="button"
          :disabled="isLoading"
          @click="refresh"
        >
          재시도
        </button>
      </div>

      <div
        class="scoreboard-display-grid"
        aria-label="Current game score"
      >
        <article class="display-team">
          <span class="caption">{{ teams[0].label }}</span>
          <strong class="display-team-name">{{ teams[0].name }}</strong>
          <strong class="display-score home-score">{{ teams[0].score }}</strong>
          <div class="metric-grid three">
            <span class="metric-tile">
              <span class="metric-label">FOUL</span>
              <strong class="metric-value">{{ teams[0].fouls }}</strong>
            </span>
            <span class="metric-tile">
              <span class="metric-label">T.O</span>
              <strong class="metric-value">{{ teams[0].timeouts }}</strong>
            </span>
            <span class="metric-tile">
              <span class="metric-label">BALL</span>
              <strong class="metric-value">-</strong>
            </span>
          </div>
        </article>

        <aside class="display-clock">
          <span class="status-chip live">{{ quarterLabel }}</span>
          <strong class="game-clock">{{ clockLabel }}</strong>
          <div class="shot-clock">
            <span class="caption">SHOT</span>
            <strong class="shot-number">{{ pilotGame.shotClock }}</strong>
          </div>
        </aside>

        <article class="display-team">
          <span class="caption">{{ teams[1].label }}</span>
          <strong class="display-team-name">{{ teams[1].name }}</strong>
          <strong class="display-score away-score">{{ teams[1].score }}</strong>
          <div class="metric-grid three">
            <span class="metric-tile">
              <span class="metric-label">FOUL</span>
              <strong class="metric-value">{{ teams[1].fouls }}</strong>
            </span>
            <span class="metric-tile">
              <span class="metric-label">T.O</span>
              <strong class="metric-value">{{ teams[1].timeouts }}</strong>
            </span>
            <span class="metric-tile">
              <span class="metric-label">BALL</span>
              <strong class="metric-value">-</strong>
            </span>
          </div>
        </article>
      </div>

      <p class="display-note">
        관중용 표시 화면 · 운영 메뉴 없음
      </p>
    </section>
  </main>
</template>
