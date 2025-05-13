from pathlib import Path
from types import SimpleNamespace
from typing import Annotated

import streamlit as st
from langchain_core.messages import HumanMessage
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict

from agent_web_search.app import search_agent

CSS_PATH = Path(__file__).parent / "static/css" / "style.css"


def load_css():
    with open(CSS_PATH) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_css()


class State(TypedDict):
    """State for the app."""

    messages: Annotated[list, add_messages]


# Role used by Streamlit to display avatars and messages.
ROLES = SimpleNamespace(
    user="user",
    assistant="assistant",
)

st.title("Web Search")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the chat messages.
for message in st.session_state.messages:
    # Default to assistant role if not specified.
    role = getattr(message, "type", ROLES.assistant)

    with st.chat_message(role):
        st.write(message.content)

# Display the chat input box.
if prompt := st.chat_input("Get the latest news about..."):

    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message(ROLES.user):
        st.write(prompt)

    # Invoke the search and get the assistant response.
    state = State(messages=st.session_state.messages)
    result = search_agent.invoke(state)
    assistant_message = result["messages"][-1]

    # Update the session state with the new message.
    st.session_state.messages.append(assistant_message)
    with st.chat_message(ROLES.assistant):
        st.write(assistant_message.content)
