from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)
# from langchain_core.chat_history import ChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory
from langchain.memory import ChatMessageHistory

# Load environment variables
load_dotenv(find_dotenv(), override=True)

# Step 1: Set up the chat model
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

# Step 2: Define prompt with memory placeholder
prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("You are a helpful and intelligent assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    HumanMessagePromptTemplate.from_template("{content}")
])

# Step 3: Initialize memory (conversation buffer)
chat_history = ChatMessageHistory()

# Step 4: Chain with memory using RunnableWithMessageHistory
chain = RunnableWithMessageHistory(
    prompt | llm,
    lambda session_id: chat_history,  # memory is shared here
    input_messages_key="content",
    history_messages_key="chat_history"
)

# Step 5: Chat loop with session tracking
session_id = "user-1234"  # can be user ID, conversation ID, etc.

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Goodbye!")
        break
    response = chain.invoke({"content": user_input}, config={"configurable": {"session_id": session_id}})
    print(f"Assistant: {response.content}")
    print("-" * 50)
