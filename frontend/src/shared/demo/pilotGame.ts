export type TeamSide = 'home' | 'away';

export type PilotPlayer = {
  id: string;
  number: number;
  name: string;
  points: number;
  fouls: number;
  assists: number;
  rebounds: number;
};

export type PilotTeam = {
  side: TeamSide;
  label: string;
  name: string;
  shortName: string;
  color: string;
  score: number;
  fouls: number;
  timeouts: number;
  players: PilotPlayer[];
};

export type PilotEvent = {
  time: string;
  team: string;
  text: string;
  type: 'score' | 'foul' | 'timer' | 'correction' | 'timeout';
};

export const pilotGame = {
  id: 'demo-game',
  title: '필드 파일럿 연습 경기',
  venue: '동호회 체육관 A코트',
  status: '2쿼터 진행',
  clock: '06:42',
  shotClock: 18,
  quarter: 'Q2',
  possession: 'home' as TeamSide,
  syncStatus: 'Demo state · Backend API 연결 전',
  teams: {
    home: {
      side: 'home',
      label: 'HOME',
      name: 'Blue Hoopers',
      shortName: 'BLU',
      color: '#ffd60a',
      score: 38,
      fouls: 4,
      timeouts: 3,
      players: [
        { id: 'h-7', number: 7, name: 'Kim', points: 12, fouls: 2, assists: 3, rebounds: 4 },
        { id: 'h-11', number: 11, name: 'Park', points: 8, fouls: 1, assists: 4, rebounds: 2 },
        { id: 'h-23', number: 23, name: 'Lee', points: 10, fouls: 0, assists: 1, rebounds: 7 },
        { id: 'h-31', number: 31, name: 'Choi', points: 6, fouls: 1, assists: 2, rebounds: 3 },
      ],
    },
    away: {
      side: 'away',
      label: 'AWAY',
      name: 'White Wings',
      shortName: 'WHT',
      color: '#2997ff',
      score: 35,
      fouls: 3,
      timeouts: 4,
      players: [
        { id: 'a-3', number: 3, name: 'Han', points: 9, fouls: 1, assists: 5, rebounds: 1 },
        { id: 'a-9', number: 9, name: 'Jung', points: 11, fouls: 2, assists: 2, rebounds: 5 },
        { id: 'a-14', number: 14, name: 'Seo', points: 7, fouls: 0, assists: 1, rebounds: 6 },
        { id: 'a-21', number: 21, name: 'Yoon', points: 8, fouls: 0, assists: 3, rebounds: 2 },
      ],
    },
  } satisfies Record<TeamSide, PilotTeam>,
  events: [
    { time: '06:42', team: 'BLU', text: '#7 Kim 3점 성공', type: 'score' },
    { time: '07:10', team: 'WHT', text: '#9 Jung 개인 파울', type: 'foul' },
    { time: '07:28', team: 'BLU', text: '작전 시간 사용', type: 'timeout' },
    { time: '08:01', team: 'WHT', text: '#3 Han 속공 2점', type: 'score' },
    { time: '08:44', team: 'TABLE', text: '점수 정정 사유 기록됨', type: 'correction' },
  ] satisfies PilotEvent[],
};

export const pilotTeams = [pilotGame.teams.home, pilotGame.teams.away] as const;

export const pilotWorkPackages = [
  { id: 'FP-001', label: 'Scoreboard API', status: 'Next' },
  { id: 'FP-003', label: 'Control UI', status: 'Demo' },
  { id: 'FP-004', label: 'Display sync', status: 'Planned' },
  { id: 'FP-006', label: 'Result view', status: 'Demo' },
] as const;

export const pilotMetrics = [
  { label: '필드 파일럿 목표', value: '1 경기', note: '동호회 연습 경기 기준' },
  { label: '운영 기기', value: '2 대', note: '컨트롤 + TV 표시' },
  { label: '현재 단계', value: 'UI 데모', note: 'API 연결 전' },
] as const;
