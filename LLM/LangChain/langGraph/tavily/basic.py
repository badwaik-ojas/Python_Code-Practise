from dotenv import load_dotenv

load_dotenv()

from langgraph.prebuilt import ToolNode
from langchain_tavily import TavilySearch
from langchain_core.messages import HumanMessage, AIMessage

tool = TavilySearch(max_results=1)
tool_node = ToolNode(tools=[tool])

state = {
    "messages": [
        HumanMessage(content="What's the weather in San Francisco?"),
        AIMessage(
            content="",  # 👈 FIXED: Provide a valid (even empty) string
            additional_kwargs={
                "tool_calls": [
                    {
                        "id": "1",
                        "type": "function",
                        "function": {
                            "name": tool.name,
                            "arguments": '{"query": "current weather in San Francisco"}'
                        }
                    }
                ]
            }
        )
    ]
}

result = tool_node.invoke(state)

# Output the ToolMessage content
print("ToolNode Output:", result["messages"][-1].content)
