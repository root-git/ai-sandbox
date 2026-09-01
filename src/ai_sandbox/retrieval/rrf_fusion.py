# import Dict and List typing constructs for type annotations
from typing import Dict, List

# Define function to calculate RRf scoores given ranked document lists and smoothing constant k
def compute_rrf_scores(ranked_lists: List[List[str]], k:int = 60) -> Dict[str, float]:
    # Initialize an empty dictionary to store cumulative RRF scores per document ID
    rrf_scores: Dict[str, float] = {}
    # Iterate through each candidate document list provided by different retrieval models
    for candidate_list in ranked_lists:
        # Loop over documents with 1-based index reporesenting their rank in the current list
        for rank, doc_id in enumerate(candidate_list, start=1):
            # Fetch existing score for doc_id or default to 0.0 if not present
            current_score = rrf_scores.get(doc_id, 0.0)
            # Add the reciprocal rand score (1 / (k + rank)) to current_score
            rrf_scores[doc_id] = current_score + (1.0 / (k + rank))

    return rrf_scores