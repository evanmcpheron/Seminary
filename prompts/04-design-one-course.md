---
prompt_id: 04-design-one-course
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

1. Course research audit has passed.
2. Required sources are verified.
3. Course identity matches the lock file.

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

- Course status may advance to designed.
- Outcomes, assessment map, schedule, and workload are coherent.
- No substantive weekly content was generated.

Stop and report changed files, sources, validation, unresolved items, and required human review.
