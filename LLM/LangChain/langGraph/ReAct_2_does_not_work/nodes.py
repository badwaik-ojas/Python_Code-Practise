from dotenv import load_dotenv
from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode
from react import reach_agent_runnable, tools
from state import AgentState

load_dotenv()

SYSTEM_MESSAGE = """
You are a helpful assistant that can use tools to answer questions.
"""


def run_agent_reasoning_engine(state: AgentState):
    agent_outcome = reach_agent_runnable.invoke(state)
    return {"agent_outcome": agent_outcome}


tool_node = ToolNode(tools)

def execute_tools(state: AgentState):
    agent_action = state["agent_outcome"]
    output = tool_node.invoke(agent_action)
    return {'intermediate_steps': [(agent_action, str(output))] }
