
# Import NumPy for vector manipulations and byte conversions
import numpy as np
# Import the Redis client library to interact with the database
import redis
# Import Vector permission structures from redis search modules
from redis.commands.search.field import VectorField
# Import the Query object from redis.commands.search.query to build vector search queries
from redis.commands.search.query import Query

# Define the dimensions of our embedding vectors (e.g., 1536 for OpenAI models)
VECTOR_DIM = 1536


def create_vector_index(client: redis.Redis) -> None:
    # Initialize index schema definition for Redis Search
    schema = (
        # Define a VectorField named "vector" using HNSW, FLOAT32, and COSINE distance metric
        VectorField(
            "vector",
            "HNSW",
            {
                "TYPE": "FLOAT32",
                "DIM": VECTOR_DIM,
                "DISTANCE_METRIC": "COSINE",
            },
        ),
    )
    # Create the search index on Redis with the specified schema
    client.ft("idx:cache").create_index(schema)