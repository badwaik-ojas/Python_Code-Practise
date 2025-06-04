from typing import Any, Dict

from graph.state import GraphState
from ingestion import retriever


def retrieve(state: GraphState) -> Dict[str, Any]:
    print("---RETRIEVE---")
    question = state["question"]

    documents = retriever.invoke(question)
    return {"documents": documents, "question": question}

# Dummy test input
dummy_state = {
    "question": "What is Corrective RAG?",
    "documents": [],
    "generation": "",
    "web_search": False
}

# Output
print(retrieve(dummy_state))
