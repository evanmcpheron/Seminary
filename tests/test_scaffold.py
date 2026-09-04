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


def test_course_startup_prompt_filenames_match_purposes():
    expected = {
        "03-generate-course-shell.md": {
            "prompt_id": "03-generate-course-shell",
            "purpose": "Generate One Course Shell",
        },
        "04-research-one-course.md": {
            "prompt_id": "04-research-one-course",
            "purpose": "Research One Course",
        },
        "05-design-one-course.md": {
            "prompt_id": "05-design-one-course",
            "purpose": "Design One Course",
        },
    }
    actual = {}
    for path in (ROOT / "prompts").glob("0[3-5]-*.md"):
        _, front_matter, _ = path.read_text(encoding="utf-8").split("---", 2)
        metadata = yaml.safe_load(front_matter)
        actual[path.name] = {
            "prompt_id": metadata["prompt_id"],
            "purpose": metadata["purpose"],
        }

    assert actual == expected


def test_twelve_year_directories_exist():
    years = [p for p in (ROOT / "courses").iterdir() if p.is_dir() and p.name.startswith("year-")]
    assert len(years) == 12
