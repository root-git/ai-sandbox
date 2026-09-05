import operator # Provides built-in functions for operations like addition/concatenation
from typing import(
    Annotated,
    TypedDict,
) # import Annotated for metadata attachment and TypeDict for state schema definition

# Define the central state object schema for the LangGraph state machine
class GraphState(TypedDict):
    # Track the history of user and assistant queries as an append-only list of strings
    query_history: Annotated[list[str], operator.add]
    # Track retrieved documents from vector search or context retrieval using operator.add
    retrieved_documents: Annotated[list[str], operator.add]
    # Track intermediate execution steps or reasoning trajectories during generation using operator.add
    generation_steps: Annotated[list[str], operator.add]
