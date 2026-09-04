#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import sys

_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from seminary_tools.common import copy_tree_without_overwrite, dump_yaml, load_yaml, replace_placeholders

YEAR_DIRECTORIES = {
    1: "year-01-undergraduate-freshman", 2: "year-02-undergraduate-sophomore",
    3: "year-03-undergraduate-junior", 4: "year-04-undergraduate-senior",
    5: "year-05-mdiv-01", 6: "year-06-mdiv-02", 7: "year-07-mdiv-03",
    8: "year-08-phd-01", 9: "year-09-phd-02", 10: "year-10-phd-03",
    11: "year-11-phd-04", 12: "year-12-phd-05",
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate non-substantive course shells from locked curriculum metadata")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--apply", action="store_true")
    parser.add_argument("--course-id", action="append", default=[], help="Generate only this canonical record_id; may be repeated")
    parser.add_argument("--all", action="store_true", help="Target every canonical course record")
    args = parser.parse_args()

    if args.all and args.course_id:
        parser.error("Use either --all or --course-id, not both")
    if args.apply and not args.all and not args.course_id:
        parser.error("--apply requires at least one --course-id or an explicit --all")

    root = Path(__file__).resolve().parents[1]
    manifest = load_yaml(root / "curriculum/curriculum.yaml")
    if manifest.get("status") == "awaiting-import":
        raise SystemExit("Import the canonical spreadsheet before generating course shells")

    template = root / "templates/course"
    planned: list[tuple[dict, Path]] = []
    for record in manifest.get("records", []):
        if record.get("record_type") != "course":
            continue
        year = int(record["planned_year"])
        term = record["planned_term"]
        course_id = record["record_id"]
        destination = root / "courses" / YEAR_DIRECTORIES[year] / term / course_id
        if args.all or not args.course_id or record["record_id"] in args.course_id:
            planned.append((record, destination))

    missing_requested = sorted(set(args.course_id) - {record["record_id"] for record, _ in planned})
    if missing_requested:
        raise SystemExit(f"Unknown course record_id(s): {', '.join(missing_requested)}")

    for record, destination in planned:
        print(destination.relative_to(root))
        if args.dry_run:
            continue
        destination.mkdir(parents=True, exist_ok=True)
        copy_tree_without_overwrite(template, destination)
        credits = float(record["credits"])
        academic_stage = "undergraduate" if record["planned_year"] <= 4 else "mdiv" if record["planned_year"] <= 7 else "phd"
        replacements = {
            "__COURSE_ID__": record["record_id"],
            "__COURSE_CODE__": record.get("course_code") or "UNNUMBERED",
            "__COURSE_TITLE__": record["title"],
            "__CATALOG_SOURCE_INSTITUTION__": record["institution"],
            "__CATALOG_YEAR__": "2026-27",
            "__CATALOG_URL__": record.get("catalog_url") or "TODO-VERIFY",
            "__ACADEMIC_STAGE__": academic_stage,
            "__PROGRAM_YEAR__": str(record["planned_year"]),
            "__TERM__": record["planned_term"],
            "__CREDIT_HOURS__": str(int(credits) if credits.is_integer() else credits),
            "__ESTIMATED_TOTAL_HOURS__": str(int(credits * 45)),
            "__WEEKLY_WORKLOAD_HOURS__": str(round((credits * 45) / 15, 1)),
            "__CATALOG_DESCRIPTION__": record.get("catalog_description") or "TODO-VERIFY",
        }
        replace_placeholders(destination, replacements)

        # Write machine-readable metadata through YAML serialization so catalog
        # descriptions containing quotation marks, colons, or Unicode remain valid.
        course_metadata = {
            "schema_version": "1.0.0",
            "course_id": record["record_id"],
            "course_code": record.get("course_code") or "UNNUMBERED",
            "course_title": record["title"],
            "catalog_source_institution": record["institution"],
            "catalog_year": "2026-27",
            "catalog_url": record.get("catalog_url") or "TODO-VERIFY",
            "independent_curriculum_notice": True,
            "academic_stage": academic_stage,
            "program_year": record["planned_year"],
            "term": record["planned_term"],
            "credit_hours": int(credits) if credits.is_integer() else credits,
            "instructional_weeks": 15,
            "estimated_total_hours": int(credits * 45),
            "prerequisites": [],
            "corequisites": [],
            "course_description": record.get("catalog_description") or "TODO-VERIFY",
            "curriculum_description": "TODO-VERIFY",
            "confessional_framework": "broadly_evangelical_protestant",
            "learning_outcomes": [],
            "required_texts": [],
            "recommended_texts": [],
            "assessment_breakdown": [],
            "grading_scale": "standard_project_scale",
            "meeting_pattern": "TODO-VERIFY",
            "weekly_workload_hours": round((credits * 45) / 15, 1),
            "primary_instructor_role": "independent_curriculum_facilitator",
            "external_evaluator_required": False,
            "biblical_languages_required": [],
            "software_required": [],
            "required_bible_editions": ["ESV", "NASB_2020"],
            "major_assignments": [],
            "final_assessment_type": "TODO-VERIFY",
            "ministry_or_fieldwork_requirement": None,
            "relationship_to_later_courses": [],
            "academic_source_standard": "SOURCE-POLICY.md",
            "copyright_restrictions": "no_unauthorized_copies",
            "source_verification_date": None,
            "last_content_audit_date": None,
            "known_unresolved_questions": [],
            "curriculum_version": "0.1.0",
            "status": "shell",
        }
        dump_yaml(course_metadata, destination / "course.yaml")

        weeks_root = destination / "weeks"
        weeks_root.mkdir(exist_ok=True)
        for week in range(1, 16):
            week_destination = weeks_root / f"week-{week:02d}"
            if week_destination.exists():
                continue
            copy_tree_without_overwrite(root / "templates/week", week_destination)
            replace_placeholders(week_destination, {
                "__COURSE_ID__": record["record_id"],
                "__COURSE_CODE__": record.get("course_code") or "UNNUMBERED",
                "__WEEK_NUMBER__": str(week),
                "__WEEK_TITLE__": "TODO-VERIFY",
                "__LECTURE_1_TITLE__": "TODO-VERIFY",
                "__LECTURE_2_TITLE__": "TODO-VERIFY",
                "__LESSON_NUMBER__": "TODO-VERIFY",
                "__LESSON_TITLE__": "TODO-VERIFY",
            })
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
