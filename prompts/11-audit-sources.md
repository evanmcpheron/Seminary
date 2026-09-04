---
prompt_id: 11-audit-sources
purpose: Audit Sources for One Scoped Unit
write_scope:
  - one audit report
  - source record corrections within the scoped unit
  - the explicitly named course's course.yaml when a full-course audit advances lifecycle status
  - provenance/
commit_allowed: false
---

# Audit Sources for One Scoped Unit

## Preconditions

Before taking any action, apply `AGENTS.md` and complete its required reading order, including `MASTER_PROMPT.md`, `PROJECT-DECISIONS.yaml`, every root policy file, and this active prompt. Also read `curriculum/curriculum.yaml` and `curriculum/curriculum.lock.yaml` when present, inspect `git status` and relevant existing files, check for any more-specific `AGENTS.md` governing the write scope, and read the files needed to verify each precondition below.

1. The target course, week, lecture, or assessment is named.
2. All claimed sources are available for inspection.
3. If this is the full-course audit used as the lifecycle gate, substantive production is complete and `course.yaml` status is `in-production`.

## Authorized actions

1. Verify bibliographic fields, access, links, quotations, page ranges, and copyright status.
2. Flag uncited claims and inaccessible sources.
3. Do not replace sources merely for theological agreement.
4. Require free alternatives for paid articles where feasible.
5. For a full-course audit only, if production is complete and the source audit passes without blocking verification issues, advance `course.yaml` status from `in-production` to `ready-for-audit`. Unit-scoped audits do not change course status.

## Forbidden actions

- Do not modify files outside the declared write scope.
- Do not invent unverified facts or sources.
- Do not begin a later prompt automatically.
- Do not commit unless the active prompt is explicitly overridden with owner authorization.

## Required validation

Run `python scripts/validate.py --mode draft` and the relevant tests. Add a provenance record.

## Exit criteria

- Every required source is verified or explicitly blocked.
- No fabricated or inaccessible citation remains hidden.
- Audit verdict is recorded.
- A passing full-course lifecycle-gate audit leaves `course.yaml` at `ready-for-audit`; unit-scoped audits leave course status unchanged.

Stop and report changed files, sources, validation, unresolved items, and required human review.
