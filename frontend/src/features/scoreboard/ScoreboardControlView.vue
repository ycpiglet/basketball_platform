<script setup lang="ts">
import { onMounted } from 'vue';
import { pilotGame } from '@/shared/demo/pilotGame';
import type { TeamSide } from './scoreboardApi';
import { useScoreboardGame } from './useScoreboardGame';

const {
  state,
  teams,
  eventRows,
  statusLabel,
  clockLabel,
  quarterLabel,
  isFinal,
  isClockRunning,
  isLoading,
  isActionPending,
  errorMessage,
  ensureGame,
  refresh,
  score,
  teamFoul,
  playerFoul,
  timeout,
  correction,
  start,
  stop,
  nextQuarter,
  finalize,
} = useScoreboardGame();

onMounted(() => {
  void ensureGame();
});

function isControlDisabled(): boolean {
  return isLoading.value || isActionPending.value || isFinal.value || !state.value;
}

function isClockActionDisabled(): boolean {
  return isLoading.value || isActionPending.value || isFinal.value || !state.value;
}

function correctTeamScore(team: TeamSide): void {
  const currentScore = team === 'home' ? state.value?.home.score : state.value?.away.score;
  const scoreInput = window.prompt('정정할 점수를 입력하세요.', String(currentScore ?? 0));

  if (scoreInput === null) {
    return;
  }

  const correctedScore = Number(scoreInput);
  const reason = window.prompt('정정 사유를 입력하세요.', 'Scorekeeper correction');

  if (!Number.isInteger(correctedScore) || correctedScore < 0 || !reason) {
    return;
  }

  void correction(team, correctedScore, reason);
}
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
            <span class="status-chip live">{{ statusLabel }}</span>
            <span class="caption">
              {{ isLoading ? 'Backend 상태 불러오는 중' : 'Backend API 연결됨' }}
            </span>
          </div>
          <button
            class="btn-ghost"
            type="button"
            :disabled="isLoading || isActionPending"
            @click="ensureGame"
          >
            경기 상태 준비
          </button>
        </aside>
      </header>

      <section
        v-if="errorMessage"
        class="panel error-card"
      >
        <div class="split-row">
          <strong>{{ errorMessage }}</strong>
          <button
            class="btn-ghost"
            type="button"
            :disabled="isLoading"
            @click="ensureGame"
          >
            재시도
          </button>
        </div>
      </section>

      <section
        class="live-box-score"
        aria-label="Live scoreboard preview"
      >
        <article class="team-panel home">
          <div class="team-header">
            <span class="team-logo">{{ teams[0].shortName }}</span>
            <div>
              <p class="caption">
                {{ teams[0].label }}
              </p>
              <h2>{{ teams[0].name }}</h2>
            </div>
          </div>
          <strong class="score-number home-score">{{ teams[0].score }}</strong>
          <div class="metric-grid three">
            <div class="metric-tile">
              <span class="metric-label">파울</span>
              <strong class="metric-value">{{ teams[0].fouls }}</strong>
            </div>
            <div class="metric-tile">
              <span class="metric-label">타임아웃</span>
              <strong class="metric-value">{{ teams[0].timeouts }}</strong>
            </div>
            <div class="metric-tile">
              <span class="metric-label">선수</span>
              <strong class="metric-value">{{ teams[0].players.length }}</strong>
            </div>
          </div>
        </article>

        <aside class="game-core">
          <span class="status-chip live">{{ quarterLabel }}</span>
          <strong class="game-clock">{{ clockLabel }}</strong>
          <div class="shot-clock">
            <span class="caption">SHOT</span>
            <strong class="shot-number">{{ pilotGame.shotClock }}</strong>
          </div>
          <p class="caption">
            {{ isClockRunning ? '경기 시간 진행 중' : '경기 시간 정지' }}
          </p>
        </aside>

        <article class="team-panel away">
          <div class="team-header">
            <span class="team-logo">{{ teams[1].shortName }}</span>
            <div>
              <p class="caption">
                {{ teams[1].label }}
              </p>
              <h2>{{ teams[1].name }}</h2>
            </div>
          </div>
          <strong class="score-number away-score">{{ teams[1].score }}</strong>
          <div class="metric-grid three">
            <div class="metric-tile">
              <span class="metric-label">파울</span>
              <strong class="metric-value">{{ teams[1].fouls }}</strong>
            </div>
            <div class="metric-tile">
              <span class="metric-label">타임아웃</span>
              <strong class="metric-value">{{ teams[1].timeouts }}</strong>
            </div>
            <div class="metric-tile">
              <span class="metric-label">선수</span>
              <strong class="metric-value">{{ teams[1].players.length }}</strong>
            </div>
          </div>
        </article>
      </section>

      <section class="control-grid">
        <article
          v-for="team in teams"
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
              :disabled="isControlDisabled()"
              @click="score(team.side, 1)"
            >
              +1
            </button>
            <button
              class="score-btn"
              type="button"
              :disabled="isControlDisabled()"
              @click="score(team.side, 2)"
            >
              +2
            </button>
            <button
              class="score-btn"
              type="button"
              :disabled="isControlDisabled()"
              @click="score(team.side, 3)"
            >
              +3
            </button>
          </div>
          <div class="aux-control-grid">
            <button
              class="score-btn secondary"
              type="button"
              :disabled="isControlDisabled()"
              @click="teamFoul(team.side)"
            >
              팀 파울
            </button>
            <button
              class="score-btn secondary"
              type="button"
              :disabled="isControlDisabled()"
              @click="timeout(team.side)"
            >
              타임아웃
            </button>
            <button
              class="btn-warn"
              type="button"
              :disabled="isControlDisabled()"
              @click="correctTeamScore(team.side)"
            >
              점수 정정
            </button>
            <button
              class="btn-danger"
              type="button"
              :disabled="isControlDisabled()"
              @click="playerFoul(team.side)"
            >
              개인 파울
            </button>
          </div>
        </article>

        <aside class="timer-panel">
          <div class="timer-face">
            <span class="status-chip live">{{ quarterLabel }}</span>
            <strong class="game-clock">{{ clockLabel }}</strong>
            <p class="caption">
              {{ statusLabel }}
            </p>
          </div>
          <div class="timer-button-grid">
            <button
              class="btn-success"
              type="button"
              :disabled="isClockActionDisabled()"
              @click="start"
            >
              시작
            </button>
            <button
              class="btn-danger"
              type="button"
              :disabled="isClockActionDisabled()"
              @click="stop"
            >
              정지
            </button>
            <button
              class="btn-ghost"
              type="button"
              :disabled="isClockActionDisabled()"
              @click="nextQuarter"
            >
              쿼터 +
            </button>
            <button
              class="btn-ghost"
              type="button"
              :disabled="isLoading || isActionPending"
              @click="refresh"
            >
              새로고침
            </button>
          </div>
          <button
            class="btn-dark"
            type="button"
            :disabled="isClockActionDisabled()"
            @click="finalize"
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
            v-for="event in eventRows"
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
