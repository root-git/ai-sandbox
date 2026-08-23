# Import the pytest testing framwwork
import pytest
# Import the function tool schema target to test
from ai_sandbox.tools.schemas import weather_tool_schema

# Define a test case to validate the OpenAI tool schema output
def test_weather_tool_schema():
    # Assert that the schema type is a dictionary structure
    assert isinstance(weather_tool_schema, dict)
    # Assert that the schema type is defined as a function
    assert weather_tool_schema["type"] == "function"
    # Assert that the inner function name matches the underlying model name
    assert weather_tool_schema["function"]["name"] == "WeatherQuery"
    # Assert that parameters dictionary contains the 'location' property
    assert "location" in weather_tool_schema["function"]["parameters"]["properties"]