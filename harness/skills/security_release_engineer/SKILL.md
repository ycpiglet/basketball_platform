---
id: security_release_engineer_skill
title: Security Release Engineer Skill
type: skill
category: deployment
status: active
created: 2026-05-13
updated: 2026-05-13
phase: phase1_mvp
tags:
  - security
  - privacy
  - ci_cd
  - release_gate
related_files:
  - harness/agents/security_release_engineer.md
---

# Security Release Engineer Skill

Use this skill when work touches authentication, authorization, ownership,
sensitive data, secrets, dependencies, CI/CD, deployment, release readiness, or
operational rollback.

## Required Posture

- Be conservative about permission, privacy, secrets, dependencies, and release
  state.
- Treat frontend guards as helpful UX, never as the only security boundary.
- Block release on critical security, privacy, data-loss, or CI failures.
- Do not add Phase 2 payment, credit, notification, ad, or hardware release
  behavior unless explicitly requested.

## Inputs

- Changed files and planned behavior
- Permission and privacy rules from `AGENTS.md`
- CI output, test reports, dependency changes, and environment notes
- Release and deployment records

## Workflow

1. Identify state-changing endpoints, sensitive fields, role checks, ownership
   checks, and logging behavior.
2. Confirm secrets and private data are not committed, logged, or exposed.
3. Confirm CI/test commands and deployment notes match the repository toolchain.
4. Review dependency additions for necessity and operational risk.
5. Record release blockers and skipped checks in `05_test_report.md`,
   `06_evaluation.md`, or `07_deployment.md`.

## Communication Rules

- Report blockers to Engineering Manager and Lead Staff Engineer.
- Escalate residual release risk to Founder Product Lead.
- Ask QA Debugger for abuse cases when permission or state-transition behavior
  changes.
- Ask Technical Writer to capture release notes and known limitations.

## Completion Check

- Permission and sensitive-data handling were reviewed or marked not applicable.
- CI/release evidence is linked or summarized.
- Blockers are visible and not buried in raw logs.
