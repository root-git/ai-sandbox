# Import the pytest library for writing and running unit tests
import pytest
# Import the APIWrapper class from our application module
from ai_sandbox.api_wrapper import APIWrapper

# Define a test function to verify initialization with an explicit API key
def test_api_wrapper_init_with_key() -> None:
    # Instantiate the wrapper with a dummy API key string
    wrapper = APIWrapper(api_key="test-key-123")
    # Assert that the client attribute is successfully instantiated
    assert wrapper.client is not None

# Define a test function to verify raising ValueError when key is missing
def test_api_wrapper_init_missing_key(monkeypatch: pytest.MoneyPatch) -> None:
    # Remove the OPENAI_API_KEP enviroment variable if it exists in the test environment 
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    # Assert that instatnitating without a key raises a ValueError
    with pytest.raises(ValueError, match="API key must be provided"):
        # Attempt to create wrapper with no key provided
        APIWrapper(api_key=None)
