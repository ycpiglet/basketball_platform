<script setup lang="ts">
defineProps<{
  eyebrow: string;
  title: string;
  description: string;
  nextSteps?: string[];
}>();
</script>

<template>
  <main class="screen-pad">
    <div class="container crud-grid">
      <section class="stack-lg">
        <p class="section-kicker">
          {{ eyebrow }}
        </p>
        <h1>{{ title }}</h1>
        <p class="lead">
          {{ description }}
        </p>
        <div class="button-row">
          <RouterLink
            class="btn"
            to="/scoreboard/control"
          >
            파일럿 운영
          </RouterLink>
          <RouterLink
            class="btn-ghost"
            to="/dashboard"
          >
            대시보드
          </RouterLink>
        </div>
      </section>

      <aside class="crud-panel">
        <div class="split-row">
          <h2>Phase 1 준비 상태</h2>
          <span class="status-chip">Placeholder</span>
        </div>
        <div class="event-list">
          <div
            v-for="step in nextSteps ?? ['검색, 필터, 페이지네이션', '권한별 액션', 'API 연결 후 오류/재시도 상태']"
            :key="step"
            class="event-row"
          >
            <strong>TODO</strong>
            <span class="tag">MVP</span>
            <span>{{ step }}</span>
          </div>
        </div>
      </aside>
    </div>
  </main>
</template>
