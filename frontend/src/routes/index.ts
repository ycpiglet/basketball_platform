import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router';
import HomeView from '@/app/HomeView.vue';
import ScoreboardControlView from '@/features/scoreboard/ScoreboardControlView.vue';
import ScoreboardDisplayView from '@/features/scoreboard/ScoreboardDisplayView.vue';
import DigitalScoreSheetView from '@/features/records/DigitalScoreSheetView.vue';
import EntityPlaceholderView from '@/shared/EntityPlaceholderView.vue';
import AccessDeniedView from '@/shared/AccessDeniedView.vue';
import { getDevSession } from '@/shared/auth/session';
import { hasMinimumRole, type Role } from '@/shared/types/roles';

const entityProps = (entityName: string) => ({ entityName });

export const routes: RouteRecordRaw[] = [
  { path: '/', name: 'home', component: HomeView },
  {
    path: '/games/:gameId/control',
    name: 'scoreboard-control',
    component: ScoreboardControlView,
    meta: { minimumRole: 'team_manager' satisfies Role },
  },
  {
    path: '/games/:gameId/display',
    name: 'scoreboard-display',
    component: ScoreboardDisplayView,
    meta: { publicDisplay: true },
  },
  {
    path: '/games/:gameId/record',
    name: 'digital-score-sheet',
    component: DigitalScoreSheetView,
    meta: { minimumRole: 'team_manager' satisfies Role },
  },
  { path: '/teams', name: 'teams', component: EntityPlaceholderView, props: entityProps('Teams') },
  { path: '/players', name: 'players', component: EntityPlaceholderView, props: entityProps('Players') },
  { path: '/leagues', name: 'leagues', component: EntityPlaceholderView, props: entityProps('Leagues') },
  { path: '/tournaments', name: 'tournaments', component: EntityPlaceholderView, props: entityProps('Tournaments') },
  { path: '/access-denied', name: 'access-denied', component: AccessDeniedView },
];

export const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to) => {
  const requiredRole = to.meta.minimumRole as Role | undefined;

  if (!requiredRole) {
    return true;
  }

  const session = getDevSession();

  if (!hasMinimumRole(session.role, requiredRole)) {
    return { name: 'access-denied', query: { requiredRole } };
  }

  return true;
});
