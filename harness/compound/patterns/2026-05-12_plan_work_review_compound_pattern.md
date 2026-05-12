---
id: 2026_05_12_plan_work_review_compound_pattern
title: Plan Work Review Compound Pattern
type: compound
category: harness
status: active
created: 2026-05-12
updated: 2026-05-12
phase: phase1_mvp
tags:
  - plan_work_review
  - compound
  - sandbox
  - workflow
  - reusable_process
related_runs:
  - harness/runs/2026-05-12_sandbox_compound_framework/
related_files:
  - harness/workflows/task_lifecycle.md
  - harness/README.md
search_terms:
  - plan work review loop
  - compound synthesis
  - avoid repeated mistakes
---

# Plan Work Review Compound Pattern

## Synthesis

The harness lifecycle is now:

```text
intake -> plan -> sandbox when uncertain -> work -> review -> compound -> status
```

The compound step is mandatory for substantial runs. It extracts reusable
knowledge from the run so the next agent does not repeat the same investigation
or recreate discarded work.

## Evidence

- `harness/sandbox/` now defines experiment isolation.
- `harness/compound/` now defines synthesized knowledge records.
- `harness/metadata_schema.md` defines searchable YAML frontmatter.

## Reuse

- Use sandbox for experiments and spikes.
- Use run files for chronological task execution.
- Use compound records for durable lessons and current state.
- Use `summary/status.md` as the short entrypoint.

## Avoid

- Do not put every raw log into `summary/status.md`.
- Do not leave useful lessons buried only in run-local files.
- Do not delete failed attempts; mark them rejected or deferred.

## Next Actions

- At the end of each substantial run, update or create one compound record.
- Link the compound record from `08_final_summary.md` and `summary/status.md`
  when it affects future planning.

