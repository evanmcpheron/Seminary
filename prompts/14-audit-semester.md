---
prompt_id: 14-audit-semester
purpose: Audit One Semester Workload and Coordination
write_scope:
  - one semester audit report
  - provenance/
commit_allowed: false
---

# Audit One Semester Workload and Coordination

## Preconditions

Before taking any action, apply `AGENTS.md` and complete its required reading order, including `MASTER_PROMPT.md`, `PROJECT-DECISIONS.yaml`, every root policy file, and this active prompt. Also read `curriculum/curriculum.yaml` and `curriculum/curriculum.lock.yaml` when present, inspect `git status` and relevant existing files, check for any more-specific `AGENTS.md` governing the write scope, and read the files needed to verify each precondition below.

1. All course designs in the named term are available.
2. No full semester content generation is authorized.

## Authorized actions

1. Sum weekly workload across courses.
2. Identify assignment and exam clustering.
3. Check prerequisites and cross-course dependencies.
4. Recommend calendar adjustments without changing course identity.

## Forbidden actions

- Do not modify files outside the declared write scope.
- Do not invent unverified facts or sources.
- Do not begin a later prompt automatically.
- Do not commit unless the active prompt is explicitly overridden with owner authorization.

## Required validation

Run `python scripts/validate.py --mode draft` and the relevant tests. Add a provenance record.

## Exit criteria

- Peak weekly workload is reported.
- Clashes and overloads are listed.
- Any proposed schedule change awaits approval.

Stop and report changed files, sources, validation, unresolved items, and required human review.
