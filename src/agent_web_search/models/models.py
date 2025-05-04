"""Large language modles for the web search agent."""

from langchain_openai import AzureChatOpenAI, ChatOpenAI
from langchain_openai.chat_models.base import BaseChatOpenAI

from .openai_config import OpenAIConfig


def create_model(openai_config: OpenAIConfig) -> BaseChatOpenAI:
    """Get the appropriate model based on the configuration.

    Args:
        openai_config (OpenAIConfig): The OpenAI configuration.

    Returns:
        BaseChatOpenAI: An instance of the appropriate model. If no API version is
        provided, default to ChatOpenAI. Otherwise, use AzureChatOpenAI.
    """
    # If there is no API version, assume we are using OpenAI directly.
    if not openai_config.api_version:
        return ChatOpenAI(
            model=openai_config.model_id,
            openai_api_base=str(openai_config.api_base),
            openai_api_key=openai_config.api_key,
        )

    # Otherwise, assume we are using Azure OpenAI.
    return AzureChatOpenAI(
        azure_deployment=openai_config.model_id,
        azure_endpoint=str(openai_config.api_base),
        api_key=openai_config.api_key,
        api_version=openai_config.api_version,
    )
