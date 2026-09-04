.PHONY: setup bootstrap check import shells validate release-check test

setup:
	python -m pip install -e '.[dev]'

bootstrap:
	python scripts/bootstrap_repository.py --apply

check:
	python scripts/bootstrap_repository.py --check

import:
	python scripts/import_curriculum.py --input curriculum/source/Theological_Education_Curriculum_Plan_2026-27_Swapped.xlsx --output curriculum/curriculum.yaml

shells:
	python scripts/generate_course_shells.py --apply --course-id $(COURSE_ID)

validate:
	python scripts/validate.py --mode draft

release-check:
	python scripts/validate.py --mode release

test:
	pytest
