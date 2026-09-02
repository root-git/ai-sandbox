# Import the CrossEncoder class from sentence_transformers library for full cross-attention scoring
from sentence_transformers import CrossEncoder # Enables simultaneous query-document encoding

# Define function to rerank top chunks based on query-document cross-attention scoring
def rerank_chunks(query: str, chunks: list[str], top_k:  int =5) -> list[str]:
    # Initialize CrossEncoder model with BAAI/bge-reranker-base weights
    model = CrossEncoder("BAAI/bge-reranker-base") # Load transformer reranker model into memory

    # Construct input pairs of [query, chunk] for cross-attention evaluation
    pairs = [
        [query, chunk] for chunk in chunks
    ] # Format each chunk into a query-document pairs

    # Compute similarity scores across all query-document pairs
    scores = (
        model.predict(pairs)
    ) # Evaluate full cross-attention and return numpy array of scores

    # Pair each score back with its original chunk string
    scored_chunks = list(
        zip(scores, chunks)
    ) # Create typlie list of (scorem chunk_text)

    # Sort pairs in descending order based on score
    scored_chunks.sort(
        key=lambda x: x[0], reverse=True
    ) # Order highest scores first

    # Extract and return only the text of the top k highest scoring chunks
    return [
        chunk for _, chunk in scored_chunks[:top_k]
    ]  # Slice top_k elements and unwrap chunk text

