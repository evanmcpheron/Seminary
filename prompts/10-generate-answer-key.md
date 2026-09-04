---
prompt_id: 10-generate-answer-key
purpose: Generate One Instructor Answer Key
write_scope:
  - one instructor-materials answer-key file
  - provenance/
commit_allowed: false
---

# Generate One Instructor Answer Key

## Preconditions

Before taking any action, apply `AGENTS.md` and complete its required reading order, including `MASTER_PROMPT.md`, `PROJECT-DECISIONS.yaml`, every root policy file, and this active prompt. Also read `curriculum/curriculum.yaml` and `curriculum/curriculum.lock.yaml` when present, inspect `git status` and relevant existing files, check for any more-specific `AGENTS.md` governing the write scope, and read the files needed to verify each precondition below.

1. The assessment is final.
2. Assigned sources and lectures are final.

## Authorized actions

1. Answer each item from approved course content.
2. Explain scoring and acceptable variants.
3. Identify common errors.
4. Do not alter the assessment to fit the key without reporting the mismatch.

## Forbidden actions

- Do not modify files outside the declared write scope.
- Do not invent unverified facts or sources.
- Do not begin a later prompt automatically.
- Do not commit unless the active prompt is explicitly overridden with owner authorization.

## Required validation

Run `python scripts/validate.py --mode draft` and the relevant tests. Add a provenance record.

## Exit criteria

- Key is complete and consistent.
- Ambiguities are reported.
- Student-facing files were not modified.

Stop and report changed files, sources, validation, unresolved items, and required human review.
