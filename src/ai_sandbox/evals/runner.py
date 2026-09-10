# Import typing helpers for structured function signatures
from typing import Any, Dict

# Define the main function to run automated Raga evaluations on dataset samples
def run_evaluation_pipeline(data_samples: Dict[str, Any]) -> Any:
    # Defer HuggingFace Dataset import inside function to avoid module-level initialization overhead
    from datasets import Dataset

    # Defer Ragas evaluate function import inside function to prevent top-level import failure cascade
    from ragas import evaluate

    # Defer Ragas metrics imports inside function body to avoid top-level third-party dependency issues
    from ragas.metrics import answer_correctness, faithfulness

    # Convert the raw input dictionary containing evaluation samples into a HuggingFaceDataset object
    dataset = Dataset.from_dict(data_samples)

    # Execute evaluation across all dataset items using the specified deferred Ragas metrics
    results = evaluate(
        dataset=dataset, metrics=[faithfulness, answer_correctness]
    )

    # Return the resulting evaluated metrics summary object
    return results