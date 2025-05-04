"""Configure the package using environment variables."""

import logging

from decouple import config
from dotenv import load_dotenv

load_dotenv()

LOG_LEVEL = config("LOG_LEVEL", default=logging.INFO)


# Tavily
TAVILY_API_KEY = config("TAVILY_API_KEY")


# OpenAI
OPENAI_API_KEY = config("OPENAI_API_KEY")
OPENAI_API_BASE = config("OPENAI_API_BASE", default="https://api.openai.com/v1")

# The identifier of the model to use. This is the simple name of the model on OpenAI,
# e.g., "gpt-4o", or the model deployment name on Azure, which can be custom.
OPENAI_MODEL_ID = config("OPENAI_MODEL_ID", default="gpt-4o")

# Azure requires an API version. If we have one, assume we are using Azure.
OPENAI_API_VERSION = config("OPENAI_API_VERSION", default=None)
SHOULD_USE_AZURE = bool(OPENAI_API_VERSION)
