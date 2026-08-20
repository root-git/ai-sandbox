import pytest
import logging 
from unittest.mock import patch
from pydantic import BaseModel

# Import parse_jason function 
from ai_sandbox.json_parser import parse_json

# Define a sample Pydantic model to use across test cases
class SampleModel(BaseModel):
    id: int 
    name: str

def test_parse_json_success():
    """Verify successful parsing of a valid JSON string into Pydantic model instance."""
    raw_json = '{"id": 1, "name": "Alice"}'

    result = parse_json(raw_json, SampleModel)

    # Assert model was instantiated correctly
    assert result is not None
    assert isinstance(result, SampleModel)
    assert result.id == 1
    assert result.name == "Alice"

def test_parse_json_validation_error_return_none():
    """Verify that an invalid schema returns None instead of raising ValidationError."""
    raw_json = '{"id": "not_a_number", "name": "Alice"}'

    result = parse_json(raw_json, SampleModel)

    # Assert that validation failure returns None gracefully
    assert result is None

def test_parse_json_malformed_json_returns_none():
    """Verify that malformed JSON syntax returns None."""
    raw_json = '{"id": 1, "name": "Alice"'  # Missing closing brace

    result = parse_json(raw_json, SampleModel)

    # Assert that malformed JSON returns None
    assert result is None

def test_parse_json_logs_error_on_failure(caplog):
    """Verify that an error is logged when validation failks."""
    raw_json = '{"id": "invalid"}'

    # Capture log output during execution at ERROR level
    with caplog.at_level(logging.ERROR):
        result = parse_json(raw_json, SampleModel)

    # Assert that the result is None due to validation failure
    assert result is None

    # Assert that the expected error error log was captured
    assert "JSON validation failed:" in caplog.text