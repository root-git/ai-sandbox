# File: src/ai_sandbox/evaluations/triad_pipeline.py

# Import Dataset container from Hugging Face datasets module
from datasets import Dataset  # Type hint and container wrapper for input data

def evaluate_rag_triad(eval_dataset: Dataset) -> dict:
    # Dynamically import ragas evaluate inside the function to avoid module-level initialization errors
    from ragas import evaluate  # Deferred import to isolate runtime loading
    # Dynamically import core triad metrics from ragas.metrics
    from ragas.metrics import answer_relevance, context_precision, faithfulness  # Individual metric functions
    
    # Define active list of triad evaluation metrics
    metrics = [
        faithfulness,  # Checks factual alignment with context
        answer_relevance,  # Checks direct answer address to prompt
        context_precision,  # Checks ranking accuracy of retrieved chunks
    ]
    
    # Run evaluation over the dataset
    results = evaluate(
        dataset=eval_dataset,  # Hugging Face evaluation dataset
        metrics=metrics,  # Array of triad metric objects
    )
    
    # Return resulting dictionary/dataframe of evaluation scores
    return results