# Start Here

See `INSTALL.md` for safe copy instructions.

This scaffold is intentionally conservative. It establishes governance, directory structure, schemas, templates, validation, and prompt boundaries. It does **not** fabricate course content or assume that a missing spreadsheet has been imported.

## First Codex session

From the repository root, give Codex this instruction:

> Read `AGENTS.md`, `MASTER_PROMPT.md`, and `prompts/01-bootstrap-repository.md` in that order. Inspect the repository before editing. Execute the bootstrap prompt idempotently. Do not import the curriculum, create course shells, research books, or generate lessons unless those actions are explicitly included in the active scoped prompt. Run the required validation commands and report every file changed.

## Second Codex session

After placing the canonical spreadsheet in `curriculum/source/`, use:

> Read `AGENTS.md`, `MASTER_PROMPT.md`, and `prompts/02-import-and-lock-curriculum.md`. Execute only that prompt. Preserve the spreadsheet as the canonical inventory, create the YAML manifest and lock file, report prerequisite or workload conflicts without silently changing them, run validation, and stop.

## Branch policy

- Default branch: `main`.
- Work in a feature branch such as `bootstrap/repository`, `course/bith-301`, or `week/bith-301-01`.
- Codex may create a local focused commit only when the active prompt explicitly sets `COMMIT_ALLOWED: true`.
- Codex must never push, merge, force-push, rewrite history, or modify branch protection without an explicit owner instruction.

## Required local inputs

The canonical spreadsheet is not bundled unless it was explicitly supplied with this archive. Place it at:

```text
curriculum/source/Theological_Education_Curriculum_Plan_2026-27_Swapped.xlsx
```

Do not rename catalog courses, change credits, or revise catalog descriptions during import.
