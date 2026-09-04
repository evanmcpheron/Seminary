# Curriculum Production Workflow

## Phase 0 — Bootstrap

Create or verify governance, directories, templates, schemas, scripts, tests, and CI. Do not create course content.

## Phase 1 — Import and lock

Import the spreadsheet into YAML, record the source SHA-256 hash, and create a lock file. Report inconsistencies without silently correcting them.

## Phase 2 — Reconcile schedule

Move courses only when required by prerequisites or workload. Preserve every course. Record each move, old term, new term, rationale, and approval in `curriculum/schedule-overrides.yaml`.

## Phase 3 — Research one course

Verify textbooks, editions, articles, primary sources, media, and comparable academic course models. Produce a source audit before design.

## Phase 4 — Design one course

Define outcomes, assessment map, workload, calendar, bibliography, prerequisites, and human-evaluation requirements. No lecture production yet.

## Phase 5 — Generate shell

Create the course folder from templates and approved metadata. Do not create substantive weekly content.

## Phase 6 — Produce one week

Generate objectives, lectures, readings, study guide, discussion, assignment, and quiz for one week. Lectures come before dependent assignments.

## Phase 7 — Audit

Audit sources, theology, coherence, workload, outcome alignment, copyright, and student authorship boundaries.

## Phase 8 — Revise and release

Apply only approved findings, validate, record provenance, and tag a course version when authorized.
