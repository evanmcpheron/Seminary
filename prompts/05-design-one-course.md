---
prompt_id: 05-design-one-course
purpose: Design One Course
write_scope:
  - one explicitly named course README.md
  - course.yaml
  - syllabus.md
  - schedule.md
  - bibliography.md
  - learning-outcomes.md
  - policies.md
  - assignment and assessment maps
  - one explicitly named course's source records, limited to final acquisition classifications and access metadata
  - provenance/
commit_allowed: false
---

# Design One Course

## Preconditions

Before taking any action, apply `AGENTS.md` and complete its required reading order, including `MASTER_PROMPT.md`, `PROJECT-DECISIONS.yaml`, every root policy file, and this active prompt. Also read `curriculum/curriculum.yaml` and `curriculum/curriculum.lock.yaml` when present, inspect `git status` and relevant existing files, check for any more-specific `AGENTS.md` governing the write scope, and read the files needed to verify each precondition below.

1. Prompt 03 has generated the course shell and Prompt 04 has completed for this same course.
2. `research-report.md` exists and `course.yaml` status is `researching`. An
   explicitly owner-authorized acquisition-design revision may instead begin
   from `designed` or `in-production`; changes after release audits must use
   Prompt 15 so superseded audit evidence is invalidated.
3. Required sources for design are verified and no blocking research `TODO-VERIFY` remains.
4. Course identity matches the reconciled manifest and immutable lock metadata.

## Authorized actions

1. Define measurable learning outcomes.
2. Map assessments to outcomes.
3. Allocate exactly the credit-hour workload.
4. Design the 15-week sequence and final assessment.
5. Specify human-evaluation requirements in structured `course.yaml` metadata.
6. Apply stage calibration from `ACADEMIC-STANDARDS.md` and `QUALITY-ASSURANCE.md`; later-stage rigor must come from greater independence, primary-source engagement, methods, research, and evaluation rather than inflated lecture length.
7. For every PhD course, set `external_evaluator_required: true` and `human_evaluation.mandatory_external_signoff: true`. For MDiv preaching, pastoral, ministry/field-education, and designated language-performance work, require qualified human evaluation. When signoff is mandatory, reserve `human_evaluation.completion_record_path` for the eventual human-created record.
8. Identify which assessments require student-authored work and preserve the AI-use boundary explicitly.
9. Make the final acquisition decision for every student-required source. Use
   only the canonical designations in `SOURCE-POLICY.md`, reconcile every course
   `required_texts` entry with its verified source record, and ensure required
   Scripture uses a verified lawful `required-free` route at USD 0.
10. For every `required-purchase`, record `use_extent`, all instructional weeks
    of material use, and a concise `purchase_justification`. Never require a
    complete book for an `isolated-excerpt`.
11. Concentrate assigned reading in genuinely useful core books or anthologies
    instead of fragmenting purchases across incidental selections. Do not impose
    a numeric book cap when each purchase is independently justified, and do not
    reduce academic quality merely to eliminate cost.
12. Do not write lectures or full assignments.

## Forbidden actions

- Do not modify files outside the declared write scope.
- Do not invent unverified facts or sources.
- Do not begin a later prompt automatically.
- Do not treat AI grading or AI approval as required human evaluation.
- Do not commit unless the active prompt is explicitly overridden with owner authorization.

## Required validation

Run `python scripts/validate.py --mode draft` and the relevant tests. Add a provenance record.

## Exit criteria

- A new design advances from `researching` to `designed`; an authorized
  acquisition-design revision preserves `designed` or `in-production` as
  appropriate.
- Outcomes, assessment map, schedule, and workload are coherent.
- Every required text resolves to a matching verified source record, every
  required purchase has auditable substantial-use evidence, and required
  Scripture access costs USD 0.
- Human-evaluation metadata is explicit and stage-appropriate.
- PhD designs do not default to undergraduate-style lecture volume and identify qualified human oversight.
- No substantive weekly content was generated.
- The next production step is one approved week (`06`) or a more granular lecture/assignment/assessment prompt (`07`–`10`), subject to each prompt's preconditions.

Stop and report changed files, sources, validation, unresolved items, and required human review.
