# Contributing

## Scope discipline

Contributions must be tied to one numbered prompt and one explicit write scope. A change may address one course design, one course shell, one week, one lecture, one assignment, one assessment, one audit, or one approved revision set.

## Branch names

- `bootstrap/<topic>`
- `curriculum/<topic>`
- `course/<course-id>`
- `week/<course-id>-<week>`
- `audit/<scope>`
- `fix/<scope>`

## Required checks

```bash
python scripts/validate.py --mode draft
pytest
```

Release candidates also require:

```bash
python scripts/validate.py --mode release
```

## Commit rules

Use focused commits. Do not combine unrelated courses or weeks. AI agents may commit only when the active prompt explicitly allows it. Never push or merge without owner authorization.

## Pull requests

State:

- Active prompt.
- Allowed write scope.
- Files changed.
- Sources verified.
- Workload impact.
- Theological or interpretive issues.
- Validation results.
- Outstanding human review.
