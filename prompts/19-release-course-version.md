---
prompt_id: 19-release-course-version
purpose: Release One Audited Course Version
write_scope:
  - one course version metadata file
  - course changelog
  - release provenance record
commit_allowed: false
---

# Release One Audited Course Version

## Preconditions

Before taking any action, apply `AGENTS.md` and complete its required reading order, including `MASTER_PROMPT.md`, `PROJECT-DECISIONS.yaml`, every root policy file, and this active prompt. Also read `curriculum/curriculum.yaml` and `curriculum/curriculum.lock.yaml` when present, inspect `git status` and relevant existing files, check for any more-specific `AGENTS.md` governing the write scope, and read the files needed to verify each precondition below.

1. Source, theology, coherence, and copyright audits pass.
2. Required human review is complete.
3. No TODO-VERIFY markers remain.

## Authorized actions

1. Run release validation.
2. Update course status and version.
3. Write a changelog.
4. Prepare but do not push a Git tag or release unless explicitly authorized.

## Forbidden actions

- Do not modify files outside the declared write scope.
- Do not invent unverified facts or sources.
- Do not begin a later prompt automatically.
- Do not commit unless the active prompt is explicitly overridden with owner authorization.

## Required validation

Run `python scripts/validate.py --mode draft` and the relevant tests. Add a provenance record.

## Exit criteria

- Release validation passes.
- Version metadata and changelog are complete.
- No unauthorized Git operation occurred.

Stop and report changed files, sources, validation, unresolved items, and required human review.
