import streamlit as st

from agent_web_search.app.graph import graph

# from decouple import config

# from agent_web_search.agents import get_search_agent
# from agent_web_search.models import OpenAIConfig, get_model
# from agent_web_search.tools import SearchToolConfig, get_search_tool


# OPENAI_API_KEY = config("OPENAI_API_KEY")
# TAVILY_API_KEY = config("TAVILY_API_KEY")

# # Create the model.
# openai_config = OpenAIConfig(
#     model_id="gpt-4o",
#     api_key=OPENAI_API_KEY,
# )
# model = get_model(openai_config)

# # Create the search tool.
# search_tool_config = SearchToolConfig(api_key=TAVILY_API_KEY)
# search_tool = get_search_tool(search_tool_config)

# # Create the agent.
# graph = get_search_agent(model, search_tool)

# Streamlit UI
st.title("Basic Chat with Web Search")
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("What's the latest news?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    response = graph.invoke({"input": prompt})
    answer = response["output"]

    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.chat_message("assistant").write(answer)
