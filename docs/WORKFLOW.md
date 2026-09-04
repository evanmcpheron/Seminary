# Curriculum Production Workflow

## Phase 0 — Bootstrap

Create or verify governance, directories, templates, schemas, scripts, tests, and CI. Do not create course content.

## Phase 1 — Import and lock

Import the spreadsheet into YAML, record the source SHA-256 hash, and create a lock file. Report inconsistencies without silently correcting them.

## Phase 2 — Reconcile schedule

Move courses only when required by prerequisites or workload. Preserve every course. Record each move, old term, new term, rationale, and approval in `curriculum/schedule-overrides.yaml`.

## Phase 3 — Generate one course shell (`05`)

Create the course folder from templates and reconciled curriculum metadata. The generated `course.yaml` begins with status `shell`. Do not create substantive weekly content.

## Phase 4 — Research one course (`03`)

Work inside the generated shell. Verify textbooks, editions, articles, primary sources, media, prerequisites, and comparable academic course models. Produce `research-report.md`, verified source records, and research-state metadata before design. The course advances to `researching`.

## Phase 5 — Design one course (`04`)

Using the completed research pass, define outcomes, assessment map, workload, calendar, bibliography, prerequisites, and human-evaluation requirements. No lecture production yet. The course advances to `designed`.

## Phase 6 — Produce one week

Generate objectives, lectures, readings, study guide, discussion, assignment, and quiz for one week. Lectures come before dependent assignments. The first substantive production run advances the course from `designed` to `in-production`.

## Phase 7 — Audit

When substantive production is complete, run a full-course source audit as the lifecycle gate to `ready-for-audit`, then audit theology, coherence, workload, outcome alignment, copyright, and student authorship boundaries.

## Phase 8 — Revise and release

Apply only approved findings, validate, record provenance, and tag a course version when authorized.
