import pytest
import respx
from httpx import Response
from ai_sandbox.concurrent_fetch import fetch_all

@pytest.mark.asyncio
@respx.mock
async def test_fetch_all_success():
    # 1. Mock the target endpoints
    urls = [f"https://api.example.com/item/{i}" for i in range(5)]
    for url in urls:
        respx.get(url).mock(return_value=Response(200, json={"status": "ok"}))

    # 2. Execute fetch_all
    results = await fetch_all(urls)

    # 3.Assert expected output structure
    assert len(results) == 5
    assert all(item == {"status": "ok"} for item in results)