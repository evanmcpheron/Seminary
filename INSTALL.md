# Install into `evanmcpheron/Seminary`

## Safe copy into an existing working tree

Unzip the archive outside the repository, inspect it, then copy without overwriting existing files:

```bash
unzip Seminary-bootstrap.zip
rsync -av --ignore-existing Seminary-bootstrap/ /path/to/Seminary/
cd /path/to/Seminary
```

Review conflicts manually rather than replacing existing work. Then install and verify:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
python scripts/bootstrap_repository.py --check
python scripts/validate.py --mode scaffold
pytest
```

Place the canonical spreadsheet at:

```text
curriculum/source/Theological_Education_Curriculum_Plan_2026-27_Swapped.xlsx
```

Then execute `prompts/02-import-and-lock-curriculum.md` through Codex. Do not generate course content before import and schedule reconciliation.
