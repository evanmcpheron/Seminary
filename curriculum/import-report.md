# Curriculum Import Report

## Run status

**Completed.** The canonical spreadsheet at
`curriculum/source/Theological_Education_Curriculum_Plan_2026-27_Swapped.xlsx`
was imported into `curriculum/curriculum.yaml` and locked in
`curriculum/curriculum.lock.yaml`.

No course was renamed, removed, merged, replaced, or moved. No prerequisite or
workload correction was made.

## Import totals

| Measure | Result |
|---|---:|
| Spreadsheet inventory records imported | 108 |
| Course records | 68 |
| Non-course doctoral records | 40 |
| Calculated numeric credits | 223.0 |

The numeric-credit total is 133 Wheaton credits plus 90 Gordon-Conwell credits.
Princeton's 40 records use textual non-course credit labels because the source
does not assign a universal numeric credit value; they contribute zero to the
calculated numeric-credit total.

| Inventory worksheet | Imported records | Course records | Non-course records | Numeric credits |
|---|---:|---:|---:|---:|
| Wheaton Plan | 36 | 36 | 0 | 133 |
| GCTS Plan | 32 | 32 | 0 | 90 |
| Princeton Plan | 40 | 0 | 40 | 0 |
| **Total** | **108** | **68** | **40** | **223** |

## Source identity

- Canonical path: `curriculum/source/Theological_Education_Curriculum_Plan_2026-27_Swapped.xlsx`
- SHA-256: `876f558fae72b407292d0aac3f36692fb23c0290774b434fcc8a0abc6313cbb1`
- Workbook format: Microsoft Excel 2007+ (`.xlsx`)
- Imported inventory sheets: `Wheaton Plan`, `GCTS Plan`, and `Princeton Plan`

The workbook's overview, alternatives, audit, requirements, and sources sheets
are supporting documentation, not plan-inventory rows, and were not converted
into curriculum records. The Wheaton total row, GCTS total row, and Princeton
credit-total explanatory row are also non-record footers and were not imported.

## Record accounting and locked metadata

All 108 nonblank inventory rows between the three plan-sheet headers and their
footers are represented exactly once by source sheet and source row. All 108
generated record IDs are unique.

An exact source-to-manifest comparison confirmed preservation of every imported
course code/requirement label, title/published label, credit value, catalog
description, mapped institution, source year, and source term. The comparison
also covered requirement status, rationale, prerequisite/completion condition,
offering note, and catalog URL in the manifest. The lock preserves the required
identity metadata and intentionally omits only `selection_rationale` and
`offering_accuracy_note`, as defined by the repository import tool.

`curriculum/curriculum.yaml` has status `imported-unreconciled`.
`curriculum/curriculum.lock.yaml` has status `locked`.

## Princeton non-course classifications

| Classification | Records | Representation |
|---|---:|---|
| Competencies/preparation | 5 | `record_type: competency` |
| Examinations | 8 | `record_type: examination` |
| Seminar categories | 14 | `record_type: doctoral-seminar-category` |
| Colloquia | 4 | `record_type: milestone` plus `doctoral_record_category: colloquium` |
| Dissertation work | 4 | `record_type: milestone` plus `doctoral_record_category: dissertation-work` |
| Milestones | 5 | `record_type: milestone` plus `doctoral_record_category: milestone` |
| **Total** | **40** | |

The subtype field distinguishes colloquia and dissertation work without using
values excluded by the current curriculum schema. Every Princeton inventory row
has a resolved classification; there are no unclassified doctoral records.

## Prerequisite conflicts and dependencies

The following conflicts are present in the canonical schedule and remain
uncorrected:

| Source row | Record | Planned placement | Conflict |
|---|---|---|---|
| Wheaton Plan 5 | `BITH 301` — How We Got the Bible | Year 1 Fall | No listed prerequisite option occurs earlier in the plan. `BITH 211` is in Year 1 Spring, `BITH 213` is in Year 2 Fall, and the other listed alternatives are absent. The source itself says prior credit or approval may be required. |
| Wheaton Plan 7 | `ARCH 369` — Religions of Israel and the Near East | Year 1 Fall | No listed prerequisite option occurs earlier in the plan. `BITH 211` is in Year 1 Spring, and the other listed alternatives are absent. The source itself says prior credit or approval may be required. |
| Wheaton Plan 22 | `BITH 388` — Person and Work of Christ | Year 2 Spring | `BITH 315` is concurrent rather than prior, `BITH 372` is later in Year 4 Fall, and the other listed alternatives are absent. The source says the prerequisite must be completed or otherwise approved before enrollment. |

Additional unresolved dependency: Wheaton Plan row 28, `BITH 459` — Greek
Exegesis, says "catalog prerequisites apply" without naming them. This import
cannot verify the complete prerequisite set from the canonical row alone.
`TODO-VERIFY` the exact prerequisite relationship in the authorized
reconciliation/research workflow before dependent generation.

All other explicitly named course-to-course prerequisites have an earlier
qualifying course in the imported plan. Same-term doctoral sequences that state
an internal order—written comprehensives before the oral examination, and
proposal approval before initial dissertation work—must retain that order when
later scheduled in detail.

## Workload overloads

The canonical source and project decision record expressly identify both
Wheaton Year 1 semesters as overloads:

| Term | Credits | Credit-hour work | 15-week average |
|---|---:|---:|---:|
| Wheaton Year 1 Fall | 20 | 900 hours | 60 hours/week |
| Wheaton Year 1 Spring | 20 | 900 hours | 60 hours/week |

The remaining Wheaton fall/spring loads are 16, 16, 16, 16, 14, and 15 credits.
The four 16-credit terms imply 48 hours/week under the project model and are
heavy, but the source decision specifically designates the 20-credit freshman
terms for summer redistribution. No threshold was invented in this import.

Gordon-Conwell fall/spring terms contain 12–13 credits. Each January or summer
term contains one 3-credit course requiring 135 total hours; its weekly
intensity cannot be calculated until the compressed term length is defined.
Princeton workload cannot be converted to numeric credit hours because the
canonical source intentionally provides no universal per-seminar credit values.

No workload was redistributed in this prompt.

## Anomalies and unresolved items

1. The repository importer opens the workbook in read-only mode, but this
   workbook has no cached worksheet-dimension metadata. The direct command
   failed with `sheet.max_row` equal to `None`. A runtime-only compatibility shim
   reopened the same canonical workbook in normal read mode and then invoked the
   unchanged repository import tool. The workbook and importer source were not
   modified. Future direct reruns retain this tooling limitation.
2. The importer's initial heuristic labeled Princeton Plan row 15 (Doctoral
   Elective I) as a milestone. That generated classification was corrected from
   the spreadsheet's description of the record as an approved doctoral seminar.
   No source field was changed.
3. Princeton Plan rows 41 and 42 initially produced the same generated record
   ID because their code, title, and project year match. The IDs now end in
   `-fall` and `-spring`; the two records and all source metadata remain separate.
4. The three prerequisite conflicts and the unresolved `BITH 459` prerequisite
   detail listed above remain unresolved.
5. The two 20-credit Wheaton freshman overloads remain unresolved.
6. The workbook states that the customized 133-credit Wheaton plan replaces
   eight general/core courses and is not proof of complete Wheaton
   general-education coverage. A separate institutional-style audit remains
   required; no requirement was invented or corrected here.
7. Wheaton `BITH 388` and `BITH 392` are marked as offered occasionally. Their
   planned-term availability remains unverified.
8. The workbook states that Gordon-Conwell term placements are planning
   sequences rather than promises of annual availability. `IS/WM 520` (row 10),
   `SE 571` (row 16), and `TH 662` (row 32) are specifically labeled proposed
   placements. All offering checks remain for a later authorized workflow.
9. Princeton advisor-selected seminars have intentionally variable titles and
   no universal public per-seminar credit values. Residence-committee selection
   and approval remain required; no named seminar or numeric credit was invented.
10. Ministry placements, doctoral competency examinations, residence reviews,
    comprehensive examinations, committee approvals, dissertation supervision,
    defense, and final submission remain future human-evaluated completion
    conditions. Importing them does not mark them complete.

No inventory row is missing, duplicated, unclassified, or otherwise unresolved
at the import/accounting level.

## Validation and tests

- Source-to-manifest and manifest-to-lock preservation audit: passed; 108 of 108
  records accounted for, 108 unique IDs, exact required metadata preserved, and
  doctoral category counts matched 5/8/14/4/4/5.
- `python scripts/validate.py --mode draft`: passed with 0 errors and 0 warnings.
- `pytest`: passed, 5 tests.

## Human review and next permitted prompt

Human approval is required for any schedule override, prior-credit/permission
resolution, or overload redistribution. The next permitted prompt is
`prompts/02a-reconcile-prerequisites-and-workload.md`. It has not been started.
