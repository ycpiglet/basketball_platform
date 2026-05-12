---
id: sandbox_readme
title: Sandbox Workspace
type: sandbox
category: harness
status: active
created: 2026-05-12
updated: 2026-05-12
phase: phase1_mvp
tags:
  - sandbox
  - experiment
  - spike
  - promotion_gate
  - reusable_work
related_runs:
  - harness/runs/2026-05-12_sandbox_compound_framework/
---

# Sandbox Workspace

The sandbox is for isolated experiments, spikes, comparisons, and throwaway
prototypes. It prevents risky ideas from being mixed with implementation records
or product requirements too early.

## When To Use

Use `harness/sandbox/` when:

- Trying an implementation approach before committing to it.
- Comparing libraries, state models, API shapes, or deployment options.
- Reproducing a bug in isolation.
- Testing a migration or refactor strategy.
- Exploring a UI interaction before making it part of the product.

## Rules

- A sandbox experiment is not product truth.
- Do not delete an experiment just because it failed. Mark it `rejected` or
  `deferred` and explain why.
- Do not promote sandbox output into product code until it passes a promotion
  review.
- Record what can be reused, what should be discarded, and what mistake should
  not be repeated.
- Link promoted work back to the sandbox experiment.

## Folder Naming

```text
harness/sandbox/experiments/YYYY-MM-DD_short_slug/
```

Copy the files from `harness/sandbox/_template/`.

## Promotion Outcomes

| Outcome | Meaning |
|---|---|
| Adopt | Use the approach as-is. |
| Adapt | Reuse part of the approach with changes. |
| Reject | Do not use this approach again unless conditions change. |
| Defer | Useful idea, but not for the current phase or priority. |

