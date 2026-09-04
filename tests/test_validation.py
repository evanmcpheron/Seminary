from pathlib import Path

from seminary_tools.validation import validate_repository


def test_scaffold_validation_passes():
    root = Path(__file__).resolve().parents[1]
    report = validate_repository(root, mode="scaffold")
    assert report.errors == []
