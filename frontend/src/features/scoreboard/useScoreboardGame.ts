import { computed, onBeforeUnmount, ref } from 'vue';
import {
  addPlayerFoul,
  addPoints,
  addTeamFoul,
  correctScore,
  ensureScoreboardGame,
  finalizeGame,
  getScoreboardGame,
  PILOT_GAME_ID,
  ScoreboardApiError,
  setQuarter,
  startClock,
  stopClock,
  useTimeout,
  type ScoreboardState,
  type TeamSide,
} from './scoreboardApi';
import {
  buildScoreboardTeams,
  defaultPlayerId,
  eventRowsFromState,
  formatGameClock,
  gameStatusLabel,
} from './scoreboardViewModel';

const POLL_INTERVAL_MS = 2000;

export function useScoreboardGame() {
  const state = ref<ScoreboardState | null>(null);
  const isLoading = ref(false);
  const isActionPending = ref(false);
  const errorMessage = ref<string | null>(null);
  let pollTimer: number | undefined;

  const teams = computed(() => buildScoreboardTeams(state.value));
  const homeTeam = computed(() => teams.value[0]);
  const awayTeam = computed(() => teams.value[1]);
  const eventRows = computed(() => eventRowsFromState(state.value));
  const statusLabel = computed(() => gameStatusLabel(state.value));
  const clockLabel = computed(() => formatGameClock(state.value?.clock.remaining_seconds ?? 600));
  const quarterLabel = computed(() => `Q${state.value?.clock.quarter ?? 1}`);
  const isFinal = computed(() => state.value?.game_status === 'final');
  const isClockRunning = computed(() => state.value?.clock.status === 'running');

  async function ensureGame(): Promise<void> {
    await runLoad(async () => {
      state.value = await ensureScoreboardGame(PILOT_GAME_ID);
    });
  }

  async function refresh(): Promise<void> {
    await runLoad(async () => {
      state.value = await getScoreboardGame(PILOT_GAME_ID);
    });
  }

  async function score(team: TeamSide, points: 1 | 2 | 3): Promise<void> {
    await runAction(async () => {
      const teamView = team === 'home' ? homeTeam.value : awayTeam.value;
      state.value = await addPoints(PILOT_GAME_ID, team, defaultPlayerId(teamView), points);
    });
  }

  async function teamFoul(team: TeamSide): Promise<void> {
    await runAction(async () => {
      state.value = await addTeamFoul(PILOT_GAME_ID, team);
    });
  }

  async function playerFoul(team: TeamSide): Promise<void> {
    await runAction(async () => {
      const teamView = team === 'home' ? homeTeam.value : awayTeam.value;
      state.value = await addPlayerFoul(PILOT_GAME_ID, team, defaultPlayerId(teamView));
    });
  }

  async function timeout(team: TeamSide): Promise<void> {
    await runAction(async () => {
      state.value = await useTimeout(PILOT_GAME_ID, team);
    });
  }

  async function correction(team: TeamSide, scoreValue: number, reason: string): Promise<void> {
    await runAction(async () => {
      state.value = await correctScore(PILOT_GAME_ID, team, scoreValue, reason);
    });
  }

  async function start(): Promise<void> {
    await runAction(async () => {
      state.value = await startClock(PILOT_GAME_ID);
    });
  }

  async function stop(): Promise<void> {
    await runAction(async () => {
      state.value = await stopClock(PILOT_GAME_ID, state.value?.clock.remaining_seconds ?? 600);
    });
  }

  async function nextQuarter(): Promise<void> {
    await runAction(async () => {
      const nextQuarterValue = (state.value?.clock.quarter ?? 1) + 1;
      state.value = await setQuarter(PILOT_GAME_ID, nextQuarterValue, 600);
    });
  }

  async function finalize(): Promise<void> {
    await runAction(async () => {
      state.value = await finalizeGame(PILOT_GAME_ID);
    });
  }

  function startPolling(): void {
    stopPolling();
    pollTimer = window.setInterval(() => {
      void refresh();
    }, POLL_INTERVAL_MS);
  }

  function stopPolling(): void {
    if (pollTimer !== undefined) {
      window.clearInterval(pollTimer);
      pollTimer = undefined;
    }
  }

  onBeforeUnmount(stopPolling);

  async function runLoad(task: () => Promise<void>): Promise<void> {
    isLoading.value = true;
    errorMessage.value = null;

    try {
      await task();
    } catch (error) {
      errorMessage.value = toUserMessage(error);
    } finally {
      isLoading.value = false;
    }
  }

  async function runAction(task: () => Promise<void>): Promise<void> {
    isActionPending.value = true;
    errorMessage.value = null;

    try {
      await task();
    } catch (error) {
      errorMessage.value = toUserMessage(error);
    } finally {
      isActionPending.value = false;
    }
  }

  return {
    state,
    teams,
    homeTeam,
    awayTeam,
    eventRows,
    statusLabel,
    clockLabel,
    quarterLabel,
    isFinal,
    isClockRunning,
    isLoading,
    isActionPending,
    errorMessage,
    ensureGame,
    refresh,
    score,
    teamFoul,
    playerFoul,
    timeout,
    correction,
    start,
    stop,
    nextQuarter,
    finalize,
    startPolling,
    stopPolling,
  };
}

function toUserMessage(error: unknown): string {
  if (error instanceof ScoreboardApiError) {
    return error.message;
  }

  if (error instanceof TypeError) {
    return 'Backend API에 연결할 수 없습니다.';
  }

  return 'Scoreboard 상태를 처리하지 못했습니다.';
}
