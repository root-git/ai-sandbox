import pytest # import pytest testing framework for assertions
from ai_sandbox.graph.state import (
    GraphState,
) # Import GraphState dictionary schema to test structure

# Test initialization and typing validation logic for GraphState dictionary creation
def test_graph_state_initialization() -> None:
    # Construct an instance of GraphState matching the schema
    state: GraphState = {
        # Initialize query history with a starting sample query
        "query_history": ["What is LangGraph?"],
        # Initialize retrieved documents list with dummy context
        "retrieved_documents": ["Doc 1: LangGraph introduction."],
        # Initialize generation steps list with the first step
        "generation_steps": ["step_1_retrieval"],
    }

    # Assert that query_history is correctly stored as a list with expected element
    assert state["query_history"] == ["What is LangGraph?"]
    # Assert that retrieved_documents contains the correct initial document item
    assert state["retrieved_documents"] == ["Doc 1: LangGraph introduction."]
    # Assert that generation_steps contains the expected initial pipeline step
    assert state["generation_steps"] == ["step_1_retrieval"]
