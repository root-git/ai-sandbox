# Import the OpenAI client for executing structured API calls
from openai import OpenAI
# Import BaseModel from Pydantic to define the target output schema
from pydantic import BaseModel


# Define the target schema to enforce on the model response
class ExtractEntity(BaseModel):
    # Field to capture the name of the extracted entity
    name: str
    # Field to capture the type/category of the extracted entity
    entity_type: str

# Encapsulate API execution insde a function to avoid module-level initialization errors
def run_strict_parser() -> ExtractEntity:
    # Initialize the standard OpenAi API client instance at runtime
    client = OpenAI()

    # Call the beta chat completions endpoint with structured parsing
    response = client.beta.chat.completions.parse( 
    # Specify an OpenAI model version supporting structured outputs
    model ="gpt-4o-2024-08-06", 
    # Pass the list of chat messages for execution
    messages=[
        # System message establising the role of the assistant 
        {"role": "system", "contenxt": "Extract the primary entity."},
        # User message containing the input text to parse
        {"role": "user", "content": "Apple Inc. released a new product."},
    ],
    # Enforce strict parsing against the Pydantic schema using response_format
    response_format=ExtractEntity, 
    )

    # Access the automatically validated ExtractEntity object from the response choice
    return response.choices[0].message.parsed