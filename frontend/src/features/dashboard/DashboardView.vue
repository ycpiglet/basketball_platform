<script setup lang="ts">
import { pilotGame, pilotWorkPackages } from '@/shared/demo/pilotGame';
</script>

<template>
  <main class="screen-pad">
    <div class="container stack-lg">
      <header class="two-column">
        <div class="stack">
          <p class="section-kicker">
            Operations dashboard
          </p>
          <h1>오늘의 파일럿 운영 상태</h1>
          <p class="lead">
            실제 동호회 적용 전, 경기 운영 흐름과 미구현 위험을 한눈에 보는 화면입니다.
          </p>
        </div>
        <aside class="panel">
          <span class="status-chip live">{{ pilotGame.title }}</span>
          <p class="muted">
            {{ pilotGame.venue }}
          </p>
        </aside>
      </header>

      <section class="dashboard-grid">
        <article
          v-for="item in pilotWorkPackages"
          :key="item.id"
          class="feature-panel"
        >
          <div class="split-row">
            <strong>{{ item.id }}</strong>
            <span class="status-chip">{{ item.status }}</span>
          </div>
          <h3>{{ item.label }}</h3>
        </article>
      </section>

      <section class="two-column">
        <article class="panel">
          <p class="section-kicker">
            Run order
          </p>
          <div class="event-list">
            <div class="event-row">
              <strong>01</strong>
              <span class="tag">준비</span>
              <span>팀, 선수, 경기 규칙 확인</span>
            </div>
            <div class="event-row">
              <strong>02</strong>
              <span class="tag">운영</span>
              <span>컨트롤 화면과 TV 표시 화면 동시 사용</span>
            </div>
            <div class="event-row">
              <strong>03</strong>
              <span class="tag">검토</span>
              <span>결과와 이벤트 로그 확인 후 피드백 수집</span>
            </div>
          </div>
        </article>
        <article class="panel">
          <p class="section-kicker">
            Known blockers
          </p>
          <div class="stack">
            <span class="status-chip">Backend API 미연결</span>
            <span class="status-chip">Python 3.11+ 테스트 환경 필요</span>
            <span class="status-chip">Persistence 전략 미정</span>
          </div>
        </article>
      </section>
    </div>
  </main>
</template>
