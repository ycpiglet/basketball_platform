<script setup lang="ts">
defineProps<{
  eyebrow: string;
  title: string;
  description: string;
  nextSteps?: string[];
}>();
</script>

<template>
  <main class="page-shell">
    <section class="hero-card placeholder-card">
      <p class="eyebrow">{{ eyebrow }}</p>
      <h1>{{ title }}</h1>
      <p>{{ description }}</p>

      <div v-if="nextSteps?.length" class="next-step-panel" aria-label="Planned MVP work">
        <h2>Planned next steps</h2>
        <ul>
          <li v-for="step in nextSteps" :key="step">{{ step }}</li>
        </ul>
      </div>
    </section>
  </main>
</template>
