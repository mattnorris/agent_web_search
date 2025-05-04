"""Configure the package using environment variables."""

import logging
import os
from types import SimpleNamespace

from decouple import config

from agent_web_search.config import LOG_LEVEL

logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)

LANGSMITH_ENDPOINT = config(
    "LANGSMITH_ENDPOINT", default="https://api.smith.langchain.com"
)
logger.debug("LangSmith endpoint: %s", LANGSMITH_ENDPOINT)

# LangSmith expects the tracing option to be a string, not a boolean.
LANGSMITH_TRACING_OPTIONS = SimpleNamespace(TRUE="true", FALSE="false")

should_trace = config(
    "LANGSMITH_TRACING", default=LANGSMITH_TRACING_OPTIONS.FALSE, cast=bool
)
LANGSMITH_TRACING = (
    LANGSMITH_TRACING_OPTIONS.TRUE if should_trace else LANGSMITH_TRACING_OPTIONS.FALSE
)

# Require the API key and project name if tracing is enabled.
LANGSMITH_API_KEY = config("LANGSMITH_API_KEY") if should_trace else ""
LANGSMITH_PROJECT = config("LANGSMITH_PROJECT") if should_trace else ""

# Configure LangSmith to explicitly add the tracer if not using the environment variables.
LANGSMITH_SHOULD_EXPLICITLY_ADD_TRACER = config(
    "SHOULD_EXPLICITLY_ADD_TRACER", default="false", cast=bool
)

# If the LangSmith tracer is not explicitly added, set the secrets in the environment.
if not LANGSMITH_SHOULD_EXPLICITLY_ADD_TRACER:
    os.environ["LANGSMITH_API_KEY"] = LANGSMITH_API_KEY
    os.environ["LANGSMITH_ENDPOINT"] = LANGSMITH_ENDPOINT
    os.environ["LANGSMITH_PROJECT"] = LANGSMITH_PROJECT
    os.environ["LANGSMITH_TRACING"] = LANGSMITH_TRACING
