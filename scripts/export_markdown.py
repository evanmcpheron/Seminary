#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import subprocess


def main() -> int:
    parser = argparse.ArgumentParser(description="Export canonical Markdown to DOCX or PDF using Pandoc")
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    pandoc = shutil.which("pandoc")
    if not pandoc:
        raise SystemExit("Pandoc is not installed; canonical Markdown remains available")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([pandoc, str(args.input), "-o", str(args.output)], check=True)
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
