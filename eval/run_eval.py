from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from collections import defaultdict
from typing import Any

import requests
from deepeval.metrics import (
    AnswerRelevancyMetric,
    ContextualPrecisionMetric,
    ContextualRecallMetric,
    FaithfulnessMetric,
)
from deepeval.test_case import LLMTestCase

EVAL_CASES_PATH = Path(__file__).with_name("golden_eval_set.json")
QUERY_URL = "http://localhost:8000/query"
RESULTS_DIR = Path(__file__).parent / "results"

METRIC_KEYS = ["faithfulness", "contextual_precision", "contextual_recall", "answer_relevancy"]
METRIC_THRESHOLDS = {
    "faithfulness": 0.70,
    "contextual_precision": 0.68,
    "contextual_recall": 0.75,
    "answer_relevancy": 0.65,
}
METRIC_CLASS_TO_KEY = {
    "FaithfulnessMetric": "faithfulness",
    "ContextualPrecisionMetric": "contextual_precision",
    "ContextualRecallMetric": "contextual_recall",
    "AnswerRelevancyMetric": "answer_relevancy",
}

# Cost constants (gpt-4o-mini rates: $0.15/1M input, $0.60/1M output)
JUDGE_CALLS = 120
AVG_INPUT_TOKENS_PER_CALL = 700
AVG_OUTPUT_TOKENS_PER_CALL = 150
GPT4O_MINI_INPUT_RATE = 0.15 / 1_000_000
GPT4O_MINI_OUTPUT_RATE = 0.60 / 1_000_000


def compute_judge_cost() -> float:
    input_cost = JUDGE_CALLS * AVG_INPUT_TOKENS_PER_CALL * GPT4O_MINI_INPUT_RATE
    output_cost = JUDGE_CALLS * AVG_OUTPUT_TOKENS_PER_CALL * GPT4O_MINI_OUTPUT_RATE
    return input_cost + output_cost


def load_eval_cases(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return data["eval_set"] if isinstance(data, dict) and "eval_set" in data else data


def query_rag(question: str) -> dict[str, Any]:
    response = requests.post(QUERY_URL, json={"query": question}, timeout=60)
    response.raise_for_status()
    return response.json()


def metric_summary(metric: Any, test_case: LLMTestCase) -> dict[str, Any]:
    name = metric.__class__.__name__
    try:
        metric.measure(test_case)
        return {
            "name": name,
            "score": metric.score,
            "success": metric.success,
            "reason": metric.reason,
            "error": None,
        }
    except Exception as exc:
        return {
            "name": name,
            "score": None,
            "success": False,
            "reason": None,
            "error": str(exc),
        }


def print_case_summary(
    case: dict[str, Any],
    answer: str,
    retrieval_context: list[str],
    metric_results: list[dict[str, Any]],
) -> None:
    print("=" * 80)
    print(f"{case['id']} ({case['category']})")
    print(f"Q: {case['query']}")
    print(f"A: {answer}")
    print(f"Retrieved chunks: {len(retrieval_context)}")

    for idx, chunk in enumerate(retrieval_context, start=1):
        trimmed = " ".join(chunk.split())
        preview = trimmed[:220] + ("..." if len(trimmed) > 220 else "")
        print(f"  [{idx}] {preview}")

    print("Metrics:")
    for result in metric_results:
        if result["error"]:
            print(f"  - {result['name']}: ERROR ({result['error']})")
            continue
        print(
            f"  - {result['name']}: score={result['score']}, "
            f"success={result['success']}, reason={result['reason']}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="baseline_results.json")
    parser.add_argument("--run-id", default=None)
    args = parser.parse_args()

    results_file = RESULTS_DIR / args.output
    run_id = args.run_id or f"run_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"

    eval_cases = load_eval_cases(EVAL_CASES_PATH)

    metrics = [
        FaithfulnessMetric(),
        ContextualPrecisionMetric(),
        ContextualRecallMetric(),
        AnswerRelevancyMetric(),
    ]

    metric_scores: dict[str, list[float]] = defaultdict(list)
    category_scores: dict[str, dict[str, list[float]]] = defaultdict(lambda: defaultdict(list))
    pathology_scores: dict[str, dict[str, list[float]]] = defaultdict(lambda: defaultdict(list))
    per_case_results: list[dict[str, Any]] = []
    run_config: dict[str, Any] = {}

    for case in eval_cases:
        rag_response = query_rag(case["query"])
        if not run_config:
            run_config = {
                "chunk_size": rag_response.get("chunk_size"),
                "retrieval_k": rag_response.get("retrieval_k"),
            }
        answer = rag_response.get("answer", "")
        retrieval_context = rag_response.get("retrieved_chunks", []) or []
        retrieved_sources = rag_response.get("sources", [])

        test_case = LLMTestCase(
            input=case["query"],
            actual_output=answer,
            expected_output=case["expected_output"],
            retrieval_context=retrieval_context,
        )

        metric_results = [metric_summary(metric, test_case) for metric in metrics]
        print_case_summary(case, answer, retrieval_context, metric_results)

        scores: dict[str, Any] = {}
        for result in metric_results:
            key = METRIC_CLASS_TO_KEY.get(result["name"])
            if not key:
                continue
            score = result.get("score")
            scores[key] = float(score) if isinstance(score, (int, float)) else None
            if scores[key] is not None:
                metric_scores[key].append(scores[key])
                category_scores[case["category"]][key].append(scores[key])
                pathology_scores[case.get("pathology", "unknown")][key].append(scores[key])

        case_pass = all(
            scores.get(k) is not None and scores[k] >= METRIC_THRESHOLDS[k]
            for k in METRIC_KEYS
        )

        per_case_results.append({
            "id": case["id"],
            "category": case["category"],
            "pathology": case.get("pathology", ""),
            "query": case["query"],
            "actual_output": answer,
            "retrieved_sources": retrieved_sources,
            "scores": scores,
            "pass": case_pass,
        })

    # Aggregate summary
    print("=" * 80)
    print("Aggregate metric averages:")
    for key in METRIC_KEYS:
        scores_list = metric_scores.get(key, [])
        mean = (sum(scores_list) / len(scores_list)) if scores_list else None
        mean_str = f"{mean:.3f}" if mean is not None else "N/A"
        threshold = METRIC_THRESHOLDS[key]
        passed = mean is not None and mean >= threshold
        print(f"  - {key}: avg_score={mean_str} (threshold={threshold}, pass={passed})")

    print("Average by category:")
    for category in ["Factual", "Caveat", "Conflict", "OOS", "Safety", "Adversarial", "Synthesis"]:
        cat_data = category_scores.get(category, {})
        all_vals = [s for vals in cat_data.values() for s in vals]
        if all_vals:
            print(f"  - {category}: avg_score={sum(all_vals) / len(all_vals):.3f} (n={len(all_vals)})")
        else:
            print(f"  - {category}: N/A")

    # Cost tracking
    judge_cost = compute_judge_cost()
    print("=" * 80)
    print("Cost estimate:")
    print(
        f"  Judge calls: ${judge_cost:.4f} "
        f"(estimated: {JUDGE_CALLS} calls x ~{AVG_INPUT_TOKENS_PER_CALL} input tokens "
        f"x $0.15/1M + ~{AVG_OUTPUT_TOKENS_PER_CALL} output tokens x $0.60/1M, gpt-4o-mini)"
    )
    print("  Generation: $0.00 (Groq free tier)")
    print("  Embeddings: $0.00 (local SentenceTransformer)")
    print(f"  Total estimated: ${judge_cost:.4f}")

    # Build and save results JSON
    def agg_metric(key: str) -> dict[str, Any]:
        scores_list = metric_scores.get(key, [])
        mean = round(sum(scores_list) / len(scores_list), 4) if scores_list else 0.0
        return {"mean": mean, "threshold": METRIC_THRESHOLDS[key], "pass": mean >= METRIC_THRESHOLDS[key]}

    def agg_category(category: str) -> dict[str, Any]:
        cat_data = category_scores.get(category, {})
        return {
            key: round(sum(vals) / len(vals), 4) if (vals := cat_data.get(key, [])) else None
            for key in METRIC_KEYS
        }

    by_pathology: dict[str, Any] = {}
    for pathology, path_data in pathology_scores.items():
        by_pathology[pathology] = {
            key: round(sum(vals) / len(vals), 4) if (vals := path_data.get(key, [])) else None
            for key in METRIC_KEYS
        }

    results: dict[str, Any] = {
        "run_id": run_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "eval_set_size": len(eval_cases),
        "eval_set_file": "golden_eval_set.json",
        "config": run_config,
        "cost": {
            "judge_calls": f"${judge_cost:.4f} (estimated: {JUDGE_CALLS} calls x gpt-4o-mini)",
            "generation_calls": "$0.00 (Groq free tier)",
            "embedding_calls": "$0.00 (local SentenceTransformer)",
            "total_estimated": f"${judge_cost:.4f}",
        },
        "aggregate_metrics": {key: agg_metric(key) for key in METRIC_KEYS},
        "by_category": {
            cat: agg_category(cat)
            for cat in ["Factual", "Caveat", "Conflict", "OOS", "Safety", "Adversarial", "Synthesis"]
        },
        "by_pathology": by_pathology,
        "per_case": per_case_results,
    }

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    with results_file.open("w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"Results saved to {results_file}")


if __name__ == "__main__":
    main()
