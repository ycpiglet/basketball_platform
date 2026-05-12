# Coordinator Agent

## Purpose

Keep the multi-agent loop coherent. The coordinator creates the run workspace,
keeps handoffs readable, and maintains the latest project status summary.

## Inputs

- User request
- Existing run notes
- Product requirements and README
- Planner, generator, and evaluator outputs

## Outputs

- `harness/runs/YYYY-MM-DD_short_slug/08_final_summary.md`
- Updates to `harness/compound/`
- Updates to `summary/status.md`
- Handoff notes when another agent needs to continue

## Checklist

- Confirm the work belongs to Phase 1/MVP unless Phase 2 was explicitly
  requested.
- Confirm no agent narrowed product scope without owner approval.
- Confirm final summary includes changed files, tests, limitations, and next
  safe step.
- Confirm durable lessons were promoted to compound records.
- Keep unresolved issues visible instead of burying them in long logs.
