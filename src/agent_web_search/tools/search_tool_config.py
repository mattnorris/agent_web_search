"""SearchToolConfig is a Pydantic model for configuring the search tool."""

from pydantic import BaseModel, Field, field_validator


class SearchToolConfig(BaseModel):
    """Configuration for the search tool.

    Attributes:
        api_key (str): The API key for the search tool.
        max_results (int): The maximum number of results to return from the search tool.

    Methods:
        validate_api_key: Validates the API key.
    """

    api_key: str = Field()
    max_results: int = Field(
        default=5,
        ge=1,
        description="The maximum number of results to return from the search tool.",
    )

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

    # Pydantic configuration does not need arbirtrary public methods.
    class Config:  # pylint: disable=too-few-public-methods
        """Configuration for this SearchToolConfig.

        Attributes:
            extra (str): Specifies how to handle extra fields.
            title (str): The title of this config.
            description (str): A description of this config.
        """

        # Allow only the fields defined in this config.
        extra = "forbid"

        title = "SearchToolConfig"
        description = "Configuration for the search tool."
