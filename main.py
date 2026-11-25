#!/usr/bin/env python3
"""Entry for the make.fun news-image-20261125 bounty.

The image summing up Wednesday 25 November 2026 lives beside this file as
entry.png: a newspaper front page drawn at build time — Hormuz shipping
attacks as the lead, with Ukraine's €115bn aid ask, Pakistan's first
astronaut, the Australia–Solomon Islands treaty, the Huawei verdict, the
West Java mine rescue, and Senegal's restored Africa Cup title. This
program copies it to the output directory: /output inside the grader's
container, or $MAKEFUN_OUTPUT_DIR when run locally.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.png", OUT_DIR / "entry.png")


if __name__ == "__main__":
    main()
