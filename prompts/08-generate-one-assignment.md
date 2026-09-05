---
prompt_id: 08-generate-one-assignment
purpose: Generate One Assignment and Rubric
write_scope:
  - one assignment file
  - one rubric
  - related grading guide
  - provenance/
commit_allowed: false
---

# Generate One Assignment and Rubric

## Preconditions

Before taking any action, apply `AGENTS.md` and complete its required reading order, including `MASTER_PROMPT.md`, `PROJECT-DECISIONS.yaml`, every root policy file, and this active prompt. Also read `curriculum/curriculum.yaml` and `curriculum/curriculum.lock.yaml` when present, inspect `git status` and relevant existing files, check for any more-specific `AGENTS.md` governing the write scope, and read the files needed to verify each precondition below.

1. Required lectures and readings are complete.
2. Learning outcomes are fixed.
3. Assignment workload is budgeted.

## Authorized actions

1. Create student-facing instructions.
2. Require student authorship and AI-use declaration.
3. Map criteria to outcomes.
4. Create a detailed rubric and separate grading guide.
5. Do not write a student response.

## Forbidden actions

- Do not modify files outside the declared write scope.
- Do not invent unverified facts or sources.
- Do not introduce a new required reading or student purchase outside the
  approved course design; require an explicit design revision first.
- Do not begin a later prompt automatically.
- Do not commit unless the active prompt is explicitly overridden with owner authorization.

## Required validation

Run `python scripts/validate.py --mode draft` and the relevant tests. Add a provenance record.

## Exit criteria

- Assignment, rubric, and grading guide align.
- No answer is exposed in student-facing files.
- Workload remains within course budget.

Stop and report changed files, sources, validation, unresolved items, and required human review.
