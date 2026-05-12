---
id: harness_metadata_schema
title: Harness Metadata Schema
type: schema
category: harness
status: active
created: 2026-05-12
updated: 2026-05-12
phase: phase1_mvp
tags:
  - metadata
  - yaml_frontmatter
  - search
  - compound
related_runs:
  - harness/runs/2026-05-12_sandbox_compound_framework/
---

# Harness Metadata Schema

Use YAML frontmatter at the top of new harness documents so agents can search,
filter, and synthesize context without rereading every file.

## Required Fields

```yaml
---
id: short_unique_id
title: Human Readable Title
type: run | sandbox | compound | issue | debug | decision | test_case | requirements | status | template
category: harness | backend | frontend | database | documents | deployment | field_pilot | product
status: draft | active | complete | superseded | blocked | rejected
created: YYYY-MM-DD
updated: YYYY-MM-DD
phase: phase1_mvp | phase2 | n/a
tags:
  - searchable_tag
related_runs:
  - harness/runs/YYYY-MM-DD_slug/
---
```

## Optional Fields

```yaml
owner: planner | generator | evaluator | coordinator | backend | frontend | product
related_files:
  - path/to/file
related_issues:
  - harness/issue_log/YYYY-MM-DD_issue.md
related_debug:
  - harness/debugging/YYYY-MM-DD_debug.md
related_tests:
  - harness/test_cases/path/to/test.md
supersedes:
  - path/to/older_doc.md
reuses:
  - path/to/reusable_asset_or_pattern.md
blocks:
  - issue_or_task_id
search_terms:
  - phrase agents may search for
decision:
  - adopt | adapt | reject | defer
```

## Tag Rules

- Use lowercase snake_case tags.
- Prefer stable tags over one-off phrasing.
- Include domain tags such as `scoreboard`, `backend`, `frontend`, `field_pilot`.
- Include process tags such as `sandbox`, `compound`, `debugging`, `validation`.
- Include risk tags such as `test_environment`, `permission`, `persistence`.

## Search Examples

```bash
rg "tags:" harness/compound
rg "test_environment" harness
rg "status: blocked" harness
rg "field_pilot" harness docs/requirements summary
```

