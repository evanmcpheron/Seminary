# Seminary

An independent, non-accredited theological education curriculum modeled on the course titles, descriptions, requirements, and academic progression found in the current Wheaton College, Gordon-Conwell Theological Seminary, and Princeton Theological Seminary catalogs.

This repository is **not** produced, approved, taught, accredited, or endorsed by those institutions. Institutional names are retained only as catalog-source metadata. Generated lectures, assignments, examinations, rubrics, and syllabi are original independent curriculum materials and must never be represented as official institutional materials.

## Intended outcome

The project is designed to approximate the rigor, sequence, workload, formative practices, and scholarly habits of a serious undergraduate-to-doctoral theological education while remaining honest about its independent and non-accredited status. Its constructive framework is broadly evangelical and Protestant, confessionally committed to historic Christianity, biblical inerrancy, and the 66-book Protestant canon.

## Program map

| Project years | Stage | Normal structure |
|---:|---|---|
| 1–4 | Undergraduate | Fall, spring, and selected summer redistribution |
| 5–7 | Master of Divinity | Fall, January, spring, and summer |
| 8–9 | PhD residence | Seminars, languages, colloquia, and research milestones |
| 10 | PhD examinations/proposal | Comprehensive examinations and dissertation proposal |
| 11–12 | PhD dissertation | Research milestones rather than artificial weekly lessons |

## Start here

1. Read [`INSTALL.md`](INSTALL.md) and [`START-HERE.md`](START-HERE.md).
2. Read [`AGENTS.md`](AGENTS.md) and [`MASTER_PROMPT.md`](MASTER_PROMPT.md).
3. Place the canonical curriculum spreadsheet in `curriculum/source/`.
4. Run the bootstrap and validation commands described below.
5. Import and lock the curriculum before creating any course content.
6. Follow [`PROMPT-FLOW.md`](PROMPT-FLOW.md) for the required execution order and per-prompt inputs.

```bash
python -m venv .venv
source .venv/bin/activate        # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
python scripts/bootstrap_repository.py --check
python scripts/validate.py --mode scaffold
pytest
```

After the canonical spreadsheet has been placed in `curriculum/source/`:

```bash
python scripts/import_curriculum.py \
  --input curriculum/source/Theological_Education_Curriculum_Plan_2026-27_Swapped.xlsx \
  --output curriculum/curriculum.yaml

python scripts/generate_course_shells.py --dry-run --all
python scripts/generate_course_shells.py --apply --course-id <record-id>
python scripts/validate.py --mode draft
```

## Non-negotiable production order

Prompt numbers are stable identifiers, not a strict numeric execution sequence. For a newly started course, the required per-course order is **05 → 03 → 04** so that the course lifecycle remains `shell` → `researching` → `designed`.

1. Import and lock curriculum metadata.
2. Reconcile prerequisites and workload without deleting courses.
3. Generate one course shell (`05`).
4. Research that course (`03`).
5. Design that course (`04`).
6. Produce one week at a time (`06`), or use the more granular `07`–`10` prompts when needed.
7. Generate lectures before dependent assignments.
8. Audit sources, theology, workload, and course coherence.
9. Revise only approved findings.
10. Release a version only after validation succeeds.

See [`PROMPT-FLOW.md`](PROMPT-FLOW.md) for invocation examples, required information, status transitions, semester-audit timing, and the role of the canonical spreadsheet versus the machine-readable curriculum manifests.

Semester-level **scaffolding and indexes** may be generated together. Full instructional content for an entire semester may not be generated in one undifferentiated pass.

## Canonical sources

- `curriculum/source/*.xlsx`: source spreadsheet supplied by the repository owner.
- `curriculum/curriculum.yaml`: imported machine-readable curriculum inventory.
- `curriculum/curriculum.lock.yaml`: hash-locked metadata snapshot.
- `PROJECT-DECISIONS.yaml`: owner-approved project decisions.
- `MASTER_PROMPT.md`: governing operating prompt.
- Root policy documents: binding standards for all generated content.

## Privacy

Private devotional journals, counseling information, pastoral confidences, and sensitive personal records must never be committed. Only completion records and appropriately redacted reflections belong in version control.
