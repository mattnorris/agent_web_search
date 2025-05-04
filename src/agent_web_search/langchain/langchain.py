"""Explicitly create a LangChain tracer."""

from langchain_core.tracers import LangChainTracer
from langsmith import Client

from .config import LANGSMITH_API_KEY, LANGSMITH_ENDPOINT, LANGSMITH_PROJECT

# NOTE: Avoid environment variable issues by creating a client and tracer explicitly.
client = Client(api_key=LANGSMITH_API_KEY, api_url=LANGSMITH_ENDPOINT)
tracer = LangChainTracer(project_name=LANGSMITH_PROJECT, client=client)
