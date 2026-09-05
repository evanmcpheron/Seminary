---
prompt_id: 06-generate-one-week
purpose: Generate One Week of One Course
write_scope:
  - one explicitly named course/week directory
  - the explicitly named course's course.yaml, limited to production-state metadata
  - related source records
  - related instructor materials for that week
  - provenance/
commit_allowed: true
---

# Generate One Week of One Course

## Preconditions

Before taking any action, apply `AGENTS.md` and complete its required reading order, including `MASTER_PROMPT.md`, `PROJECT-DECISIONS.yaml`, every root policy file, and this active prompt. Also read `curriculum/curriculum.yaml` and `curriculum/curriculum.lock.yaml` when present, inspect `git status` and relevant existing files, check for any more-specific `AGENTS.md` governing the write scope, and read the files needed to verify each precondition below.

1. Course design is approved and `course.yaml` status is `designed` or `in-production`.
2. Week objectives and workload are approved.
3. Required sources are verified.

## Authorized actions

1. If this is the first substantive production run for the course, advance `course.yaml` status from `designed` to `in-production`; otherwise preserve `in-production`.
2. Generate objectives and lecture outlines.
3. Generate and source-audit lectures before dependent assignments.
4. Generate readings, study guide, guided discussion, assignment, quiz, rubric, and answer key only for this week.
5. Respect the week's workload budget.
6. Separate practice from graded work.

## Forbidden actions

- Do not modify files outside the declared write scope.
- Do not invent unverified facts or sources.
- Do not begin a later prompt automatically.
- Do not commit unless the active prompt is explicitly overridden with owner authorization.

## Required validation

Run `python scripts/validate.py --mode draft` and the relevant tests. Add a provenance record.

## Exit criteria

- One week is complete.
- `course.yaml` status is `in-production`.
- All claims and sources are auditable.
- Workload is within budget.
- No other week was modified.

Stop and report changed files, sources, validation, unresolved items, and required human review.
