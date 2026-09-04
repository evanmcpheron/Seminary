#!/usr/bin/env python3
"""Apply owner-approved schedule overrides without changing locked course identity.

This tool is intentionally conservative. Populate curriculum/schedule-overrides.yaml through
an audited scheduling task before running it. It updates only planned_year and planned_term in
curriculum/curriculum.yaml and never edits the spreadsheet or curriculum.lock.yaml.
"""
from __future__ import annotations

from pathlib import Path
import sys

_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from seminary_tools.common import dump_yaml, load_yaml


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    manifest_path = root / "curriculum/curriculum.yaml"
    manifest = load_yaml(manifest_path)
    overrides = load_yaml(root / "curriculum/schedule-overrides.yaml") or {}
    by_id = {record["record_id"]: record for record in manifest.get("records", [])}

    for override in overrides.get("overrides", []):
        if not override.get("owner_approved"):
            raise SystemExit(f"Override is not owner-approved: {override}")
        record_id = override["record_id"]
        if record_id not in by_id:
            raise SystemExit(f"Unknown record_id in override: {record_id}")
        record = by_id[record_id]
        record["planned_year"] = int(override["new_project_year"])
        record["planned_term"] = override["new_term"]

    manifest["status"] = "schedule-reconciled"
    dump_yaml(manifest, manifest_path)
    print(f"Applied {len(overrides.get('overrides', []))} approved override(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
