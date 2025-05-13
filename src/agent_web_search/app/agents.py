"""Create the actual agent graph for web search."""

from agent_web_search.agents import create_search_agent
from agent_web_search.config import (
    OPENAI_API_BASE,
    OPENAI_API_KEY,
    OPENAI_API_VERSION,
    OPENAI_MODEL_ID,
    TAVILY_API_KEY,
)
from agent_web_search.models import OpenAIConfig, create_model
from agent_web_search.tools import SearchToolConfig, create_search_tool

# Create the large language model (LLM) for the agent.
openai_config = OpenAIConfig(
    model_id=OPENAI_MODEL_ID,
    api_base=OPENAI_API_BASE,
    api_key=OPENAI_API_KEY,
    api_version=OPENAI_API_VERSION,
)
model = create_model(openai_config)

# Create the search tool for the agent.
search_tool_config = SearchToolConfig(api_key=TAVILY_API_KEY)
search_tool = create_search_tool(search_tool_config)

# Create the search agent itself, a graph.
search_agent = create_search_agent(model, search_tool)
