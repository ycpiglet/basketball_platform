<script setup lang="ts">
import { pilotGame, pilotTeams } from '@/shared/demo/pilotGame';
</script>

<template>
  <main class="screen-pad">
    <div class="container stack-lg">
      <header class="two-column">
        <div class="stack">
          <p class="section-kicker">
            Scoreboard control
          </p>
          <h1>경기 운영 컨트롤</h1>
          <p class="lead">
            점수, 파울, 타임아웃, 쿼터, 경기 시간을 한 화면에서 다루는 터치 우선 운영 화면입니다.
          </p>
        </div>
        <aside class="panel">
          <div class="split-row">
            <span class="status-chip live">{{ pilotGame.status }}</span>
            <span class="caption">{{ pilotGame.syncStatus }}</span>
          </div>
        </aside>
      </header>

      <section
        class="live-box-score"
        aria-label="Live scoreboard preview"
      >
        <article class="team-panel home">
          <div class="team-header">
            <span class="team-logo">{{ pilotGame.teams.home.shortName }}</span>
            <div>
              <p class="caption">
                {{ pilotGame.teams.home.label }}
              </p>
              <h2>{{ pilotGame.teams.home.name }}</h2>
            </div>
          </div>
          <strong class="score-number home-score">{{ pilotGame.teams.home.score }}</strong>
          <div class="metric-grid three">
            <div class="metric-tile">
              <span class="metric-label">파울</span>
              <strong class="metric-value">{{ pilotGame.teams.home.fouls }}</strong>
            </div>
            <div class="metric-tile">
              <span class="metric-label">타임아웃</span>
              <strong class="metric-value">{{ pilotGame.teams.home.timeouts }}</strong>
            </div>
            <div class="metric-tile">
              <span class="metric-label">선수</span>
              <strong class="metric-value">{{ pilotGame.teams.home.players.length }}</strong>
            </div>
          </div>
        </article>

        <aside class="game-core">
          <span class="status-chip live">{{ pilotGame.quarter }}</span>
          <strong class="game-clock">{{ pilotGame.clock }}</strong>
          <div class="shot-clock">
            <span class="caption">SHOT</span>
            <strong class="shot-number">{{ pilotGame.shotClock }}</strong>
          </div>
          <p class="caption">
            소유권: {{ pilotGame.teams[pilotGame.possession].shortName }}
          </p>
        </aside>

        <article class="team-panel away">
          <div class="team-header">
            <span class="team-logo">{{ pilotGame.teams.away.shortName }}</span>
            <div>
              <p class="caption">
                {{ pilotGame.teams.away.label }}
              </p>
              <h2>{{ pilotGame.teams.away.name }}</h2>
            </div>
          </div>
          <strong class="score-number away-score">{{ pilotGame.teams.away.score }}</strong>
          <div class="metric-grid three">
            <div class="metric-tile">
              <span class="metric-label">파울</span>
              <strong class="metric-value">{{ pilotGame.teams.away.fouls }}</strong>
            </div>
            <div class="metric-tile">
              <span class="metric-label">타임아웃</span>
              <strong class="metric-value">{{ pilotGame.teams.away.timeouts }}</strong>
            </div>
            <div class="metric-tile">
              <span class="metric-label">선수</span>
              <strong class="metric-value">{{ pilotGame.teams.away.players.length }}</strong>
            </div>
          </div>
        </article>
      </section>

      <section class="control-grid">
        <article
          v-for="team in pilotTeams"
          :key="`${team.side}-controls`"
          :class="['team-panel', team.side]"
        >
          <div>
            <p class="eyebrow">
              {{ team.label }}
            </p>
            <h2>{{ team.name }}</h2>
          </div>
          <div
            class="score-control-grid"
            aria-label="Score controls"
          >
            <button
              class="score-btn"
              type="button"
            >
              +1
            </button>
            <button
              class="score-btn"
              type="button"
            >
              +2
            </button>
            <button
              class="score-btn"
              type="button"
            >
              +3
            </button>
          </div>
          <div class="aux-control-grid">
            <button
              class="score-btn secondary"
              type="button"
            >
              팀 파울
            </button>
            <button
              class="score-btn secondary"
              type="button"
            >
              타임아웃
            </button>
            <button
              class="btn-warn"
              type="button"
            >
              점수 정정
            </button>
            <button
              class="btn-danger"
              type="button"
            >
              입력 취소
            </button>
          </div>
        </article>

        <aside class="timer-panel">
          <div class="timer-face">
            <span class="status-chip live">{{ pilotGame.quarter }}</span>
            <strong class="game-clock">{{ pilotGame.clock }}</strong>
            <p class="caption">
              경기 시간은 backend 연결 전 demo state입니다.
            </p>
          </div>
          <div class="timer-button-grid">
            <button
              class="btn-success"
              type="button"
            >
              시작
            </button>
            <button
              class="btn-danger"
              type="button"
            >
              정지
            </button>
            <button
              class="btn-ghost"
              type="button"
            >
              쿼터 +
            </button>
            <button
              class="btn-ghost"
              type="button"
            >
              24초 리셋
            </button>
          </div>
          <button
            class="btn-dark"
            type="button"
          >
            경기 종료
          </button>
        </aside>
      </section>

      <section class="panel">
        <div class="split-row">
          <div>
            <p class="section-kicker">
              Recent events
            </p>
            <h2>최근 입력 로그</h2>
          </div>
          <RouterLink
            class="btn-ghost"
            to="/games/demo-game/live"
          >
            기록지 열기
          </RouterLink>
        </div>
        <div class="event-list">
          <div
            v-for="event in pilotGame.events"
            :key="`${event.time}-${event.text}`"
            class="event-row"
          >
            <strong class="number">{{ event.time }}</strong>
            <span class="tag">{{ event.team }}</span>
            <span>{{ event.text }}</span>
          </div>
        </div>
      </section>
    </div>
  </main>
</template>
