#!/usr/bin/env python3
"""Pathology-level analysis of eval results.

Usage (single file):
    python eval/analyze_pathology.py eval/results/baseline_results.json

Usage (comparison):
    python eval/analyze_pathology.py eval/results/baseline_results.json eval/results/regression_results.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

PATHOLOGY_META = {
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
CATEGORY_ORDER = ["Factual", "Caveat", "Synthesis", "Conflict", "OOS", "Safety", "Adversarial"]

PREC_GATE = 0.68
RECALL_GATE = 0.75


def load_results(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sorted_pathologies() -> list[str]:
    cat_rank = {c: i for i, c in enumerate(CATEGORY_ORDER)}
    return sorted(PATHOLOGY_META, key=lambda p: (cat_rank[PATHOLOGY_META[p][0]], p))


def is_flagged(prec: float, recall: float) -> bool:
    return prec < PREC_GATE or recall < RECALL_GATE


def run_header(results: dict) -> str:
    cfg = results.get("config", {})
    return (
        f"Run: {results.get('run_id', '?')}  |  "
        f"retrieval_k={cfg.get('retrieval_k', '?')}  "
        f"chunk_size={cfg.get('chunk_size', '?')}"
    )


def print_single(results: dict) -> None:
    by_path = results["by_pathology"]
    paths = sorted_pathologies()

    P, C, N, S = 30, 12, 3, 7
    hdr = (
        f"{'pathology':<{P}} {'category':<{C}} {'n':>{N}} "
        f"{'prec':>{S}} {'recall':>{S}} {'faith':>{S}} {'relev':>{S}}"
    )
    bar = "-" * len(hdr)
    print(f"\n{hdr}")
    print(bar)

    n_flagged = 0
    for p in paths:
        if p not in by_path:
            continue
        cat, n = PATHOLOGY_META[p]
        s = by_path[p]
        prec = s["contextual_precision"]
        rec = s["contextual_recall"]
        faith = s["faithfulness"]
        relev = s["answer_relevancy"]
        mark = " \u26a0" if is_flagged(prec, rec) else ""
        print(
            f"{p:<{P}} {cat:<{C}} {n:>{N}} "
            f"{prec:>{S}.3f} {rec:>{S}.3f} {faith:>{S}.3f} {relev:>{S}.3f}{mark}"
        )
        if mark:
            n_flagged += 1

    print(bar)
    print(f"\n{n_flagged} pathologies flagged (prec < {PREC_GATE} or recall < {RECALL_GATE})")


def print_comparison(r1: dict, r2: dict) -> None:
    bp1 = r1["by_pathology"]
    bp2 = r2["by_pathology"]
    paths = sorted_pathologies()

    P, C, N, S, D = 30, 12, 3, 7, 8
    hdr = (
        f"{'pathology':<{P}} {'category':<{C}} {'n':>{N}} "
        f"{'prec':>{S}} {'recall':>{S}} {'faith':>{S}} {'relev':>{S}} "
        f"{'\u0394prec':>{D}} {'\u0394recall':>{D}}"
    )
    bar = "-" * len(hdr)
    print(f"\n{hdr}")
    print(bar)

    n_flagged = 0
    deltas: list[tuple[str, str, float, float]] = []
    for p in paths:
        if p not in bp1 or p not in bp2:
            continue
        cat, n = PATHOLOGY_META[p]
        s1, s2 = bp1[p], bp2[p]
        prec2 = s2["contextual_precision"]
        rec2 = s2["contextual_recall"]
        dp = prec2 - s1["contextual_precision"]
        dr = rec2 - s1["contextual_recall"]
        mark = " \u26a0" if is_flagged(prec2, rec2) else ""
        print(
            f"{p:<{P}} {cat:<{C}} {n:>{N}} "
            f"{prec2:>{S}.3f} {rec2:>{S}.3f} "
            f"{s2['faithfulness']:>{S}.3f} {s2['answer_relevancy']:>{S}.3f} "
            f"{dp:>+{D}.3f} {dr:>+{D}.3f}{mark}"
        )
        if mark:
            n_flagged += 1
        deltas.append((p, cat, dp, dr))

    print(bar)
    print(f"\n{n_flagged} pathologies flagged (prec < {PREC_GATE} or recall < {RECALL_GATE})")

    top5 = sorted(deltas, key=lambda x: abs(x[2]), reverse=True)[:5]
    print(f"\nTop 5 regressions by |\u0394prec|:")
    print(f"  {'pathology':<{P}} {'category':<{C}} {'\u0394prec':>{D}} {'\u0394recall':>{D}}")
    print("  " + "-" * (P + 1 + C + 1 + D + 1 + D))
    for p, cat, dp, dr in top5:
        print(f"  {p:<{P}} {cat:<{C}} {dp:>+{D}.3f} {dr:>+{D}.3f}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Pathology-level analysis of eval results.")
    parser.add_argument("file1", type=Path, help="Baseline results JSON")
    parser.add_argument("file2", type=Path, nargs="?", help="Comparison results JSON")
    args = parser.parse_args()

    r1 = load_results(args.file1)
    print(run_header(r1))

    if args.file2 is None:
        print_single(r1)
    else:
        r2 = load_results(args.file2)
        print(f"vs. {run_header(r2)}")
        print_comparison(r1, r2)


if __name__ == "__main__":
    main()
