from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from langchain_community.utilities.duckduckgo_search import DuckDuckGoSearchAPIWrapper
from langchain.tools import Tool
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

# Step 1: Initialize the DuckDuckGo search wrapper
search = DuckDuckGoSearchAPIWrapper(
    backend='api',
    max_results=3,
    region='us-en',
    safesearch='moderate',
    source='text',  # or 'news'
    time='w'        # past week
)

# Step 2: Wrap it as a LangChain Tool
duckduckgo_tool = [Tool(
    name="duckduckgo_search",
    func=search.run,
    description="Useful for answering questions about current events or recent information from the internet."
)]

# Step 3: Initialize an LLM (you can replace with your preferred LLM provider)
llm = ChatOpenAI(temperature=0.7)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant with access to a duck duck go interpreter. Use the tool to answer my question"),
    ("user", "{input}"),
    ("placeholder", "{agent_scratchpad}"),  # Required for tool-using agents
])

# 4. Create Tool-Ucsing Agent
agent = create_tool_calling_agent(llm=llm, tools=duckduckgo_tool, prompt=prompt)

# 5. Create Executor
agent_executor = AgentExecutor(agent=agent, tools=duckduckgo_tool, verbose=True)

# Step 5: Ask a question
user_query_1 = "what is the latest situation of migrants in Italy? please provide the answer with link included"
response = agent_executor.invoke({"input": user_query_1})
print(response)
