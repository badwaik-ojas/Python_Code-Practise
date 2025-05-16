from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv(find_dotenv())  # Finds and loads .env


# 1. Define a ChatPromptTemplate using System and Human messages with dynamic placeholders
chat_template = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("You respond only in the JSON format."),
    HumanMessagePromptTemplate.from_template("Top {n} countries in {area} by population.")
])

# 2. Format the prompt with actual input values
messages = chat_template.format_messages(n="10", area="Europe")

# Print to see how the final prompt looks
print("--- Formatted Messages ---")
for msg in messages:
    print(f"{msg.type.upper()}: {msg.content}")

# 3. Instantiate the chat model (ChatOpenAI)
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# 4. Invoke the model with the formatted messages
output = llm.invoke(messages)

# 5. Display the final output
print("\n--- LLM Response ---")
print(output.content)