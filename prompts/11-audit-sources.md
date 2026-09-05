---
prompt_id: 11-audit-sources
purpose: Independently Audit Sources and Copyright for One Scoped Unit
write_scope:
  - one audit report
  - one full-course audits/source-copyright.audit.yaml when the target is a full course
  - source record corrections within the scoped unit
  - the explicitly named course's course.yaml, limited to source-verification metadata for a full-course audit
  - provenance/
commit_allowed: false
---

# Independently Audit Sources and Copyright for One Scoped Unit

## Preconditions

Before taking any action, apply `AGENTS.md` and complete its required reading order, including `MASTER_PROMPT.md`, `PROJECT-DECISIONS.yaml`, every root policy file, and this active prompt. Also read `curriculum/curriculum.yaml` and `curriculum/curriculum.lock.yaml` when present, inspect `git status` and relevant existing files, check for any more-specific `AGENTS.md` governing the write scope, and read the files needed to verify each precondition below.

1. The target course, week, lecture, or assessment is named.
2. All claimed sources are available for inspection.
3. If this is the full-course release audit, substantive production is complete and `course.yaml` status is `in-production`.
4. This audit is a new run, separate from all generation runs being reviewed. Developmental audits created during Prompt 06 do not satisfy this precondition.

## Authorized actions

1. Verify bibliographic fields, access, links, quotations, page ranges, claim support, and copyright/licensing status.
2. Flag uncited claims, inaccessible sources, unsupported quotations, and source records whose current-access evidence is stale under `QUALITY-ASSURANCE.md`.
3. Do not replace sources merely for theological agreement.
4. Require free alternatives for paid articles where feasible.
5. For a full-course audit, create `audits/source-copyright.md` and `audits/source-copyright.audit.yaml`. The manifest must validate against `schemas/audit.schema.json`, identify this audit's provenance `run_id`, list the generation run IDs reviewed, declare separate-run and clean-context independence, record the verdict and findings, and store the current output of `python scripts/course_fingerprint.py <course-path>` as `content_fingerprint`.
6. Correct source records only when the correction is independently verified. Reverification may update `accessed_at` without changing stable bibliographic identity.
7. For a full-course audit, update `course.yaml.source_verification_date` to the completed audit date after all required sources are rechecked.
8. Preserve `course.yaml` lifecycle status. Prompt 11 does not advance a course to `ready-for-audit`.

## Forbidden actions

- Do not modify files outside the declared write scope.
- Do not invent unverified facts or sources.
- Do not begin a later prompt automatically.
- Do not convert a same-run generator self-check into a release audit.
- Do not commit unless the active prompt is explicitly overridden with owner authorization.

## Required validation

Run `python scripts/validate.py --mode draft` and the relevant tests. Add a provenance record for the audit run.

## Exit criteria

- Every required source is verified or explicitly blocked.
- No fabricated, unsupported, inaccessible, or copyright-invalid citation remains hidden.
- Full-course audit report and machine-readable manifest agree on the verdict.
- A full-course passing audit leaves `course.yaml` at `in-production`; lifecycle advancement occurs only after Prompt 13.

Stop and report changed files, sources, validation, unresolved items, and required human review.
