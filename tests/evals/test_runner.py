
# Import sys module to dynamically manipulate loaded Python modules
import sys
# Import MagicMock to create mocked dependencies
from unittest.mock import MagicMock

# Define expected dictionary output from the evaluation function
mock_results = {"faithfulness": 0.95, "answer_correctness": 0.88}

# Create a mock evaluation function that explicitly returns the results dictionary
mock_evaluate = MagicMock(return_value=mock_results)

# Create a mock ragas module object
mock_ragas = MagicMock()
# Bind the mock evaluate function to the mock ragas module
mock_ragas.evaluate = mock_evaluate

# Register the mock ragas module directly into sys.modules
sys.modules["ragas"] = mock_ragas
# Register mock metrics into sys.modules to allow deferred importing
sys.modules["ragas.metrics"] = MagicMock()

# Import the target runner function after setting up sys.modules
from ai_sandbox.evals.runner import run_evaluation_pipeline


# Define unit test to verify pipeline execution and score extraction
def test_run_evaluation_pipeline():
    # Construct sample test data dictionary matching Ragas structure
    sample_data = {
        "question": ["What is automated evaluation?"],
        "contexts": [["Automated evaluation turns subjective quality into objective metrics."]],
        "answer": ["It converts subjective quality into numeric metrics."],
        "ground_truth": ["Automated evaluation turns subjective output quality into objective numeric metrics."],
    }

    # Execute evaluation pipeline runner function using mocked Ragas module
    results = run_evaluation_pipeline(sample_data)

    # Assert that faithfulness score matches expected mocked dictionary value
    assert results["faithfulness"] == 0.95
    # Assert that answer correctness score matches expected mocked dictionary value
    assert results["answer_correctness"] == 0.88