"""Methods for creating the search agent itself."""

from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.graph.graph import CompiledGraph
from langgraph.prebuilt import create_react_agent

from .langchain import LANGSMITH_SHOULD_EXPLICITLY_ADD_TRACER as SHOULD_ADD_TRACER
from .langchain import tracer


def create_search_agent(model, search_tool: TavilySearchResults) -> CompiledGraph:
    """Get the search agent.

    Args:
        model: The model to use for the agent.
        search_tool: The search tool to use for the agent.

    Returns:
        The search agent.
    """
    if SHOULD_ADD_TRACER:
        model.callback_manager.add_handler(tracer)

    return create_react_agent(model, [search_tool])
