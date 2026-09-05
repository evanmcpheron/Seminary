---
prompt_id: 18-support-one-dissertation-chapter
purpose: Support One Dissertation Chapter Without Authoring It
write_scope:
  - one chapter research-management directory
  - source audit
  - argument map
  - feedback record
  - one chapter *.milestone.yaml state record
  - provenance/
commit_allowed: false
---

# Support One Dissertation Chapter Without Authoring It

## Preconditions

Before taking any action, apply `AGENTS.md` and complete its required reading order, including `MASTER_PROMPT.md`, `PROJECT-DECISIONS.yaml`, every root policy file, and this active prompt. Also read `curriculum/curriculum.yaml` and `curriculum/curriculum.lock.yaml` when present, inspect `git status` and relevant existing files, check for any more-specific `AGENTS.md` governing the write scope, and read the files needed to verify each precondition below.

1. Prospectus is approved by the qualified human supervisor/committee and the approval record is available.
2. The chapter scope is explicit.
3. Student-authored draft or research notes exist.
4. The chapter's required primary sources and original-language evidence are available for inspection where relevant.

## Authorized actions

1. Organize verified sources and primary-text evidence.
2. Question the argument and identify gaps, unstated premises, weak counterarguments, and evidential overreach.
3. Audit citations, quotations, source freshness, and counterarguments.
4. Provide diagnostic feedback on a student-authored draft.
5. Compare the chapter against the approved prospectus scope and method without deciding substantive conclusions for the student.
6. Produce a feedback record that clearly distinguishes AI feedback from later human supervisor judgment.
7. Create or update the chapter `*.milestone.yaml` conforming to `schemas/milestone.schema.json` with `human_review_required: true` and `student_authorship_required: true`; AI may not set its status to `complete`.
8. Do not draft replacement prose.

## Forbidden actions

- Do not modify files outside the declared write scope.
- Do not invent unverified facts or sources.
- Do not begin a later prompt automatically.
- Do not draft, rewrite, or polish dissertation prose for submission.
- Do not mark a chapter approved, complete, defensible, or dissertation-ready on behalf of the human supervisor or committee.
- Do not create a human-review record.
- Do not commit unless the active prompt is explicitly overridden with owner authorization.

## Required validation

Run `python scripts/validate.py --mode draft` and the relevant tests. Add a provenance record.

## Exit criteria

- Research and AI-feedback records are complete.
- Student authorship is preserved.
- Human supervisor review remains required after the AI feedback cycle.
- Any chapter-completion claim requires the chapter milestone to point to a later qualified human review record with `review_type: dissertation-chapter`; AI feedback alone is never sufficient.

Stop and report changed files, sources, validation, unresolved items, and required human review.
