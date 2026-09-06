# Import standard json module to support JSON file writing and reading
import json
# Import standard type annotations for strict static typing
from typing import Dict, List

# Define function to serialize and persist test dataset cases to disk
def save_test_dataset(
        file_path: str, dataset: List[Dict[str,str]]
) -> None:
    # Open target file path in write mode using UTF-8 encoding context manager
    with open(file_path, "w", encoding="utf-8") as f:
        # Dump Python dataset list into JSON file f with formatted 2-space indentation
        json.dump(dataset, f, indent=2)

# Define function to load saved test dataset back from disk for evaluation runs
def load_test_dataset(file_path: str) -> List[Dict[str, str]]:
    # Open existing dataset file path in read mode using UTF-8 encoding
    with open(file_path, "r", encoding="utf-8") as f:
        # Parse JSON file contents back into Python memory list of dictionaries
        return json.load(f)
    