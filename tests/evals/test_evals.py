# Import the pytest testing framework to write standard unit test assertions
import pytest

# Import the runner function that executes the model evaluations and returns metrics
from ai_sandbox.evals.runner import run_evaluation

# Define the unit test function for evaluation output faithfulness
def test_faithfulness_metric_threshold():
    # Execute the evaluation runner to retrieve output scores
    results = run_evaluation()

    # Extract the faithfulness metric score from the results dictionary, defaulting ti 0.0 if absent
    faithfulness_score = results.get("faithfulness", 0.0)

    # Assert that the faithfulness score meets or exceeds the target threshold of 0.85
    assert faithfulness_score >= 0.85, f"Faithfulness score {faithfulness_score} is below required threshold 0.85"
    