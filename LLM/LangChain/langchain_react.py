from langchain_core.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.utilities.duckduckgo_search import DuckDuckGoSearchAPIWrapper
from langchain_experimental.tools.python.tool import PythonREPLTool
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain import hub
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

# Tool 1: Python
python_tool = Tool(
    name="Python_REPL",
    func=PythonREPLTool().run,
    description="Useful for executing Python code."
)

# Tool 2: Wikipedia
wiki_tool = Tool(
    name="Wikipedia",
    func=WikipediaAPIWrapper().run,
    description="Useful for factual information."
)

# Tool 3: DuckDuckGo
duckduckgo_tool = Tool(
    name="DuckDuckGo_Search",
    func=DuckDuckGoSearchAPIWrapper().run,
    description="Useful for general web searches."
)

tools = [python_tool, wiki_tool, duckduckgo_tool]

llm = ChatOpenAI(model="gpt-4-turbo-preview", temperature=0)

prompt = hub.pull("hwchase17/react")  # ReAct prompt template

agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True,
                               handle_parsing_errors=True, max_iterations=10)

response = agent_executor.invoke({"input": "Which is largest political party in the world?"})
print(response)



