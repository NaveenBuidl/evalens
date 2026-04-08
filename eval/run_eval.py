from __future__ import annotations

import json
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

EVAL_CASES_PATH = Path(__file__).with_name("eval_cases_v0.json")
QUERY_URL = "http://127.0.0.1:8000/query"


def load_eval_cases(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


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
    print(f"Q: {case['question']}")
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
    eval_cases = load_eval_cases(EVAL_CASES_PATH)

    metrics = [
        FaithfulnessMetric(),
        ContextualPrecisionMetric(),
        ContextualRecallMetric(),
        AnswerRelevancyMetric(),
    ]

    metric_scores: dict[str, list[float]] = defaultdict(list)
    category_scores: dict[str, list[float]] = defaultdict(list)

    for case in eval_cases:
        rag_response = query_rag(case["question"])
        answer = rag_response.get("answer", "")
        retrieval_context = rag_response.get("retrieved_chunks", []) or []

        test_case = LLMTestCase(
            input=case["question"],
            actual_output=answer,
            expected_output=case.get("expected_outcome", ""),
            retrieval_context=retrieval_context,
        )

        metric_results = [metric_summary(metric, test_case) for metric in metrics]
        print_case_summary(case, answer, retrieval_context, metric_results)

        case_scores: list[float] = []
        for result in metric_results:
            score = result.get("score")
            if isinstance(score, (int, float)):
                metric_scores[result["name"]].append(float(score))
                case_scores.append(float(score))

        if case_scores:
            category_scores[case["category"]].append(sum(case_scores) / len(case_scores))

    print("=" * 80)
    print("Aggregate metric averages:")
    for metric_name in [metric.__class__.__name__ for metric in metrics]:
        scores = metric_scores.get(metric_name, [])
        average = (sum(scores) / len(scores)) if scores else None
        average_str = f"{average:.3f}" if average is not None else "N/A"
        print(f"  - {metric_name}: avg_score={average_str} (n={len(scores)})")

    print("Simple average by category:")
    for category in ["factual", "conflict", "oos", "caveat"]:
        scores = category_scores.get(category, [])
        average = (sum(scores) / len(scores)) if scores else None
        average_str = f"{average:.3f}" if average is not None else "N/A"
        print(f"  - {category}: avg_score={average_str} (n={len(scores)})")


if __name__ == "__main__":
    main()
