<script setup lang="ts">
import { ROUTE_PATHS } from '@/routes/route-constants';
import { pilotGame, pilotMetrics, pilotWorkPackages } from '@/shared/demo/pilotGame';
import { setDevRole } from '@/shared/auth/session';
import { roles, type Role } from '@/shared/types/roles';

function chooseRole(role: Role): void {
  setDevRole(role);
  window.location.reload();
}
</script>

<template>
  <main>
    <section class="hero-section">
      <div class="container hero-grid">
        <div class="stack-lg">
          <div class="inline-list">
            <span class="tag live">Phase 1 Field Pilot</span>
            <span class="tag warn">Demo UI · API 연결 전</span>
          </div>
          <h1>동호회 한 경기를 끝까지 운영하는 MVP 화면</h1>
          <p class="lead">
            Vercel 배포 테스트를 넘어서, 실제 아마추어 농구 현장에서 점수판 컨트롤,
            디지털 기록지, TV 표시, 결과 확인까지 이어지는 첫 번째 파일럿 흐름입니다.
          </p>
          <div class="button-row">
            <RouterLink
              class="btn"
              :to="ROUTE_PATHS.scoreboardControl"
            >
              경기 운영 시작
            </RouterLink>
            <RouterLink
              class="btn-ghost"
              :to="ROUTE_PATHS.scoreboardDisplay"
            >
              TV 표시 보기
            </RouterLink>
          </div>
        </div>

        <aside
          class="product-object"
          aria-label="Pilot game preview"
        >
          <div class="split-row">
            <span class="status-chip live">{{ pilotGame.status }}</span>
            <span class="caption">{{ pilotGame.venue }}</span>
          </div>
          <div class="mini-display">
            <div class="mini-display-score">
              <article class="mini-display-team">
                <span class="caption">{{ pilotGame.teams.home.label }}</span>
                <strong class="mini-score home-score">
                  {{ pilotGame.teams.home.score }}
                </strong>
                <span>{{ pilotGame.teams.home.shortName }}</span>
              </article>
              <div class="display-clock">
                <span class="tag dark">{{ pilotGame.quarter }}</span>
                <strong class="game-clock">{{ pilotGame.clock }}</strong>
              </div>
              <article class="mini-display-team">
                <span class="caption">{{ pilotGame.teams.away.label }}</span>
                <strong class="mini-score away-score">
                  {{ pilotGame.teams.away.score }}
                </strong>
                <span>{{ pilotGame.teams.away.shortName }}</span>
              </article>
            </div>
          </div>
          <p class="caption">
            {{ pilotGame.syncStatus }}
          </p>
        </aside>
      </div>
    </section>

    <section class="section">
      <div class="container dashboard-grid">
        <article
          v-for="metric in pilotMetrics"
          :key="metric.label"
          class="metric-panel"
        >
          <p class="eyebrow">
            {{ metric.label }}
          </p>
          <h2>{{ metric.value }}</h2>
          <p class="muted">
            {{ metric.note }}
          </p>
        </article>
      </div>
    </section>

    <section class="section">
      <div class="container two-column">
        <div class="stack-lg">
          <p class="section-kicker">
            Pilot workflow
          </p>
          <h2>다음 구현 목표는 연결된 vertical slice입니다.</h2>
          <p class="muted">
            기준 프로토타입의 화면 흐름을 Vue 라우트로 옮긴 데모입니다.
            다음 단계에서 서버 상태와 연결해 현장 테스트 가능한 상태로 만듭니다.
          </p>
        </div>
        <div class="stack">
          <article
            v-for="item in pilotWorkPackages"
            :key="item.id"
            class="feature-panel"
          >
            <div class="split-row">
              <strong>{{ item.id }}</strong>
              <span class="status-chip">{{ item.status }}</span>
            </div>
            <p>{{ item.label }}</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container panel">
        <div class="split-row">
          <div>
            <p class="section-kicker">
              Development guard
            </p>
            <h2>역할별 화면 접근 확인</h2>
          </div>
          <div
            class="role-strip"
            aria-label="Development role picker"
          >
            <button
              v-for="role in roles"
              :key="role"
              class="role-btn"
              type="button"
              @click="chooseRole(role)"
            >
              {{ role }}
            </button>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>
