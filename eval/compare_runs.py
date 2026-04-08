from __future__ import annotations

import argparse
import re
from pathlib import Path


def read_text(path: Path) -> str:
    raw = path.read_bytes()
    for enc in ("utf-8", "utf-16", "utf-16-le", "utf-16-be"):
        try:
            return raw.decode(enc).replace("\x00", "")
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace").replace("\x00", "")


def parse_sections(path: Path) -> tuple[dict[str, float], dict[str, float]]:
    text = read_text(path)
    lines = [line.strip() for line in text.splitlines()]

    aggregate: dict[str, float] = {}
    categories: dict[str, float] = {}

    in_aggregate = False
    in_categories = False
    avg_re = re.compile(r"^-\s+(\w+):\s+avg_score=([^\s]+)")

    for line in lines:
        if line == "Aggregate metric averages:":
            in_aggregate = True
            in_categories = False
            continue
        if line == "Simple average by category:":
            in_categories = True
            in_aggregate = False
            continue
        if not line:
            continue

        m = avg_re.match(line)
        if not m:
            continue

        name, value = m.groups()
        if value == "N/A":
            continue
        try:
            score = float(value)
        except ValueError:
            continue

        if in_aggregate:
            aggregate[name] = score
        elif in_categories:
            categories[name] = score

    return aggregate, categories


def print_table(title: str, baseline: dict[str, float], degraded: dict[str, float]) -> None:
    keys = sorted(set(baseline) | set(degraded))
    print(f"\n{title}")
    print("-" * len(title))
    print(f"{'name':35} {'baseline':>10} {'degraded':>10} {'delta':>10}")
    for key in keys:
        b = baseline.get(key)
        d = degraded.get(key)
        if b is None or d is None:
            print(f"{key:35} {str(b):>10} {str(d):>10} {'N/A':>10}")
        else:
            print(f"{key:35} {b:10.3f} {d:10.3f} {d - b:+10.3f}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare baseline vs degraded eval outputs.")
    parser.add_argument("baseline", type=Path, help="Path to baseline eval output file")
    parser.add_argument("degraded", type=Path, help="Path to degraded eval output file")
    args = parser.parse_args()

    base_agg, base_cat = parse_sections(args.baseline)
    deg_agg, deg_cat = parse_sections(args.degraded)

    print(f"Baseline: {args.baseline}")
    print(f"Degraded: {args.degraded}")

    print_table("Aggregate metric averages", base_agg, deg_agg)
    print_table("Category averages", base_cat, deg_cat)


if __name__ == "__main__":
    main()