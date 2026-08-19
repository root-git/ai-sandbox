import asyncio
import httpx

async def fetch_data(url: str) -> dict:
    """Fetch a JSON payload asynchronously from the given URL.
    
    Args: 
        url (str): The URL to fetch data from.
    Returns:
        The parsed JSON payload as a dictionary.
    """
    # Open an async HTTP client session (manages connection pool and auto-closes sockets)
    async with httpx.AsyncClient() as client:
        # Send GET request and pause (iyeld to event loop) until network response arrives
        response = await client.get(url)

        # Parse and return JSON payload as a Python dict 
        return response.json()