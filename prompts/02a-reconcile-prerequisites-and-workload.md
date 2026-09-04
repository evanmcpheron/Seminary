---
prompt_id: 02a-reconcile-prerequisites-and-workload
purpose: Reconcile Prerequisites and Workload
write_scope:
  - curriculum/schedule-overrides.yaml
  - curriculum/curriculum.yaml
  - curriculum/prerequisite-report.md
  - curriculum/workload-report.md
  - provenance/
commit_allowed: false
---

# Reconcile Prerequisites and Workload

## Preconditions

Before taking any action, apply `AGENTS.md` and complete its required reading order, including `MASTER_PROMPT.md`, `PROJECT-DECISIONS.yaml`, every root policy file, and this active prompt. Also read `curriculum/curriculum.yaml` and `curriculum/curriculum.lock.yaml` when present, inspect `git status` and relevant existing files, check for any more-specific `AGENTS.md` governing the write scope, and read the files needed to verify each precondition below.

1. Curriculum import is complete.
2. Lock file exists and remains immutable.
3. All moved courses must be preserved.

## Authorized actions

1. Verify published prerequisites from authoritative catalog sources.
2. Identify invalid sequencing.
3. Propose the minimum moves needed within undergraduate years.
4. Redistribute overload into summer terms while preserving total work.
5. Record each move with old term, new term, rationale, source, and owner approval.
6. Apply only approved overrides.

## Forbidden actions

- Do not modify files outside the declared write scope.
- Do not invent unverified facts or sources.
- Do not begin a later prompt automatically.
- Do not commit unless the active prompt is explicitly overridden with owner authorization.

## Required validation

Run `python scripts/validate.py --mode draft` and the relevant tests. Add a provenance record.

## Exit criteria

- No prerequisite violation remains unexplained.
- All courses remain present.
- Term workloads are reported.
- Locked identity metadata is unchanged.

Stop and report changed files, sources, validation, unresolved items, and required human review.
