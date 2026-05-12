<script setup lang="ts">
import { pilotGame } from '@/shared/demo/pilotGame';
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
        <span class="status-chip">{{ pilotGame.status }}</span>
      </div>

      <div
        class="scoreboard-display-grid"
        aria-label="Current game score"
      >
        <article class="display-team">
          <span class="caption">{{ pilotGame.teams.home.label }}</span>
          <strong class="display-team-name">{{ pilotGame.teams.home.name }}</strong>
          <strong class="display-score home-score">{{ pilotGame.teams.home.score }}</strong>
          <div class="metric-grid three">
            <span class="metric-tile">
              <span class="metric-label">FOUL</span>
              <strong class="metric-value">{{ pilotGame.teams.home.fouls }}</strong>
            </span>
            <span class="metric-tile">
              <span class="metric-label">T.O</span>
              <strong class="metric-value">{{ pilotGame.teams.home.timeouts }}</strong>
            </span>
            <span class="metric-tile">
              <span class="metric-label">BALL</span>
              <strong class="metric-value">{{ pilotGame.possession === 'home' ? 'YES' : '-' }}</strong>
            </span>
          </div>
        </article>

        <aside class="display-clock">
          <span class="status-chip live">{{ pilotGame.quarter }}</span>
          <strong class="game-clock">{{ pilotGame.clock }}</strong>
          <div class="shot-clock">
            <span class="caption">SHOT</span>
            <strong class="shot-number">{{ pilotGame.shotClock }}</strong>
          </div>
        </aside>

        <article class="display-team">
          <span class="caption">{{ pilotGame.teams.away.label }}</span>
          <strong class="display-team-name">{{ pilotGame.teams.away.name }}</strong>
          <strong class="display-score away-score">{{ pilotGame.teams.away.score }}</strong>
          <div class="metric-grid three">
            <span class="metric-tile">
              <span class="metric-label">FOUL</span>
              <strong class="metric-value">{{ pilotGame.teams.away.fouls }}</strong>
            </span>
            <span class="metric-tile">
              <span class="metric-label">T.O</span>
              <strong class="metric-value">{{ pilotGame.teams.away.timeouts }}</strong>
            </span>
            <span class="metric-tile">
              <span class="metric-label">BALL</span>
              <strong class="metric-value">{{ pilotGame.possession === 'away' ? 'YES' : '-' }}</strong>
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
