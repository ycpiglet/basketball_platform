# 재개 인수인계 — 2026-09-28 종료 기준

## 기준과 증거 경계

- 기준: **2026-09-28 23:59:59 KST**. 9월 29일 변경/대화는 분석하지 않았다.
- 기준 원격/커밋: `origin/main` `8cb3b44` (2026-05-12). 이 문서는 그 커밋에서 분기한 `codex/handoff-pre-20260929`에만 존재한다.
- 채팅 원문은 저장소에 없다. 단, 2026-05-13으로 명시된 uncommitted harness/run 문서와 patch가 남아 있어 아래의 중단 상태는 강한 증거가 있다. 이 patch는 **아직 커밋/통합/재검증된 결과가 아니다**.

## 제품 목표

실제 아마추어 경기에서 쓰는 Phase 1 MVP: 신뢰 가능한 scoreboard control/display, digital scoresheet, 경기·팀·선수 CRUD, 권한·로그·검증, 터치 친화 UI를 우선한다. 결제/지갑/광고 같은 Phase 2는 시작하지 않는다.

## 과거 대화/작업의 재구성

`summary/status.md`와 four run folders가 남긴 결론은 “데모 UI를 실제 field-pilot vertical slice로 올리자”였다.

1. backend pilot scoreboard API를 FastAPI service/store/schema와 테스트로 만든다.
2. Vue control route가 API를 읽고 mutation하며, public display route가 polling으로 같은 상태를 읽게 만든다.
3. Playwright E2E와 Vercel/Supabase/Sentry 운영 환경 문서를 추가한다.
4. 역할 기반 harness를 7개 operating role로 정리하고 각 handoff/compound state를 남긴다.

## 중단 지점과 현재 결과

main에는 2026-05-12의 UI/harness까지만 커밋됐다. 그 위에 **29 tracked files, 2,352 insertions / 134 deletions 및 untracked scoreboard API·frontend modules·E2E·harness records**가 남아 있다. 즉, 의도된 결과는 “pre-alpha connected scoreboard slice”지만 Git 기준으로는 미완료 작업 트리다.

다음 파일이 재개 정본이다.

- `summary/status.md`: 즉시 목표와 open items
- `harness/compound/state/2026-05-13_pilot_scoreboard_api_state.md`
- `harness/compound/state/2026-05-13_frontend_scoreboard_api_connection_state.md`
- `harness/compound/state/2026-05-13_cloud_integrations_state.md`
- `harness/runs/2026-05-13_pilot_scoreboard_api/`, `...frontend_scoreboard_api_connection/`, `...cloud_observability_e2e_integrations/`, `...agent_role_operating_model/`

특히 아직 남은 것은 결과/box score 생성, mobile/tablet/TV visual QA, host Python 3.11+/ruff 또는 Docker-only 검증 방침 결정, 실제 Vercel/Supabase/Sentry secrets 외부 설정이다. 실제 cloud credentials나 배포는 이 기록만으로 승인되지 않는다.

## 안전한 재개 순서

1. `AGENTS.md`, `requirements_en.md`, `requirements_ko.md`, `README.md`, 위 state/run records를 읽는다.
2. 기존 dirty worktree를 직접 수정·커밋하지 말고, patch를 별도 새 branch/worktree로 복구한다. 먼저 `git diff --stat` 및 untracked 목록을 inventory로 고정한다.
3. backend API 테스트와 frontend unit/E2E를 먼저 실행해 실제 동작 상태를 판별한다. 명시된 Docker Python 3.11 검증과 host 환경 실패를 구분해 보고한다.
4. API contract를 고정한 뒤 result/box score와 visual QA를 별도 task로 분리한다. Phase 2 금지와 backend authorization/logging 규칙을 유지한다.

## 프롬프트/정본

공통 prompt는 `AGENTS.md`; tool-specific 보조 prompt는 `CLAUDE.md`, `GEMINI.md`다. 대화 원문 대신 위 harness run의 plan/work/review/compound 기록이 회복 가능한 대화 맥락이다.
