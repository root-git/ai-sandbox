# Import pytest framework for unit test execution and assertion
import pytest

# Import the target recursive text chunking function to test
from ai_sandbox.text_processing.chunker import recursive_chunk_text

# Define test case verifying splitting behavior across paragraph boundaries 
def test_recursive_chunk_text_splits_and_overlaps():
    # Construct multi-paragraph sample raw markdown string
    sample_text = "Paragraph 1 line text.\n\nParagraph 2 line text.\n\nParagraph line text."

    # Execute chunker function with small max size to force split with overlap
    result = recursive_chunk_text(sample_text, max_chunk_size=45, overlap=20)

    # Assert that text was successfully split into muliple distinct chunks
    assert len(result) > 1
    # Verify first chunk contains expected strating paragraph text
    assert "Paragraph 1 line text." in result[0]

# Define test case verifying short text within limits returns single chunk
def test_recurisve_chunk_text_single_chunk():
    # Construct short sinlge-paragraph sample text
    short_text = "Short single text blocks."

    # Execute chunker with large max size budget
    result = recursive_chunk_text(short_text, max_chunk_size=500, overlap=50)

    # Assert that full text returns within a single chunk element
    assert len(result) == 1
    # Assert that content matches original input exactly
    assert result[0] == short_text