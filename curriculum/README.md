# Curriculum Control

The spreadsheet in `source/` is the canonical course inventory. `curriculum.yaml` is generated from it and must preserve course codes, titles, credits, catalog descriptions, and source URLs. `curriculum.lock.yaml` is generated during import and records the spreadsheet hash plus immutable course metadata.

Schedule changes are stored separately in `schedule-overrides.yaml`. They may change planned year/term placement only. Every override requires a rationale and owner approval.
