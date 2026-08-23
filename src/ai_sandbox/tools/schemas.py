# Import the BaseModel class from pydantic to construct structured schemas 
from pydantic import BaseModel
# Import the openai package to access built-in helper functions
import openai 

# Define a Pydantic model representing function parameters 
class WeatherQuery(BaseModel):
    # Define a location string field for the city name
    location: str

# Convert the Pydantic model into an OpenAi-compatible function tool dictionary
weather_tool_schema = openai.pydantic_function_tool(WeatherQuery)