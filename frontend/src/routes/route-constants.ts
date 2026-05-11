export const ROUTE_PATHS = {
  home: '/',
  dashboard: '/dashboard',
  scoreboardControl: '/scoreboard/control',
  scoreboardDisplay: '/scoreboard/display',
  gameLive: '/games/:id/live',
  gameResult: '/games/:id/result',
  teams: '/teams',
  players: '/players',
  leagues: '/leagues',
  tournaments: '/tournaments',
  accessDenied: '/access-denied',
} as const;

export const ROUTE_NAMES = {
  home: 'home',
  dashboard: 'dashboard',
  scoreboardControl: 'scoreboard-control',
  scoreboardDisplay: 'scoreboard-display',
  gameLive: 'game-live',
  gameResult: 'game-result',
  teams: 'teams',
  players: 'players',
  leagues: 'leagues',
  tournaments: 'tournaments',
  accessDenied: 'access-denied',
} as const;

export type RouteName = (typeof ROUTE_NAMES)[keyof typeof ROUTE_NAMES];
export type RoutePath = (typeof ROUTE_PATHS)[keyof typeof ROUTE_PATHS];
