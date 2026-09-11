# Import pytest framework for assertion and testing functionality
import pytest # Testing framework for running evaluation assertions

# Import the implementation functions to benchmark chunking and evaluation behavior
from ai_sandbox.retrieval.chunking_experiment import ( # Functions under test
    create_chunks, # FUnction to generate text chunks
    evaluate_chunk_performance, # Function to calculate chunk retrieval recall
    )

# Test case to verify that different chunk sizes generate expected chunk counts and bounds
def test_create_chunk_sizing():
    # Define a synthetic document long enough to rpoduce multiple chunks acroos sizes
    sample_document = "Artificai Intelligence " * 200 # Repeated text string for test

    # Generate chunks for a small token size limit
    chunks_small = create_chunks(sample_document, chunk_size=250, chunk_overlap=20)

    # Generate chunks for a larger token size limit
    chunks_large = create_chunks(sample_document, chunk_size=1000, chunk_overlap=20)

    # Assert that smaller chunk sizes produce a higher number of total chunks
    assert len(chunks_small) > len(chunks_large) # Smaller chunk size mush yield higher chunk density

# Test case to benchmark and compare recall performance across chunk configurations
def test_chunking_experiment_benchmark():
    # Define a corpus containing a target key phrase embedded in surrounding text
    corpus = "Information REtrieval system use indexing. Empirical benchmarking determines optimal parameters over guesswork. Chunking strategies dictate vector density." # Sample corpus

    # Specify the target query phrase to search for in retrieval evaluation
    query = "Empirical benchmarking" # Target query string

    # Run experiment on 250 token configuration 
    chunks_250 = create_chunks(corpus, chunk_size=250, chunk_overlap=10) # Generate 250-token chunks
    score_250 = evaluate_chunk_performance(chunks_250, query) # Score retrieval for 250 config

    # Run experiment on 500 token configuration 
    chunks_500 = create_chunks(corpus, chunk_size=500, chunk_overlap=10) # Generate 500-token chunks
    score_500 = evaluate_chunk_performance(chunks_500, query) # Score retrieval for 500 config

    # Run experiment on 250 token configuration 
    chunks_1000 = create_chunks(corpus, chunk_size=1000, chunk_overlap=10) # Generate 1000-token chunks
    score_1000 = evaluate_chunk_performance(chunks_1000, query) # Score retrieval for 1000 config

    # Verify that valid float scores between 0.0 and 1.0 are returned for all configurations
    assert 0.0 <= score_250 <= 1.0 # Assert 250 configuration returns valid recall score
    assert 0.0 <= score_500 <= 1.0 # Assert 500 configuration returns valid recall score
    assert 0.0 <= score_1000 <= 1.0 # Assert 1000 configuration returns valid recall score