---
prompt_id: 03-research-one-course
purpose: Research One Course
write_scope:
  - one explicitly named course resources directory
  - one course research-report.md
  - one course source records
  - provenance/
commit_allowed: false
---

# Research One Course

## Preconditions

1. The course exists in the reconciled manifest.
2. The course shell exists or an approved target path is supplied.
3. The course code is explicitly named.

## Authorized actions

1. Verify catalog description and prerequisites.
2. Research primary sources, textbooks, articles, reference works, media, and comparable academic models.
3. Verify every bibliographic field.
4. Mark access category and cost.
5. Provide free article alternatives where feasible.
6. Do not design weekly content.

## Forbidden actions

- Do not modify files outside the declared write scope.
- Do not invent unverified facts or sources.
- Do not begin a later prompt automatically.
- Do not commit unless the active prompt is explicitly overridden with owner authorization.

## Required validation

Run `python scripts/validate.py --mode draft` and the relevant tests. Add a provenance record.

## Exit criteria

- Source report is complete.
- Required resources are verified.
- Unresolvable items are explicit.
- No syllabus or lecture content was generated.

Stop and report changed files, sources, validation, unresolved items, and required human review.
