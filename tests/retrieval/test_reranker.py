# Import unittest mock module to isolate CrossEncoder behavior without loading real weights
from unittest.mock import MagicMock, patch # Provides mocking utilities for testing

# Import the target rerank_chunks function from the retrieval module
from ai_sandbox.retrieval.reranker import (
    rerank_chunks,
) # import function under test

# Apply patch decorator to mock the CrossEncoder class inside reranker module
@patch(
    "ai_sandbox.retrieval.reranker.CrossEncoder"
) # Replace CrossEncoder with mock object
def test_rerank_chunks_top_k(mock_cross_encoder_class: MagicMock) -> None:
    # Create a mock model instance to ne returned by CrossEncoder call
    mock_model = (
        MagicMock()
    ) # Instantiate mock object to simulate model behavior

    # Configure predict method of mock model to return pre-determined score array
    mock_model.predict.return_value = [
        0.1,
        0.9,
        0.4,
        0.8,
    ] # Mock scores for 4 chunks

    # Assign mock model instance as return value when CrossEncoder class is initiaized
    mock_cross_encoder_class.return_value = (
        mock_model # Inject mock model instance
    )

    # Define test input
    query = "python vector search" # Target serach query string
    chunks = [
        "Chunk 1",
        "Chunk 2",
        "Chunk 3",
        "Chunk 4",
    ] # Candidate list of 4 text chunks

    # Execute rerank_chunks asking for top 2 results
    result = rerank_chunks(
        query=query, chunks=chunks, top_k=2
    ) # Call function under test

    # Assert that output contains top 2 highest scoring chunks ("Chunk 2" with 0.9 and "Chunk 4" with 0.8)
    assert result == [
        "Chunk 2",
        "Chunk 4",
    ] # Verify descending order score filtering

    # Apply patch decorator to mock CrossEncoder for empty list test case
    @patch("ai_sandbox.retrieval.reranker.CrossEncoder") # Intercept CrossEncoder init
    def test_rerank_chunks_empty_list(
        mock_cross_encoder_class: MagicMock,
    ) -> None:
        # Create mock model instance 
        mock_model = MagicMock() # Instantiate mock object

        # Configure predict method to return empty array when given no input pairs
        mock_model.predict.return_value = [] # Empty score array

        # Set mock model as output of CrossEncoder contructor call
        mock_cross_encoder_class.return_value = (
            mock_model # Inject mock model instance
        )

        # Execute rerank_chunks with empty candidate list
        result = rerank_chunks(
            query="test query", chunks=[], top_k=5
        ) # Pass empty chunks list

        # Assert that function handles empty input gracefully without throwing errors
        assert result == [] # Output should be empty list