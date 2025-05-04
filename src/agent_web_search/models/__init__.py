"""Export functions and configuration classes for working with models."""

from .models import create_model
from .openai_config import OpenAIConfig

__all__ = ["create_model", "OpenAIConfig"]
