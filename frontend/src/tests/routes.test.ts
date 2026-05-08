import { describe, expect, it } from 'vitest';
import { routes } from '@/routes';
import { ROUTE_NAMES, ROUTE_PATHS } from '@/routes/route-constants';

const routePaths = routes.map((route) => route.path);
const routeNames = routes.map((route) => route.name);

describe('Phase 1 MVP routes', () => {
  it('registers every requested placeholder path', () => {
    expect(routePaths).toEqual(
      expect.arrayContaining([
        ROUTE_PATHS.home,
        ROUTE_PATHS.scoreboardControl,
        ROUTE_PATHS.scoreboardDisplay,
        ROUTE_PATHS.gameLive,
        ROUTE_PATHS.gameResult,
        ROUTE_PATHS.teams,
        ROUTE_PATHS.players,
        ROUTE_PATHS.leagues,
        ROUTE_PATHS.tournaments,
        ROUTE_PATHS.dashboard,
      ]),
    );
  });

  it('marks the scoreboard display route as public display only', () => {
    const displayRoute = routes.find((route) => route.name === ROUTE_NAMES.scoreboardDisplay);

    expect(displayRoute?.meta?.publicDisplay).toBe(true);
    expect(displayRoute?.meta?.minimumRole).toBeUndefined();
  });

  it('keeps operational live routes role-gated by the development RBAC guard', () => {
    const protectedRouteNames = [
      ROUTE_NAMES.dashboard,
      ROUTE_NAMES.scoreboardControl,
      ROUTE_NAMES.gameLive,
    ];

    for (const routeName of protectedRouteNames) {
      expect(routeNames).toContain(routeName);
      expect(routes.find((route) => route.name === routeName)?.meta?.minimumRole).toBeDefined();
    }
  });
});
