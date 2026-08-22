# Define function that accepts a system prompt template string and dynamic keyword arguments
def build_system_prompt(template: str, **kwargs) -> str:
    # Use str.format() with unpacked kwargs to dynamically inject values into template placeholders
    formatted_prompt: str = template.format(**kwargs)

    # Return the dynamically generated system prompt string
    return formatted_prompt
