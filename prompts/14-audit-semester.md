---
prompt_id: 14-audit-semester
purpose: Audit One Semester or Program-Year Progression
write_scope:
  - one semester or longitudinal audit report
  - one machine-readable audit manifest under quality/
  - provenance/
commit_allowed: false
---

# Audit One Semester or Program-Year Progression

Run this prompt in exactly one declared mode: `semester` or `longitudinal`.

## Preconditions

Before taking any action, apply `AGENTS.md` and complete its required reading order, including `MASTER_PROMPT.md`, `PROJECT-DECISIONS.yaml`, every root policy file, and this active prompt. Also read `curriculum/curriculum.yaml` and `curriculum/curriculum.lock.yaml` when present, inspect `git status` and relevant existing files, check for any more-specific `AGENTS.md` governing the write scope, and read the files needed to verify each precondition below.

### Semester mode

1. All course designs in the named term are available.
2. No full semester content generation is authorized.

### Longitudinal mode

1. The project year is explicitly named.
2. That year's course designs, completed content, course audits, results available for progression decisions, and semester audits are available.
3. Earlier-year longitudinal reports are read when present so repeated weaknesses and trends are visible.
4. This is a separate audit run; do not reuse a course-generation run as the longitudinal review.

## Authorized actions

### Semester mode

1. Sum weekly workload across courses.
2. Identify assignment and exam clustering.
3. Check prerequisites and cross-course dependencies.
4. Recommend calendar adjustments without changing course identity.
5. Write `quality/semesters/year-XX-TERM.md` and the matching `.audit.yaml` manifest with `audit_type: semester-workload`.

### Longitudinal mode

1. Compare the named year with prior stages for increasing source difficulty, primary-source engagement, research independence, argument complexity, cumulative assessment, original-language expectations, and reduced scaffolding.
2. Check that MDiv work contains the required human formation/performance components and that AI has not substituted for preaching, pastoral, ministry, or designated language evaluation.
3. Check that PhD work is seminar- and research-centered rather than an expanded lecture sequence. Inspect historiography, methods, student-led analysis, seminar papers, colloquia, comprehensives, prospectus work, and supervised research as applicable.
4. Sample representative assignments and reading expectations against credible public academic benchmarks. Record the benchmark evidence without copying proprietary materials or claiming equivalence.
5. Identify cross-year repetition, missing prerequisite mastery, declining source quality, inflated word count without increased difficulty, excessive AI scaffolding, and assessment patterns that fail to require independent student judgment.
6. Write `quality/longitudinal/year-XX.md` and `quality/longitudinal/year-XX.audit.yaml` with `audit_type: longitudinal-progression`.
7. Fail the longitudinal audit when material stage drift is found. Do not mark a year passed merely because all individual courses passed local validation.

## Forbidden actions

- Do not modify course content or canonical curriculum data in this audit prompt.
- Do not invent unverified facts, benchmarks, results, or sources.
- Do not begin a later prompt automatically.
- Do not treat greater lecture length as evidence of academic progression.
- Do not commit unless the active prompt is explicitly overridden with owner authorization.

## Required validation

Run `python scripts/validate.py --mode draft` and the relevant tests. Add a provenance record for the audit run. Every machine-readable manifest must validate against `schemas/audit.schema.json` and point to its human-readable report.

## Exit criteria

### Semester mode

- Peak weekly workload is reported.
- Clashes and overloads are listed.
- Any proposed schedule change awaits approval.

### Longitudinal mode

- The report states whether the year's rigor progressed appropriately.
- Repeated weaknesses and quality-drift risks are explicit.
- Human-review gaps are explicit.
- The manifest verdict is `pass` only when no blocking progression issue remains.
- A passing `year-XX.audit.yaml` is available before any course in project year `XX + 1` is released.

Stop and report changed files, sources, validation, unresolved items, and required human review.
