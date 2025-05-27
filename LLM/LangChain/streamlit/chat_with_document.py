# Load the document based on its file type

def load_document(file):
    import os
    name, ext = os.path.splitext(file)

    if ext == ".pdf":
        from langchain_community.document_loaders import PyPDFLoader
        print("Loading", file)
        loader = PyPDFLoader(file)
    elif ext == ".txt":
        from langchain_community.document_loaders import TextLoader
        print("Loading", file)
        loader = TextLoader(file, encoding="utf-8")
    elif ext == '.docx':
        from langchain_community.document_loaders import Docx2txtLoader
        print("Loading", file)
        loader = Docx2txtLoader(file)
    else:
        print("Unsupported file type:", ext)
        return None
    print("Document Loaded")
    print("*"*50)
    return loader.load()

# Chunk the data into manageable pieces

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def chunk_data(data, chunk_size=256, chunk_overlap=64):
    print("Chunking data...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", " ", ""]
    )
    chunks = text_splitter.split_documents(data)
    print("Data chunked successfully.")
    print("*"*50)
    print(f"Total chunks created: {len(chunks)}")
    print("*"*50)
    return [Document(page_content=chunk.page_content, metadata=chunk.metadata, id=i) for i, chunk in enumerate(chunks)]

# Create embeddings for the chunks

from dotenv import load_dotenv, find_dotenv
from langchain_openai import OpenAIEmbeddings
import chromadb
from langchain_chroma import Chroma
from uuid import uuid4

load_dotenv(find_dotenv())
# Constants
PERSIST_DIRECTORY = "./streamlit_chroma_db"
EMBEDDING_MODEL = "text-embedding-3-large"
COLLECTION_NAME = "rag_collection"
def create_embeddings(chunks, persist_directory=PERSIST_DIRECTORY):
    client = chromadb.PersistentClient(path=persist_directory)
    embedding_model = OpenAIEmbeddings(model=EMBEDDING_MODEL)
    vectordb = Chroma(
        collection_name=COLLECTION_NAME,
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=embedding_model
    )

    if client.get_collection(name=COLLECTION_NAME).count() > 0:
        print(f"Existing embeddings found in {persist_directory}.")
        return vectordb

    uuids = [str(uuid4()) for _ in range(len(chunks))]

    vectordb.add_documents(documents=chunks, ids=uuids)

    return vectordb

# Load existing embeddings
def load_embeddings(persist_directory=PERSIST_DIRECTORY):
    client = chromadb.PersistentClient(path=persist_directory)
    embedding_model = OpenAIEmbeddings(model=EMBEDDING_MODEL)
    vectordb = Chroma(
        persist_directory=persist_directory,
        collection_name=COLLECTION_NAME,  # Ensure this matches the collection name used during creation
        embedding_function=embedding_model
    )
    return vectordb

def remove_embedding(persist_directory=PERSIST_DIRECTORY):
    import shutil
    try:
        shutil.rmtree(persist_directory)
        print(f"Removed existing embeddings directory: {persist_directory}")
    except FileNotFoundError:
        print(f"No existing embeddings directory found at: {persist_directory}")
    except Exception as e:
        print(f"An error occurred while removing the embeddings directory: {e}")

import tiktoken
def calculate_embedding_cost(chunks, model="text-embedding-ada-002", price_per_1k_tokens=0.0001):
    enc = tiktoken.encoding_for_model(model)
    total_tokens = sum(len(enc.encode(doc.page_content)) for doc in chunks)
    return total_tokens, total_tokens / 1000 * price_per_1k_tokens

from langchain_openai import ChatOpenAI
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)
from langchain_core.runnables.history import RunnableWithMessageHistory


def ask_and_get_answer(vectordb, q, k):

    retriever = vectordb.as_retriever(search_kwargs={"k": k})

    system_prompt = (
        "Use the given context to answer the question. "
        "If you don't know the answer, say you don't know. "
        "Context: {context}"
    )

    llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.5)  # Reduced temperature for more focused output

    store = {}

    def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
        if session_id not in store:
            store[session_id] = InMemoryChatMessageHistory()
        return store[session_id]

    session_id = "user-1234"  # Can be user ID, conversation ID, etc.

    prompt = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(system_prompt),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{question}")
        ])

    rag_chain = RunnableWithMessageHistory(
        prompt | llm,
        get_session_history,
        input_messages_key="question",
        history_messages_key="chat_history"
        )
    

    try:
        question = q
        context_docs = retriever.invoke(question)
        print(f"Retrieved {len(context_docs)} documents relevant to the question.")     
        print("\n", "*" * 50, "\n")
        for i, doc in enumerate(context_docs):
            print(f"Document {i + 1}:")
            print(doc.page_content)
            print("\n", "*" * 50, "\n")
        print("Creating Question-Answer Chain...")

        result = rag_chain.invoke({"context": context_docs, "question":question}, config={"configurable": {"session_id": session_id}})
        print(f"Answer: {result}")
        print("\n" + "*" * 50 + "\n")
        return result.content

    except KeyboardInterrupt:
        print("\nExiting...")
        return
    
    return 

def clear_history():
    if 'history' in st.session_state:
        del st.session_state['history']

import streamlit as st

if __name__ == "__main__":

    st.subheader("Chat with Document")
    with st.sidebar:
        remove_embedding()
        upload_file = st.file_uploader("Upload a document (PDF, TXT, DOCX)", type=["pdf", "txt", "docx"])   
        chunk_size = st.number_input("Chunk Size", min_value=100, max_value=2048, value=512, on_change=clear_history)
        k = st.number_input("Number of Documents to Retrieve", min_value=1, max_value=5, value=3, on_change=clear_history)  
        add_data = st.button("Add Data", on_click=clear_history)

        import os
        if upload_file and add_data:
            with st.spinner("Processing your document..."):
                # Load the document
                bytes_data = upload_file.read()
                file_name = os.path.join("./RAG/", upload_file.name)
                with open(file_name, "wb") as f:
                    f.write(bytes_data)

                data = load_document(file_name)
                chunk_data = chunk_data(data, chunk_size=chunk_size)
                st.write(f'Chunks created: {len(chunk_data)}')

                tokens, embedding_cost = calculate_embedding_cost(chunk_data)
                st.write(f"Total tokens: {tokens}, Estimated embedding cost: ${embedding_cost:.6f}")
                
                vectordb = create_embeddings(chunk_data)

                st.session_state.vs = vectordb
                print(st.session_state.values)
                st.success('file uploaded and embedded successfully!')

    q = st.text_input("Ask a question about the document")
    if q:
        if q.lower() == 'remove':
            st.session_state.vs = None
            st.success("Embeddings removed successfully!")
            st.stop()
        print(st.session_state)
        if st.session_state.get('vs', None) :
            vectordb = st.session_state.vs
            st.write(f"K: {k}")
            answer = ask_and_get_answer(vectordb, q, k)
            st.text_area("Answer: ", value=answer)

            st.divider()
            if 'history' not in st.session_state:
                st.session_state.history = ''
            value = f"Q: {q}\n A: {answer}" if 'answer' in locals() else f"Q: {q}\n A: No answer yet."
            st.session_state.history = f'{value} \n {"-"*100} \n {st.session_state.history}'
            h = st.session_state.get('history', '')
            st.text_area("Chat History", value=h, height=300, key="history")
    

                



