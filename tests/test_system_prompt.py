# Import pytest for wrting assertions and running tests
import pytest

# Import the traget function to test from the prompts module
from src.ai_sandbox.system_prompt import build_system_prompt

# Define a test function to verify correct parameter inject into prompt template
def test_build_system_prompt_success():
    # Define a sample system prompt template with string placeholders
    template = "You are an assistant for {user_name}. Current date is {current_date}"

    # Call build_system_prompt with dynamic keyword arguments
    result = build_system_prompt(
        template, user_name = "Lulu", current_date="2026-08-22"
    )

    # Define the expected formatted output string
    expected = "You are an assistant for Lulu. Current date is 2026-08-22"

    # Assert that the function output matches the expected formatted string
    assert result == expected

# Define a test function to verify handling of extra unused keyword arguments
def test_build_system_prompt_unused_kwargs():
    # Define a simple template with only one dynamic parameter
    template = "Hello {name}!"

    # Call the build_system_prompt function passing extra unused dynamic arguments
    result = build_system_prompt(template, name="Lulu", extra_param="ignored")

    # Assert that the template formats successfully while ignoring extra parameters
    assert result == "Hello Lulu!"

