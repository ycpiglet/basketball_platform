import { expect, test, type Page } from '@playwright/test';

const scoreboardState = {
  game_id: 'demo-game',
  game_status: 'in_progress',
  clock: {
    quarter: 2,
    remaining_seconds: 455,
    status: 'stopped',
  },
  home: {
    score: 12,
    team_fouls: 3,
    timeouts_remaining: 4,
  },
  away: {
    score: 9,
    team_fouls: 2,
    timeouts_remaining: 5,
  },
  player_stats: [],
  event_log: [
    {
      sequence: 1,
      event_type: 'score_added',
      occurred_at: '2026-05-13T10:00:00Z',
      summary: 'Added 3 point(s) for home.',
      payload: { team: 'home', points: 3 },
    },
  ],
};

test('scoreboard control renders backend state and sends score updates', async ({ page }) => {
  await mockScoreboardApi(page);
  await page.addInitScript(() => {
    window.localStorage.setItem('basketball_platform_dev_role', 'team_manager');
  });

  await page.goto('/scoreboard/control');

  await expect(page.getByRole('heading', { name: '경기 운영 컨트롤' })).toBeVisible();
  await expect(page.getByText('07:35').first()).toBeVisible();
  await expect(page.getByText('12').first()).toBeVisible();

  await page.getByRole('button', { name: '+3' }).first().click();

  await expect(page.getByText('15').first()).toBeVisible();
});

test('scoreboard display renders without operator controls', async ({ page }) => {
  await mockScoreboardApi(page);

  await page.goto('/scoreboard/display');

  await expect(page.getByLabel('Public scoreboard display')).toBeVisible();
  await expect(page.getByText('Blue Hoopers')).toBeVisible();
  await expect(page.getByText('White Wings')).toBeVisible();
  await expect(page.getByRole('button', { name: '+3' })).toHaveCount(0);
});

async function mockScoreboardApi(page: Page): Promise<void> {
  let currentState = structuredClone(scoreboardState);

  await page.route('**/api/v1/scoreboard/games/demo-game', async (route) => {
    await route.fulfill({ json: currentState });
  });

  await page.route('**/api/v1/scoreboard/games/demo-game/points', async (route) => {
    const payload = route.request().postDataJSON() as { team: 'home' | 'away'; points: number };
    currentState = {
      ...currentState,
      [payload.team]: {
        ...currentState[payload.team],
        score: currentState[payload.team].score + payload.points,
      },
    };
    await route.fulfill({ json: currentState });
  });
}
