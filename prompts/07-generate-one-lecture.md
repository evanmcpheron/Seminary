---
prompt_id: 07-generate-one-lecture
purpose: Generate One Lecture
write_scope:
  - one explicitly named lecture file
  - its outline
  - the explicitly named course's course.yaml, limited to production-state metadata
  - related source records
  - provenance/
commit_allowed: false
---

# Generate One Lecture

## Preconditions

Before taking any action, apply `AGENTS.md` and complete its required reading order, including `MASTER_PROMPT.md`, `PROJECT-DECISIONS.yaml`, every root policy file, and this active prompt. Also read `curriculum/curriculum.yaml` and `curriculum/curriculum.lock.yaml` when present, inspect `git status` and relevant existing files, check for any more-specific `AGENTS.md` governing the write scope, and read the files needed to verify each precondition below.

1. Course design is approved and `course.yaml` status is `designed` or `in-production`.
2. Lecture outline is approved.
3. Learning objectives are fixed.
4. Sources are verified.
5. The approved course `required_texts` and source-record acquisition
   classifications reconcile under `SOURCE-POLICY.md`.

## Authorized actions

1. If this is the first substantive production run for the course, advance `course.yaml` status from `designed` to `in-production`; otherwise preserve `in-production`.
2. Write the full lecture to the level appropriate for the course.
3. Distinguish primary sources, consensus, disputes, confessional conclusions, and synthesis.
4. Add formal citations, summary, questions, and verification section.
5. Do not create dependent assignments.
6. Additional verified lecture scholarship remains non-required unless an
   explicit course-design revision approves it as student-required.

## Forbidden actions

- Do not modify files outside the declared write scope.
- Do not invent unverified facts or sources.
- Do not introduce or elevate a source to `required-purchase`. If a new student
  purchase proves necessary, stop and require an explicit Prompt 05
  acquisition-design revision.
- Do not begin a later prompt automatically.
- Do not commit unless the active prompt is explicitly overridden with owner authorization.

## Required validation

Run `python scripts/validate.py --mode draft` and the relevant tests. Add a provenance record.

## Exit criteria

- Lecture is complete and source-audited.
- `course.yaml` status is `in-production`.
- No unsupported claims remain.
- Dependent assignment generation may now proceed.

Stop and report changed files, sources, validation, unresolved items, and required human review.
