from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_community.chat_message_histories import RedisChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# Load environment variables
load_dotenv(find_dotenv(), override=True)

# Initialize the chat model
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

# Define the chat prompt template
prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("You are a helpful and intelligent assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    HumanMessagePromptTemplate.from_template("{content}")
])

# Dictionary to store chat histories per session
store = {}

def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

# Create the chain with message history
chain = RunnableWithMessageHistory(
    prompt | llm,
    get_session_history,
    input_messages_key="content",
    history_messages_key="chat_history"
)

# Chat loop with session tracking
session_id = "user-1234"  # Can be user ID, conversation ID, etc.

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Goodbye!")
        print(store)
        break
    response = chain.invoke(
        {"content": user_input},
        config={"configurable": {"session_id": session_id}}
    )
    print(f"Assistant: {response.content}")
    print("-" * 50)

'''
🧠 Goal of the Code
You are building a ChatGPT-like assistant that:

Remembers past messages (has memory)

Lets users ask follow-up questions

Uses LangChain + OpenAI GPT model

🔍 Code Breakdown
🔹 Step 1: Import Required Tools
python
Copy
Edit
from dotenv import load_dotenv, find_dotenv
Loads your .env file which holds your OpenAI API key.

python
Copy
Edit
from langchain_openai import ChatOpenAI
Loads the OpenAI model (e.g., gpt-3.5-turbo).

python
Copy
Edit
from langchain_core.prompts import ...
Imports tools to design a chat prompt.

python
Copy
Edit
from langchain_core.chat_history import InMemoryChatMessageHistory
This class stores chat messages in memory, like a temporary notebook.

python
Copy
Edit
from langchain_core.runnables.history import RunnableWithMessageHistory
This wraps the whole chat so it can remember conversations.

🔹 Step 2: Load API Key
python
Copy
Edit
load_dotenv(find_dotenv(), override=True)
Loads your .env so you can use OPENAI_API_KEY behind the scenes.

🔹 Step 3: Create a Chat Model
python
Copy
Edit
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
You’re using the OpenAI GPT model:

temperature=0.7 makes answers creative but reasonable

You can set it between 0 (more focused) and 2 (more creative)

🔹 Step 4: Design the Prompt
python
Copy
Edit
prompt = ChatPromptTemplate.from_messages([...])
This builds the instructions for the assistant:

System message: “You are a helpful assistant.”

Placeholder: where the memory (chat history) is inserted

Human message: the user’s latest input

🔹 Step 5: Define Chat Memory
python
Copy
Edit
store = {}
This is a dictionary that will hold chat history for each user.

python
Copy
Edit
def get_session_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]
This function returns the memory for a user. If it’s a new user, it creates a new memory store.

🔹 Step 6: Create a Chat Chain With Memory
python
Copy
Edit
chain = RunnableWithMessageHistory(...)
This connects:

The prompt + model (prompt | llm)

The memory system (get_session_history)

The input key ("content")

The memory key ("chat_history")

This tells LangChain: “Whenever a user speaks, store it under chat_history, and show it in the next prompt.”

🔹 Step 7: Loop to Chat with the User
python
Copy
Edit
session_id = "user-1234"
Represents the current user or conversation.

python
Copy
Edit
while True:
    user_input = input("You: ")
Asks the user for input in the console.

python
Copy
Edit
if user_input.lower() in ["exit", "quit", "bye"]:
Checks if they want to stop the chat.

python
Copy
Edit
response = chain.invoke({...})
Sends the message to the chatbot and gets a response, including memory.

python
Copy
Edit
print(f"Assistant: {response.content}")
Shows the assistant's response.

💡 Real-Life Use Cases
Customer Support Bots: Remember what the customer has already said.

Personal Assistants: Track tasks or reminders over time.

Tutoring Bots: Follow up on previously discussed topics.

📘 What You Should Learn Next
Memory Types: Explore other memory types like ConversationSummaryMemory for summarizing long chats.

Storage: Save memory permanently using a database like Redis.

Vector DB Integration: Add tools like Pinecone for smarter retrieval-based responses.

'''