# Seminary Prompt Execution Flow

This file is the operational guide for running the numbered prompts in `prompts/`. Prompt filenames match the normal startup dependency order.

After the repository bootstrap, curriculum setup and the per-course startup sequence proceed numerically:

```text
02 Import and lock curriculum
   ↓
02a Reconcile prerequisites and workload
   ↓
03 Generate shell
   ↓
04 Research course
   ↓
05 Design course
   ↓
06/07–10 Produce instructional units
   ↓
11–13 Audit
   ↓
15 Revise approved findings when needed
   ↓
19 Release
```

That order matches the lifecycle required by `courses/AGENTS.md`:

```text
shell → researching → designed → in-production → ready-for-audit → released
```

## 1. Rules that apply to every prompt

Before asking Codex or another agent to run any numbered prompt:

1. Start from the repository root.
2. Confirm the intended branch and inspect `git status`.
3. The agent must read `AGENTS.md`, `MASTER_PROMPT.md`, `PROJECT-DECISIONS.yaml`, all required root policy files, the active numbered prompt, and any more-specific `AGENTS.md` that governs the target path.
4. Run **one numbered prompt for one declared unit** unless the active prompt explicitly permits a broader shell/index/audit operation.
5. Name the target explicitly. Do not say only “run Prompt 03.”
6. Do not ask the agent to begin the next prompt automatically.
7. Every substantive run must create the required provenance record and run the validation/tests required by the active prompt.
8. `COMMIT_ALLOWED: false` means the agent must not create a commit unless the owner separately gives explicit authorization that overrides that restriction.
9. Never modify `curriculum/curriculum.lock.yaml` during course production. It is immutable identity metadata.
10. Use `curriculum/curriculum.yaml` for the **current reconciled placement** of a course. Approved schedule moves are reflected there and in `curriculum/schedule-overrides.yaml`.

A good invocation always identifies the prompt and target together. For example:

```text
Run prompts/03-generate-course-shell.md for PHIL 241 — Suffering only.
Resolve the canonical record_id and reconciled path from curriculum/curriculum.yaml.
Do not modify any other course. Stop after the prompt's validation and report.
```

## 2. What information must be supplied versus read from the repository

The owner does **not** need to repeat metadata that is already canonical in the repository. Codex should resolve existing facts from the manifests and course files.

### Usually required explicitly in the invocation

- The numbered prompt to run.
- The course code for course-scoped prompts.
- The week number for week-scoped prompts.
- The lecture, assignment, assessment, audit unit, semester, comprehensive field, or dissertation chapter when the prompt operates below or above course scope.
- Any human approval the prompt specifically requires and which is not already recorded in the repository.
- Any option that genuinely cannot be inferred from approved design files, such as an assessment mode/time limit if those were not already fixed.

### Usually resolved by Codex from repository files

- Canonical `record_id`.
- Course title.
- Credits.
- Catalog source institution.
- Catalog URL.
- Catalog description.
- Reconciled project year and term.
- Approved schedule overrides.
- Existing research, design, source records, week objectives, and workload budgets.
- Prior audit reports and their file paths.

If an explicitly required fact is missing from both the invocation and the repository, the agent must not invent it. It should record `TODO-VERIFY` where allowed or stop the blocked dependency as required by the active prompt.

## 3. Repository-wide setup flow

These prompts establish the project and are not repeated for every course.

### Prompt 00 — Master project constitution

**Role:** Governs every other prompt. It is a constitution, not a bulk-generation command.

**Required information:** None beyond the active task. It must be read for every run.

**Do not:** Treat Prompt 00 as authorization to generate an entire curriculum.

### Prompt 01 — Bootstrap repository

**Run when:** Creating or repairing the initial repository scaffold.

**Required information:** The repository root and owner-approved project decisions.

**Expected result:** Governance files, schemas, templates, scripts, directory structure, validation, and tests exist without generating substantive course content.

**Current repository:** This stage is already complete unless the scaffold is intentionally rebuilt.

### Prompt 02 — Import and lock curriculum

**Run when:** Importing a new owner-approved canonical spreadsheet or intentionally replacing the canonical curriculum source.

**Required information:** Exact path to the canonical `.xlsx`.

**Primary input:**

```text
curriculum/source/Theological_Education_Curriculum_Plan_2026-27_Swapped.xlsx
```

**Expected result:**

- `curriculum/curriculum.yaml`
- `curriculum/curriculum.lock.yaml`
- spreadsheet SHA-256 recorded
- import report
- validation/tests

**Do not:** Silently correct prerequisite or workload problems during import.

### Prompt 02a — Reconcile prerequisites and workload

**Run when:** After import, before course shells are created, or after an owner-approved curriculum change that requires a new reconciliation pass.

**Required information:** Owner approval for any schedule moves that will actually be applied.

**Expected result:**

- prerequisite verification
- workload analysis
- approved moves in `curriculum/schedule-overrides.yaml`
- reconciled placements in `curriculum/curriculum.yaml`
- reports documenting unresolved offering/availability questions

**Current repository:** The four approved undergraduate moves have been applied and the manifest status is `schedule-reconciled`.

## 4. Required per-course startup order: 03 → 04 → 05

This is the most important sequencing rule.

### Prompt 03 — Generate one course shell

**Run first for every new course.**

**Explicit invocation information:**

- Course code, for example `PHIL 241`.

Codex must resolve the canonical `record_id`, reconciled year, term, and destination path from `curriculum/curriculum.yaml`.

**Example:**

```text
Run prompts/03-generate-course-shell.md for PHIL 241 — Suffering only.
Resolve the canonical record_id and reconciled target path from curriculum/curriculum.yaml.
Generate only this shell. Do not start Prompt 04.
```

**Expected result:**

- one new course directory
- locked/reconciled identity metadata
- `course.yaml` with `status: shell`
- 15 empty week shells for a taught course
- no substantive teaching content
- provenance and validation

**Why Prompt 03 comes before Prompt 04:** Prompt 04 writes research artifacts into a course directory. Creating research files before shell generation would either require an ad hoc target path or create a directory conflict when the shell generator later runs.

### Prompt 04 — Research one course

**Run after Prompt 03 for the same course.**

**Explicit invocation information:**

- Course code.

**Repository preconditions:**

- The course exists in the reconciled manifest.
- The generated shell exists at the reconciled path.
- `course.yaml` identity matches the manifest/lock.
- Course status is `shell` or an authorized resumed `researching` state.

**Example:**

```text
Run prompts/04-research-one-course.md for PHIL 241 — Suffering only.
Use the existing shell created by Prompt 03 and the reconciled curriculum record.
Research and verify sources only; do not design the syllabus or weekly schedule.
Stop after validation and report the next permitted prompt.
```

**Expected result:**

- `research-report.md`
- verified course source records
- populated research resources
- verified prerequisites/corequisites where applicable
- research verification metadata
- `course.yaml` status becomes `researching`
- no syllabus design or lecture production

A required source that cannot be verified blocks dependent design when the prompt or source policy says it is required. Do not substitute invented bibliographic data.

### Prompt 05 — Design one course

**Run after Prompt 04 is complete and blocking research questions are resolved.**

**Explicit invocation information:**

- Course code.

**Repository preconditions:**

- Prompt 04 research report exists.
- Required design sources are verified.
- `course.yaml` status is `researching`.
- Identity metadata still agrees with the reconciled manifest and lock.

**Example:**

```text
Run prompts/05-design-one-course.md for PHIL 241 — Suffering only.
Use the completed Prompt 04 research and verified source records.
Design the course but do not write lectures, full assignments, or substantive week content.
```

**Expected result:**

- learning outcomes
- syllabus
- course schedule
- bibliography
- policies
- assessment/assignment maps
- exact course workload allocation
- human-evaluation requirements where applicable
- `course.yaml` status becomes `designed`

## 5. Semester coordination gate — Prompt 14

Prompt 14 is numbered later because it is an audit tool, but it is useful **after every course in a term has reached the designed stage and before large-scale week production begins**.

### Prompt 14 — Audit one semester

**Explicit invocation information:**

- Project year.
- Exact term ID, such as `term-01-fall`.

**Repository preconditions:** All course designs for that term exist.

**Example:**

```text
Run prompts/14-audit-semester.md for year-01-undergraduate-freshman / term-01-fall only.
Audit workload and assessment clustering across the designed courses.
Do not alter course identities or silently apply calendar changes.
```

**Use the result to:** Identify workload peaks, exam clustering, cross-course dependencies, and schedule recommendations before producing many weeks that would later require revision.

If the owner approves findings from Prompt 14, use Prompt 15 to apply only those approved changes.

## 6. Instructional production

After a course is designed and any required semester-level calendar adjustments are approved, produce content in small units.

### Prompt 06 — Generate one week

**Default production unit.**

**Explicit invocation information:**

- Course code.
- Week number.

**Repository preconditions:** The course design, week objectives, workload budget, and required sources are approved/verified.

**Example:**

```text
Run prompts/06-generate-one-week.md for PHIL 241, week 01 only.
Use the approved week objectives and workload from the course design.
Generate lectures before any assignment or graded assessment that depends on them.
```

Prompt 06 may produce all materials for **one week only**. It must still generate/source-audit lectures before dependent assignments or quizzes within that week. The first Prompt 06 production run advances the course from `designed` to `in-production`.

### Prompt 07 — Generate one lecture

Use this instead of, or within a more granular workflow than, Prompt 06 when a lecture should be produced and reviewed independently.

**Explicit invocation information:**

- Course code.
- Week number.
- Exact lecture identifier/file.

**Repository preconditions:** Approved course design, approved lecture outline, fixed objectives, verified sources. If Prompt 07 is the first substantive production action, it advances the course from `designed` to `in-production`.

### Prompt 08 — Generate one assignment and rubric

**Explicit invocation information:**

- Course code.
- Assignment identifier/title.

**Repository preconditions:** All lectures/readings the assignment depends on are complete, outcomes fixed, workload budgeted.

**Do not:** Generate a student submission. This prompt creates instructions, rubric, and grading guidance only.

### Prompt 09 — Generate one assessment

**Explicit invocation information:**

- Course code.
- Assessment identifier.
- Mode/time limit if not already fixed in the approved design.

**Repository preconditions:** Assessed material has already been taught and learning outcomes are fixed.

This prompt may create its own separate instructor answer key as part of the assessment package.

### Prompt 10 — Generate one answer key

Use when a finalized existing assessment needs a dedicated instructor key or when the assessment was created separately from Prompt 09.

**Explicit invocation information:**

- Course code.
- Exact finalized assessment to key.

**Repository preconditions:** Assessment, assigned sources, and lectures are final.

Do not run Prompt 10 redundantly if Prompt 09 already produced the required final key and no separate key pass is needed.

## 7. Audit and revision flow

For a completed course, use the audits in dependency order.

### Prompt 11 — Audit sources

**Explicit invocation information:** Target scope: course, week, lecture, assignment, or assessment.

**Expected result:** Every required source is verified or explicitly blocked; fabricated/inaccessible citations are surfaced. When Prompt 11 is run as the full-course audit after substantive production is complete and it passes, it advances the course from `in-production` to `ready-for-audit`. Unit-scoped source audits do not change course status.

### Prompt 12 — Audit theology and representation

**Explicit invocation information:** Exact content scope.

**Repository precondition:** Source audit is available.

**Expected result:** Confessional consistency and fair representation are evaluated without silently revising content.

### Prompt 13 — Audit course coherence

**Explicit invocation information:** Course code.

**Repository preconditions:** Course design and current content are available; source and theology audits exist.

**Expected result:** Prerequisite fit, progression, workload, outcomes, assignments, assessments, rubrics, answer keys, and human-review requirements are checked together. Findings are recommendations, not automatic edits.

### Prompt 15 — Revise approved audit findings

**Run only after owner approval.**

**Explicit invocation information:**

- Exact audit report.
- Exact approved finding numbers/descriptions.
- Exact files allowed to change.

**Example:**

```text
Run prompts/15-revise-after-audit.md for PHIL 241.
Apply only findings 2 and 4 from <audit-report-path>.
Allowed files: <file-1>, <file-2>.
Do not change any other finding or file.
```

Re-run the relevant audits after revision when required.

## 8. Course release — Prompt 19

**Explicit invocation information:** Course code/version target.

**Repository preconditions:**

- Source, theology, coherence, and copyright audits pass.
- `course.yaml` status is `ready-for-audit`.
- Required human review is complete.
- No blocking `TODO-VERIFY` remains.
- Release validation succeeds.

**Expected result:** Release metadata/changelog and course version/status update. Git tag or remote release actions still require separate explicit authorization.

## 9. Doctoral workflow

The doctoral prompts depend on actual program progress and human supervision rather than merely reaching a file-generation step.

### Prompt 16 — Build one comprehensive examination field

**Explicit invocation information:**

- Examination field.
- Human evaluator roles/identities as appropriate for the private workflow.

**Preconditions:** Doctoral coursework/languages substantially complete.

**Do not:** Generate student comprehensive answers.

### Prompt 17 — Build dissertation prospectus process

**Explicit invocation information:** The student's approved research direction/process scope.

**Preconditions:** Comprehensives complete, verified bibliography/research interests exist, human supervisor identified.

**Do not:** Write the student's prospectus prose.

### Prompt 18 — Support one dissertation chapter

**Explicit invocation information:** Exact chapter scope.

**Preconditions:** Prospectus approved and student-authored draft or research notes exist.

**Do:** Organize sources, audit citations, map arguments, identify gaps, and critique student-authored work.

**Do not:** Draft replacement dissertation prose.

## 10. Canonical spreadsheet and machine-readable curriculum data

The canonical workbook is:

```text
curriculum/source/Theological_Education_Curriculum_Plan_2026-27_Swapped.xlsx
```

### What has already been parsed into YAML

The repository importer reads the three inventory worksheets:

- `Wheaton Plan`
- `GCTS Plan`
- `Princeton Plan`

Those rows are represented in `curriculum/curriculum.yaml`, with immutable identity metadata mirrored in `curriculum/curriculum.lock.yaml`. The imported/reconciled data is sufficient for routine course startup and includes, as applicable:

- canonical record ID
- record type
- source worksheet/row
- institution
- source year/term
- reconciled planned year/term
- course code or published requirement label
- title
- credits or textual doctoral credit label
- requirement status
- catalog-based description
- selection rationale in the mutable manifest
- prerequisite/completion-condition note
- offering/accuracy note in the mutable manifest
- catalog URL

For Prompt 03, Prompt 04, and Prompt 05, Codex should normally use `curriculum/curriculum.yaml` plus the lock and reconciliation reports rather than reparsing the workbook for basic course identity.

### What has not been imported into the curriculum manifest

The current importer intentionally does **not** convert these supporting worksheets into structured manifest records:

- `Overview`
- `Wheaton Alternatives`
- `GCTS Alternatives`
- `Princeton Alternatives`
- `Wheaton Audit`
- `GCTS Audit`
- `Princeton Requirements`
- `Sources`

Those sheets contain useful supplemental information such as alternative elective choices, degree-audit summaries, requirement cross-checks, program-wide rationale/accuracy boundaries, and source lists.

Therefore:

- **Yes:** the workbook is parsed enough for Codex to instantiate and research/design the currently selected curriculum courses reliably.
- **No:** not every useful workbook worksheet has been normalized into machine-readable repository files.

If a later task needs an alternative course choice, institutional-style degree audit, or one of the workbook's program-level requirement/source summaries, the agent must either inspect the canonical workbook directly or use a future dedicated extraction step. Supplemental workbook sheets must never silently override `curriculum/curriculum.lock.yaml` or owner-approved reconciliation decisions.

## 11. Current starting point for this repository snapshot

The curriculum has already been imported and reconciled. The four approved undergraduate moves are applied, `curriculum/curriculum.yaml` is `schedule-reconciled`, and the course tree contains year/term scaffolding but no instantiated individual course directories yet.

For the **first course**, the next operational action is therefore:

```text
Prompt 03 for one explicitly named course
→ Prompt 04 for that same course
→ Prompt 05 for that same course
```

Do not start with Prompt 04 on a course that does not yet have its Prompt 03 shell.
