# Architecture

## Governance layer

Root policy documents and `MASTER_PROMPT.md` define immutable project rules. `PROJECT-DECISIONS.yaml` is the machine-readable decision record.

## Curriculum layer

The spreadsheet in `curriculum/source/` is the source inventory. Import creates `curriculum/curriculum.yaml` and a hash-locked snapshot. Schedule reconciliation may change only planned placement, never source course identity.

## Content layer

Course directories live under `courses/<year>/<term>/<course-id>/`. Each contains machine-readable metadata, human-readable syllabus material, weekly units, assessments, rubrics, instructor materials, and source records.

## Formation layer

`formation/` stores non-private completion records and portfolios. Private devotional or pastoral material is excluded from Git.

## Doctoral layer

`dissertation/` stores research-interest development, verified bibliographies, seminar-paper revisions, comprehensive preparation, prospectus, committee records, chapter milestones, and defense preparation. Dissertation prose must remain student-authored.

## Control layer

Schemas, scripts, tests, provenance records, and GitHub Actions validate metadata, source status, workload, prerequisites, required files, and unauthorized changes.
