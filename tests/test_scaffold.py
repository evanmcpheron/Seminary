from pathlib import Path
import json

import yaml

ROOT = Path(__file__).resolve().parents[1]


def test_required_governance_files_exist():
    for rel in [
        "README.md", "AGENTS.md", "MASTER_PROMPT.md", "PROJECT-DECISIONS.yaml",
        "DISCLAIMER.md", "THEOLOGICAL-COMMITMENTS.md", "ACADEMIC-STANDARDS.md",
        "SOURCE-POLICY.md", "WRITING-STYLE-GUIDE.md", "ASSESSMENT-POLICY.md",
        "AI-USE-POLICY.md"
    ]:
        assert (ROOT / rel).is_file(), rel


def test_schemas_are_valid_json():
    for path in (ROOT / "schemas").glob("*.json"):
        json.loads(path.read_text(encoding="utf-8"))


def test_yaml_governance_loads():
    for rel in ["PROJECT-DECISIONS.yaml", "curriculum/curriculum.yaml", "curriculum/prerequisites.yaml", "curriculum/schedule-overrides.yaml"]:
        with (ROOT / rel).open(encoding="utf-8") as handle:
            assert yaml.safe_load(handle) is not None


def test_twelve_year_directories_exist():
    years = [p for p in (ROOT / "courses").iterdir() if p.is_dir() and p.name.startswith("year-")]
    assert len(years) == 12
