# Import pytest for writing and running assertions
import pytest

# Import the routing function under test from the target module path
from ai_sandbox.graph.fallback_router import route_by_reranker_score

def test_route_to_generation_when_above_threshold() -> None:
    # Construct a sample state containing reranker scores where at least one exceeds the 0.7 threshold
    state = {"reranker_scores": [0.4, 0.85, 0.6]}

    # Call the router function with the sample state
    result = route_by_reranker_score(state, threshold=0.7)

    # Assert that execution routes to the generation node when confidence is high
    assert result == "generation_node"

def test_route_to_fallback_when_below_threshold() -> None:
    # Construct a sample state containing reranker scores all below the 0.7 threshold
    state = {"reranker_scores": [0.2, 0.5, 0.69]}

    # Call the router function with the sample state
    result = route_by_reranker_score(state, threshold=0.7)

    # Assert that execution routes to the fallback node when confidence is low
    assert result == "fallback_node"

def test_route_to_fallback_when_scores_empty() -> None:
    # Construct an empty state simulation missing or unpoulated reranker scores
    state = {"reranker_scores": []}

    # Call the router function with the empty state
    result = route_by_reranker_score(state, threshold=0.7)

    # Assert that empty scores safely default to 0.0 and route to fallback_node
    assert result == "fallback_node"