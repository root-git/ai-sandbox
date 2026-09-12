# Import typing primitives for definiting structured function signatures and output containers
from typing import Any, Dict, List # Standard library type hint annotations

# Import the character-based text splitter to divide raw text into manageable token chunks
from langchain_text_splitters import RecursiveCharacterTextSplitter # Splitting utility from LangChain

# define a function to split long source text into configurable text chunks
def create_chunks(text: str, chunk_size: int, chunk_overlap: int =50) -> List[str]:
    # Instatiate the splitter with specific chunk length and overlay bounds
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap) # Configured splitter instance

    # Execute the text splitting process and return the resulting chunk array
    return splitter.split_text(text) # list of string chunks matching specified sizes

# Define an evaluation function to calculate retrieval hit rate for a query against generated chunks
def evaluate_chunk_performance(chunks: List[str], ground_truth_query: str) -> float:
    # Check if the query target string is contained within any of the generated text chunks
    hits = [chunk for chunk in chunks if ground_truth_query.lower() in chunk.lower()] # Filter chunks matching query

    # Calculate simple recall socre based on hit presence relative to total chunk count
    return len(hits)/len(chunks) if chunks else 0.0 # Precision/Recall ratio score as float
