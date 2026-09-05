# Prompt Suite

`00-master-project-constitution.md` governs every task. Numbered prompts are executed separately and define the permitted write scope. The `02a` prompt is an intentionally separate scheduling gate added between import and course work.

Prompt filenames match the normal numeric execution sequence. For every newly instantiated course, run **03 → 04 → 05** so the course lifecycle remains `shell` → `researching` → `designed`. Do not run Prompt 04 against a new course until Prompt 03 has created its shell.

| Execution order | Prompt | Purpose |
|---:|---|---|
| 1 | 00 | Master project constitution; applies to every run |
| 2 | 01 | Bootstrap repository |
| 3 | 02 | Import and lock curriculum |
| 4 | 02a | Reconcile prerequisites and workload |
| 5 | 03 | Generate one course shell |
| 6 | 04 | Research that course |
| 7 | 05 | Design that course |
| 8 | 06 | Generate one week |
| as needed | 07 | Generate one lecture |
| as needed | 08 | Generate one assignment and rubric |
| as needed | 09 | Generate one assessment |
| as needed | 10 | Generate one answer key |
| audit | 11 | Independently audit sources and copyright |
| audit | 12 | Independently audit theology and fair representation |
| audit | 13 | Independently audit course coherence and advance the lifecycle gate |
| term/year gate | 14 | Audit semester workload or annual longitudinal progression |
| revision | 15 | Revise approved audit findings and invalidate superseded audit evidence |
| doctoral | 16 | Build one comprehensive field |
| doctoral | 17 | Build dissertation prospectus process |
| doctoral | 18 | Support one dissertation chapter without authoring it |
| release | 19 | Release one course version |

For complete invocation requirements, branching guidance, status transitions, and examples, read the root [`PROMPT-FLOW.md`](../PROMPT-FLOW.md).

Default execution is one prompt, one declared unit, one provenance record, validation, and stop. Full-course release audits are separate clean-context runs under Prompts 11-13; developmental source checks created during production do not satisfy those gates.
