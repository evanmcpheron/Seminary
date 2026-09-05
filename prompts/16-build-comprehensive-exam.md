---
prompt_id: 16-build-comprehensive-exam
purpose: Build One Comprehensive Examination Field
write_scope:
  - one comprehensive-exam field directory
  - reading list
  - exam instructions
  - scoring guide
  - human evaluator form
  - human-review requirement metadata
  - one comprehensive-field *.milestone.yaml state record
  - provenance/
commit_allowed: false
---

# Build One Comprehensive Examination Field

## Preconditions

Before taking any action, apply `AGENTS.md` and complete its required reading order, including `MASTER_PROMPT.md`, `PROJECT-DECISIONS.yaml`, every root policy file, and this active prompt. Also read `curriculum/curriculum.yaml` and `curriculum/curriculum.lock.yaml` when present, inspect `git status` and relevant existing files, check for any more-specific `AGENTS.md` governing the write scope, and read the files needed to verify each precondition below.

1. Doctoral coursework and language requirements are substantially complete.
2. The examination field is explicitly named.
3. Qualified human evaluators are identified by role and qualification; AI cannot fill an evaluator seat.
4. The most recent applicable longitudinal progression audit passes.

## Authorized actions

1. Build a verified reading list with current source verification.
2. Define written and oral components.
3. Create exam administration and scoring guidance.
4. Create a blank human-review requirement/template based on `templates/evaluation/human-review-record.yaml` without fabricating a completed review.
5. Create a `*.milestone.yaml` record conforming to `schemas/milestone.schema.json` with `human_review_required: true` and `student_authorship_required: true`; leave it `planned`, `in-progress`, or `awaiting-human-review`. AI may not set it to `complete`.
6. Define what evidence the human evaluators must retain for the comprehensive decision.
7. Do not generate student answers.
8. Require qualified human administration and evaluation for the completion decision.

## Forbidden actions

- Do not modify files outside the declared write scope.
- Do not invent unverified facts or sources.
- Do not begin a later prompt automatically.
- Do not score the student's comprehensive examination as the authoritative evaluator.
- Do not generate, prewrite, or substantially rewrite student comprehensive answers.
- Do not create a passing human-review record before an actual human evaluation occurs.
- Do not commit unless the active prompt is explicitly overridden with owner authorization.

## Required validation

Run `python scripts/validate.py --mode draft` and the relevant tests. Add a provenance record.

## Exit criteria

- Field exam is rigorous and source-verified.
- Human administration and scoring are defined.
- No answer is presented as student work.
- The field milestone cannot be marked `complete` until its `human_review_record_path` resolves to a qualified human review record that validates against `schemas/human-review.schema.json` and records a passing decision.

Stop and report changed files, sources, validation, unresolved items, and required human review.
