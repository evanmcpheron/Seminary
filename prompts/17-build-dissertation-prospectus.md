---
prompt_id: 17-build-dissertation-prospectus
purpose: Build the Dissertation Prospectus Process
write_scope:
  - dissertation/prospectus/
  - dissertation/methodology-review/
  - dissertation/committee/
  - one prospectus *.milestone.yaml state record
  - provenance/
commit_allowed: false
---

# Build the Dissertation Prospectus Process

## Preconditions

Before taking any action, apply `AGENTS.md` and complete its required reading order, including `MASTER_PROMPT.md`, `PROJECT-DECISIONS.yaml`, every root policy file, and this active prompt. Also read `curriculum/curriculum.yaml` and `curriculum/curriculum.lock.yaml` when present, inspect `git status` and relevant existing files, check for any more-specific `AGENTS.md` governing the write scope, and read the files needed to verify each precondition below.

1. The student has completed required comprehensives with qualified human evaluation.
2. Research interests and verified bibliography exist.
3. A qualified human supervisor is identified and at least two additional readers are planned for the dissertation process.
4. The most recent applicable longitudinal progression audit passes.

## Authorized actions

1. Guide topic narrowing, research question, thesis hypothesis, primary sources, methods, contribution, chapter outline, bibliography, timetable, and committee review.
2. Audit whether the proposed project has a plausible original contribution and adequate primary-source/language preparation without deciding the student's conclusions for them.
3. Create rubrics, checklists, feedback questions, and blank human-review requirements.
4. Create or update a prospectus `*.milestone.yaml` conforming to `schemas/milestone.schema.json` with `human_review_required: true` and `student_authorship_required: true`; AI may move it only among `planned`, `in-progress`, and `awaiting-human-review`, never to `complete`.
5. Record the supervisor and reader roles without storing unnecessary personal information.
6. Do not write the student's prospectus prose.

## Forbidden actions

- Do not modify files outside the declared write scope.
- Do not invent unverified facts or sources.
- Do not begin a later prompt automatically.
- Do not preselect the thesis or predetermine the dissertation conclusion.
- Do not create or simulate supervisor/committee approval.
- Do not rewrite the prospectus into submission-ready prose for the student.
- Do not commit unless the active prompt is explicitly overridden with owner authorization.

## Required validation

Run `python scripts/validate.py --mode draft` and the relevant tests. Add a provenance record.

## Exit criteria

- A student-authored prospectus can be developed.
- Supervisor and readers have formal review roles.
- No dissertation conclusion is predetermined.
- Prospectus approval remains incomplete until the milestone points to a qualified human review record that validates against `schemas/human-review.schema.json` with `review_type: prospectus` and a passing decision.

Stop and report changed files, sources, validation, unresolved items, and required human review.
