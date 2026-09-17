# Import pytest to utilize testing fixtures and assertion capabilities
import pytest
# Import the functions under test from the deployment module
from ai_sandbox.deployment.cloud_run import get_secret, get_server_config

# Test case for retrieveing an existing environment secret
def test_get_secret_existing(monkeypatch: pytest.MonkeyPatch) -> None:
    # Set a mock environment variable using monkeypatch
    monkeypatch.setenv("API_KEY", "super_secret_val")
    # Assert that get_secre retrieves the expected mock value
    assert get_secret("API_KEY") == "super_secret_val"

# Test case for handling missing environment variables with defaults
def test_get_secret_default() -> None:
    # Assert that requesting an unset key returns the custom default fallback
    assert get_secret("MISSING_KEY", "fallback") == "fallback"

# Test case for server configuration port binding fallback
def test_get_server_config_default(monkeypatch: pytest.MonkeyPatch) -> None:
    # Ensure PORT is cleared from environment for default test
    monkeypatch.delenv("PORT", raising=False)
    # Call get_server_config to get resolved binding dictionary
    config = get_server_config()
    # Assert that host binds to all interfaces and port defaults to integer 8080
    assert config == {"host": "0.0.0.0", "port": 8080}

# Test casefor server configuration dynamtic port binding from environment
def test_get_server_config_custom_port(monkeypatch: pytest.MonkeyPatch) -> None:
    # Simulate GCP Cloud Run injection of dynamic port string
    monkeypatch.setenv("PORT", "9000")
    # Call get_server_config to resolve dynamic port mapping 
    config = get_server_config()
    # Assert that string PORT is correctly cast to integer 9000
    assert config["port"] == 9000