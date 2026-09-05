---
prompt_id: 15-revise-after-audit
purpose: Apply One Approved Audit Revision Set and Invalidate Superseded Audit Evidence
write_scope:
  - only files explicitly named in the approved audit disposition
  - the affected course's course.yaml, limited to lifecycle/audit metadata when substantive course content changes
  - provenance/
commit_allowed: false
---

# Apply One Approved Audit Revision Set and Invalidate Superseded Audit Evidence

## Preconditions

Before taking any action, apply `AGENTS.md` and complete its required reading order, including `MASTER_PROMPT.md`, `PROJECT-DECISIONS.yaml`, every root policy file, and this active prompt. Also read `curriculum/curriculum.yaml` and `curriculum/curriculum.lock.yaml` when present, inspect `git status` and relevant existing files, check for any more-specific `AGENTS.md` governing the write scope, and read the files needed to verify each precondition below.

1. An audit report exists.
2. The owner has approved specific findings.
3. Allowed files are listed.
4. If the affected course has full-course audit manifests, record which of those audits cover the files being changed.

## Authorized actions

1. Apply only approved corrections.
2. Preserve curriculum lock metadata.
3. Update revision dates and provenance.
4. If any release-scoped course content changes after a full-course audit, set `course.yaml` status back to `in-production` before validation. Existing audit files remain historical evidence in Git but no longer authorize release of the changed content.
5. Report the independent audits that must be rerun. Do not run Prompt 11, 12, or 13 automatically under this prompt.

## Forbidden actions

- Do not modify files outside the declared write scope.
- Do not invent unverified facts or sources.
- Do not begin a later prompt automatically.
- Do not leave a substantively changed course at `ready-for-audit` or `released` on the authority of pre-revision audit manifests.
- Do not edit an audit manifest's fingerprint or verdict merely to make revised content appear previously audited.
- Do not commit unless the active prompt is explicitly overridden with owner authorization.

## Required validation

Run `python scripts/validate.py --mode draft` and the relevant tests. Add a provenance record.

## Exit criteria

- Every approved finding is resolved or explained.
- No unapproved change occurred.
- Any superseded release audits are treated as invalid for lifecycle purposes.
- Validation passes.
- The next required independent audit prompt(s) are reported explicitly when substantive course content changed.

Stop and report changed files, sources, validation, unresolved items, and required human review.
