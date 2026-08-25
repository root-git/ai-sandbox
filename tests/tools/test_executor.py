# Import pytest framework for assertion and test structure
import pytest
# Import SimpleNamespace to construct lightweight mock objects simulating OpenAI response structures
from types import SimpleNamespace 
# Import the function under test from the target module
from ai_sandbox.tools.executor import execute_tool_call

# Define a dummy tool function to test function execution and argument passing
def add_numbers(a: int, b:int) -> int:
    # Add two integers together and return the result
    return a + b

# Define a test case for executing a mock tool call successfully
def test_executor_tool_call_success():
    # Construct a mock function object containing a tool name and serialized JSON arguments
    mock_function = SimpleNamespace(
        name = "add_numbers",
        arguments ='{"a": 5, "b": 10}'
    )
    # Construct a mock tool_call object wrapping the mock function
    mock_tool_call = SimpleNamespace(function=mock_function)

    # Define a mapping dictionary of tool names to callable functions
    tools_map = {"add_numbers": add_numbers}

    # Call the tool execution function with the mock tool call and map
    result = execute_tool_call(mock_tool_call, tools_map)

    # Assert that the execution result is properly converted to a string output matching expected math
    assert result == "15"