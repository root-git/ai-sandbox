# Import pytest testing framework for test execution
import pytest 
# import the compute_rrf_scores function from our implementation module
from ai_sandbox.retrieval.rrf_fusion import compute_rrf_scores

# Define test function for RRF fusion logic and result ordering
def test_compute_rrf_scores():
    # Define vector search candidate result list ranked 1 to 3
    vector_results = ["docA", "docB", "docC"]
    # Define BM25 keyword search candidate result list ranked 1 to 3
    bm25_results = ["docB", "docA", "docD"]

    # Calculate aggregated RRF scores across both candidate lists
    scores = compute_rrf_scores([vector_results, bm25_results], k=60)

    # Assert docB score calculation (1/62 + 1/61) mathces expected value
    assert pytest.approx(scores["docB"], rel=1e-4) == (1/62) + (1/61)
    # Assert doc A score calculation (1/61 +1/62) matches docB score
    assert pytest.approx(scores["docA"], rel=1e-4) == (1/61) + (1/62)
    # Assert docC score calculation (1/63) matches single top-3 occurrence
    assert pytest.approx(scores["docC"], rel=1e-4) == 1/63

    # Sort document IDs in descending order by RRF socre to select top-5 candidates
    top_results = sorted(scores.keys(), key=lambda d: scores[d], reverse=True)[:5]
    # Assert top-2 documents are docA and docB (tied for highest score)
    assert set(top_results[:2]) == {"docA", "docB"}