from pprint import pprint

from dotenv import load_dotenv

load_dotenv()


from LLM.LangChain.langGraph.advance_rag.graph.chains.generation import generation_chain
from LLM.LangChain.langGraph.advance_rag.graph.chains.hallucination_grader import (GradeHallucinations,
                                               hallucination_grader)
from LLM.LangChain.langGraph.advance_rag.graph.chains.retrieval_grader import GradeDocuments, retrieval_grader
from LLM.LangChain.langGraph.advance_rag.graph.chains.retrieval_grader import GradeDocuments, retrieval_grader
from LLM.LangChain.langGraph.advance_rag.graph.chains.router import RouteQuery, question_router
from LLM.LangChain.langGraph.advance_rag.graph.ingestion import retriever


def test_retrival_grader_answer_yes():
    question = "agent system"
    docs = retriever.invoke(question)

    doc_txt = docs
    res: GradeDocuments = retrieval_grader.invoke(
        {"question": question, "document": doc_txt}
    )

    assert res.binary_score == "yes"

def test_retrival_grader_answer_no():
    question = "how to make pizza?"
    docs = retriever.invoke(question)
    doc_txt = docs
    res: GradeDocuments = retrieval_grader.invoke(
        {"question": question, "document": doc_txt}
    )

    assert res.binary_score == "no"


# def test_generation_chain() -> None:
#     question = "agent system"
#     docs = retriever.invoke(question)
#     generation = generation_chain.invoke({"context": docs, "question": question})
#     pprint(generation)


def test_hallucination_grader_answer_yes() -> None:
    question = "agent memory"
    docs = retriever.invoke(question)

    generation = generation_chain.invoke({"context": docs, "question": question})
    res: GradeHallucinations = hallucination_grader.invoke(
        {"documents": docs, "generation": generation}
    )
    assert res.binary_score


def test_hallucination_grader_answer_no() -> None:
    question = "how to make pizza?"
    docs = retriever.invoke(question)

    res: GradeHallucinations = hallucination_grader.invoke(
        {
            "documents": docs,
            "generation": "In order to make pizza we need to first start with the dough",
        }
    )
    assert not res.binary_score


def test_router_to_vectorstore() -> None:
    question = "agent system"

    res: RouteQuery = question_router.invoke({"question": question})
    assert res.datasource == "vectorstore"


def test_router_to_websearch() -> None:
    question = "how to make pizza"

    res: RouteQuery = question_router.invoke({"question": question})
    assert res.datasource == "websearch"
