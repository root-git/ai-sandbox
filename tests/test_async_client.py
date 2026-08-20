import pytest
from unittest.mock import AsyncMock, patch
import httpx

# Import the fetch_data function from the async_client module
from ai_sandbox.async_client import fetch_data

@pytest.mark.asyncio
async def test_fetch_data_success():
    """Test successful JSON data retrieval from a valid endpoint."""
    mock_payload = {"status": "ok", "items": [1, 2, 3]}

    # Create a mock response object with a json() method returning the payload
    mock_response = AsyncMock()
    mock_response = httpx.Response(200, json=mock_payload)
    
    # Patch https.AsyncClient.get to avoid making real network requests
    with patch("httpx.AsyncClient.get", return_value=mock_response) as mock_get:
        test_url = "https://api.example.com/data"
        result = await fetch_data(test_url)

        # Assert client called with correct URL and returned expected dictionary
        mock_get.assert_called_once_with(test_url)
        assert result == mock_payload
        assert isinstance(result, dict)

@pytest.mark.asyncio
async def test_fetch_data_http_error():
    """Test exception propagation when the GET request raises an HTTP error."""
    with patch("httpx.AsyncClient.get") as mock_get:
        # Simulate an HTTP 404 error on request execution
        mock_get.side_effect = httpx.HTTPStatusError(
            message="404 Not Found",
            request=AsyncMock(),
            response=httpx.Response(404),
        )

        # Verify that HTTPStatusError is raised to the caller
        with pytest.raises(httpx.HTTPStatusError):
            await fetch_data("https://api.example.com/not-found")


            


