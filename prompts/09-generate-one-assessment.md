---
prompt_id: 09-generate-one-assessment
purpose: Generate One Quiz, Exam, or Oral Assessment
write_scope:
  - one assessment directory
  - one rubric or scoring standard
  - one instructor answer key
  - provenance/
commit_allowed: false
---

# Generate One Quiz, Exam, or Oral Assessment

## Preconditions

1. Assessed content has been taught.
2. Mode and time limit are approved.
3. Learning outcomes are fixed.

## Authorized actions

1. Create the student assessment.
2. Create the separate answer key with explanations.
3. Check item validity, difficulty, coverage, and ambiguity.
4. Identify open-book, closed-book, timed, or oral conditions.

## Forbidden actions

- Do not modify files outside the declared write scope.
- Do not invent unverified facts or sources.
- Do not begin a later prompt automatically.
- Do not commit unless the active prompt is explicitly overridden with owner authorization.

## Required validation

Run `python scripts/validate.py --mode draft` and the relevant tests. Add a provenance record.

## Exit criteria

- Assessment and key agree.
- Every item maps to an outcome.
- No student-facing answers are exposed.

Stop and report changed files, sources, validation, unresolved items, and required human review.
