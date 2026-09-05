# Quality Assurance and Release Gates

This policy exists to prevent quality drift, self-confirming AI review, stale source claims, and false progression from undergraduate work into graduate and doctoral stages. It supplements `MASTER_PROMPT.md`, `ACADEMIC-STANDARDS.md`, `SOURCE-POLICY.md`, and the numbered prompts.

## 1. Two different kinds of audit

Developmental audits performed while generating a week, lecture, assignment, or assessment are useful but are not release audits. A Prompt 06 lecture source audit may catch errors before dependent work is generated, but it does not satisfy the independent course-audit gates.

A course release requires three separate full-course audits:

1. `source-copyright`
2. `theology-fairness`
3. `course-coherence`

Each full-course audit must create both a human-readable report and a machine-readable `*.audit.yaml` manifest under the course's `audits/` directory.

## 2. Independent-review rule

A release audit must be a separate run from the generation runs it evaluates. Its manifest must:

- identify the audit provenance `run_id`;
- list the generation provenance run IDs it reviewed;
- assert `separate_run: true` and `clean_context: true`;
- use the generated artifacts, verified source records, and governing policies as evidence rather than relying on the generator's hidden reasoning or prior self-assessment;
- record blocking and nonblocking findings explicitly; and
- record the release-scoped `content_fingerprint` produced by `python scripts/course_fingerprint.py <course-path>`.

The same model family may be used when no materially different reviewer is available, but the review must still be a fresh run with a clean task context. A generator's own same-run self-check can never be promoted into an independent release audit.

## 3. Course lifecycle gate

The lifecycle is:

`shell` -> `researching` -> `designed` -> `in-production` -> `ready-for-audit` -> `released`

Prompt 11 and Prompt 12 do not advance lifecycle status. Prompt 13 may advance a fully produced course from `in-production` to `ready-for-audit` only when the source/copyright, theology/fairness, and coherence audit manifests all pass and contain no blocking findings.

Prompt 19 may advance `ready-for-audit` to `released` only after release validation succeeds and all required human review is complete. If substantive course content changes after an audit, its fingerprint no longer matches and the affected release audits must be rerun.

### Resource-acquisition blockers

A course cannot advance through the audit/release gates while any required text
uses a noncanonical designation, lacks a matching verified source record, or
conflicts with that source record's acquisition category. A required purchase
without structured evidence of meaningful use, or one whose `use_extent` is
`isolated-excerpt`, is blocking. Any required-purchase Scripture source or any
required Scripture source without a verified lawful USD 0 route is also
blocking.

The independent source/copyright audit must compare every purchase
justification and claimed week of material use with the syllabus, schedule, and
actual assigned readings. Passing schema validation does not substitute for
that evidentiary check.

## 4. Source freshness

Verification is not permanent. Release-candidate sources must be rechecked when their access evidence is older than the following default limits:

| Source type | Maximum verification age at release |
|---|---:|
| catalog, website, video, podcast | 180 days |
| book, article, chapter, primary text, reference work, Scripture record | 730 days |

A source record may be reverified without changing its bibliographic identity. Reverification must update `accessed_at` and record any changed access, edition, URL, price, transcript, or licensing facts. Historical bibliographic facts do not become false merely because the access check ages; the purpose of the freshness gate is to prevent old availability and access claims from being treated as current.

## 5. Human-review escalation

AI may never attest that a required human evaluation occurred.

- Years 1-3: routine external signoff is not required unless the course design explicitly requires it.
- Year 4: senior-capstone human review remains strongly recommended and should be recorded when completed.
- MDiv: preaching, pastoral, ministry/field-education, and designated language-performance work requires qualified human evaluation.
- PhD: every released doctoral course or milestone requiring scholarly completion must have qualified human oversight. Comprehensive examinations, prospectus approval, dissertation chapters, and defense decisions remain human decisions.

Where `course.yaml` sets `external_evaluator_required: true` or `human_evaluation.mandatory_external_signoff: true`, it must also provide `human_evaluation.completion_record_path`. The referenced record must validate against `schemas/human-review.schema.json` before release.

For PhD courses, release validation treats external human signoff as mandatory even if a generated course design mistakenly marks it optional.

## 6. Longitudinal progression audit

At the end of each project year, Prompt 14 must be run in longitudinal mode after that year's term audits are complete. It creates:

- `quality/longitudinal/year-XX.md`
- `quality/longitudinal/year-XX.audit.yaml`

The audit must compare the completed year with earlier stages and test whether rigor is increasing appropriately rather than merely increasing word count. It must examine at least:

- primary-source difficulty and proportion;
- reading independence and research independence;
- writing length only as one factor, with greater weight on argument complexity and evidence use;
- assessment complexity and cumulative synthesis;
- original-language expectations where appropriate;
- reduced scaffolding over time;
- MDiv formation and ministry-performance requirements;
- PhD seminar, historiographic, methodological, and research expectations; and
- whether doctoral work is becoming student research rather than AI-authored lecture consumption.

Before any Year 2 or later course may be released, the previous project's year longitudinal audit must pass. This creates a recurring check against slow quality drift.

## 7. Doctoral anti-simulation rule

Doctoral rigor is not measured by longer AI lectures. In PhD years:

- lectures should be used sparingly;
- seminars should center primary sources, historiography, methods, research problems, colloquia, and student-led analysis;
- at least two seminar papers should be developed toward conference-quality work;
- comprehensives must be administered and scored by qualified humans;
- the prospectus must be student-authored and human-approved;
- dissertation prose must be student-authored;
- AI may organize research, test arguments, check citations, surface counterarguments, and critique drafts, but it may not make completion decisions.

If a doctoral stage begins to resemble an undergraduate lecture sequence with larger word counts, the longitudinal audit must fail until the design is corrected.

Human-gated doctoral milestones use `*.milestone.yaml` records validated by `schemas/milestone.schema.json`. Comprehensive fields, prospectus approval, dissertation chapters, and defense milestones may be `planned`, `in-progress`, or `awaiting-human-review` without a completed human review, but they may not be marked `complete` unless `human_review_record_path` resolves to a passing human-attested review record.

## 8. Machine-readable audit evidence

Audit manifests validate against `schemas/audit.schema.json`. A passing audit must use verdict `pass` or `pass-with-nonblocking-findings` and must have an empty `blocking_findings` list.

All paths stored inside audit manifests, course human-evaluation metadata, and human-review records must be repository-relative paths. Absolute paths and paths escaping the repository are invalid.

The validator checks that:

- required audit manifests exist for `ready-for-audit` and `released` courses;
- audit run IDs resolve to provenance records;
- an audit run is not also listed as a generation run it reviews;
- clean-context and separate-run declarations are true;
- report paths exist;
- all three course-audit fingerprints match the current release-scoped course content;
- release-candidate source verification is fresh;
- required-text acquisition designations, source-record reconciliation,
  purchase justifications, and zero-cost Scripture access are valid;
- required human-review records exist and pass;
- completed human-gated milestone records resolve to passing human review; and
- the prior-year longitudinal audit exists before releasing Year 2+ work.

These checks do not prove scholarly correctness. They force the repository to retain evidence that the required review process actually occurred and make missing gates visible to CI.
