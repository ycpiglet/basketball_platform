<script setup lang="ts">
import { useRoute } from 'vue-router';
import { pilotGame, pilotTeams } from '@/shared/demo/pilotGame';

const route = useRoute();
const gameId = String(route.params.id ?? pilotGame.id);
const eventButtons = ['2점', '3점', '자유투', '개인 파울', '리바운드', '어시스트', '스틸', '턴오버'];
</script>

<template>
  <main class="screen-pad">
    <div class="container stack-lg">
      <header class="two-column">
        <div class="stack">
          <p class="section-kicker">
            Digital score sheet
          </p>
          <h1>{{ gameId }} 기록지</h1>
          <p class="lead">
            선수 이벤트와 경기 로그를 한 화면에서 확인하는 demo score sheet입니다.
          </p>
        </div>
        <aside class="panel">
          <div class="split-row">
            <span class="status-chip live">{{ pilotGame.status }}</span>
            <RouterLink
              class="btn-ghost"
              to="/scoreboard/control"
            >
              컨트롤로 이동
            </RouterLink>
          </div>
        </aside>
      </header>

      <section class="two-column">
        <article class="sheet-panel">
          <div class="split-row">
            <div>
              <p class="eyebrow">
                Event entry
              </p>
              <h2>선수 이벤트 입력</h2>
            </div>
            <span class="status-chip">{{ pilotGame.clock }}</span>
          </div>
          <div class="form-grid">
            <span class="input-like">팀 선택: {{ pilotGame.teams.home.name }}</span>
            <span class="input-like">선수 선택: #7 Kim</span>
            <span class="input-like">기록 위치: Q2 {{ pilotGame.clock }}</span>
          </div>
          <div class="score-control-grid">
            <button
              v-for="button in eventButtons"
              :key="button"
              class="score-btn secondary"
              type="button"
            >
              {{ button }}
            </button>
          </div>
        </article>

        <aside class="sheet-panel dark-panel">
          <p class="eyebrow">
            Live summary
          </p>
          <div class="mini-display-score">
            <article class="mini-display-team">
              <span class="caption">{{ pilotGame.teams.home.shortName }}</span>
              <strong class="mini-score home-score">
                {{ pilotGame.teams.home.score }}
              </strong>
            </article>
            <strong class="game-clock">{{ pilotGame.clock }}</strong>
            <article class="mini-display-team">
              <span class="caption">{{ pilotGame.teams.away.shortName }}</span>
              <strong class="mini-score away-score">
                {{ pilotGame.teams.away.score }}
              </strong>
            </article>
          </div>
        </aside>
      </section>

      <section class="two-column">
        <article
          v-for="team in pilotTeams"
          :key="`${team.side}-box`"
          class="panel"
        >
          <div class="split-row">
            <h2>{{ team.name }}</h2>
            <span class="status-chip">{{ team.label }}</span>
          </div>
          <div class="stat-table">
            <div class="stat-head">
              <span>No</span>
              <span>Player</span>
              <span>PTS</span>
              <span>F</span>
              <span>AST</span>
              <span>REB</span>
            </div>
            <div
              v-for="player in team.players"
              :key="player.id"
              class="stat-row"
            >
              <strong>{{ player.number }}</strong>
              <span>{{ player.name }}</span>
              <strong>{{ player.points }}</strong>
              <span>{{ player.fouls }}</span>
              <span>{{ player.assists }}</span>
              <span>{{ player.rebounds }}</span>
            </div>
          </div>
        </article>
      </section>

      <section class="panel">
        <p class="section-kicker">
          Event log
        </p>
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
