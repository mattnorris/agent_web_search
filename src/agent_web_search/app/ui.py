"""Streamlit UI for the Web Search Agent."""

from pathlib import Path
from types import SimpleNamespace
from typing import Annotated

import streamlit as st
from langchain_core.messages import HumanMessage
from langgraph.graph.message import add_messages
from streamlit import chat_input, chat_message, session_state, write
from typing_extensions import TypedDict

from agent_web_search.app import search_agent

CSS_PATH = Path(__file__).parent / "static/css" / "style.css"


# NOTE: This is not called currently because there is a visible delay when loading the customn font.
def load_css():
    """Load the CSS file and apply it to the Streamlit app."""
    with open(CSS_PATH, encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


class State(TypedDict):
    """State for the app."""

    messages: Annotated[list, add_messages]


# Role used by Streamlit to display avatars and messages.
ROLES = SimpleNamespace(
    user="user",
    assistant="assistant",
)

# NOTE: The avatars are not used currently because of a Replit issue.
# External images are not displayed.
AVATARS = SimpleNamespace(
    user="https://github.com/mattnorris.png",
    assistant="https://external-content.duckduckgo.com/ip3/tavily.com.ico",
)

TITLE = "Web Search Agent"

st.set_page_config(
    page_title=TITLE,
    page_icon="🤖",
)

st.title(TITLE)

if "messages" not in session_state:
    session_state.messages = []


def run(
    messages: list,
    roles: SimpleNamespace = ROLES,
    # avatars: SimpleNamespace = AVATARS,
):
    """Run the Streamlit app.

    This function is responsible for displaying the chat messages and handling user input.

    It is defined as a separate function so that variables can be passed in,
    making its loop more efficient.

    Args:
        messages (list): List of chat messages.
        roles (SimpleNamespace): Roles for the chat messages.
        avatars (SimpleNamespace): Avatars for the chat messages.
    """
    # Display the chat messages.
    for message in messages:
        # Default to assistant role if not specified.
        role = getattr(message, "type", roles.assistant)

        with chat_message(role):
            write(message.content)

    # Display the chat input box.
    if prompt := chat_input("Get the latest news about..."):
        messages.append(HumanMessage(content=prompt))
        with chat_message(roles.user):
            write(prompt)

        # Invoke the search and get the assistant response.
        state = State(messages=messages)
        result = search_agent.invoke(state)
        assistant_message = result["messages"][-1]

        # Update the session state with the new message.
        messages.append(assistant_message)
        with chat_message(roles.assistant):
            write(assistant_message.content)


run(session_state.messages)
