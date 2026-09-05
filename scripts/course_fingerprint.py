#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import sys

_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from seminary_tools.validation import course_content_fingerprint


def main() -> int:
    parser = argparse.ArgumentParser(description="Compute the release-scoped fingerprint for one course directory")
    parser.add_argument("course_path", help="Repository-relative path to the course directory")
    args = parser.parse_args()

    requested = Path(args.course_path)
    if requested.is_absolute():
        parser.error("course_path must be repository-relative")
    course_dir = (_REPO_ROOT / requested).resolve()
    if _REPO_ROOT.resolve() not in course_dir.parents:
        parser.error("course_path must remain inside the repository")
    if not course_dir.is_dir() or not (course_dir / "course.yaml").is_file():
        parser.error("course_path must name an instantiated course directory containing course.yaml")

    print(course_content_fingerprint(course_dir))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
