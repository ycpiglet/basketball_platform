<script setup lang="ts">
import { useRoute } from 'vue-router';
import { pilotGame, pilotTeams } from '@/shared/demo/pilotGame';

const route = useRoute();
const gameId = String(route.params.id ?? pilotGame.id);
</script>

<template>
  <main class="screen-pad">
    <div class="container stack-lg">
      <header class="two-column">
        <div class="stack">
          <p class="section-kicker">
            Game result
          </p>
          <h1>{{ gameId }} 결과 요약</h1>
          <p class="lead">
            필드 파일럿 이후 최종 점수, 박스 스코어, 정정 로그를 검토하는 화면입니다.
          </p>
        </div>
        <aside class="panel">
          <span class="status-chip live">Manual review before publish</span>
          <p class="muted">
            공식 결과 게시 전에는 수기 검토 상태를 유지합니다.
          </p>
        </aside>
      </header>

      <section class="product-object">
        <div class="mini-display-score">
          <article class="mini-display-team">
            <span class="caption">{{ pilotGame.teams.home.label }}</span>
            <strong class="display-score home-score">
              {{ pilotGame.teams.home.score }}
            </strong>
            <span>{{ pilotGame.teams.home.name }}</span>
          </article>
          <div class="display-clock">
            <span class="tag dark">FINAL SAMPLE</span>
            <strong class="game-clock">{{ pilotGame.quarter }}</strong>
          </div>
          <article class="mini-display-team">
            <span class="caption">{{ pilotGame.teams.away.label }}</span>
            <strong class="display-score away-score">
              {{ pilotGame.teams.away.score }}
            </strong>
            <span>{{ pilotGame.teams.away.name }}</span>
          </article>
        </div>
      </section>

      <section class="result-grid">
        <article class="result-panel">
          <p class="eyebrow">
            Corrections
          </p>
          <h2>1</h2>
          <p class="muted">
            정정 사유가 기록된 이벤트만 결과 검토 대상입니다.
          </p>
        </article>
        <article class="result-panel">
          <p class="eyebrow">
            Events
          </p>
          <h2>{{ pilotGame.events.length }}</h2>
          <p class="muted">
            현재 demo event log 기준입니다.
          </p>
        </article>
        <article class="result-panel">
          <p class="eyebrow">
            Publish state
          </p>
          <h2>Review</h2>
          <p class="muted">
            백엔드 검증과 권한 모델 연결 후 게시합니다.
          </p>
        </article>
      </section>

      <section class="two-column">
        <article
          v-for="team in pilotTeams"
          :key="`${team.side}-result`"
          class="panel"
        >
          <div class="split-row">
            <h2>{{ team.name }}</h2>
            <span class="status-chip">{{ team.score }} PTS</span>
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
    </div>
  </main>
</template>
