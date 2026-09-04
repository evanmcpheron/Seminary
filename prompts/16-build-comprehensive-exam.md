---
prompt_id: 16-build-comprehensive-exam
purpose: Build One Comprehensive Examination Field
write_scope:
  - one comprehensive-exam field directory
  - reading list
  - exam instructions
  - scoring guide
  - human evaluator form
  - provenance/
commit_allowed: false
---

# Build One Comprehensive Examination Field

## Preconditions

Before taking any action, apply `AGENTS.md` and complete its required reading order, including `MASTER_PROMPT.md`, `PROJECT-DECISIONS.yaml`, every root policy file, and this active prompt. Also read `curriculum/curriculum.yaml` and `curriculum/curriculum.lock.yaml` when present, inspect `git status` and relevant existing files, check for any more-specific `AGENTS.md` governing the write scope, and read the files needed to verify each precondition below.

1. Doctoral coursework and language requirements are substantially complete.
2. The examination field is explicitly named.
3. Human evaluators are identified.

## Authorized actions

1. Build a verified reading list.
2. Define written and oral components.
3. Create exam administration and scoring guidance.
4. Do not generate student answers.
5. Require qualified human evaluation.

## Forbidden actions

- Do not modify files outside the declared write scope.
- Do not invent unverified facts or sources.
- Do not begin a later prompt automatically.
- Do not commit unless the active prompt is explicitly overridden with owner authorization.

## Required validation

Run `python scripts/validate.py --mode draft` and the relevant tests. Add a provenance record.

## Exit criteria

- Field exam is rigorous and source-verified.
- Human administration and scoring are defined.
- No answer is presented as student work.

Stop and report changed files, sources, validation, unresolved items, and required human review.
