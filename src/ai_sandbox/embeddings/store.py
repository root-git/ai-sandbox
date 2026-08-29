# Import the main OpenAi client class from the official SDK to manage API requests
from openai import OpenAI

# Define a function to take text chunks and return a list of floating-point vector embeddings
def create_embeddings(client: OpenAI, chunks: list[str]) -> list[list[float]]:
    # Request vector embeddings from OpenAI API using the specifed lightweight model and text input 
    response = client.embeddings.create(input=chunks, model="text-embedding-3-small")
    # Extract and return the numberical vector float array from each embedding object in the response 
    return [item.embedding for item in response.data]

# Define a function execture an upsert operation for generated vectors and text metadata into the database 
def upsert_vectors(db_connection, vectors: list[list[float]], metadata: list[dict]) -> None:
    # Execute database upsert query to store vectors alongsign corresponding text metadata
    db_connection.execute(" UPSERT INTO vectors (vector, metadata) VALUES (?,?)", (vectors, metadata))
