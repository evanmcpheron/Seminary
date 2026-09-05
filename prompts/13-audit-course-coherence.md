---
prompt_id: 13-audit-course-coherence
purpose: Independently Audit One Course for Coherence and Release Readiness
write_scope:
  - one coherence audit report
  - one audits/course-coherence.audit.yaml
  - the explicitly named course's course.yaml when all release audits pass
  - provenance/
commit_allowed: false
---

# Independently Audit One Course for Coherence and Release Readiness

## Preconditions

Before taking any action, apply `AGENTS.md` and complete its required reading order, including `MASTER_PROMPT.md`, `PROJECT-DECISIONS.yaml`, every root policy file, and this active prompt. Also read `curriculum/curriculum.yaml` and `curriculum/curriculum.lock.yaml` when present, inspect `git status` and relevant existing files, check for any more-specific `AGENTS.md` governing the write scope, and read the files needed to verify each precondition below.

1. Course design and all substantive course content are available and `course.yaml` status is `in-production`.
2. `audits/source-copyright.audit.yaml` and `audits/theology-fairness.audit.yaml` exist and pass without blocking findings.
3. This is a new audit run separate from the generation runs being reviewed.

## Authorized actions

1. Check prerequisite fit, learning progression, workload, outcomes, assignments, assessments, rubrics, answer keys, and human-review requirements.
2. Check lectures precede dependent work.
3. Check progression thresholds and retake policy.
4. Check stage calibration: source difficulty, primary-source engagement, decreasing scaffolding, assessment complexity, research independence, and appropriate original-language expectations.
5. For advanced undergraduate, MDiv, and PhD work, compare representative expectations with credible public academic benchmarks when useful. Benchmarking tests rigor; it does not authorize copying or claims of institutional equivalence.
6. For PhD courses, fail the audit if the instructional design merely scales undergraduate lectures upward instead of centering seminar research, primary sources, historiography, methods, student-led analysis, and qualified human supervision.
7. Create `audits/course-coherence.md` and `audits/course-coherence.audit.yaml`. The manifest must validate against `schemas/audit.schema.json`, reference this audit provenance, list generation run IDs reviewed, declare independent clean-context review, include `depends_on_audits: [source-copyright, theology-fairness]`, and store the current output of `python scripts/course_fingerprint.py <course-path>` as `content_fingerprint`.
8. If and only if all three course audit manifests pass without blocking findings, advance `course.yaml` from `in-production` to `ready-for-audit` and set `last_content_audit_date`.

## Forbidden actions

- Do not modify files outside the declared write scope.
- Do not invent unverified facts or sources.
- Do not begin a later prompt automatically.
- Do not silently revise course content to make the audit pass.
- Do not advance lifecycle status when any required audit is missing or failing.
- Do not commit unless the active prompt is explicitly overridden with owner authorization.

## Required validation

Run `python scripts/validate.py --mode draft` and the relevant tests after writing the audit manifests and any permitted lifecycle metadata. Add a provenance record for the audit run.

## Exit criteria

- All mismatches are listed with file paths.
- No revisions are silently applied.
- The machine-readable audit manifest and report agree.
- Release recommendation is explicit.
- `course.yaml` is `ready-for-audit` only when all three independent audit gates pass.

Stop and report changed files, sources, validation, unresolved items, and required human review.
