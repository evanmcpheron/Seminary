---
prompt_id: 12-audit-theology
purpose: Audit Theology and Fair Representation
write_scope:
  - one theological audit report
  - provenance/
commit_allowed: false
---

# Audit Theology and Fair Representation

## Preconditions

Before taking any action, apply `AGENTS.md` and complete its required reading order, including `MASTER_PROMPT.md`, `PROJECT-DECISIONS.yaml`, every root policy file, and this active prompt. Also read `curriculum/curriculum.yaml` and `curriculum/curriculum.lock.yaml` when present, inspect `git status` and relevant existing files, check for any more-specific `AGENTS.md` governing the write scope, and read the files needed to verify each precondition below.

1. The target content is named.
2. The source audit is available.

## Authorized actions

1. Check consistency with historic Christian and Protestant commitments.
2. Check that alternatives are represented accurately.
3. Check complementarian treatment for fairness and respect.
4. Check that confessional evaluation follows rather than replaces evidence.
5. Flag political-partisan capture.

## Forbidden actions

- Do not modify files outside the declared write scope.
- Do not invent unverified facts or sources.
- Do not begin a later prompt automatically.
- Do not commit unless the active prompt is explicitly overridden with owner authorization.

## Required validation

Run `python scripts/validate.py --mode draft` and the relevant tests. Add a provenance record.

## Exit criteria

- Confessional commitments are explicit.
- Opposing views are not caricatured.
- Corrections are recommendations, not silently applied.

Stop and report changed files, sources, validation, unresolved items, and required human review.
