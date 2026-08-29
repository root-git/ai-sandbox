# Import the pytest library for running unit test assertions
import pytest
# Import MagicMock to mock the external OpenAI API call
from unittest.mock import MagicMock
# Import the custom function under test from the application module
from ai_sandbox.embeddings.store import create_embeddings

# Define a unit test function to verify embedding creation logic without calling external APIs
def test_create_embeddings():
    # Instantiate a mock OpenAI client instance
    mock_client = MagicMock()
    # Mock the return object structure for client.embeddings.create
    mock_response = MagicMock()
    # Define a dummy embedding vector to simulate OpenAI API return data
    mock_item = MagicMock()
    # Assign a sample vector list to the mock item's embedding attribute
    mock_item.embedding = [0.1, 0.2, 0.3]
    # Attach mock data array to the mocked API response object
    mock_response.data = [mock_item]
    
    # Set the mocked API client call to return our custom mock response
    mock_client.embeddings.create.return_value = mock_response

    # Execute the target function using sample text chunks and mock client
    result = create_embeddings(mock_client, ["test chunk"])

    # Assert that the function extracted and returned the correct vector list
    assert result == [[0.1, 0.2, 0.3]]
    # Verify that the API call was executed once with the exact parameters used during execution
    mock_client.embeddings.create.assert_called_once_with(
        input=["test chunk"],
        model="text-embedding-3-small"
    )