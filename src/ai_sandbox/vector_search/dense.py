# Import numpy for vector math operations
import numpy as np

def compute_cosine_similarity(query_vector: np.ndarray, doc_vectors: np.ndarray) -> np.ndarray:
    # Compute dot product between single query vector and multiple document vectors
    dot_products = np.dot(doc_vectors, query_vector)
    # Calculate the Eucliden norm (magnitude) of the query vector using np.linale.norm
    query_norm = np.linalg.norm(query_vector)
    # Calculate the Euclidean norm (magnitude) of each document vector along axis 1 (per row)
    doc_norms = np.linalg.norm(doc_vectors, axis=1)
    # Avoid division by zero by setting a lower floor using np.maximum with a small epsilon
    denom = np.maximum(query_norm * doc_norms, 1e-10)
    # Return cosine similarity scores calcualted as dot product divided by norm product
    return dot_products /denom

