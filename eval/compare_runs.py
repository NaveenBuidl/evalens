from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


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


_PATHOLOGY_META = {
    "clean_retrieval_baseline":      ("Factual",     4),
    "cross_doc_retrieval":           ("Factual",     1),
    "label_disambiguation":          ("Factual",     1),
    "multi_entity_retrieval":        ("Factual",     1),
    "conditional_truth_collapse":    ("Caveat",      3),
    "gap_by_omission":               ("Caveat",      1),
    "same_doc_multi_fact":           ("Caveat",      1),
    "topic_presence_answer_absence": ("Caveat",      1),
    "cross_doc_assembly":            ("Synthesis",   1),
    "cross_doc_contradiction":       ("Conflict",    1),
    "framing_dependent_conflict":    ("Conflict",    2),
    "terminology_alias_confusion":   ("Conflict",    1),
    "clean_oos":                     ("OOS",         2),
    "plausible_absence":             ("OOS",         1),
    "semantic_mismatch_oos":         ("OOS",         1),
    "internal_data_fabrication":     ("Safety",      1),
    "pii_fabrication":               ("Safety",      1),
    "prompt_injection":              ("Safety",      1),
    "scope_boundary":                ("Safety",      1),
    "ungrounded_persuasion":         ("Safety",      1),
    "authority_contamination":       ("Adversarial", 1),
    "false_premise":                 ("Adversarial", 1),
    "loaded_question":               ("Adversarial", 1),
}


def _load_pathology(path: Path) -> tuple[str, dict]:
    """Try to load by_pathology from a JSON results file. Returns (run_id, by_pathology)."""
    try:
        data = json.loads(path.read_bytes().decode("utf-8", errors="replace"))
        return data.get("run_id", str(path)), data.get("by_pathology", {})
    except (json.JSONDecodeError, Exception):
        return str(path), {}


def _print_pathology_impact(base_path: Path, deg_path: Path) -> None:
    base_id, bp1 = _load_pathology(base_path)
    deg_id, bp2 = _load_pathology(deg_path)
    if not bp1 or not bp2:
        return

    deltas = []
    for p, (cat, _) in _PATHOLOGY_META.items():
        if p in bp1 and p in bp2:
            dp = bp2[p]["contextual_precision"] - bp1[p]["contextual_precision"]
            deltas.append((p, cat, dp))

    regressions = sorted(
        [(p, cat, dp) for p, cat, dp in deltas if dp < 0],
        key=lambda x: x[2],
    )[:5]

    title = f"PATHOLOGY IMPACT  ({base_id} \u2192 {deg_id})"
    print(f"\n{title}")
    print("-" * len(title))
    print(f"Top regressions by \u0394prec:\n")
    print(f"  {'pathology':<32} {'category':<12} {'\u0394prec':>8}")
    print("  " + "-" * 54)
    for p, cat, dp in regressions:
        print(f"  {p:<32} {cat:<12} {dp:>+8.3f}")
    print(f"\nFull breakdown: python eval/analyze_pathology.py {base_path} {deg_path}")


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

    _print_pathology_impact(args.baseline, args.degraded)


if __name__ == "__main__":
    main()