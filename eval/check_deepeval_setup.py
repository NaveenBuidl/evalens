from __future__ import annotations

from deepeval.metrics import (
    AnswerRelevancyMetric,
    ContextualPrecisionMetric,
    ContextualRecallMetric,
    FaithfulnessMetric,
)
from deepeval.test_case import LLMTestCase


def run_metric(metric, test_case: LLMTestCase) -> None:
    name = metric.__class__.__name__
    try:
        metric.measure(test_case)
        print(f"{name}: SUCCESS")
    except Exception as exc:  # smoke check: we only care whether metric can run
        print(f"{name}: FAILED ({exc})")


def main() -> None:
    test_case = LLMTestCase(
        input="What is Evalens?",
        actual_output="Evalens is a tiny RAG demo for evaluating retrieval and answer quality.",
        expected_output="Evalens is a minimal retrieval-augmented generation project.",
        retrieval_context=[
            "Evalens is a small tracer-bullet RAG project used for evaluation experiments."
        ],
    )

    metrics = [
        FaithfulnessMetric(),
        ContextualPrecisionMetric(),
        ContextualRecallMetric(),
        AnswerRelevancyMetric(),
    ]

    for metric in metrics:
        run_metric(metric, test_case)


if __name__ == "__main__":
    main()