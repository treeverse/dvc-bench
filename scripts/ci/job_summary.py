"""Render pytest-benchmark JSONs as a Markdown GitHub Actions job summary.

For each *.json under <benchmarks_dir>, emit a <details> section with one
sub-table per benchmark variant. Rows are DVC revisions, columns are stats.
"""  # noqa: INP001

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

from tabulate import tabulate

SAVE_PREFIX = re.compile(r"^\d+_")
PARAM_SUFFIX = re.compile(r"\[[^]]*\]$")
COLS = ("min", "max", "mean", "stddev", "median", "iqr", "ops")


def variant(name: str) -> str:
    return PARAM_SUFFIX.sub("", name)


def render_file(path: Path) -> str:
    data = json.loads(path.read_text())
    funcname = SAVE_PREFIX.sub("", path.stem)

    by_variant: dict[str, list[dict]] = defaultdict(list)
    for b in data["benchmarks"]:
        params = b.get("params") or {}
        row = {**params, **{c: b["stats"].get(c) for c in COLS}}
        by_variant[variant(b["name"])].append(row)

    out = [f"<details><summary>{funcname}</summary>\n"]
    for v, rows in by_variant.items():
        out.append(f"#### {v}\n")
        out.append(tabulate(rows, headers="keys", tablefmt="pipe", floatfmt=".4f"))
        out.append("")
    out.append("</details>\n")
    return "\n".join(out)


def main(benchmarks_dir: str) -> None:
    for f in sorted(Path(benchmarks_dir).rglob("*.json")):
        sys.stdout.write(render_file(f))


if __name__ == "__main__":
    main(sys.argv[1])
