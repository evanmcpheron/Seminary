#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import sys

REQUIRED_DIRECTORIES = [
    "curriculum/source", "courses", "formation", "dissertation", "prompts",
    "schemas", "scripts", "templates", "tests", "provenance", ".github/workflows"
]
REQUIRED_FILES = [
    "README.md", "AGENTS.md", "MASTER_PROMPT.md", "PROJECT-DECISIONS.yaml",
    "curriculum/curriculum.yaml", "schemas/course.schema.json",
    "schemas/curriculum.schema.json", ".github/workflows/validate.yml"
]


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify or create only missing top-level Seminary scaffold paths")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    missing_dirs = [item for item in REQUIRED_DIRECTORIES if not (root / item).is_dir()]
    missing_files = [item for item in REQUIRED_FILES if not (root / item).is_file()]

    if args.apply:
        for item in missing_dirs:
            (root / item).mkdir(parents=True, exist_ok=True)
            print(f"created directory: {item}")
        # This script never fabricates missing governance files. They must come from the checked-in scaffold.
        if missing_files:
            print("ERROR: required boilerplate files are missing and will not be fabricated by this safety check:", file=sys.stderr)
            for item in missing_files:
                print(f"  - {item}", file=sys.stderr)
            return 1
        return 0

    if missing_dirs or missing_files:
        for item in missing_dirs:
            print(f"missing directory: {item}")
        for item in missing_files:
            print(f"missing file: {item}")
        return 1
    print("bootstrap scaffold check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
