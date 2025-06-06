from dotenv import load_dotenv, find_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from uuid import uuid4

load_dotenv(find_dotenv(), override=True)

urls = [
    "https://lilianweng.github.io/posts/2023-06-23-agent/",
    "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
    "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
]

docs = [WebBaseLoader(url).load() for url in urls]
docs_list = [item for sublist in docs for item in sublist]

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=400, chunk_overlap=50
)
doc_splits = text_splitter.split_documents(docs_list)
uuids = [str(uuid4()) for _ in range(len(doc_splits))]


# vectordb = Chroma(
#         collection_name="rag-chroma",
#         persist_directory="./.chroma",
#         embedding_function=OpenAIEmbeddings()
#                 )
# vectordb.add_documents(documents=doc_splits)


persist_directory = "./langgraph_chroma_db"
# vector_store = Chroma.from_documents(
#     documents=doc_splits,
#     embedding=OpenAIEmbeddings(),
#     ids=uuids,
#     persist_directory=persist_directory,
#     collection_name="rag-chroma" # Optional: name your collection
# )

retriever = Chroma(
    collection_name="rag-chroma",
    persist_directory=persist_directory,
    embedding_function=OpenAIEmbeddings(),
).as_retriever()

# print(retriever.invoke("What is Corrective RAG?"))