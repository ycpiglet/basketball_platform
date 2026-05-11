import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router';
import HomeView from '@/app/HomeView.vue';
import DashboardView from '@/features/dashboard/DashboardView.vue';
import GameLiveView from '@/features/games/GameLiveView.vue';
import GameResultView from '@/features/games/GameResultView.vue';
import LeaguesView from '@/features/leagues/LeaguesView.vue';
import PlayersView from '@/features/players/PlayersView.vue';
import ScoreboardControlView from '@/features/scoreboard/ScoreboardControlView.vue';
import ScoreboardDisplayView from '@/features/scoreboard/ScoreboardDisplayView.vue';
import TeamsView from '@/features/teams/TeamsView.vue';
import TournamentsView from '@/features/tournaments/TournamentsView.vue';
import AccessDeniedView from '@/shared/AccessDeniedView.vue';
import { getDevSession } from '@/shared/auth/session';
import { hasMinimumRole, type Role } from '@/shared/types/roles';
import { ROUTE_NAMES, ROUTE_PATHS } from './route-constants';

export const routes: RouteRecordRaw[] = [
  { path: ROUTE_PATHS.home, name: ROUTE_NAMES.home, component: HomeView },
  {
    path: ROUTE_PATHS.dashboard,
    name: ROUTE_NAMES.dashboard,
    component: DashboardView,
    meta: { minimumRole: 'user' satisfies Role },
  },
  {
    path: ROUTE_PATHS.scoreboardControl,
    name: ROUTE_NAMES.scoreboardControl,
    component: ScoreboardControlView,
    meta: { minimumRole: 'team_manager' satisfies Role },
  },
  {
    path: ROUTE_PATHS.scoreboardDisplay,
    name: ROUTE_NAMES.scoreboardDisplay,
    component: ScoreboardDisplayView,
    meta: { publicDisplay: true },
  },
  {
    path: ROUTE_PATHS.gameLive,
    name: ROUTE_NAMES.gameLive,
    component: GameLiveView,
    meta: { minimumRole: 'team_manager' satisfies Role },
  },
  {
    path: ROUTE_PATHS.gameResult,
    name: ROUTE_NAMES.gameResult,
    component: GameResultView,
  },
  { path: ROUTE_PATHS.teams, name: ROUTE_NAMES.teams, component: TeamsView },
  { path: ROUTE_PATHS.players, name: ROUTE_NAMES.players, component: PlayersView },
  { path: ROUTE_PATHS.leagues, name: ROUTE_NAMES.leagues, component: LeaguesView },
  { path: ROUTE_PATHS.tournaments, name: ROUTE_NAMES.tournaments, component: TournamentsView },
  { path: ROUTE_PATHS.accessDenied, name: ROUTE_NAMES.accessDenied, component: AccessDeniedView },
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
    return { name: ROUTE_NAMES.accessDenied, query: { requiredRole } };
  }

  return true;
});
