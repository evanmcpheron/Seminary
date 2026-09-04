---
prompt_id: 02-import-and-lock-curriculum
purpose: Import and Lock the Canonical Curriculum
write_scope:
  - curriculum/curriculum.yaml
  - curriculum/curriculum.lock.yaml
  - curriculum/import-report.md
  - provenance/
commit_allowed: false
---

# Import and Lock the Canonical Curriculum

## Preconditions

Before taking any action, apply `AGENTS.md` and complete its required reading order, including `MASTER_PROMPT.md`, `PROJECT-DECISIONS.yaml`, every root policy file, and this active prompt. Also read `curriculum/curriculum.yaml` and `curriculum/curriculum.lock.yaml` when present, inspect `git status` and relevant existing files, check for any more-specific `AGENTS.md` governing the write scope, and read the files needed to verify each precondition below.

1. The canonical spreadsheet exists in curriculum/source/.
2. The spreadsheet filename and hash are recorded.
3. No course content has been generated.

## Authorized actions

1. Run the import tool against the spreadsheet.
2. Preserve exact course identity metadata.
3. Classify non-course Princeton records as competencies, examinations, seminar categories, or milestones.
4. Report prerequisites, overloads, and anomalies without silently correcting them.
5. Create and validate the lock file.

## Forbidden actions

- Do not modify files outside the declared write scope.
- Do not invent unverified facts or sources.
- Do not begin a later prompt automatically.
- Do not commit unless the active prompt is explicitly overridden with owner authorization.

## Required validation

Run `python scripts/validate.py --mode draft` and the relevant tests. Add a provenance record.

## Exit criteria

- Manifest and lock file exist.
- Every spreadsheet record is accounted for.
- Import report lists all anomalies.
- Next prompt is schedule reconciliation.

Stop and report changed files, sources, validation, unresolved items, and required human review.
