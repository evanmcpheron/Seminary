#!/usr/bin/env python3
from __future__ import annotations

import argparse
from copy import deepcopy
from pathlib import Path
import sys

_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from seminary_tools.common import dump_yaml
from seminary_tools.curriculum_import import import_workbook


def main() -> int:
    parser = argparse.ArgumentParser(description="Import and lock the canonical curriculum spreadsheet")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--lock-output", type=Path, default=Path("curriculum/curriculum.lock.yaml"))
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    input_path = args.input if args.input.is_absolute() else root / args.input
    output_path = args.output if args.output.is_absolute() else root / args.output
    lock_path = args.lock_output if args.lock_output.is_absolute() else root / args.lock_output

    if not input_path.exists():
        raise SystemExit(f"Canonical spreadsheet not found: {input_path}")
    manifest = import_workbook(input_path)
    # Store repository-relative path when possible.
    try:
        manifest["source_spreadsheet"]["path"] = input_path.relative_to(root).as_posix()
    except ValueError:
        manifest["source_spreadsheet"]["path"] = input_path.as_posix()

    dump_yaml(manifest, output_path)
    lock = deepcopy(manifest)
    lock["status"] = "locked"
    for record in lock["records"]:
        record.pop("selection_rationale", None)
        record.pop("offering_accuracy_note", None)
    dump_yaml(lock, lock_path)
    print(f"Imported {len(manifest['records'])} records")
    print(f"Manifest: {output_path}")
    print(f"Lock file: {lock_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
