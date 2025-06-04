from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from dotenv import load_dotenv, find_dotenv
from typing_extensions import TypedDict

# Load environment variables
load_dotenv(find_dotenv(), override=True)
# Step 1: Define state
class AgentState(TypedDict):
    question: str
    result: str
    use_tool: bool

# Step 2: Setup tools and model
llm = ChatOpenAI(model="gpt-4", temperature=0)
wiki_tool = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

# Step 3: Define nodes (logic units)
def decide_use_tool(state: AgentState):
    question = state["question"]
    if "who" in question.lower() or "what" in question.lower():
        return {"use_tool": True}
    return {"use_tool": False}

def query_wiki(state: AgentState):
    result = wiki_tool.run(state["question"])
    return {"result": result}

def call_llm(state: AgentState):
    prompt = f"Answer this question directly: {state['question']}"
    print(prompt)
    result = llm.invoke([HumanMessage(content=prompt)])
    print(result.content)
    return {"result": result.content}

# Step 4: Build LangGraph
graph = StateGraph(AgentState)

# Add nodes
graph.add_node("decide", RunnableLambda(decide_use_tool))
graph.add_node("tool", RunnableLambda(query_wiki))
graph.add_node("llm", RunnableLambda(call_llm))

# Set entry point
graph.set_entry_point("decide")

# Add logic-based routing
graph.add_conditional_edges(
    "decide",
    lambda state: "tool" if state.get("use_tool") else "llm"
)

# Terminal edges
graph.add_edge("tool", END)
graph.add_edge("llm", END)

# Compile agent
agent_executor = graph.compile()

# Run it!
response = agent_executor.invoke({"question": "gravity was discovered by?"})
print(response)
