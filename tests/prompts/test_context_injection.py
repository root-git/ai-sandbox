# Import pytest framework for assertion and test runner capabilities
import pytest

# Import the grounded prompt generator function to test target behavior
from ai_sandbox.prompts.context_injection import generate_grounded_prompt

# Define unit test verifying correctly assembled grounded prompts
def test_generate_grounded_prompt_formatting():
    # Define sample context chunks representing retrieved facts
    sample_context = "The AI sandox runs on Python 3.11 with uv."

    # Define a sample user query targeting the context facts
    sample_query = "What python version is used?"

    # Call the prompt generation function to obtain formatted output
    prompt = generate_grounded_prompt(sample_context, sample_query)

    # Assert that system instrictions enforing zero-hallucination boundary exist in prompt
    assert "Answer using ONLY the facts in [CONTEXT]" in prompt

    # Assert that fallback instructions for unknown facts exist in prompt
    assert "If unknown, state 'Insufficient Context'." in prompt

    # Assert that provided context chunks are properly embedded under context tag
    assert f"[CONTEXT]: {sample_context}" in prompt

    # Assert that user query is properly embedded under query tag
    assert f"[USER QUERY]: {sample_query}" in prompt
    