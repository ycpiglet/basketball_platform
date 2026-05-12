# Runs

Each run is a bounded work session for a user request, bug, feature, refactor,
or release preparation task.

## Folder Name

Use:

```text
YYYY-MM-DD_short_slug
```

Example:

```text
2026-05-12_harness_structure
```

## Required Files

Copy the files from `_template/` into the run folder:

```text
00_context.md
01_plan.md
02_work_log.md
03_issue_log.md
04_debug_log.md
05_test_report.md
06_evaluation.md
07_deployment.md
08_final_summary.md
```

Small tasks may leave a section as `N/A`, but should not delete the file. Stable
file names make cross-agent continuation easier.

## Run Index

| Date | Run | Purpose | Status |
|---|---|---|---|
| 2026-05-12 | `2026-05-12_harness_structure` | Established harness directories, role docs, run templates, validation, and test case structure. | Complete |
| 2026-05-12 | `2026-05-12_python_coding_skill_location` | Moved the Python coding standard into `harness/skills/python_coding/SKILL.md` and documented usage. | Complete |
| 2026-05-12 | `2026-05-12_amateur_club_field_pilot_spec` | Defines the field pilot goal, work packages, risks, tests, and next vertical slice. | Complete |
| 2026-05-12 | `2026-05-12_sandbox_compound_framework` | Adds sandbox experiments, compound synthesis, YAML metadata schema, and searchable reusable knowledge records. | Complete |
| 2026-05-12 | `2026-05-12_frontend_public_prototype_ui_migration` | Migrates Vue frontend placeholder UI toward the `public/index.html` field-pilot design direction. | Complete |
