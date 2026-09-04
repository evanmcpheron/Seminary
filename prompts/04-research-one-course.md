---
prompt_id: 04-research-one-course
purpose: Research One Course
write_scope:
  - one explicitly named course resources directory
  - one course research-report.md
  - one course source records
  - the explicitly named course's course.yaml, limited to research-state metadata
  - provenance/
commit_allowed: false
---

# Research One Course

## Preconditions

Before taking any action, apply `AGENTS.md` and complete its required reading order, including `MASTER_PROMPT.md`, `PROJECT-DECISIONS.yaml`, every root policy file, and this active prompt. Also read `curriculum/curriculum.yaml` and `curriculum/curriculum.lock.yaml` when present, inspect `git status` and relevant existing files, check for any more-specific `AGENTS.md` governing the write scope, and read the files needed to verify each precondition below.

1. The course exists in the reconciled `curriculum/curriculum.yaml` manifest.
2. Prompt 03 has already generated the course shell at the reconciled path.
3. The course code is explicitly named in the invocation and resolves to exactly one canonical `record_id`.
4. `course.yaml` identity metadata matches the curriculum manifest and lock file.
5. `course.yaml` status is `shell` or `researching`; do not use this prompt to rewrite a course already at `designed` or later status without explicit owner authorization for a scoped research refresh.

## Authorized actions

1. Verify catalog description and prerequisites against authoritative sources; if locked identity metadata conflicts with an authoritative source, stop and report the discrepancy rather than changing the lock.
2. Research primary sources, textbooks, articles, reference works, media, and comparable academic models.
3. Verify every bibliographic field.
4. Mark access category and cost.
5. Provide free article alternatives where feasible.
6. Write or update `research-report.md` and the scoped verified source records.
7. Update `course.yaml` only for research-state metadata: `prerequisites`, `corequisites`, `source_verification_date`, `known_unresolved_questions`, and `status: researching`. Do not populate learning outcomes, assessments, schedule design, or other Prompt 05 fields.
8. Do not design weekly content.

## Forbidden actions

- Do not modify files outside the declared write scope.
- Do not invent unverified facts or sources.
- Do not begin a later prompt automatically.
- Do not commit unless the active prompt is explicitly overridden with owner authorization.

## Required validation

Run `python scripts/validate.py --mode draft` and the relevant tests. Add a provenance record.

## Exit criteria

- `research-report.md` is complete.
- Required resources are verified or explicitly blocked with `TODO-VERIFY`.
- Unresolvable items are explicit.
- `course.yaml` has status `researching`.
- No syllabus, assessment design, weekly schedule, or lecture content was generated.
- The next permitted per-course prompt is `05-design-one-course.md` for this same course after any blocking `TODO-VERIFY` items required for design are resolved.

Stop and report changed files, sources, validation, unresolved items, and required human review.
