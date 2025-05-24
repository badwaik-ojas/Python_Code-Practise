from langchain_openai import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_message_histories import FileChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv(), override=True)
# Set up the LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

# Define the prompt template
prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("You are a helpful assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    HumanMessagePromptTemplate.from_template("{content}")
])

# Use persistent file-based history
history = FileChatMessageHistory(file_path="chat_history.json")

# Memory with persistent backend
memory = ConversationBufferMemory(chat_memory=history, return_messages=True)

# Create the chain with memory
chain = RunnableWithMessageHistory(
    prompt | llm,
    lambda session_id: memory.chat_memory,  # assign session-specific memory
    input_messages_key="content",
    history_messages_key="chat_history"
)

# Example session
session_id = "user-123"

# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    response = chain.invoke({"content": user_input}, config={"configurable": {"session_id": session_id}})
    print(f"Assistant: {response.content}")
    print("-" * 50)
