"""Tools for the web search agent."""

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.utilities.tavily_search import TavilySearchAPIWrapper

from .search_tool_config import SearchToolConfig


def create_search_tool(search_tool_config: SearchToolConfig):
    """Get the search tool."""

    # NOTE: Use the search wrapper to avoid environment variable issues.
    wrapper = TavilySearchAPIWrapper(tavily_api_key=search_tool_config.api_key)
    max_results = search_tool_config.max_results

    return TavilySearchResults(api_wrapper=wrapper, max_results=max_results)
