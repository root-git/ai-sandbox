# Import pytest framework for writing unit tests
import pytest
# Import the function to test from the bounds manager module
from ai_sandbox.context.bounds_manager import truncate_context

# Define test case to ensure chunks fitting withing budget are all preserved
def test_truncate_context_within_budget():
    # Define a list of input context string chunks
    chunks = ["Hello world", "This is a short test sentence."]
    # Set a high token budget that easily fits both bunks
    max_budget = 100
    # Invoke the function to get selected context chunks
    result = truncate_context(chunks, max_budget)
    # Assert that all chunks are retained without truncation
    assert result == chunks

# Define test case to ensure truncation stops once max token budget is exeeded
def test_truncate_context_exceeds_budget():
    # Define a list of input chunks with known token lengths
    chunks = [
        "First chunk with some words.",
        "Second chunk that adds more tokens.",
        "Third chunk that should be excluded due to budget limit."
    ]
    # Set a restrictive token budget allowing only initial chunks
    max_budget = 12
    # Invoke the truncation function with the tight budget constraint
    result = truncate_context(chunks, max_budget)
    # Assert that only the first chunk fitting within 12 tokens is retained
    assert len(result) == 1
    # Verify the specific context retained matches the first item
    assert result[0] == "First chunk with some words."