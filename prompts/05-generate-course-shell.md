---
prompt_id: 05-generate-course-shell
purpose: Generate One Course Shell
write_scope:
  - one explicitly named course directory
  - one provenance record
commit_allowed: false
---

# Generate One Course Shell

## Preconditions

Before taking any action, apply `AGENTS.md` and complete its required reading order, including `MASTER_PROMPT.md`, `PROJECT-DECISIONS.yaml`, every root policy file, and this active prompt. Also read `curriculum/curriculum.yaml` and `curriculum/curriculum.lock.yaml` when present, inspect `git status` and relevant existing files, check for any more-specific `AGENTS.md` governing the write scope, and read the files needed to verify each precondition below.

1. Course exists in reconciled curriculum.
2. Target year and term are approved.
3. No course directory conflict exists.

## Authorized actions

1. Run the shell generator for the one named course.
2. Populate locked metadata only.
3. Create 15 empty week shells for taught courses.
4. Use milestone structure for dissertation work.
5. Do not generate substantive content.

## Forbidden actions

- Do not modify files outside the declared write scope.
- Do not invent unverified facts or sources.
- Do not begin a later prompt automatically.
- Do not commit unless the active prompt is explicitly overridden with owner authorization.

## Required validation

Run `python scripts/validate.py --mode draft` and the relevant tests. Add a provenance record.

## Exit criteria

- Shell exists and validates.
- No placeholders are replaced with invented content.
- No other course was modified.

Stop and report changed files, sources, validation, unresolved items, and required human review.
