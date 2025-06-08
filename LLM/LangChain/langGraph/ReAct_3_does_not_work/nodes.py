from dotenv import load_dotenv
from langgraph.prebuilt import ToolNode

from react import react_agent_runnable, tools
from state import AgentState

load_dotenv()
from langchain.agents import create_react_agent, AgentExecutor


def run_agent_reasoning_engine(state: AgentState):
    agent_outcome = react_agent_runnable.invoke(state)
    return {"agent_outcome": agent_outcome}


tool_executor = ToolNode(tools)


# def execute_tools(state: AgentState):
#     """
#     Execute the tool chosen by the agent
#     Takes the agent's action from state and runs the appropriate tool
#     Returns the tool's output as part of the agent's intermediate steps
#     """
#     agent_action = state["agent_outcome"]
#     output = tool_executor.invoke(agent_action)
#     print(f"Tool output: {output}")
#     return {"intermediate_steps": [(agent_action, str(output))]}

def execute_tools(state: AgentState):
    """
    Execute the tool chosen by the agent.
    """
    agent_action = state["agent_outcome"]
    print(f"\nAgent action received: {agent_action}\n")

    if not hasattr(agent_action, 'tool') or not hasattr(agent_action, 'tool_input'):
        print("Invalid agent action. Missing tool or tool_input.")
        return {"intermediate_steps": [(agent_action, "Invalid agent action.")]}

    # Log available tools
    print(f"Available tools: {[tool.name for tool in tools]}")
    print(f"Tool requested: {agent_action.tool}")

    output = tool_executor.invoke(agent_action)
    print(f"\nTool output: {output}\n")

    return {"intermediate_steps": [(agent_action, str(output))]}
