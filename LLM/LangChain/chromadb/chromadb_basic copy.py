from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
import load_from_file_util as load_util
import chuck_the_data as chuck_util
from dotenv import load_dotenv, find_dotenv
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import chromadb
import os
from uuid import uuid4

load_dotenv(find_dotenv())

# --- Constants ---
PERSIST_DIRECTORY = "./chroma_db"
COLLECTION_NAME = "bhagwat_gita_collection"
EMBEDDING_MODEL = "text-embedding-3-small"

# --- Embeddings Creation and Management ---
def create_embeddings(chunks, persist_directory=PERSIST_DIRECTORY, collection_name=COLLECTION_NAME):
    client = chromadb.PersistentClient(path=persist_directory)
    embedding_model = OpenAIEmbeddings(model=EMBEDDING_MODEL)
    vectordb = Chroma(
                client=client,
                collection_name=collection_name,
                embedding_function=embedding_model
            )

    try:
        existing_collection = client.get_collection(name=collection_name)
        if existing_collection.count() > 0:
            print(f"Existing embeddings found in '{collection_name}'. Loading it.")
    except Exception:
        print(f"Collection '{collection_name}' not found or empty. Creating new embeddings.")

    uuids = [str(uuid4()) for _ in range(len(chunks))]

    vector_store = vectordb.add_documents(
        documents=chunks,
        embedding=embedding_model
    )
    print("Embeddings created and saved.")
    return vector_store

def load_embeddings(persist_directory=PERSIST_DIRECTORY, collection_name=COLLECTION_NAME):
    client = chromadb.PersistentClient(path=persist_directory)
    embedding_model = OpenAIEmbeddings(model=EMBEDDING_MODEL)

    try:
        existing_collection = client.get_collection(name=collection_name)
        if existing_collection.count() == 0:
            print(f"Collection '{collection_name}' is empty. No embeddings to load.")
            return None
        print(f"Loaded collection '{collection_name}' with {existing_collection.count()} items.")

        vectordb = Chroma(
            client=client,
            collection_name=collection_name,
            embedding_function=embedding_model
        )
        return vectordb
    except Exception as e:
        print(f"Error loading embeddings: {e}")
        return None

def remove_embedding_directory(persist_directory=PERSIST_DIRECTORY):
    import shutil
    try:
        if os.path.exists(persist_directory):
            shutil.rmtree(persist_directory)
            print(f"Removed embeddings directory: {persist_directory}")
        else:
            print(f"No embeddings directory found at: {persist_directory}")
    except Exception as e:
        print(f"Error removing embeddings directory: {e}")

# --- Main Application Logic ---
def main():
    print("Loading document...")
    load_data = load_util.load_document("LLM/bhagwat_gita_quotes.txt")
    
    if not load_data:
        print("Error: No data loaded from the file.")
        return
    
    print(f"Loaded {len(load_data)} initial documents.")
    # --- DIAGNOSTIC STEP 1: Check the raw loaded document content ---
    for i, doc in enumerate(load_data):
        print(f"\n--- Initial Document {i+1} ---")
        print(f"Type: {type(doc)}")
        print(f"Content (first 100 chars): '{doc.page_content[:100]}...'")
        print(f"Metadata: {doc.metadata}")
        if not doc.page_content.strip():
            print("WARNING: Initial document page_content is empty or just whitespace!")
    # ---------------------------------------------------------------

    print("\nChunking data...")
    chunks = chuck_util.chunk_data(load_data)
    
    if not chunks:
        print("Error: No chunks created from the loaded data.")
        return

    print(f"Created {len(chunks)} chunks.")
    # --- DIAGNOSTIC STEP 2: Check the chunked document content ---
    for i, chunk in enumerate(chunks[:5]): # Print first 5 chunks to avoid too much output
        print(f"\n--- Chunk {i+1} ---")
        print(f"Type: {type(chunk)}")
        print(f"Content (first 100 chars): '{chunk.page_content[:100]}...'")
        print(f"Metadata: {chunk.metadata}")
        if not chunk.page_content.strip():
            print("WARNING: Chunk page_content is empty or just whitespace!")
    # ------------------------------------------------------------

    create_embeddings(chunks)
    vectordb = load_embeddings()
    
    if vectordb is None:
        print("Failed to prepare vector database. Exiting.")
        return

    print("VectorDB is ready.")

    # --- Retrieval and RAG Chain ---
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})
    question = "What is the essence of Bhagavad Gita?" 
    
    results_direct_search = vectordb.similarity_search(question, k=3) 

    print("\n🔎 Top matches (Direct search):")
    for i, doc in enumerate(results_direct_search):
        print(f"\nResult {i+1}:\n{doc.page_content}")

    context_docs = retriever.invoke(question)
    print(f"\nRetrieved {len(context_docs)} relevant documents using retriever.")     
    print("\n" + "*" * 50 + "\n")
    for i, doc in enumerate(context_docs):
        print(f"Document {i + 1}:\n{doc.page_content}")
        print("\n" + "*" * 50 + "\n")

    print("Setting up Question-Answer Chain...")

    system_prompt = (
        "Use the given context to answer the question. "
        "If you don't know the answer, say you don't know. "
        "Use three sentence maximum and keep the answer concise. "
        "Context: {context}"
    )
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )
    llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.5)
    print("LLM initialized.")

    rag_chain = (
        {"context": retriever, "input": RunnablePassthrough()}
        | prompt
        | llm
    )
    print("Retrieval chain created.")
    
    final_answer = rag_chain.invoke(question)
    
    return final_answer.content

if __name__ == "__main__":
    print(main())