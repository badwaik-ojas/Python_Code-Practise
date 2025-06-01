# File: app.py

import os
import streamlit as st
from dotenv import load_dotenv

# LangChain imports (latest structure)
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

# Display chat messages in a conversational format
from streamlit_chat import message as chat_message

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Page configuration
st.set_page_config(page_title="Your Custom Assistant", page_icon="💬")
st.subheader("💬 Your Custom ChatGPT")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar input for system role
with st.sidebar:
    system_prompt = st.text_input("System Role", value="You are a helpful assistant.")
    # Ensure there's a system message at the beginning
    if len(st.session_state.messages) >= 1:
        if not isinstance(st.session_state.messages[0], SystemMessage):
            st.session_state.messages.insert(0, SystemMessage(content="You are a helpful assistant."))
    elif system_prompt:
        st.session_state.messages.append(SystemMessage(content=system_prompt))
    # Initialize LLM
    chat = ChatOpenAI(
        temperature=0.5,
        model="gpt-3.5-turbo",
        api_key=openai_api_key
    )

    # Input box for user message
    user_input = st.text_input("Send a message:", key="user_input")

# On user input, call the model
if user_input:
    st.session_state.messages.append(HumanMessage(content=user_input))
    with st.spinner("Working on your request..."):
        response = chat.invoke(st.session_state.messages)
    st.session_state.messages.append(AIMessage(content=response.content))

# Display chat messages in a chat-like format (skip system message)
for i, msg in enumerate(st.session_state.messages[1:], start=1):
    if isinstance(msg, HumanMessage):
        chat_message(msg.content, is_user=True, key=f"user-{i} 😊")
    elif isinstance(msg, AIMessage):
        chat_message(msg.content, is_user=False, key=f"bot-{i} 🤖")
