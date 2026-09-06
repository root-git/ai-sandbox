# Import json module to parse and validate JSON structure
import json 
# Import pytest framework for running assertiion checks
import pytest
# Import pathlib Path for clean, cross-platfom file path management
from pathlib import Path

# Import dataset creation/loading utilies from the evaluation module
from ai_sandbox.eval.dataset import save_test_dataset

# Define fixture to manage a temporary test dataset file path
@pytest.fixture
def temp_dataset_path(tmp_path: Path) -> Path:
    # Construct a temporary file path inside pytest's isolated tmp_path
    return tmp_path/ "test_dataset.json"

# Test case to verify that saving creating a valid structured JSON file works
def test_save_test_dataset(temp_dataset_path: Path) -> None:
    # Construct a sample dataset with explicit evaluation fields
    sample_data = [
        {
            "question": "What is precision?",
            "reference_context": "Precision measures relevant items.",
            "ground_truth_answer": "Fraction of retrieved instances that are relevant.",
        }
    ]

    # Execute functino under test to write dateset to disk
    save_test_dataset(str(temp_dataset_path), sample_data)

    # Assert that the file was created successfully on disk
    assert temp_dataset_path.exists()

    # Read back saved file contents to verify JSON formatting and contents
    with open(temp_dataset_path, "r", encoding="utf-8") as f:
        # Load serialized contents into Python memory structure
        loaded_data = json.load(f)

    # Validate that loaded structure mathces lengths and keys of original input
    assert len(loaded_data) == 1
    # Verify key structure matches required schema
    assert "question" in loaded_data[0]
    # Verify exact value match for ground truth answer
    assert (
        loaded_data[0]["ground_truth_answer"]
        == "Fraction of retrieved instances that are relevant."
    )
