# langchain_agent.py

from langchain_openai import ChatOpenAI
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain_experimental.tools.python.tool import PythonREPLTool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # Finds and loads .env

# Step 1: Create the LLM (Function-enabled chat model)
llm = ChatOpenAI(temperature=0)

# Step 2: Define the Python REPL tool
python_tool = PythonREPLTool()

# Step 3: Define the structured prompt required for OpenAI function agents
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI that can run Python code."),
    ("user", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

# Step 4: Create the agent
agent = create_openai_functions_agent(
    llm=llm,
    tools=[python_tool],
    prompt=prompt,
)

# Step 5: Create an executor for the agent
agent_executor = AgentExecutor(agent=agent, tools=[python_tool], verbose=True)

# Step 6: Run the agent with an example question
response = agent_executor.invoke({"input": "What is 7.1 to the power of 3.1?"})

# Step 7: Print the output
print("\nFinal Answer:", response["output"])
