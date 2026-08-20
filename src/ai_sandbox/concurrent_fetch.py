import asyncio
import httpx 

# Defines a asynchronous coroutine function that takes a shared HTTP client and target URL
async def fetch(client: httpx.AsyncClient, url:str) -> dict:
    # Send an HTTP GET request asynchrounously, pausing execution of this task until the network response arrives
    response = await client.get(url)

    # Parse the response payload from JSON into a Python dictionary and returns it 
    return response.json()

# Defines the entry coroution function that takes a list of URLs and retyrns a list of dictionaries
async def fetch_all(urls: list[str]) -> list[dict]:
    # Opens an async context manager that crates and automatically closes a persistent HTTP client session 
    async with httpx.AsyncClient() as client:
        # Uses a list comprehension to instantiate a list of unwaited fetch coroutine objects for each URL
        tasks =[fetch(client, url) for url in urls]

        # Unpacks the coroutine list into asyncio.gather, executing all 5 requests concurrently and awaiting their aggregated results
        results = await asyncio.gather(*tasks)

        # Returns the gathered list of parsed JSON responses back to the caller
        return results