---
prompt_id: 07-generate-one-lecture
purpose: Generate One Lecture
write_scope:
  - one explicitly named lecture file
  - its outline
  - related source records
  - provenance/
commit_allowed: false
---

# Generate One Lecture

## Preconditions

1. Lecture outline is approved.
2. Learning objectives are fixed.
3. Sources are verified.

## Authorized actions

1. Write the full lecture to the level appropriate for the course.
2. Distinguish primary sources, consensus, disputes, confessional conclusions, and synthesis.
3. Add formal citations, summary, questions, and verification section.
4. Do not create dependent assignments.

## Forbidden actions

- Do not modify files outside the declared write scope.
- Do not invent unverified facts or sources.
- Do not begin a later prompt automatically.
- Do not commit unless the active prompt is explicitly overridden with owner authorization.

## Required validation

Run `python scripts/validate.py --mode draft` and the relevant tests. Add a provenance record.

## Exit criteria

- Lecture is complete and source-audited.
- No unsupported claims remain.
- Dependent assignment generation may now proceed.

Stop and report changed files, sources, validation, unresolved items, and required human review.
