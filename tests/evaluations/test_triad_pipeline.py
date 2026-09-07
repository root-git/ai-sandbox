# File: tests/evaluations/test_triad_pipeline.py

# Import sys module to patch sys.modules before ragas initialization
import sys  # Allows injecting mock modules into sys.modules
# Import MagicMock and patch utilities from standard library
from unittest.mock import MagicMock, patch  # Mocking tools to bypass live Ragas imports
# Import Dataset structure from Hugging Face datasets module
from datasets import Dataset  # Data structure required by pipeline function

# Pre-emptively mock ragas in sys.modules to prevent Python 3.14 / langchain_community import crashes
mock_ragas = MagicMock()  # Create generic mock container for ragas package
sys.modules["ragas"] = mock_ragas  # Register mock ragas in sys.modules runtime registry
sys.modules["ragas.metrics"] = MagicMock()  # Register mock ragas.metrics sub-module

# Import function under test directly from ai_sandbox (without 'src.')
from ai_sandbox.evaluations.triad_pipeline import evaluate_rag_triad  # Target function to test

def test_evaluate_rag_triad_execution():
    # Construct mock dataset containing typical RAG triad fields
    dummy_data = {
        "question": ["What is RAG?"],  # User query list
        "contexts": [["RAG stands for Retrieval-Augmented Generation."]],  # Context list
        "answer": ["RAG is Retrieval-Augmented Generation."],  # Generated answer
        "ground_truth": ["RAG means Retrieval-Augmented Generation."]  # Truth standard
    }
    # Convert Python dictionary into a Hugging Face Dataset object
    eval_dataset = Dataset.from_dict(dummy_data)  # Standard data structure for evaluation
    
    # Configure mock evaluate return dictionary on the injected ragas module
    mock_ragas.evaluate.return_value = {
        "faithfulness": 1.0,  # Max score for faithfulness
        "answer_relevance": 1.0,  # Max score for answer relevance
        "context_precision": 1.0  # Max score for context precision
    }
    
    # Execute target evaluation function
    results = evaluate_rag_triad(eval_dataset)  # Run pipeline under test
    
    # Verify that mock ragas.evaluate was called exactly once
    mock_ragas.evaluate.assert_called_once()  # Asserts evaluate runner execution
    
    # Assert return object contains expected evaluation metric keys
    assert "faithfulness" in results  # Ensure faithfulness metric key exists
    assert "answer_relevance" in results  # Ensure answer_relevance metric key exists
    assert "context_precision" in results  # Ensure context_precision metric key exists