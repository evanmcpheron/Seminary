from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import json
import re
from typing import Any

import yaml
from jsonschema import Draft202012Validator

from .common import load_yaml, sha256_file


@dataclass
class Report:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def validate_schema(instance: Any, schema_path: Path, label: str, report: Report) -> None:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    for error in sorted(validator.iter_errors(instance), key=lambda item: list(item.path)):
        location = ".".join(str(part) for part in error.path) or "<root>"
        report.error(f"{label}: schema error at {location}: {error.message}")


def validate_repository(root: Path, mode: str = "draft") -> Report:
    report = Report()
    required_root = [
        "README.md", "AGENTS.md", "MASTER_PROMPT.md", "PROJECT-DECISIONS.yaml",
        "DISCLAIMER.md", "THEOLOGICAL-COMMITMENTS.md", "ACADEMIC-STANDARDS.md",
        "SOURCE-POLICY.md", "WRITING-STYLE-GUIDE.md", "ASSESSMENT-POLICY.md",
        "AI-USE-POLICY.md", "curriculum/curriculum.yaml"
    ]
    for rel in required_root:
        if not (root / rel).exists():
            report.error(f"Missing required file: {rel}")

    curriculum_path = root / "curriculum/curriculum.yaml"
    curriculum: dict[str, Any] = {}
    if curriculum_path.exists():
        curriculum = load_yaml(curriculum_path) or {}
        validate_schema(curriculum, root / "schemas/curriculum.schema.json", str(curriculum_path), report)
        source = curriculum.get("source_spreadsheet", {})
        source_path_raw = source.get("path")
        source_hash = source.get("sha256")
        if source_path_raw:
            source_path = Path(source_path_raw)
            if not source_path.is_absolute():
                source_path = root / source_path
            if source_path.exists() and source_hash:
                current = sha256_file(source_path)
                if current != source_hash:
                    report.error("Canonical spreadsheet hash no longer matches curriculum.yaml")
            elif curriculum.get("status") != "awaiting-import" and not source_path.exists():
                report.error(f"Imported curriculum source is missing: {source_path}")
        if curriculum.get("status") == "awaiting-import":
            report.warn("Curriculum has not yet been imported from the canonical spreadsheet")

    manifest_courses = {
        record.get("record_id"): record
        for record in curriculum.get("records", [])
        if record.get("record_type") == "course"
    }
    seen_codes: dict[str, Path] = {}
    course_files = [p for p in (root / "courses").rglob("course.yaml") if "templates" not in p.parts]

    for course_file in course_files:
        data = load_yaml(course_file) or {}
        validate_schema(data, root / "schemas/course.schema.json", str(course_file), report)
        course_id = data.get("course_id")
        code = data.get("course_code")
        if code in seen_codes:
            report.error(f"Duplicate instantiated course code {code}: {seen_codes[code]} and {course_file}")
        elif code:
            seen_codes[code] = course_file

        if course_id not in manifest_courses:
            report.error(f"Course shell absent from canonical curriculum manifest: {course_id} ({course_file})")
        else:
            source = manifest_courses[course_id]
            comparisons = {
                "course_code": source.get("course_code"),
                "course_title": source.get("title"),
                "credit_hours": source.get("credits"),
                "catalog_url": source.get("catalog_url"),
            }
            for field_name, expected in comparisons.items():
                if expected is not None and data.get(field_name) != expected:
                    report.error(f"Locked metadata mismatch in {course_file}: {field_name}={data.get(field_name)!r}, expected {expected!r}")

        credits = data.get("credit_hours")
        total = data.get("estimated_total_hours")
        if isinstance(credits, (int, float)) and isinstance(total, (int, float)):
            expected_total = float(credits) * 45
            if abs(float(total) - expected_total) > max(2.0, expected_total * 0.05):
                report.error(f"Workload mismatch in {course_file}: {total} hours; expected about {expected_total}")

        status = data.get("status")
        text_files = list(course_file.parent.rglob("*.md")) + list(course_file.parent.rglob("*.yaml"))
        if status in {"ready-for-audit", "released"}:
            for path in text_files:
                text = path.read_text(encoding="utf-8", errors="replace")
                if "TODO-VERIFY" in text or "UNVERIFIED" in text.upper():
                    report.error(f"Unverified marker remains in {status} course: {path}")

        if status in {"designed", "in-production", "ready-for-audit", "released"}:
            expected_files = ["README.md", "syllabus.md", "schedule.md", "bibliography.md", "learning-outcomes.md", "policies.md"]
            for filename in expected_files:
                if not (course_file.parent / filename).exists():
                    report.error(f"Missing required course file {filename}: {course_file.parent}")

    # Source records
    for source_file in root.rglob("*.source.yaml"):
        data = load_yaml(source_file) or {}
        validate_schema(data, root / "schemas/source.schema.json", str(source_file), report)
        if data.get("verification_status") != "verified":
            report.error(f"Source record is not verified: {source_file}")

    # Provenance records
    for prov_file in (root / "provenance").glob("*.yaml"):
        data = load_yaml(prov_file) or {}
        validate_schema(data, root / "schemas/provenance.schema.json", str(prov_file), report)

    # Misrepresentation check in generated course tree only.
    forbidden_patterns = [
        re.compile(r"official\s+(wheaton|gordon[- ]conwell|princeton)\s+(syllabus|course)", re.I),
        re.compile(r"accredited\s+by\s+(wheaton|gordon[- ]conwell|princeton)", re.I),
    ]
    for path in (root / "courses").rglob("*.md"):
        text = path.read_text(encoding="utf-8", errors="replace")
        for pattern in forbidden_patterns:
            if pattern.search(text):
                report.error(f"Institutional misrepresentation language in {path}")

    if mode == "release":
        if curriculum.get("status") not in {"schedule-reconciled", "locked"}:
            report.error("Release validation requires a reconciled or locked curriculum")
        if not course_files:
            report.error("Release validation found no instantiated courses")

    return report
