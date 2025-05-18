from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_experimental.tools.python.tool import PythonREPLTool
from dotenv import load_dotenv, find_dotenv
from langchain.tools import Tool
from langchain.utilities import WikipediaAPIWrapper

load_dotenv(find_dotenv())

# LLM
llm = ChatOpenAI(temperature=0)

# Create Wikipedia wrapper
wiki = WikipediaAPIWrapper()

# Wrap it as a Tool
wiki_tool = [Tool(
    name="wikipedia",
    func=wiki.run,
    description="Useful for answering questions about general world knowledge, events, or concepts using Wikipedia. Input should be a search query."
)]

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant with access to Wikipedia. Use the tools to answer questions."),
    ("user", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

# Agent & Executor
agent = create_tool_calling_agent(llm=llm, tools=wiki_tool, prompt=prompt)
executor = AgentExecutor(agent=agent, tools=wiki_tool, verbose=True)

# Example
response = executor.invoke({"input": "Who was Nikola Tesla and what were his contributions?"})
print("Response:", response)