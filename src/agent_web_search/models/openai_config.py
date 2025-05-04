"""OpenAI API Configuration Module.

This module defines the OpenAIConfig class, which is used to configure the OpenAI API client.

It includes attributes for the model ID, API base URL, API key, and API version.

It also includes validation methods for the API key and model ID.
The OpenAIConfig class is a subclass of Pydantic's BaseModel,
which provides data validation and settings management using Python type annotations.

It is used to ensure that the configuration provided is valid and meets the requirements
for using the OpenAI API.
"""

from typing import Optional

from pydantic import BaseModel, Field, HttpUrl, field_validator


class OpenAIConfig(BaseModel):
    """Configuration for OpenAI API.

    Configure the OpenAI API client.

    Attributes:
        model_id (str): The identifier of the model to use.
        api_base (HttpUrl): The base URL for the OpenAI API.
        api_key (str): The API key for authentication.
        api_version (Optional[str]): The API version to use (if applicable, i.e., Azure).

    Methods:
        validate_api_key: Validates the API key.
        validate_model_id: Validates the model ID.
    """

    model_id: str
    api_base: HttpUrl = Field(default="https://api.openai.com/v1")
    api_key: str
    api_version: Optional[str] = Field(default=None)

    @field_validator("api_key")
    @classmethod
    def validate_api_key(cls, api_key: str) -> str:
        """Validates the API key.
        Raises:
            ValueError: If the API key is empty or contains only whitespace.
        """
        if not api_key.strip():
            raise ValueError("API key cannot be empty.")
        return api_key

    @field_validator("model_id")
    @classmethod
    def validate_model_id(cls, model_id: str) -> str:
        """Validates the model ID.
        Raises:
            ValueError: If the model ID is empty or contains only whitespace.
        """
        if not model_id.strip():
            raise ValueError("Model ID cannot be empty.")
        return model_id

    # Pydantic configuration does not need arbirtrary public methods.
    class Config:  # pylint: disable=too-few-public-methods
        """Configuration for this OpenAIConfig model.

        Attributes:
            extra (str): Specifies how to handle extra fields.
            title (str): The title of this config.
            description (str): A description of this config.
        """

        # Allow extra fields in the configuration.
        extra = "ignore"
        title = "OpenAIConfig"
        description = "Configuration for OpenAI API."
