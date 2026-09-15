import pytest # Import pytest framework for writing unit tests
from ai_sandbox.performance.latency_audit import LatencyAuditor # Import LatencyAuditor class

def test_latency_auditor_cache_hit() -> None:
    """Verify that cache hits record low TTFT and fast total execution time."""
    auditor = LatencyAuditor() # Instantiate the LatencyAuditor
    result = auditor.measure_generation("Test prompt", cahce_hit=True) # Measure generation with cache hit

    assert result["cache_hit"] is True # Confirm cache_hit flag is true
    assert result["ttft"] < 0.02 # Assert TTFT is minimal for cache hits
    assert result["total_time"] <= result["ttft"] + 0.05 # Assert total time is bounded correctly

def test_latency_auditor_cache_miss() -> None:
    """Verify that cache misses record highter TTFT and total execution time."""
    auditor = LatencyAuditor() # Instantiate the LatencyAuditor
    result = auditor.measure_generation("Test prompt", cahce_hit=False) # Measure generation with cache miss

    assert result["cache_hit"] is False # Confirm cache_hit flag is false
    assert result["ttft"] > 0.05 # Assert TTFT reflects generation delay
    assert result["total_time"] > result["ttft"]  # Assert total time exceeds TTFT