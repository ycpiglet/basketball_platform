import { getDevSession } from '@/shared/auth/session';

export const PILOT_GAME_ID = 'demo-game';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? 'http://localhost:8000/api/v1';

export type TeamSide = 'home' | 'away';
export type ClockStatus = 'stopped' | 'running';
export type GameStatus = 'not_started' | 'in_progress' | 'final';

export interface ScoreboardClock {
  quarter: number;
  remaining_seconds: number;
  status: ClockStatus;
}

export interface TeamScoreboard {
  score: number;
  team_fouls: number;
  timeouts_remaining: number;
}

export interface PlayerStat {
  player_id: string;
  points: number;
  fouls: number;
}

export interface ScoreboardEvent {
  sequence: number;
  event_type:
    | 'score_added'
    | 'score_corrected'
    | 'team_foul_added'
    | 'player_foul_added'
    | 'timeout_used'
    | 'clock_started'
    | 'clock_stopped'
    | 'quarter_set'
    | 'game_ended';
  occurred_at: string;
  summary: string;
  payload: Record<string, unknown>;
}

export interface ScoreboardState {
  game_id: string;
  game_status: GameStatus;
  clock: ScoreboardClock;
  home: TeamScoreboard;
  away: TeamScoreboard;
  player_stats: PlayerStat[];
  event_log: ScoreboardEvent[];
}

export class ScoreboardApiError extends Error {
  constructor(
    message: string,
    public readonly status: number,
    public readonly code: string,
    public readonly fields: string[] = [],
  ) {
    super(message);
    this.name = 'ScoreboardApiError';
  }
}

interface BackendErrorResponse {
  error?: {
    code?: string;
    message?: string;
    fields?: string[];
  };
}

export async function getScoreboardGame(gameId = PILOT_GAME_ID): Promise<ScoreboardState> {
  return requestScoreboard<ScoreboardState>(`/scoreboard/games/${gameId}`);
}

export async function ensureScoreboardGame(gameId = PILOT_GAME_ID): Promise<ScoreboardState> {
  try {
    return await getScoreboardGame(gameId);
  } catch (error) {
    if (error instanceof ScoreboardApiError && error.status === 404) {
      return createScoreboardGame(gameId);
    }
    throw error;
  }
}

export async function createScoreboardGame(gameId = PILOT_GAME_ID): Promise<ScoreboardState> {
  return requestScoreboard<ScoreboardState>('/scoreboard/games', {
    method: 'POST',
    body: JSON.stringify({ game_id: gameId }),
    withRole: true,
  });
}

export async function addPoints(
  gameId: string,
  team: TeamSide,
  playerId: string,
  points: 1 | 2 | 3,
): Promise<ScoreboardState> {
  return requestScoreboard<ScoreboardState>(`/scoreboard/games/${gameId}/points`, {
    method: 'POST',
    body: JSON.stringify({ team, player_id: playerId, points }),
    withRole: true,
  });
}

export async function correctScore(
  gameId: string,
  team: TeamSide,
  correctedScore: number,
  reason: string,
): Promise<ScoreboardState> {
  return requestScoreboard<ScoreboardState>(`/scoreboard/games/${gameId}/score-corrections`, {
    method: 'POST',
    body: JSON.stringify({ team, corrected_score: correctedScore, reason }),
    withRole: true,
  });
}

export async function addTeamFoul(gameId: string, team: TeamSide): Promise<ScoreboardState> {
  return requestScoreboard<ScoreboardState>(`/scoreboard/games/${gameId}/team-fouls`, {
    method: 'POST',
    body: JSON.stringify({ team }),
    withRole: true,
  });
}

export async function addPlayerFoul(
  gameId: string,
  team: TeamSide,
  playerId: string,
): Promise<ScoreboardState> {
  return requestScoreboard<ScoreboardState>(`/scoreboard/games/${gameId}/player-fouls`, {
    method: 'POST',
    body: JSON.stringify({ team, player_id: playerId }),
    withRole: true,
  });
}

export async function useTimeout(gameId: string, team: TeamSide): Promise<ScoreboardState> {
  return requestScoreboard<ScoreboardState>(`/scoreboard/games/${gameId}/timeouts`, {
    method: 'POST',
    body: JSON.stringify({ team }),
    withRole: true,
  });
}

export async function setQuarter(
  gameId: string,
  quarter: number,
  remainingSeconds: number,
): Promise<ScoreboardState> {
  return requestScoreboard<ScoreboardState>(`/scoreboard/games/${gameId}/quarters`, {
    method: 'POST',
    body: JSON.stringify({ quarter, remaining_seconds: remainingSeconds }),
    withRole: true,
  });
}

export async function startClock(gameId: string): Promise<ScoreboardState> {
  return requestScoreboard<ScoreboardState>(`/scoreboard/games/${gameId}/clock/start`, {
    method: 'POST',
    withRole: true,
  });
}

export async function stopClock(
  gameId: string,
  remainingSeconds: number,
): Promise<ScoreboardState> {
  return requestScoreboard<ScoreboardState>(`/scoreboard/games/${gameId}/clock/stop`, {
    method: 'POST',
    body: JSON.stringify({ remaining_seconds: remainingSeconds }),
    withRole: true,
  });
}

export async function finalizeGame(gameId: string): Promise<ScoreboardState> {
  return requestScoreboard<ScoreboardState>(`/scoreboard/games/${gameId}/finalize`, {
    method: 'POST',
    withRole: true,
  });
}

interface ScoreboardRequestOptions extends RequestInit {
  withRole?: boolean;
}

async function requestScoreboard<T>(
  path: string,
  options: ScoreboardRequestOptions = {},
): Promise<T> {
  const headers = new Headers(options.headers);
  headers.set('Accept', 'application/json');

  if (options.body) {
    headers.set('Content-Type', 'application/json');
  }

  if (options.withRole) {
    const session = getDevSession();
    headers.set('x-user-role', session.role);
    headers.set('x-user-id', 'frontend-pilot-operator');
  }

  const response = await fetch(`${API_BASE_URL}${path}`, { ...options, headers });
  const payload = await parseJsonResponse(response);

  if (!response.ok) {
    const backendError = payload as BackendErrorResponse;
    throw new ScoreboardApiError(
      backendError.error?.message ?? 'Scoreboard API request failed.',
      response.status,
      backendError.error?.code ?? 'scoreboard_api_error',
      backendError.error?.fields ?? [],
    );
  }

  return payload as T;
}

async function parseJsonResponse(response: Response): Promise<unknown> {
  const text = await response.text();

  if (!text) {
    return {};
  }

  try {
    return JSON.parse(text) as unknown;
  } catch {
    throw new ScoreboardApiError(
      'Scoreboard API returned an invalid JSON response.',
      response.status,
      'invalid_json_response',
    );
  }
}
