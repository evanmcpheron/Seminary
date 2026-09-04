---
prompt_id: 11-audit-sources
purpose: Audit Sources for One Scoped Unit
write_scope:
  - one audit report
  - source record corrections within the scoped unit
  - provenance/
commit_allowed: false
---

# Audit Sources for One Scoped Unit

## Preconditions

1. The target course, week, lecture, or assessment is named.
2. All claimed sources are available for inspection.

## Authorized actions

1. Verify bibliographic fields, access, links, quotations, page ranges, and copyright status.
2. Flag uncited claims and inaccessible sources.
3. Do not replace sources merely for theological agreement.
4. Require free alternatives for paid articles where feasible.

## Forbidden actions

- Do not modify files outside the declared write scope.
- Do not invent unverified facts or sources.
- Do not begin a later prompt automatically.
- Do not commit unless the active prompt is explicitly overridden with owner authorization.

## Required validation

Run `python scripts/validate.py --mode draft` and the relevant tests. Add a provenance record.

## Exit criteria

- Every required source is verified or explicitly blocked.
- No fabricated or inaccessible citation remains hidden.
- Audit verdict is recorded.

Stop and report changed files, sources, validation, unresolved items, and required human review.
