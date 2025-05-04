"""Export functions and configuration classes for working with this web search agent's tools."""

from .search_tool_config import SearchToolConfig
from .tools import create_search_tool

__all__ = [
    "create_search_tool",
    "SearchToolConfig",
]
