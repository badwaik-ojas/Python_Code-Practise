from langchain.agents import initialize_agent, AgentType
from langchain.agents.agent import AgentExecutor
from langchain.tools import Tool
from langchain_experimental.tools.python.tool import PythonREPLTool
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # Finds and loads .env

# 1. Define the LLM
llm = ChatOpenAI(temperature=0)

# 2. Define tools (e.g., Python REPL)
repl_tool  = PythonREPLTool()

tools = [
    Tool(
        name="python_repl",
        func=repl_tool.run,
        description="Useful for executing Python code. Input should be valid Python code to be executed and printed.",
    ),
    # Add other tools here if needed (e.g., a search tool)
]

# 3. Initialize the agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,  # or ZERO_SHOT_REACT_DESCRIPTION
    verbose=True,  # To print steps automatically
    return_intermediate_steps=True     # ✅ This is crucial
)

# 4. Run the agent and capture output
result = agent.invoke({"input": "What is 7.1 to the power of 3.1?"})

# 5. Print final answer
print("\nFinal Output:")
print(result["output"])

# 6. Print intermediate steps
print("\nIntermediate Steps:")
for step in result["intermediate_steps"]:
    print(step)
