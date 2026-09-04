---
prompt_id: 05-design-one-course
purpose: Design One Course
write_scope:
  - one explicitly named course README.md
  - course.yaml
  - syllabus.md
  - schedule.md
  - bibliography.md
  - learning-outcomes.md
  - policies.md
  - assignment and assessment maps
  - provenance/
commit_allowed: false
---

# Design One Course

## Preconditions

Before taking any action, apply `AGENTS.md` and complete its required reading order, including `MASTER_PROMPT.md`, `PROJECT-DECISIONS.yaml`, every root policy file, and this active prompt. Also read `curriculum/curriculum.yaml` and `curriculum/curriculum.lock.yaml` when present, inspect `git status` and relevant existing files, check for any more-specific `AGENTS.md` governing the write scope, and read the files needed to verify each precondition below.

1. Prompt 03 has generated the course shell and Prompt 04 has completed for this same course.
2. `research-report.md` exists and `course.yaml` status is `researching`.
3. Required sources for design are verified and no blocking research `TODO-VERIFY` remains.
4. Course identity matches the reconciled manifest and immutable lock metadata.

## Authorized actions

1. Define measurable learning outcomes.
2. Map assessments to outcomes.
3. Allocate exactly the credit-hour workload.
4. Design the 15-week sequence and final assessment.
5. Specify human-evaluation requirements.
6. Do not write lectures or full assignments.

## Forbidden actions

- Do not modify files outside the declared write scope.
- Do not invent unverified facts or sources.
- Do not begin a later prompt automatically.
- Do not commit unless the active prompt is explicitly overridden with owner authorization.

## Required validation

Run `python scripts/validate.py --mode draft` and the relevant tests. Add a provenance record.

## Exit criteria

- Course status advances from `researching` to `designed`.
- Outcomes, assessment map, schedule, and workload are coherent.
- No substantive weekly content was generated.
- The next production step is one approved week (`06`) or a more granular lecture/assignment/assessment prompt (`07`–`10`), subject to each prompt's preconditions.

Stop and report changed files, sources, validation, unresolved items, and required human review.
