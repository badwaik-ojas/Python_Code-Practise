from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_experimental.tools.python.tool import PythonREPLTool
from langchain_core.tools import Tool

# 1. Initialize LLM
llm = ChatOpenAI(temperature=0)

# 2. Define Tools
python_repl_tool = PythonREPLTool()
tools = [
    Tool(
        name="python_repl",
        func=python_repl_tool.run,
        description="Executes Python code for calculations or logic execution. Input must be valid Python code.",
    )
]

# 3. Define Prompt with agent_scratchpad
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant with access to a Python interpreter. Use the tool to answer coding or math questions. once you finish please say something about the result"),
    ("user", "{input}"),
    ("placeholder", "{agent_scratchpad}"),  # Required for tool-using agents
])

# 4. Create Tool-Using Agent
agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)

# 5. Create Executor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 6. Test Example
user_query_1 = "What is (3.14159 * 2)**2? please say somthing creative about the number once you calculate"
response = agent_executor.invoke({"input": user_query_1})
print("Response 1:", response)
