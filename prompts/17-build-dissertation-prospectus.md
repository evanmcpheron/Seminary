---
prompt_id: 17-build-dissertation-prospectus
purpose: Build the Dissertation Prospectus Process
write_scope:
  - dissertation/prospectus/
  - dissertation/methodology-review/
  - dissertation/committee/
  - provenance/
commit_allowed: false
---

# Build the Dissertation Prospectus Process

## Preconditions

Before taking any action, apply `AGENTS.md` and complete its required reading order, including `MASTER_PROMPT.md`, `PROJECT-DECISIONS.yaml`, every root policy file, and this active prompt. Also read `curriculum/curriculum.yaml` and `curriculum/curriculum.lock.yaml` when present, inspect `git status` and relevant existing files, check for any more-specific `AGENTS.md` governing the write scope, and read the files needed to verify each precondition below.

1. The student has completed required comprehensives.
2. Research interests and verified bibliography exist.
3. Human supervisor is identified.

## Authorized actions

1. Guide topic narrowing, research question, thesis hypothesis, primary sources, methods, contribution, chapter outline, bibliography, timetable, and committee review.
2. Do not write the student's prospectus prose.
3. Create rubrics, checklists, and feedback questions.

## Forbidden actions

- Do not modify files outside the declared write scope.
- Do not invent unverified facts or sources.
- Do not begin a later prompt automatically.
- Do not commit unless the active prompt is explicitly overridden with owner authorization.

## Required validation

Run `python scripts/validate.py --mode draft` and the relevant tests. Add a provenance record.

## Exit criteria

- A student-authored prospectus can be developed.
- Supervisor and readers have formal review roles.
- No dissertation conclusion is predetermined.

Stop and report changed files, sources, validation, unresolved items, and required human review.
