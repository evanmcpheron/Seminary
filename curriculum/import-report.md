# Curriculum Import Report

## Run status

**Blocked before import.** The required canonical spreadsheet was not present at:

`curriculum/source/Theological_Education_Curriculum_Plan_2026-27_Swapped.xlsx`

The import command exited with status 1 before reading any spreadsheet records or writing either curriculum manifest. The existing `curriculum/curriculum.yaml` remains in its `awaiting-import` state, and `curriculum/curriculum.lock.yaml` was not created. This prevents a false lock from being generated against a noncanonical source.

## Import totals

| Measure | Result |
|---|---:|
| Spreadsheet records imported | 0 |
| Course records | Unavailable (no canonical dataset imported) |
| Non-course doctoral records | Unavailable (no canonical dataset imported) |
| Calculated numeric credits | Unavailable (no canonical dataset imported) |

## Source identity

- Required canonical path: `curriculum/source/Theological_Education_Curriculum_Plan_2026-27_Swapped.xlsx`
- Required canonical source SHA-256: unavailable because the file is absent
- Noncanonical file observed, but not imported: `curriculum/source/Theological_Education_Curriculum_Plan_2026-27.xlsx`
- Noncanonical file SHA-256: `876f558fae72b407292d0aac3f36692fb23c0290774b434fcc8a0abc6313cbb1`
- Repository comparison: the noncanonical file is byte-for-byte identical to the workbook tracked at the repository root in `HEAD`; it cannot be presumed to be the missing `_Swapped.xlsx` workbook.

No spreadsheet was renamed, copied, modified, or substituted during this run.

## Anomalies and unresolved items

1. `TODO-VERIFY`: Supply or restore the owner-approved canonical workbook at the exact required `_Swapped.xlsx` path and verify its SHA-256 before import.
2. The worktree already contained a deleted tracked root workbook and an untracked unswapped workbook under `curriculum/source/`. These pre-existing user changes were preserved.
3. Record-level anomalies cannot be enumerated until the canonical workbook is available and imported.
4. Princeton non-course records cannot be counted or classified until the canonical workbook is available. No classifications were guessed from the unswapped workbook.
5. Prerequisite conflicts cannot be assessed until canonical records are imported.
6. Term workload overloads cannot be calculated until canonical records are imported.
7. `curriculum/curriculum.lock.yaml` remains absent because there is no verified canonical source from which to create it.

No prerequisite, scheduling, or workload corrections were made.

## Commands and results

- Import: `python scripts/import_curriculum.py --input curriculum/source/Theological_Education_Curriculum_Plan_2026-27_Swapped.xlsx --output curriculum/curriculum.yaml --lock-output curriculum/curriculum.lock.yaml`
  - Result: failed as expected for the missing precondition; exit 1, `Canonical spreadsheet not found`.
- Draft validation: `python scripts/validate.py --mode draft`
  - Result: passed with 0 errors and 1 warning (`Curriculum has not yet been imported from the canonical spreadsheet`).
- Tests: `pytest`
  - Result: passed, 5 tests.

## Human action and next permitted prompt

Owner action is required to place the correct owner-approved workbook at the required path. Then rerun `prompts/02-import-and-lock-curriculum.md` from the beginning. `prompts/02a-reconcile-prerequisites-and-workload.md` is the formal next prompt only after prompt 02 completes successfully; it is not yet permitted.
