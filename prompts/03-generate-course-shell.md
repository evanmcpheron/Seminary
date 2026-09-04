---
prompt_id: 03-generate-course-shell
purpose: Generate One Course Shell
write_scope:
  - one explicitly named course directory
  - one provenance record
commit_allowed: false
---

# Generate One Course Shell

## Preconditions

Before taking any action, apply `AGENTS.md` and complete its required reading order, including `MASTER_PROMPT.md`, `PROJECT-DECISIONS.yaml`, every root policy file, and this active prompt. Also read `curriculum/curriculum.yaml` and `curriculum/curriculum.lock.yaml` when present, inspect `git status` and relevant existing files, check for any more-specific `AGENTS.md` governing the write scope, and read the files needed to verify each precondition below.

1. The course exists in the reconciled `curriculum/curriculum.yaml` manifest.
2. The invocation explicitly names the course code; resolve its canonical `record_id` from the reconciled manifest rather than inventing an ID.
3. Target year and term match the reconciled manifest, including approved schedule overrides.
4. No course directory conflict exists.

## Authorized actions

1. Resolve the one named course to exactly one canonical `record_id` in `curriculum/curriculum.yaml`.
2. Run the shell generator for that `record_id` only.
3. Populate locked/reconciled metadata only.
4. Create 15 empty week shells for taught courses.
5. Use milestone structure for dissertation work.
6. Do not generate substantive content or begin Prompt 04 automatically.

## Forbidden actions

- Do not modify files outside the declared write scope.
- Do not invent unverified facts or sources.
- Do not begin a later prompt automatically.
- Do not commit unless the active prompt is explicitly overridden with owner authorization.

## Required validation

Run `python scripts/validate.py --mode draft` and the relevant tests. Add a provenance record.

## Exit criteria

- Shell exists and validates.
- `course.yaml` has status `shell`.
- The generated path and canonical `record_id` are reported.
- No placeholders are replaced with invented content.
- No other course was modified.
- The next permitted per-course prompt is `04-research-one-course.md` for this same explicitly named course.

Stop and report changed files, sources, validation, unresolved items, and required human review.
