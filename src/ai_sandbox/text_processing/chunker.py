# Importing typing modules needed for type annotations on fucntion sugnatures
from typing import List

# Define recursive text chunker splitting on double new lines with target overlap
def recursive_chunk_text(text: str, max_chunk_size: int = 500, overlap: int =50) -> List[str]:
    # splite the raw input string on double newlines to isolate paragraph blocks
    blocks = text.split("\n\n")
    # Initialize the list that will store all finalized chunk strings
    chunks =[]
    # Initialize a temporary list to hold paragraphs for the active chunk
    current_chunk =[]
    # Initialize an integer counter tracking total characters/tokens in current_chunk
    current_length = 0

    # Loop through each paragraph block extracted from the source document
    for block in blocks:
        # Calculate the length of the individual paragraph block
        block_length = len(block)

        # Check if adding the new block exceeds the defined maximum chunk boundary
        if current_length + block_length > max_chunk_size and current_chunk:
            # Combine current paragraph blocks with double newlines and save to output
            chunks.append("\n\n".join(current_chunk))
            # Keep the last block from current_chunk to provide context overlap for the next chunk
            current_chunk = [current_chunk[-1]]
            # Recalculate length of current_chunk using remaining overlapping block
            current_length = sum(len(b) for b in current_chunk)

        # Append the new block into the current working chunk list
        current_chunk.append(block)
        # Update current accumulated character count with the newly added block length
        current_length += block_length

    # Check if there are remaining unprocessed paragraph blocks after iteration finishes
    if current_chunk:
        # Join any remaining paragraph blocks and append the final chunk to results
        chunks.append("\n\n".join(current_chunk))

    # Return the aggregated list of string chunks back to caller
    return chunks
