from pathlib import Path

from seminary_tools.validation import (
    Report,
    audit_manifest_passes,
    course_content_fingerprint,
    course_requires_human_signoff,
    source_age_limit_days,
    validate_milestone_completion,
    validate_prior_year_progression,
    validate_repository,
    validate_required_course_audits,
)


def test_scaffold_validation_passes():
    root = Path(__file__).resolve().parents[1]
    report = validate_repository(root, mode="scaffold")
    assert report.errors == []


def test_source_freshness_limits_distinguish_dynamic_and_stable_sources():
    assert source_age_limit_days("website") == 180
    assert source_age_limit_days("catalog") == 180
    assert source_age_limit_days("book") == 730
    assert source_age_limit_days("article") == 730


def test_phd_course_always_requires_human_signoff():
    course = {
        "academic_stage": "phd",
        "external_evaluator_required": False,
        "human_evaluation": {"mandatory_external_signoff": False},
    }
    assert course_requires_human_signoff(course) is True


def test_blocking_findings_prevent_passing_audit():
    assert audit_manifest_passes({"verdict": "pass", "blocking_findings": []}) is True
    assert audit_manifest_passes({"verdict": "pass", "blocking_findings": ["unresolved"]}) is False
    assert audit_manifest_passes({"verdict": "fail", "blocking_findings": []}) is False


def test_ready_course_requires_all_three_release_audits(tmp_path):
    course_file = tmp_path / "courses" / "example" / "course.yaml"
    course_file.parent.mkdir(parents=True)
    course_file.write_text("course_id: example\n", encoding="utf-8")
    report = Report()

    validate_required_course_audits(
        tmp_path,
        course_file,
        {"course_id": "example"},
        report,
        provenance_by_run_id={},
        require_provenance=False,
    )

    assert sum("Missing required" in error and "release audit" in error for error in report.errors) == 3


def test_year_two_release_requires_year_one_longitudinal_audit(tmp_path):
    course_file = tmp_path / "courses" / "example" / "course.yaml"
    course_file.parent.mkdir(parents=True)
    course_file.write_text("course_id: example\n", encoding="utf-8")
    report = Report()

    validate_prior_year_progression(
        tmp_path,
        course_file,
        {"course_id": "example", "program_year": 2},
        report,
        provenance_by_run_id={},
        require_provenance=False,
    )

    assert any("previous-year longitudinal audit is missing" in error for error in report.errors)


def test_course_fingerprint_ignores_lifecycle_only_changes_but_detects_content_changes(tmp_path):
    course_dir = tmp_path / "course"
    course_dir.mkdir()
    course_file = course_dir / "course.yaml"
    course_file.write_text(
        "course_id: example\nstatus: in-production\ncurriculum_version: 0.1.0\n",
        encoding="utf-8",
    )
    lecture = course_dir / "lecture.md"
    lecture.write_text("Original content\n", encoding="utf-8")

    original = course_content_fingerprint(course_dir)
    course_file.write_text(
        "course_id: example\nstatus: ready-for-audit\ncurriculum_version: 0.2.0\n",
        encoding="utf-8",
    )
    lifecycle_only = course_content_fingerprint(course_dir)
    lecture.write_text("Changed content\n", encoding="utf-8")
    substantive_change = course_content_fingerprint(course_dir)

    assert lifecycle_only == original
    assert substantive_change != original


def test_completed_milestone_requires_human_review_record(tmp_path):
    milestone_file = tmp_path / "doctoral" / "field.milestone.yaml"
    milestone_file.parent.mkdir(parents=True)
    milestone_file.write_text("milestone_id: field-1\n", encoding="utf-8")
    report = Report()

    validate_milestone_completion(
        tmp_path,
        milestone_file,
        {
            "milestone_id": "field-1",
            "status": "complete",
            "human_review_record_path": None,
        },
        report,
    )

    assert any("human_review_record_path" in error for error in report.errors)
