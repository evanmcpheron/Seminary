---
prompt_id: 18-support-one-dissertation-chapter
purpose: Support One Dissertation Chapter Without Authoring It
write_scope:
  - one chapter research-management directory
  - source audit
  - argument map
  - feedback record
  - provenance/
commit_allowed: false
---

# Support One Dissertation Chapter Without Authoring It

## Preconditions

Before taking any action, apply `AGENTS.md` and complete its required reading order, including `MASTER_PROMPT.md`, `PROJECT-DECISIONS.yaml`, every root policy file, and this active prompt. Also read `curriculum/curriculum.yaml` and `curriculum/curriculum.lock.yaml` when present, inspect `git status` and relevant existing files, check for any more-specific `AGENTS.md` governing the write scope, and read the files needed to verify each precondition below.

1. Prospectus is approved.
2. The chapter scope is explicit.
3. Student-authored draft or research notes exist.

## Authorized actions

1. Organize verified sources and primary-text evidence.
2. Question the argument and identify gaps.
3. Audit citations and counterarguments.
4. Provide feedback on a student-authored draft.
5. Do not draft replacement prose.

## Forbidden actions

- Do not modify files outside the declared write scope.
- Do not invent unverified facts or sources.
- Do not begin a later prompt automatically.
- Do not commit unless the active prompt is explicitly overridden with owner authorization.

## Required validation

Run `python scripts/validate.py --mode draft` and the relevant tests. Add a provenance record.

## Exit criteria

- Research and feedback records are complete.
- Student authorship is preserved.
- Human supervisor review remains required.

Stop and report changed files, sources, validation, unresolved items, and required human review.
