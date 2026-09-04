#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import sys

_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from seminary_tools.validation import validate_repository


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Seminary repository metadata and guardrails")
    parser.add_argument("--mode", choices=["scaffold", "draft", "release"], default="draft")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    report = validate_repository(root, args.mode)
    for warning in report.warnings:
        print(f"WARNING: {warning}")
    for error in report.errors:
        print(f"ERROR: {error}")
    print(f"Validation complete: {len(report.errors)} error(s), {len(report.warnings)} warning(s)")
    return 1 if report.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
