from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_experimental.tools.python.tool import PythonREPLTool
from dotenv import load_dotenv, find_dotenv
from langchain.tools import Tool
from langchain_community.utilities import WikipediaAPIWrapper

load_dotenv(find_dotenv())

# LLM
llm = ChatOpenAI(temperature=0)

# Tools
python_tool = PythonREPLTool()
wiki = WikipediaAPIWrapper()

tools = [
    Tool(
        name="python_repl",
        func=python_tool.run,
        description="Executes Python code. Input must be valid Python.",
    ),
    Tool(
        name="wikipedia",
        func=wiki.run,
        description="Searches Wikipedia for world knowledge. Input should be a search term or topic.",
    ),
]

# Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant with access to a Python interpreter and Wikipedia. Use the tools to answer questions."),
    ("user", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

# Agent & Executor
agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Example
response = executor.invoke({"input": "Who was Nikola Tesla and what were his contributions? what will be age today if didnot died? use python interpreter to calculate the age"})
print("Response:", response)
