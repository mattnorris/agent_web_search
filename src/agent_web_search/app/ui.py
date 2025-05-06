import streamlit as st

from agent_web_search.app import search_agent as graph

st.title("Basic Chat with Web Search")
# Initialize with a system message to prevent empty messages list
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "This is a chat with web search capabilities."}
    ]

# Only display user and assistant messages to the user
for msg in st.session_state.messages:
    if msg["role"] in ["user", "assistant"]:
        st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("What's the latest news?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    try:
        # Ensure we pass at least the current message if chat_history processing fails
        chat_history = st.session_state.messages

        # Pass the full conversation history to the agent
        response = graph.invoke({"input": prompt, "chat_history": chat_history})
        answer = response["output"]

        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.chat_message("assistant").write(answer)
    except Exception as e:
        st.error(f"Error: {str(e)}")
        st.session_state.messages.append(
            {"role": "assistant", "content": f"Sorry, I encountered an error: {str(e)}"}
        )
