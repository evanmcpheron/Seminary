---
prompt_id: 01-bootstrap-repository
purpose: Create or verify repository boilerplate without generating curriculum content
write_scope:
  - root governance files
  - curriculum scaffold files
  - courses year/term scaffold directories
  - formation scaffold
  - dissertation scaffold
  - prompts
  - schemas
  - scripts
  - templates
  - tests
  - .github
commit_allowed: false
---

# Bootstrap Repository

## Preconditions

Read `AGENTS.md` and `MASTER_PROMPT.md`. Confirm the current working directory is the intended repository root for `evanmcpheron/Seminary`. Inspect `git status`, existing files, and directory structure.

## Objective

Create or verify an idempotent project scaffold containing governance, policies, the 12-year directory map, templates, schemas, Python tooling, tests, CI, provenance, formation, dissertation structure, and the numbered prompt suite. Do not import the curriculum spreadsheet, create course identities, select books, generate syllabi, write lectures, create assignments, or produce tests.

## Hard constraints

1. Never overwrite a substantive existing file with boilerplate.
2. When a target file exists, compare it to the required purpose. Preserve it unless the owner explicitly authorizes replacement.
3. Create only missing directories and missing clearly boilerplate files.
4. Do not alter the canonical spreadsheet.
5. Do not invent course metadata.
6. Keep private devotional and pastoral directories excluded from Git.
7. Use `main` as the documented default branch, but do not change repository settings.
8. Do not commit unless this prompt is later run with an explicit owner-supplied `COMMIT_ALLOWED: true` override.

## Required structure

Verify the root policy files, `PROJECT-DECISIONS.yaml`, `curriculum/`, twelve year directories under `courses/`, `formation/`, `dissertation/`, `prompts/`, `schemas/`, `scripts/`, `templates/`, `tests/`, `provenance/`, and `.github/workflows/`.

Undergraduate years must contain fall, spring, and summer scaffolds. MDiv years must contain fall, January, spring, and summer. PhD residence years must contain appropriate term and milestone scaffolds. Dissertation years use research-term and milestone structures, not week folders.

## Required verification

Run:

```bash
python scripts/bootstrap_repository.py --check
python scripts/validate.py --mode scaffold
pytest
```

If dependencies are not installed, report the exact install command. Do not edit tests or validation to conceal a failure.

## Provenance

Create one provenance record for this bootstrap run only when substantive files were created or modified. List all inputs, outputs, commands, validation results, and unresolved items.

## Exit report

Report:

- Repository root inspected.
- Files created.
- Existing files preserved.
- Validation and test results.
- Missing external inputs, especially the canonical spreadsheet.
- The next permitted prompt: `02-import-and-lock-curriculum.md`.

Stop after the report.
