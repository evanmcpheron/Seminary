from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
import hashlib
import json
import re
from typing import Any

from jsonschema import Draft202012Validator

from .common import load_yaml, sha256_file


RELEASE_AUDIT_FILENAMES = {
    "source-copyright": "source-copyright.audit.yaml",
    "theology-fairness": "theology-fairness.audit.yaml",
    "course-coherence": "course-coherence.audit.yaml",
}
PASSING_AUDIT_VERDICTS = {"pass", "pass-with-nonblocking-findings"}
PASSING_HUMAN_REVIEW_DECISIONS = {"pass", "pass-with-revisions"}
FAST_AGING_SOURCE_TYPES = {"catalog", "website", "video", "podcast"}
FAST_AGING_SOURCE_DAYS = 180
STABLE_SOURCE_DAYS = 730


NON_SUBSTANTIVE_COURSE_METADATA_KEYS = {
    "status",
    "last_content_audit_date",
    "curriculum_version",
    "release_metadata",
}
EXCLUDED_FINGERPRINT_DIRECTORIES = {"audits", "versions", "human-review", "release"}
EXCLUDED_FINGERPRINT_FILENAMES = {"CHANGELOG.md", "changelog.md"}


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


def parse_record_date(value: Any) -> date | None:
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        try:
            return date.fromisoformat(value)
        except ValueError:
            return None
    return None


def source_age_limit_days(source_type: str | None) -> int:
    return FAST_AGING_SOURCE_DAYS if source_type in FAST_AGING_SOURCE_TYPES else STABLE_SOURCE_DAYS


def course_requires_human_signoff(course: dict[str, Any]) -> bool:
    human_evaluation = course.get("human_evaluation") or {}
    return bool(
        course.get("academic_stage") == "phd"
        or course.get("external_evaluator_required") is True
        or human_evaluation.get("mandatory_external_signoff") is True
    )


def course_content_fingerprint(course_dir: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted((item for item in course_dir.rglob("*") if item.is_file()), key=lambda item: item.as_posix()):
        relative_path = path.relative_to(course_dir)
        if relative_path.parts and relative_path.parts[0] in EXCLUDED_FINGERPRINT_DIRECTORIES:
            continue
        if relative_path.name in EXCLUDED_FINGERPRINT_FILENAMES:
            continue

        digest.update(relative_path.as_posix().encode("utf-8"))
        digest.update(b"\0")
        if relative_path.as_posix() == "course.yaml":
            course_data = load_yaml(path) or {}
            normalized = dict(course_data)
            for key in NON_SUBSTANTIVE_COURSE_METADATA_KEYS:
                normalized.pop(key, None)
            human_evaluation = normalized.get("human_evaluation")
            if isinstance(human_evaluation, dict):
                normalized_human_evaluation = dict(human_evaluation)
                normalized_human_evaluation.pop("completion_record_path", None)
                normalized["human_evaluation"] = normalized_human_evaluation
            payload = json.dumps(normalized, sort_keys=True, separators=(",", ":"), default=str).encode("utf-8")
        else:
            payload = path.read_bytes()
        digest.update(payload)
        digest.update(b"\0")
    return digest.hexdigest()


def resolve_repository_path(root: Path, raw_path: Any, label: str, report: Report) -> Path | None:
    if not isinstance(raw_path, str) or not raw_path.strip():
        report.error(f"{label}: expected a non-empty repository-relative path")
        return None
    candidate = Path(raw_path)
    if candidate.is_absolute():
        report.error(f"{label}: absolute paths are not permitted: {raw_path}")
        return None
    root_resolved = root.resolve()
    resolved = (root / candidate).resolve()
    if resolved != root_resolved and root_resolved not in resolved.parents:
        report.error(f"{label}: path escapes repository root: {raw_path}")
        return None
    return resolved


def audit_manifest_passes(data: dict[str, Any]) -> bool:
    return data.get("verdict") in PASSING_AUDIT_VERDICTS and not data.get("blocking_findings")


def validate_audit_evidence(
    root: Path,
    audit_file: Path,
    data: dict[str, Any],
    report: Report,
    provenance_by_run_id: dict[str, Path],
    *,
    require_provenance: bool,
) -> None:
    report_path = resolve_repository_path(root, data.get("report_path"), f"{audit_file}: report_path", report)
    if report_path is not None and not report_path.is_file():
        report.error(f"{audit_file}: audit report does not exist: {data.get('report_path')}")

    audit_run_id = data.get("audit_run_id")
    generation_run_ids = data.get("generation_run_ids") or []
    if audit_run_id in generation_run_ids:
        report.error(f"{audit_file}: audit_run_id cannot also be a generation_run_id")

    if require_provenance:
        if audit_run_id not in provenance_by_run_id:
            report.error(f"{audit_file}: audit_run_id has no matching provenance record: {audit_run_id}")
        for run_id in generation_run_ids:
            if run_id not in provenance_by_run_id:
                report.error(f"{audit_file}: generation_run_id has no matching provenance record: {run_id}")


def validate_required_course_audits(
    root: Path,
    course_file: Path,
    course: dict[str, Any],
    report: Report,
    provenance_by_run_id: dict[str, Path],
    *,
    require_provenance: bool,
) -> None:
    course_id = course.get("course_id")
    expected_fingerprint = course_content_fingerprint(course_file.parent)
    manifests: dict[str, dict[str, Any]] = {}
    for audit_type, filename in RELEASE_AUDIT_FILENAMES.items():
        audit_file = course_file.parent / "audits" / filename
        if not audit_file.is_file():
            report.error(f"Missing required {audit_type} release audit: {audit_file}")
            continue
        data = load_yaml(audit_file) or {}
        validate_schema(data, root / "schemas/audit.schema.json", str(audit_file), report)
        manifests[audit_type] = data
        if data.get("audit_type") != audit_type:
            report.error(f"{audit_file}: audit_type={data.get('audit_type')!r}, expected {audit_type!r}")
        if (data.get("scope") or {}).get("course_id") != course_id:
            report.error(f"{audit_file}: scope.course_id does not match {course_id}")
        if data.get("content_fingerprint") != expected_fingerprint:
            report.error(
                f"{audit_file}: content_fingerprint does not match current release-scoped course content; "
                "rerun the affected independent audit(s)"
            )
        if not audit_manifest_passes(data):
            report.error(f"{audit_file}: release audit is not passing")
        validate_audit_evidence(
            root,
            audit_file,
            data,
            report,
            provenance_by_run_id,
            require_provenance=require_provenance,
        )

    audit_run_ids = [manifest.get("audit_run_id") for manifest in manifests.values() if manifest.get("audit_run_id")]
    if len(audit_run_ids) != len(set(audit_run_ids)):
        report.error(f"{course_file.parent / 'audits'}: release audits must use distinct audit_run_id values")

    coherence = manifests.get("course-coherence") or {}
    dependencies = set(coherence.get("depends_on_audits") or [])
    required_dependencies = {"source-copyright", "theology-fairness"}
    if coherence and not required_dependencies.issubset(dependencies):
        missing = sorted(required_dependencies - dependencies)
        report.error(f"{course_file.parent / 'audits/course-coherence.audit.yaml'}: missing audit dependencies {missing}")


def validate_human_review_record(
    root: Path,
    review_path: Path,
    report: Report,
    *,
    expected_course_id: str | None = None,
    expected_milestone_id: str | None = None,
) -> None:
    review = load_yaml(review_path) or {}
    validate_schema(review, root / "schemas/human-review.schema.json", str(review_path), report)
    scope = review.get("scope") or {}
    if expected_course_id is not None and scope.get("course_id") != expected_course_id:
        report.error(f"{review_path}: scope.course_id does not match {expected_course_id}")
    if expected_milestone_id is not None and scope.get("milestone_id") != expected_milestone_id:
        report.error(f"{review_path}: scope.milestone_id does not match {expected_milestone_id}")
    if review.get("decision") not in PASSING_HUMAN_REVIEW_DECISIONS:
        report.error(f"{review_path}: required human review does not record a passing decision")
    if review.get("attested_by_human") is not True or review.get("ai_generated_evaluation") is not False:
        report.error(f"{review_path}: required evaluation must be human-attested and not AI-generated")


def validate_required_human_review(root: Path, course_file: Path, course: dict[str, Any], report: Report) -> None:
    if not course_requires_human_signoff(course):
        return

    human_evaluation = course.get("human_evaluation") or {}
    if course.get("academic_stage") == "phd" and human_evaluation.get("mandatory_external_signoff") is not True:
        report.error(f"{course_file}: PhD release requires human_evaluation.mandatory_external_signoff=true")

    review_path = resolve_repository_path(
        root,
        human_evaluation.get("completion_record_path"),
        f"{course_file}: human_evaluation.completion_record_path",
        report,
    )
    if review_path is None:
        return
    if not review_path.is_file():
        report.error(f"{course_file}: required human review record does not exist: {review_path}")
        return

    validate_human_review_record(
        root,
        review_path,
        report,
        expected_course_id=course.get("course_id"),
    )


def validate_milestone_completion(root: Path, milestone_file: Path, milestone: dict[str, Any], report: Report) -> None:
    if milestone.get("status") != "complete":
        return
    review_path = resolve_repository_path(
        root,
        milestone.get("human_review_record_path"),
        f"{milestone_file}: human_review_record_path",
        report,
    )
    if review_path is None:
        return
    if not review_path.is_file():
        report.error(f"{milestone_file}: completed milestone lacks its required human review record: {review_path}")
        return
    validate_human_review_record(
        root,
        review_path,
        report,
        expected_milestone_id=milestone.get("milestone_id"),
    )


def validate_prior_year_progression(
    root: Path,
    course_file: Path,
    course: dict[str, Any],
    report: Report,
    provenance_by_run_id: dict[str, Path],
    *,
    require_provenance: bool,
) -> None:
    program_year = course.get("program_year")
    if not isinstance(program_year, int) or program_year <= 1:
        return

    previous_year = program_year - 1
    audit_file = root / "quality" / "longitudinal" / f"year-{previous_year:02d}.audit.yaml"
    if not audit_file.is_file():
        report.error(f"{course_file}: previous-year longitudinal audit is missing: {audit_file}")
        return

    data = load_yaml(audit_file) or {}
    validate_schema(data, root / "schemas/audit.schema.json", str(audit_file), report)
    if data.get("audit_type") != "longitudinal-progression":
        report.error(f"{audit_file}: expected audit_type 'longitudinal-progression'")
    if (data.get("scope") or {}).get("program_year") != previous_year:
        report.error(f"{audit_file}: scope.program_year must be {previous_year}")
    if not audit_manifest_passes(data):
        report.error(f"{audit_file}: previous-year longitudinal progression audit is not passing")
    validate_audit_evidence(
        root,
        audit_file,
        data,
        report,
        provenance_by_run_id,
        require_provenance=require_provenance,
    )


def validate_release_source_freshness(
    course_file: Path,
    course: dict[str, Any],
    source_records_by_id: dict[str, list[tuple[dict[str, Any], Path]]],
    report: Report,
) -> None:
    required_source_ids = {
        item.get("source_id")
        for item in course.get("required_texts", [])
        if isinstance(item, dict) and item.get("source_id")
    }

    local_source_records: dict[str, tuple[dict[str, Any], Path]] = {}
    for local_source_file in course_file.parent.rglob("*.source.yaml"):
        local_source = load_yaml(local_source_file) or {}
        local_source_id = local_source.get("source_id")
        if local_source_id:
            required_source_ids.add(local_source_id)
            local_source_records[local_source_id] = (local_source, local_source_file)

    today = date.today()
    for source_id in sorted(required_source_ids):
        record_entry = local_source_records.get(source_id)
        if record_entry is None:
            candidates = source_records_by_id.get(source_id) or []
            if len(candidates) == 1:
                record_entry = candidates[0]
            elif len(candidates) > 1:
                report.error(f"{course_file}: required source_id is ambiguous across source records: {source_id}")
                continue
        if record_entry is None:
            report.error(f"{course_file}: required source has no source record: {source_id}")
            continue
        source, source_file = record_entry
        accessed_at = parse_record_date(source.get("accessed_at"))
        if accessed_at is None:
            report.error(f"{source_file}: accessed_at is missing or is not an ISO date")
            continue
        age_days = (today - accessed_at).days
        if age_days < 0:
            report.error(f"{source_file}: accessed_at is in the future: {accessed_at.isoformat()}")
            continue
        limit = source_age_limit_days(source.get("source_type"))
        if age_days > limit:
            report.error(
                f"{source_file}: release-critical source verification is stale "
                f"({age_days} days old; limit {limit} days)"
            )


def validate_repository(root: Path, mode: str = "draft") -> Report:
    report = Report()
    required_root = [
        "README.md", "AGENTS.md", "MASTER_PROMPT.md", "PROJECT-DECISIONS.yaml",
        "DISCLAIMER.md", "THEOLOGICAL-COMMITMENTS.md", "ACADEMIC-STANDARDS.md",
        "SOURCE-POLICY.md", "WRITING-STYLE-GUIDE.md", "ASSESSMENT-POLICY.md",
        "AI-USE-POLICY.md", "QUALITY-ASSURANCE.md", "curriculum/curriculum.yaml",
        "schemas/audit.schema.json", "schemas/human-review.schema.json",
        "schemas/milestone.schema.json"
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

    provenance_by_run_id: dict[str, Path] = {}
    for prov_file in (root / "provenance").glob("*.yaml"):
        data = load_yaml(prov_file) or {}
        validate_schema(data, root / "schemas/provenance.schema.json", str(prov_file), report)
        run_id = data.get("run_id")
        if run_id:
            if run_id in provenance_by_run_id:
                report.error(f"Duplicate provenance run_id {run_id}: {provenance_by_run_id[run_id]} and {prov_file}")
            else:
                provenance_by_run_id[run_id] = prov_file

    source_records_by_id: dict[str, list[tuple[dict[str, Any], Path]]] = {}
    for source_file in root.rglob("*.source.yaml"):
        data = load_yaml(source_file) or {}
        validate_schema(data, root / "schemas/source.schema.json", str(source_file), report)
        source_id = data.get("source_id")
        if source_id:
            source_records_by_id.setdefault(source_id, []).append((data, source_file))
        if data.get("verification_status") != "verified":
            report.error(f"Source record is not verified: {source_file}")

    for audit_file in root.rglob("*.audit.yaml"):
        data = load_yaml(audit_file) or {}
        validate_schema(data, root / "schemas/audit.schema.json", str(audit_file), report)

    for review_file in root.rglob("*.human-review.yaml"):
        data = load_yaml(review_file) or {}
        validate_schema(data, root / "schemas/human-review.schema.json", str(review_file), report)

    for milestone_file in root.rglob("*.milestone.yaml"):
        data = load_yaml(milestone_file) or {}
        validate_schema(data, root / "schemas/milestone.schema.json", str(milestone_file), report)
        validate_milestone_completion(root, milestone_file, data, report)

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

            validate_required_course_audits(
                root,
                course_file,
                data,
                report,
                provenance_by_run_id,
                require_provenance=(mode == "release" or status == "released"),
            )

        if status in {"designed", "in-production", "ready-for-audit", "released"}:
            expected_files = ["README.md", "syllabus.md", "schedule.md", "bibliography.md", "learning-outcomes.md", "policies.md"]
            for filename in expected_files:
                if not (course_file.parent / filename).exists():
                    report.error(f"Missing required course file {filename}: {course_file.parent}")

        release_candidate = mode == "release" and status == "ready-for-audit"
        if release_candidate:
            validate_release_source_freshness(course_file, data, source_records_by_id, report)
            validate_required_human_review(root, course_file, data, report)
            validate_prior_year_progression(
                root,
                course_file,
                data,
                report,
                provenance_by_run_id,
                require_provenance=True,
            )
        elif status == "released":
            validate_required_human_review(root, course_file, data, report)
            validate_prior_year_progression(
                root,
                course_file,
                data,
                report,
                provenance_by_run_id,
                require_provenance=True,
            )

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
