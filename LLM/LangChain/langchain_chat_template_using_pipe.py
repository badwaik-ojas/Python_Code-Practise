'''
🧩 What is RunnableLambda?
RunnableLambda is a utility from langchain_core.runnables that wraps any Python function into a "Runnable", making it composable in LangChain's pipeline using the | operator.

Think of it as:
A bridge that turns regular Python logic (like lambda, custom functions) into something that fits inside a LangChain pipeline.

🔧 Why Use It?
In LangChain’s composable architecture:

Every component in the pipeline must be a Runnable.

A raw function like lambda x: x.content isn’t a Runnable, so it can’t be piped.

RunnableLambda solves this by converting the function into a compatible pipeline unit.

🛠️ How It Works (Step-by-Step)
python
Copy
Edit
from langchain_core.runnables import RunnableLambda

# Wrap the function using RunnableLambda
extract_content = RunnableLambda(lambda x: x.content)

# Now it's compatible with the pipe operator
result = some_runnable | extract_content
Example in Context
python
Copy
Edit
chat_prompt | llm | RunnableLambda(lambda x: x.content)
chat_prompt: Returns a list of chat messages

llm: Returns an AIMessage object

RunnableLambda(lambda x: x.content): Extracts the .content string from the AIMessage

🧠 Use Cases
Use Case	Lambda Function
Extract .content	lambda x: x.content
Get tokens count	lambda x: len(x.content.split())
Add logging	lambda x: (print(x), x)[1]
Transform output	lambda x: x.upper()

🧪 Custom Example
python
Copy
Edit
from langchain_core.runnables import RunnableLambda

def my_function(x):
    return f"Processed: {x}"

wrapped = RunnableLambda(my_function)
print(wrapped.invoke("Test"))  # Output: Processed: Test
📘 Official Docs Reference
You can read more here:

LangChain Core Docs – RunnableLambda

LangChain GitHub – RunnableLambda Source

✅ Summary
RunnableLambda makes your Python functions usable in LangChain pipelines.

It turns them into Runnable objects, so you can use them with |, .invoke(), .stream(), etc.

Useful for quick transformations, post-processing, or injecting custom logic.
'''

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.runnables import RunnableLambda


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

# Step 3: Build the pipeline using the | operator
chain = (
    messages |
    llm |
    RunnableLambda(lambda x: x.content)  # Extract content from the AIMessage
)

# Step 4: Run the chain with input values
output = chain.invoke({"n": 10, "area": "Europe"})

# Step 5: Print the result
print(output)

