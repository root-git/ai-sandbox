from datetime import UTC, datetime
from enum import Enum

from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator


class ModelProvider(str, Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"


# Model 1: Leaf Node - User Metadata
class UserProfile(BaseModel):
    user_id: str = Field(..., description="Unique user identifier")
    email: EmailStr = Field(..., description="Valid user email address")
    is_premium: bool = Field(default=False, description="Subscription status")


# Model 2: Leaf Node - LLM Configuration Parameters
class ModelConfig(BaseModel):
    provider: ModelProvider = Field(default=ModelProvider.OPENAI)
    model_name: str = Field(default="gpt-4o", min_length=2)
    temperature: float = Field(
        default=0.7,
        ge=0.0,
        le=2.0,
        description="Sampling temperature between 0.0 and 2.0",
    )
    max_tokens: int = Field(
        default=500,
        ge=1,
        le=4096,
        description="Max token limit for completion",
    )

    # Custom Field Validator: Ensure model name is non-empty after stripping whitespace
    @field_validator("model_name")
    @classmethod
    def validate_model_name(cls, value: str) -> str:
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("Model name cannot be empty or blank space.")
        return cleaned


# Model 3: Root Node - Complete AI Request (Encompasses UserProfile and ModelConfig)
class AIRequest(BaseModel):
    request_id: str = Field(..., min_length=5, description="Unique tracking ID")
    user: UserProfile
    config: ModelConfig = Field(default_factory=ModelConfig)
    prompt: str = Field(..., min_length=3, description="Input user prompt")
    tags: list[str] | None = Field(default_factory=list)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC)
    )

    # Custom Model Validator: Cross-model business constraint validation
    @model_validator(mode="after")
    def check_premium_limits(self) -> AIRequest:
        # Non-premium users cannot execute queries with temperature higher than 1.5
        if not self.user.is_premium and self.config.temperature > 1.5:
            raise ValueError("Non-premium users cannot set temperature above 1.5.")
        return self