# Import the base OS module to access system environment variables
import os
# Import the generic Execption class from thhe standard library for error handling
from typing import Any, Dict
# Import the official OpenAI client from the openai library
from openai import OpenAI 

class APIWrapper:
    """A wrapper class to manage API authentication and requests."""

    # Define the initialization method with an optional API key argument
    def __init__(self, api_key: str | None = None) -> None:
        # Rsolve the API key from argument or environment variable
        resolved_key = api_key or os.getenv("OPENAI_API_KEY")

        # Check if a valid API key was found
        if not resolved_key:
            # Raised a ValueError if authentication credentials are missing
            raise ValueError("API key must be provided or set in environment.")

        # Instantiate the OpenAI client with the resoloved API key
        self.client = OpenAI(api_key=resolved_key)