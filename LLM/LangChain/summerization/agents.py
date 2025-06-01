from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

from langchain.agents import initialize_agent, Tool
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
wikipedia = WikipediaAPIWrapper()

# Define tools
tools = [
    Tool(
        name="Wikipedia",
        func=wikipedia.run,
        description="Useful for answering general knowledge questions using Wikipedia."
    )
]

# Initialize agent
agent_executor = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

# Run query
output = agent_executor.invoke("Can you provide a short summary of George Washington?")
print(output["output"])
