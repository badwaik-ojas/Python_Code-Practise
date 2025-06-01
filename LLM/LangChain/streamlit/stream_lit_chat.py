from dotenv import load_dotenv, find_dotenv
from langchain_openai import OpenAIEmbeddings
import streamlit as st
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from streamlit_chat import message as chat_message
from langchain_openai import ChatOpenAI


load_dotenv(find_dotenv())

# Page configuration
st.set_page_config(page_title="Your Custom Assistant", page_icon="💬")
st.subheader("💬 Your Custom ChatGPT")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar inputs
with st.sidebar:
    system_prompt = st.text_input("System Role", "You are a helpful assistant.")

# Chat model
chat = ChatOpenAI(
    temperature=0.5,
    model="gpt-3.5-turbo")

# Append system message if not already present
if not any(isinstance(msg, SystemMessage) for msg in st.session_state.messages):
    st.session_state.messages.append(SystemMessage(content=system_prompt))

# User input
user_input = st.text_input("Send a message:", key="user_input")

if user_input:
    st.session_state.messages.append(HumanMessage(content=user_input))

    # Generate response
    with st.spinner("Working on your request..."):
        response = chat.invoke(st.session_state.messages)
    
    st.session_state.messages.append(AIMessage(content=response.content))

# Display messages in chat format
for msg in st.session_state.messages:
    if isinstance(msg, SystemMessage):
        continue  # Optional: Skip displaying system message
    is_user = isinstance(msg, HumanMessage)
    chat_message(msg.content, is_user=is_user)
