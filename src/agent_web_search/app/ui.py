import streamlit as st

# from agent_web_search.app import search_agent as graph
from agent_web_search.app import search_agent

st.title("Basic Chat with Web Search")
# # Initialize with a system message to prevent empty messages list
# if "messages" not in st.session_state:
#     st.session_state.messages = [
#         {"role": "system", "content": "This is a chat with web search capabilities."}
#     ]

# # Only display user and assistant messages to the user
# for msg in st.session_state.messages:
#     if msg["role"] in ["user", "assistant"]:
#         st.chat_message(msg["role"]).write(msg["content"])

# if prompt := st.chat_input("What's the latest news?"):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     st.chat_message("user").write(prompt)

#     try:
#         # Ensure we pass at least the current message if chat_history processing fails
#         chat_history = st.session_state.messages

#         # Pass the full conversation history to the agent
#         response = graph.invoke({"input": prompt, "chat_history": chat_history})
#         answer = response["output"]

#         st.session_state.messages.append({"role": "assistant", "content": answer})
#         st.chat_message("assistant").write(answer)
#     except Exception as e:
#         st.error(f"Error: {str(e)}")
#         st.session_state.messages.append(
#             {"role": "assistant", "content": f"Sorry, I encountered an error: {str(e)}"}
#         )

import streamlit as st
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent, load_tools
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from langchain_openai import OpenAI

llm = OpenAI(temperature=0, streaming=True)
# tools = load_tools(["ddg-search"])
prompt = hub.pull("hwchase17/react")
# agent = create_react_agent(llm, tools, prompt)
# agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
# agent_executor = AgentExecutor(agent=search_agent, verbose=True)

if prompt := st.chat_input():
    st.chat_message("user").write(prompt)
    with st.chat_message("assistant"):
        st_callback = StreamlitCallbackHandler(st.container())
        # response = agent_executor.invoke(
        #     {"input": prompt}, {"callbacks": [st_callback]}
        # )
        response = search_agent.invoke({"input": prompt}, {"callbacks": [st_callback]})
        st.write(response["output"])
