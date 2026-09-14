from unittest.mock import patch # Import patch decorator to mock external function calls during testing
from ai_sandbox.observability.tracing import setup_tracing # Import the tracing setup function from the observability module

@patch("phoenix.launch_app") # Mock the local Phoenix server launch to prevent opening an actual web server during test runs
@patch("openinference.instrumentation.openai.OpenAIInstrumentor.instrument") # Mock the OpenAI instrumentor method to verify its gets called 
def test_setup_tracing(mock_instrument, mock_launch_app) -> None:
    """Validates that both the Phoenix app launcher and OpenAI instrumentor are correctly invoked."""
    setup_tracing() # Call the tracing configuration function

    # Assert that the local Phoenix dashboard launcher was invoked exactly once
    mock_launch_app.assert_called_once()

    # Assert that the OpenAi instrumentor method was called exactly once to wrap execution spans
    mock_instrument.assert_called_once()