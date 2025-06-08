from dotenv import load_dotenv

load_dotenv()

from langchain_core.messages import HumanMessage
from langchain_core.agents import AgentFinish
from state import AgentState
from langgraph.graph import END, StateGraph

from nodes import run_agent_reasoning_engine, execute_tools

AGENT_REASON = "agent_reason"
ACT = "act"
LAST = -1


def should_continue(state: AgentState) -> str:
    if isinstance(state["agent_outcome"], AgentFinish):
        return END
    return ACT


flow = StateGraph(AgentState)

flow.add_node(AGENT_REASON, run_agent_reasoning_engine)
flow.set_entry_point(AGENT_REASON)
flow.add_node(ACT, execute_tools)


flow.add_conditional_edges(
    AGENT_REASON,
    should_continue,
    {
        END: END,
        ACT: ACT,
    }
)

flow.add_edge(ACT, AGENT_REASON)

app = flow.compile()
app.get_graph().draw_mermaid_png(output_file_path="graph.png")

if __name__ == "__main__":
    print("Hello ReAct with LangGraph")
    res = app.invoke(
            input={
                    "input":"what is the weather in sf? List it and then Triple it "
            }
    )
    print(res["agent_outcome"])
