# Import typing primitives for explicit type annotations
from typing import Dict, Any

# Define the function that constructs a ground system prompt from raw chunks and user query
def generate_grounded_prompt(context_chunks: str, user_query: str) -> str:
    # Set the foundational system instruction restricting responses exclusively to provided context
    system_instruction = (
        "Answer using ONLY the facts in [CONTEXT]. "
        "If unknown, state 'Insufficient Context'."
    )

    # Format and assemble the final grounded context prompt incorporating system rules, context, and query
    formatted_prompt = (
        f"{system_instruction}\n\n"
        f"[CONTEXT]: {context_chunks}\n\n"
        f"[USER QUERY]: {user_query}"
    )

    # Return the assembled, context-bound prompt string
    return formatted_prompt