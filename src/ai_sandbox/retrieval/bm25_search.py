# import BM250kapi class from rank_bm25 package for rank calculations
from rank_bm25 import BM25Okapi

# Define function to compute search scores using BM25
def search_bm25(
        corpus: list[str], query: str, top_k: int = 20
) -> list[tuple[str,float]]:
    # Tokenize each document in the corpus by splitting text on whitespace
    tokenized_corpus = [doc.lower().split() for doc in corpus]

    # Initialize the BM250kapi index with the tokenized document corpus
    bm25 = BM25Okapi(tokenized_corpus)

    # Tokenize the input seach query string into indvidual lowercase tokens
    tokenized_query = query.lower().split()

    # Calculate relevance scores for all documents given the tokenized query
    scores = bm25.get_scores(tokenized_query)

    # Pair each original document string with its corresponding BM25 score
    doc_scores = list(zip(corpus, scores))

    # Sort documents descending by score and slide the top k results
    ranked_results = sorted(doc_scores, key=lambda item: item[1], reverse=True)[
        :top_k
    ]

    # Return top ranked document-score pairs
    return ranked_results