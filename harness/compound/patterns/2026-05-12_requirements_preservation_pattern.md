---
id: 2026_05_12_requirements_preservation_pattern
title: Requirements Preservation Pattern
type: compound
category: product
status: active
created: 2026-05-12
updated: 2026-05-12
phase: phase1_mvp
tags:
  - requirements
  - archive
  - source_of_truth
  - preservation
  - no_delete
related_runs:
  - harness/runs/2026-05-12_amateur_club_field_pilot_spec/
related_files:
  - docs/requirements/README.md
  - docs/requirements/archive/2026-05-12_requirements_source_summary_for_field_pilot.md
search_terms:
  - do not delete requirements
  - derived requirements
  - archive summary
---

# Requirements Preservation Pattern

## Synthesis

New requirements documents should derive from the source requirements without
overwriting them. The field pilot spec is a Phase 1 narrowing document, not a
replacement for `requirements_en.md` or `requirements_ko.md`.

## Evidence

- `docs/requirements/README.md` defines the preservation rule.
- The field pilot created an archive summary rather than deleting the original
  source documents.

## Reuse

- Keep root source-of-truth files unchanged unless the product owner explicitly
  asks for a scope change.
- Put dated derived requirements in `docs/requirements/`.
- Put dated source summaries in `docs/requirements/archive/`.
- Link the active derived requirement from `summary/status.md`.

## Avoid

- Do not replace broad requirements with a narrower pilot document.
- Do not delete old requirements because a newer document exists.
- Do not silently reclassify Phase 2 work as Phase 1.

## Next Actions

- Use this pattern before changing requirements documents.
- If a future spec supersedes the field pilot spec, mark the old spec and status
  summary accordingly instead of deleting it.

