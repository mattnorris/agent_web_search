from typing import Annotated

import streamlit as st
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict

from agent_web_search.app import search_agent


class State(TypedDict):
    messages: Annotated[list, add_messages]


st.title("Web Search")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    role = getattr(msg, "type", "assistant")
    with st.chat_message(role):
        st.write(msg.content)

if prompt := st.chat_input("What is the latest news about..?"):
    from langchain_core.messages import HumanMessage

    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.write(prompt)

    state = State(messages=st.session_state.messages)
    result = search_agent.invoke(state)
    ai_msg = result["messages"][-1]
    st.session_state.messages.append(ai_msg)
    with st.chat_message("assistant"):
        st.write(ai_msg.content)
