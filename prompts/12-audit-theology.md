---
prompt_id: 12-audit-theology
purpose: Independently Audit Theology and Fair Representation
write_scope:
  - one theological audit report
  - one full-course audits/theology-fairness.audit.yaml when the target is a full course
  - provenance/
commit_allowed: false
---

# Independently Audit Theology and Fair Representation

## Preconditions

Before taking any action, apply `AGENTS.md` and complete its required reading order, including `MASTER_PROMPT.md`, `PROJECT-DECISIONS.yaml`, every root policy file, and this active prompt. Also read `curriculum/curriculum.yaml` and `curriculum/curriculum.lock.yaml` when present, inspect `git status` and relevant existing files, check for any more-specific `AGENTS.md` governing the write scope, and read the files needed to verify each precondition below.

1. The target content is named.
2. The independent source/copyright audit is available; for a full-course audit its manifest must pass.
3. This is a new audit run separate from the generation runs being reviewed.

## Authorized actions

1. Check consistency with historic Christian and Protestant commitments.
2. Check that alternatives are represented accurately and at their strongest responsible form.
3. Check complementarian treatment for fairness and respect.
4. Check that confessional evaluation follows rather than replaces evidence.
5. Flag political-partisan capture, manufactured consensus, or confessional claims presented as neutral scholarly consensus.
6. For a full-course audit, create `audits/theology-fairness.md` and `audits/theology-fairness.audit.yaml`. The manifest must validate against `schemas/audit.schema.json`, reference this audit provenance, list the generation run IDs reviewed, declare independent clean-context review, include `depends_on_audits: [source-copyright]`, and store the current output of `python scripts/course_fingerprint.py <course-path>` as `content_fingerprint`.
7. Preserve `course.yaml` lifecycle status.

## Forbidden actions

- Do not modify files outside the declared write scope.
- Do not invent unverified facts or sources.
- Do not begin a later prompt automatically.
- Do not silently rewrite content to make the audit pass.
- Do not commit unless the active prompt is explicitly overridden with owner authorization.

## Required validation

Run `python scripts/validate.py --mode draft` and the relevant tests. Add a provenance record for the audit run.

## Exit criteria

- Confessional commitments are explicit.
- Opposing views are not caricatured.
- Evidence, contested interpretation, and confessional judgment remain distinguishable.
- Full-course report and manifest agree on the verdict.
- Corrections are recommendations, not silently applied.

Stop and report changed files, sources, validation, unresolved items, and required human review.
