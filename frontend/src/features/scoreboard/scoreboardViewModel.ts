import { pilotGame, type PilotTeam } from '@/shared/demo/pilotGame';
import type { ScoreboardEvent, ScoreboardState, TeamSide } from './scoreboardApi';

export interface ScoreboardTeamView extends PilotTeam {
  score: number;
  fouls: number;
  timeouts: number;
}

export interface ScoreboardEventRow {
  time: string;
  team: string;
  text: string;
}

export function formatGameClock(totalSeconds: number): string {
  const safeSeconds = Math.max(0, totalSeconds);
  const minutes = Math.floor(safeSeconds / 60);
  const seconds = safeSeconds % 60;

  return `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
}

export function gameStatusLabel(state: ScoreboardState | null): string {
  if (!state) {
    return 'Backend 연결 대기';
  }

  if (state.game_status === 'final') {
    return '경기 종료';
  }

  if (state.clock.status === 'running') {
    return `${state.clock.quarter}쿼터 진행`;
  }

  if (state.game_status === 'in_progress') {
    return `${state.clock.quarter}쿼터 정지`;
  }

  return '경기 준비';
}

export function buildScoreboardTeams(state: ScoreboardState | null): ScoreboardTeamView[] {
  return (['home', 'away'] as const).map((side) => {
    const teamMeta = pilotGame.teams[side];
    const teamState = state?.[side];

    return {
      ...teamMeta,
      score: teamState?.score ?? 0,
      fouls: teamState?.team_fouls ?? 0,
      timeouts: teamState?.timeouts_remaining ?? 0,
    };
  });
}

export function eventRowsFromState(state: ScoreboardState | null): ScoreboardEventRow[] {
  if (!state) {
    return [];
  }

  return state.event_log
    .slice()
    .reverse()
    .slice(0, 8)
    .map((event) => scoreboardEventToRow(event));
}

export function scoreboardEventToRow(event: ScoreboardEvent): ScoreboardEventRow {
  const team = readTeam(event.payload.team);
  const time = new Intl.DateTimeFormat('ko-KR', {
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
  }).format(new Date(event.occurred_at));

  return {
    time,
    team: team ? pilotGame.teams[team].shortName : 'TABLE',
    text: event.summary,
  };
}

export function defaultPlayerId(team: ScoreboardTeamView): string {
  return team.players[0]?.id ?? `${team.side}-pilot-player`;
}

function readTeam(value: unknown): TeamSide | null {
  return value === 'home' || value === 'away' ? value : null;
}
