import pytest
from pydantic import ValidationError
from ai_sandbox.schemas import AIRequest, ModelConfig, UserProfile


def test_valid_ai_request_parsing():
    """Verify standard valid dictionary instantiation and default fallbacks."""
    data = {
        "request_id": "req-10001",
        "user": {"user_id": "usr_99", "email": "engineer@example.com"},
        "prompt": "Explain Quantum Computing.",
    }
    request = AIRequest(**data)
    assert request.user.email == "engineer@example.com"
    assert request.config.temperature == 0.7  # Verifies default value assignment
    assert request.config.provider == "openai"


def test_invalid_email_format():
    """Verify that malformed email strings trigger ValidationErrors."""
    with pytest.raises(ValidationError):
        UserProfile(user_id="usr_1", email="invalid_email_at_domain")


def test_numeric_range_validation():
    """Verify numeric boundaries (temperature must be <= 2.0)."""
    with pytest.raises(ValidationError):
        ModelConfig(temperature=3.5)


def test_custom_cross_field_model_validator():
    """Verify cross-model validator blocks non-premium users from high temperature."""
    data = {
        "request_id": "req-10002",
        "user": {
            "user_id": "usr_1",
            "email": "user@example.com",
            "is_premium": False,
        },
        "config": {"temperature": 1.8},
        "prompt": "Generate creative story.",
    }
    with pytest.raises(ValidationError) as exc_info:
        AIRequest(**data)
    assert "Non-premium users cannot set temperature above 1.5" in str(
        exc_info.value
    )
