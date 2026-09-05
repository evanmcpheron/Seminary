from pathlib import Path

from seminary_tools.validation import (
    Report,
    audit_manifest_passes,
    course_content_fingerprint,
    course_requires_human_signoff,
    source_age_limit_days,
    validate_milestone_completion,
    validate_prior_year_progression,
    validate_course_resource_acquisition,
    validate_repository,
    validate_required_course_audits,
    validate_source_acquisition,
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


def source_index(tmp_path, source):
    source_file = tmp_path / "courses" / "example" / "resources" / "source-records" / "source.source.yaml"
    return {source["source_id"]: [(source, source_file)]}


def validate_required_text(tmp_path, item, source):
    course_file = tmp_path / "courses" / "example" / "course.yaml"
    report = Report()
    validate_course_resource_acquisition(
        course_file,
        {
            "course_id": "example",
            "instructional_weeks": 14,
            "required_texts": [item],
        },
        source_index(tmp_path, source),
        report,
    )
    return report


def test_scripture_cannot_be_required_purchase(tmp_path):
    report = Report()
    validate_source_acquisition(
        tmp_path / "bible.source.yaml",
        {
            "source_type": "scripture",
            "access_category": "required-purchase",
            "required_cost_usd": 0,
        },
        report,
    )

    assert any("Scripture cannot be classified as required-purchase" in error for error in report.errors)


def test_verified_required_free_scripture_passes(tmp_path):
    source = {
        "source_id": "bible",
        "course_id": "example",
        "source_type": "scripture",
        "verification_status": "verified",
        "access_category": "required-free",
        "free_access_url": "https://example.test/read",
        "required_cost_usd": 0,
    }
    source_report = Report()
    validate_source_acquisition(tmp_path / "bible.source.yaml", source, source_report)
    course_report = validate_required_text(
        tmp_path,
        {"source_id": "bible", "designation": "required-free"},
        source,
    )

    assert source_report.errors == []
    assert course_report.errors == []


def test_required_purchase_without_justification_fails(tmp_path):
    source = {
        "source_id": "core-book",
        "course_id": "example",
        "source_type": "book",
        "verification_status": "verified",
        "access_category": "required-purchase",
    }
    report = validate_required_text(
        tmp_path,
        {
            "source_id": "core-book",
            "designation": "required-purchase",
            "use_extent": "whole-work",
            "instructional_weeks": [1, 2, 3],
        },
        source,
    )

    assert any("lacks purchase_justification" in error for error in report.errors)


def test_required_purchase_cannot_be_an_isolated_excerpt(tmp_path):
    source = {
        "source_id": "excerpt-book",
        "course_id": "example",
        "source_type": "book",
        "verification_status": "verified",
        "access_category": "required-purchase",
    }
    report = validate_required_text(
        tmp_path,
        {
            "source_id": "excerpt-book",
            "designation": "required-purchase",
            "use_extent": "isolated-excerpt",
            "instructional_weeks": [4],
            "purchase_justification": "One assigned excerpt.",
        },
        source,
    )

    assert any("cannot use use_extent 'isolated-excerpt'" in error for error in report.errors)


def test_justified_core_text_purchase_passes(tmp_path):
    source = {
        "source_id": "core-book",
        "course_id": "example",
        "source_type": "book",
        "verification_status": "verified",
        "access_category": "required-purchase",
    }
    report = validate_required_text(
        tmp_path,
        {
            "source_id": "core-book",
            "designation": "required-purchase",
            "use_extent": "substantial-portion",
            "instructional_weeks": [1, 3, 5, 7],
            "purchase_justification": "The book anchors four cumulative units and the final synthesis.",
        },
        source,
    )

    assert report.errors == []


def test_required_text_designation_mismatch_fails(tmp_path):
    source = {
        "source_id": "free-entry",
        "course_id": "example",
        "source_type": "reference-work",
        "verification_status": "verified",
        "access_category": "recommended",
    }
    report = validate_required_text(
        tmp_path,
        {"source_id": "free-entry", "designation": "required-free"},
        source,
    )

    assert any("conflicts with source record access_category" in error for error in report.errors)


def test_noncanonical_required_text_designation_fails(tmp_path):
    source = {
        "source_id": "media",
        "course_id": "example",
        "source_type": "video",
        "verification_status": "verified",
        "access_category": "required-free",
    }
    report = validate_required_text(
        tmp_path,
        {"source_id": "media", "designation": "required-free-media"},
        source,
    )

    assert any("noncanonical designation" in error for error in report.errors)


def test_unresolved_required_text_source_id_fails(tmp_path):
    course_file = tmp_path / "courses" / "example" / "course.yaml"
    report = Report()
    validate_course_resource_acquisition(
        course_file,
        {
            "course_id": "example",
            "instructional_weeks": 14,
            "required_texts": [{"source_id": "missing", "designation": "required-free"}],
        },
        {},
        report,
    )

    assert any("cannot be resolved to a source record" in error for error in report.errors)


def test_required_source_record_must_appear_in_course_metadata(tmp_path):
    source = {
        "source_id": "omitted-required-source",
        "course_id": "example",
        "source_type": "reference-work",
        "verification_status": "verified",
        "access_category": "required-free",
        "free_access_url": "https://example.test/free",
        "required_cost_usd": 0,
    }
    course_file = tmp_path / "courses" / "example" / "course.yaml"
    report = Report()
    validate_course_resource_acquisition(
        course_file,
        {"course_id": "example", "instructional_weeks": 14, "required_texts": []},
        source_index(tmp_path, source),
        report,
    )

    assert any("is missing from course required_texts" in error for error in report.errors)
