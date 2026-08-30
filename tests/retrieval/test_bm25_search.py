# Import pytest module for assertion processing and test routing
import pytest

# Import search_bm25 function from the implementation module
from ai_sandbox.retrieval.bm25_search import search_bm25

# Define test function to verify top keyword matches rank highest
def test_search_bm25_ranking():
    # Define a sample document corpus with distinct tops
    corpus = [
        "The quick borwn fox jumps over the lazy dog",
        "Python is a popular programming lanfguate for AI and machine learning",
        "Sparse BM25 search scores documents based on exact keyword matches",
        "Dense vector search uses neural network embeddings for sematic similarity",
    ]

    # Define a query targeting specific keywords present in document 3
    query = "bm25 keyword search"

    # Call search_bm25 function with top_k set to 2
    results = search_bm25(corpus=corpus, query=query, top_k=2)

    # Assert that results are returned
    assert len(results) == 2

    # Assert that the most relevant document is ranked first
    top_doc, top_score = results[0]
    assert (
        top_doc
        == "Sparse BM25 search scores documents based on exact keyword matches"
    )

    # Assert that the top match score is positive
    assert top_score > 0.0

# Define test function to verify handling of queries with zero matching terms
def test_search_bm25_no_matches():
    # Define a simple document corpus
    corpus = [
        "Cats and dogs are common household pets",
        "Monkeys live in tropical rainforests",
    ]

    # Define a query with words not present in the corpus
    query = "quantum computing physics"

    # Execute BM25 search for 1 result
    results = search_bm25(corpus=corpus, query=query, top_k=1)

    # Extract score from the top returned document
    _, top_score = results[0]

    # Assert that score is 0.0 when no terms match
    assert top_score == 0.0
