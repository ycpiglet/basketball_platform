<template>
  <main class="screen-pad">
    <section
      class="container panel error-card"
      role="alert"
    >
      <p class="section-kicker">
        Access denied
      </p>
      <h1>Permission required</h1>
      <p>This route is protected by the development RBAC guard. Backend authorization is still required later.</p>
      <RouterLink
        class="btn-ghost"
        to="/"
      >
        Return home
      </RouterLink>
    </section>
  </main>
</template>
