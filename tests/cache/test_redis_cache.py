# Import NumPy for array operations and byte serialization
import numpy as np 
# Import pytest to define test cases and assertions
import pytest
# Import the redis client module for mocking or connecting to the instance 
import redis 
# Import the Query class from redis search query modules
from redis.commands.search.query import Query
# Import functions and constants from the implementation module
from ai_sandbox.cache.redis_cache import VECTOR_DIM, create_vector_index

def test_semantic_cache_hit_and_miss():
    # Establish a connection to the local Redis instance running via Docker
    client = redis.Redis(host="localhost", port=6379, db=0)

    # Flush the existing database to ensure a clean test state
    client.flushdb()

    # Create the search index for vector similarity search
    create_vector_index(client)

    # Generate a base embedding vector initialized with floating=point values
    base_vector = np.random.rand(VECTOR_DIM).astype(np.float32)

    # Convert the base vector into raw bytes for storing in Redis
    base_vector_bytes = base_vector.tobytes()

    # Store a sample prompt response payload along with its vector embedding in Redis 
    client.hset(
        "doc:1",
        mapping={
            "vector": base_vector_bytes,
            "response": "This is a cached response from LLM.",
        },
    )

    # Create a query vector identical to the base vector to simulate an exact semantic hit
    query_vector_bytes = base_vector.tobytes()

    # Define a vector similarity search query targeting the top 1 nearest neighbor
    query = (
        Query("*=>[KNN 1 @vector $vec AS score]")
        .sort_by("score")
        .return_fields("response", "score")
        .dialect(2)
    )

    # Execute the search query against the 'idx:cache' nidex with parameters
    results = client.ft("idx:cache").search(
        query, query_params={"vec": query_vector_bytes}
    )

    # Assert that at least one document matched the earch query
    assert len(results.docs) > 0

    # Extract the cosine distnace score returned by Redis Search
    cosine_distance = float(results.docs[0].score)

    # Assert that the cosine distance is strictly below the threshold of 0.10
    assert cosine_distance < 0.10

    # Assert that the returned paylaod matches the expected cached output
    assert results.docs[0].response == "This is a cached response from LLM."