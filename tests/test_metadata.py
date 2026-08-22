# Import pytest framework for assertions and test orchestration
import pytest 
# Import metadata extraction function and model from core module
from src.ai_sandbox.metadata import LLMMetadata, extract_metadata

# Test metadata extraction logic with a mock standard LLM payload
def test_extract_metadata_success():
    # Define mock API payload matching standard provider usage response 
    mock_payload = {"usage": {"prompt_tokens": 1000, "completion_tokens": 500}}
    # Define start timestamp anchor
    start = 100.0
    # Define end timestamp anchor simulating 1.5 s execution time
    end = 101.5

    # Run extraction function on mock parameters
    result = extract_metadata(mock_payload, start, end)

    # Assert accurate calculation of execution latency
    assert result.latency_seconds == 1.5
    # Assert exact extraction of prompt tokens
    assert result.prompt_tokens == 1000
    # Assert exact extraction of completion tokens
    assert result.completion_tokens == 500
    # Assert correct summation of total tokens
    assert result.total_tokens == 1500
    # Assert total calculated cost matches expected formula result (1.5 + 1.0 = $0.0025)
    assert result.total_cost_usd == pytest.approx(0.0025)