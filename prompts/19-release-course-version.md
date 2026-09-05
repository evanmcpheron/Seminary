---
prompt_id: 19-release-course-version
purpose: Release One Independently Audited Course Version
write_scope:
  - the explicitly named course's course.yaml
  - one course version metadata file
  - course changelog
  - release provenance record
commit_allowed: false
---

# Release One Independently Audited Course Version

## Preconditions

Before taking any action, apply `AGENTS.md` and complete its required reading order, including `MASTER_PROMPT.md`, `PROJECT-DECISIONS.yaml`, every root policy file, and this active prompt. Also read `curriculum/curriculum.yaml` and `curriculum/curriculum.lock.yaml` when present, inspect `git status` and relevant existing files, check for any more-specific `AGENTS.md` governing the write scope, and read the files needed to verify each precondition below.

1. `audits/source-copyright.audit.yaml`, `audits/theology-fairness.audit.yaml`, and `audits/course-coherence.audit.yaml` exist, validate, and pass without blocking findings.
2. `course.yaml` status is `ready-for-audit`.
3. Required human review is complete. When external signoff is mandatory, `human_evaluation.completion_record_path` points to a passing qualified human review record; AI cannot create or attest that record.
4. For project Year 2 or later, the previous project's year `quality/longitudinal/year-XX.audit.yaml` exists and passes.
5. Required source access evidence satisfies the freshness limits in `QUALITY-ASSURANCE.md`.
6. No `TODO-VERIFY` or `UNVERIFIED` markers remain in release-scoped course content.
7. No blocking resource-acquisition violation identified in
   `QUALITY-ASSURANCE.md` or the source/copyright audit remains.

## Authorized actions

1. Run release validation while the course is still `ready-for-audit` so source freshness and release gates are checked before status changes.
2. Update course status and version only after release validation succeeds.
3. Write version metadata that records the three audit IDs, release-validation result, applicable longitudinal audit ID, and human-review record path when required.
4. Write a changelog.
5. Prepare but do not push a Git tag or release unless explicitly authorized.

## Forbidden actions

- Do not modify files outside the declared write scope.
- Do not invent unverified facts or sources.
- Do not begin a later prompt automatically.
- Do not bypass, delete, or weaken a failing audit or validator check.
- Do not release on the basis of a developmental same-run audit.
- Do not commit unless the active prompt is explicitly overridden with owner authorization.

## Required validation

Before changing lifecycle status, run:

```bash
python scripts/validate.py --mode release
pytest
```

After updating `course.yaml` to `released` and writing release metadata/changelog, run:

```bash
python scripts/validate.py --mode draft
pytest
```

Add a release provenance record containing both validation results.

## Exit criteria

- Release validation passed before the lifecycle update.
- `course.yaml` status is `released` and version metadata/changelog are complete.
- Independent audit, longitudinal, source-freshness, and required human-review evidence remain traceable.
- No unauthorized Git operation occurred.

Stop and report changed files, sources, validation, unresolved items, and required human review.
