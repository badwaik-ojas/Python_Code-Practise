from dotenv import load_dotenv
from langchain import hub
from langchain.agents import create_react_agent
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import tool
from langchain_openai.chat_models import ChatOpenAI
from langchain_tavily import TavilySearch
from langchain_core.tools import Tool


load_dotenv()


react_prompt: PromptTemplate = hub.pull("hwchase17/react")


@tool
def triple(num: float) -> float:
    """
    :param num: a number to triple
    :return: the number tripled ->  multiplied by 3
    """
    print(f"Tripling {num}")
    return 3 * float(num)

triple_func = Tool(
    name="Triple Function",
    description="Triples a given number.",
    func=triple
)

def clean_tavily_tool(input_query: str) -> str:
    clean_query = input_query.strip("\"'")
    print(f"[TAVILY DEBUG] Cleaned query: {clean_query}")
    result = TavilySearch(max_results=3).invoke(clean_query)
    return str(result)

search_tool = Tool(
    name="TavilySearch",
    func=clean_tavily_tool,
    description="Useful for general web searches."
)

tools = [search_tool, triple_func]

llm = ChatOpenAI(model="gpt-3.5-turbo")

react_agent_runnable = create_react_agent(llm, tools, react_prompt).bind(tools=tools)