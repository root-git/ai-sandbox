# Import MagicMock and patch from unittest.mocj to stub OpenAI API responses
from unittest.mock import MagicMock, patch

# Import the pytest for executing automated test suites
import pytest

# Import the target Pydantic schema class from the strict parase module
from ai_sandbox.schema_enforcement.strict_parser import (
    ExtractEntity,
    run_strict_parser,
)

# Define a unit test function to verify parsed responses with a mocked client
def test_extract_entity_parsing():
    # Instantiate a test object representing expected parsed data
    expected_data = ExtractEntity(name="Apple Inc.", entity_type="Organization")

    # Create a mock object representing the parsed message attribute
    mock_message = MagicMock()
    # Assign the expected Pydantic instance directly to the parsed attribute
    mock_message.parsed = expected_data

    # Create a mock object representing a choice element in the API response
    mock_choice = MagicMock()
    # Attach the mock message to the message attribute of the mock choice
    mock_choice.message = mock_message

    # Create a mock response object to hold the choices list
    mock_response = MagicMock()
    # Assign a real Python list containing mock_choice so index [0] resolves properly
    mock_response.choices = [mock_choice]

    # Patch the OpenAI class directly in the strict_parser module
    with patch(
        "ai_sandbox.schema_enforcement.strict_parser.OpenAI"
    ) as mock_openai_cls:
        # Create a mock client instance to represent the OpenAI client
        mock_client = MagicMock()
        # Wire OpenAI() constructor call to return our mock client instance
        mock_openai_cls.return_value = mock_client
        # Wire parse() call to return our mock_response object containing real list indexing
        mock_client.beta.chat.completions.parse.return_value = mock_response

        # Call the target function to run execution under test
        result = run_strict_parser()

        # Assert that the output matches the expected model instance
        assert isinstance(result, ExtractEntity)
        # Verify that the extracted entity name matches expectations
        assert result.name == "Apple Inc."