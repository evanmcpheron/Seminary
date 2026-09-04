---
prompt_id: 15-revise-after-audit
purpose: Apply One Approved Audit Revision Set
write_scope:
  - only files explicitly named in the approved audit disposition
  - provenance/
commit_allowed: false
---

# Apply One Approved Audit Revision Set

## Preconditions

Before taking any action, apply `AGENTS.md` and complete its required reading order, including `MASTER_PROMPT.md`, `PROJECT-DECISIONS.yaml`, every root policy file, and this active prompt. Also read `curriculum/curriculum.yaml` and `curriculum/curriculum.lock.yaml` when present, inspect `git status` and relevant existing files, check for any more-specific `AGENTS.md` governing the write scope, and read the files needed to verify each precondition below.

1. An audit report exists.
2. The owner has approved specific findings.
3. Allowed files are listed.

## Authorized actions

1. Apply only approved corrections.
2. Preserve curriculum lock metadata.
3. Update revision dates and provenance.
4. Re-run relevant audits and validation.

## Forbidden actions

- Do not modify files outside the declared write scope.
- Do not invent unverified facts or sources.
- Do not begin a later prompt automatically.
- Do not commit unless the active prompt is explicitly overridden with owner authorization.

## Required validation

Run `python scripts/validate.py --mode draft` and the relevant tests. Add a provenance record.

## Exit criteria

- Every approved finding is resolved or explained.
- No unapproved change occurred.
- Validation passes.

Stop and report changed files, sources, validation, unresolved items, and required human review.
