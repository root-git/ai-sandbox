# Import numpy for mock vector generation and assertion testing
import numpy as np
# Import pytest freamwork for assertions and unit test execution
import pytest
# Import the dense search similiarity function from the source module
from ai_sandbox.vector_search.dense import compute_cosine_similarity

def test_compute_cosine_similarity_identical_vectors():
    # Define a 1D mock query vector with 3 dimensions
    query = np.array([1.0,0.0, 0.0])
    # Define document vectors where the first document is identical to the query
    docs = np.array([[1.0,0.0,0.0], [0.0, 1.0,0.0]])
    # Compute similarity scores using the target function
    scores = compute_cosine_similarity(query, docs)
    # Assert that identical vector has a cosine similarity of 1.0
    assert pytest.approx(scores[0], abs=1e-5) == 1.0
    # Asssert that orthogonal vector has a cosine similarity of 0.0
    assert pytest.approx(scores[1], abs=1e-5) == 0.0

def test_top_20_candidate_retrieval():
    # Set seed for reproducible random vector generation
    np.random.seed(42)
    # Generate a random query vector of dimension 128
    query = np.random.randn(128)
    # Generate 100 random document vectors of dimension 128
    docs = np.random.randn(100,128)
    # Compute similarity scores across all 100 candidate documents
    scores = compute_cosine_similarity(query, docs)
    # Sort indices in dscending order to retrieve top candidates
    top_20_indices = np.argsort(scores)[::-1][:20]
    # Assert that exactly 20 candidate indices are retrieved
    assert len(top_20_indices) == 20