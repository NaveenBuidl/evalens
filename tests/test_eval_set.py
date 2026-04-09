import json
import pytest

@pytest.fixture
def eval_set():
    with open("eval/golden_eval_set.json") as f:
        data = json.load(f)
    return data["eval_set"]

def test_eval_set_loads(eval_set):
    assert len(eval_set) > 0

def test_eval_set_has_minimum_entries(eval_set):
    assert len(eval_set) >= 30

def test_all_required_fields_present(eval_set):
    required = {"id", "query", "expected_output", "relevant_docs", "category", "pathology", "expected_retrieval_behavior"}
    for entry in eval_set:
        missing = required - set(entry.keys())
        assert not missing, f"{entry['id']} missing fields: {missing}"

def test_eval_set_covers_all_categories(eval_set):
    categories = {e["category"] for e in eval_set}
    expected = {"Factual", "Caveat", "Conflict", "OOS", "Safety", "Adversarial", "Synthesis"}
    missing = expected - categories
    assert not missing, f"Missing categories: {missing}"

def test_conflict_pairs_have_multiple_docs(eval_set):
    for entry in eval_set:
        if entry["category"] == "Conflict":
            assert len(entry["relevant_docs"]) >= 2, f"{entry['id']}: Conflict case needs 2+ docs, has {len(entry['relevant_docs'])}"

def test_oos_queries_have_empty_relevant_docs(eval_set):
    for entry in eval_set:
        if entry["category"] == "OOS":
            assert len(entry["relevant_docs"]) == 0, f"{entry['id']}: OOS case should have empty relevant_docs"

def test_safety_queries_present(eval_set):
    safety_count = sum(1 for e in eval_set if e["category"] == "Safety")
    assert safety_count >= 3, f"Only {safety_count} safety cases, need 3+"

def test_unique_ids(eval_set):
    ids = [e["id"] for e in eval_set]
    assert len(ids) == len(set(ids)), "Duplicate IDs found"

def test_no_empty_queries(eval_set):
    for entry in eval_set:
        assert entry["query"].strip(), f"{entry['id']} has empty query"

def test_no_empty_expected_output(eval_set):
    for entry in eval_set:
        assert entry["expected_output"].strip(), f"{entry['id']} has empty expected_output"
