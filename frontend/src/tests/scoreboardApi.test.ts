import { afterEach, describe, expect, it, vi } from 'vitest';
import {
  addPoints,
  createScoreboardGame,
  ensureScoreboardGame,
  ScoreboardApiError,
  type ScoreboardState,
} from '@/features/scoreboard/scoreboardApi';
import {
  buildScoreboardTeams,
  formatGameClock,
  gameStatusLabel,
} from '@/features/scoreboard/scoreboardViewModel';

const scoreboardState: ScoreboardState = {
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
  event_log: [],
};

describe('scoreboard API client', () => {
  afterEach(() => {
    vi.unstubAllGlobals();
    window.localStorage.clear();
  });

  it('sends the development role headers for pilot state changes', async () => {
    window.localStorage.setItem('basketball_platform_dev_role', 'team_manager');
    const fetchMock = mockFetch(jsonResponse(scoreboardState, 201));

    await createScoreboardGame('demo-game');

    const [url, options] = fetchMock.mock.calls[0] as Parameters<typeof fetch>;
    const headers = options?.headers as Headers;
    expect(url).toBe('http://localhost:8000/api/v1/scoreboard/games');
    expect(options?.method).toBe('POST');
    expect(headers.get('x-user-role')).toBe('team_manager');
    expect(headers.get('x-user-id')).toBe('frontend-pilot-operator');
  });

  it('creates the pilot game after a not-found read', async () => {
    const fetchMock = mockFetch(
      jsonResponse({ error: { code: 'not_found', message: 'missing' } }, 404),
      jsonResponse(scoreboardState, 201),
    );

    const state = await ensureScoreboardGame('demo-game');

    expect(state.game_id).toBe('demo-game');
    expect(fetchMock).toHaveBeenCalledTimes(2);
  });

  it('surfaces backend validation errors with fields', async () => {
    mockFetch(
      jsonResponse(
        {
          error: {
            code: 'validation_error',
            message: 'Request validation failed.',
            fields: ['body.points'],
          },
        },
        422,
      ),
    );

    await expect(addPoints('demo-game', 'home', 'h-7', 3)).rejects.toMatchObject({
      status: 422,
      code: 'validation_error',
      fields: ['body.points'],
    } satisfies Partial<ScoreboardApiError>);
  });
});

describe('scoreboard view model', () => {
  it('formats game clock and status labels from backend state', () => {
    expect(formatGameClock(455)).toBe('07:35');
    expect(gameStatusLabel(scoreboardState)).toBe('2쿼터 정지');
  });

  it('maps backend team state onto pilot team metadata', () => {
    const [home, away] = buildScoreboardTeams(scoreboardState);

    expect(home.name).toBe('Blue Hoopers');
    expect(home.score).toBe(12);
    expect(home.fouls).toBe(3);
    expect(away.name).toBe('White Wings');
    expect(away.timeouts).toBe(5);
  });
});

function mockFetch(...responses: Response[]) {
  const fetchMock = vi.fn<typeof fetch>();

  for (const response of responses) {
    fetchMock.mockResolvedValueOnce(response);
  }

  vi.stubGlobal('fetch', fetchMock);
  return fetchMock;
}

function jsonResponse(payload: unknown, status = 200): Response {
  return new Response(JSON.stringify(payload), {
    status,
    headers: { 'Content-Type': 'application/json' },
  });
}
