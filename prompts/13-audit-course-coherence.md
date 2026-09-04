---
prompt_id: 13-audit-course-coherence
purpose: Audit One Course for Coherence
write_scope:
  - one coherence audit report
  - provenance/
commit_allowed: false
---

# Audit One Course for Coherence

## Preconditions

1. Course design and all current content are available.
2. Source and theology audits are available.

## Authorized actions

1. Check prerequisite fit, learning progression, workload, outcomes, assignments, assessments, rubrics, answer keys, and human review.
2. Check lectures precede dependent work.
3. Check progression thresholds and retake policy.

## Forbidden actions

- Do not modify files outside the declared write scope.
- Do not invent unverified facts or sources.
- Do not begin a later prompt automatically.
- Do not commit unless the active prompt is explicitly overridden with owner authorization.

## Required validation

Run `python scripts/validate.py --mode draft` and the relevant tests. Add a provenance record.

## Exit criteria

- All mismatches are listed with file paths.
- No revisions are silently applied.
- Release recommendation is explicit.

Stop and report changed files, sources, validation, unresolved items, and required human review.
