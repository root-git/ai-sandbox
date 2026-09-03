# Import tiktoken for BPE token encoding calculations
import tiktoken

# Define a function to truncate context chunks to remain within a maximum token budget
def truncate_context(chunks: list[str], max_token_budget: int, model_name: str="gpt-4o") -> list[str]:
    # Retrieve the encoding instance corresponding to the specific target LLM model
    encoding = tiktoken.encoding_for_model(model_name)

    # Initialize an empty list to store chunks that fit within budget
    selected_chunks = []
    # Initialize an integer tracker for accumulated tokens
    total_tokens = 0

    # Iterate through each input context chunk sequentially
    for chunk in chunks:
        # Calculate token count by encoding string text into a list of token IDs
        chunk_tokens = len(encoding.encode(chunk))

        # Check if adding the current chunk exceeds the total allowed token budget
        if total_tokens + chunk_tokens > max_token_budget:
            # Stop including further chunks when budget threshold is breached
            break

        # Append valid chunk to our output list
        selected_chunks.append(chunk)
        # Update running accumulator with the new chunk's token count
        total_tokens += chunk_tokens

    # Return the truncated context chunk list
    return selected_chunks