from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
import load_from_file_util as load_util
import chuck_the_data as chuck_util
from dotenv import load_dotenv, find_dotenv
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import chromadb
from uuid import uuid4
from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)
from langchain_core.chat_history import InMemoryChatMessageHistory

load_dotenv(find_dotenv())
# Constants
PERSIST_DIRECTORY = "./chroma_db"
EMBEDDING_MODEL = "text-embedding-3-large"
COLLECTION_NAME = "bhagwat_gita_collection"

# Create embeddings and save
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

def main():
    # Load the document
    load_data = load_util.load_document("LLM/bhagwat_gita_quotes.txt")
    
    # Split the document into chunks
    chunks = chuck_util.chunk_data(load_data)
    
    # Create embeddings and save them
    vectordb = create_embeddings(chunks)
    
    print("Embeddings created and saved successfully.")

    # load_embeddings() can be called to load existing embeddings

    # vectordb = load_embeddings()
    print("Existing embeddings loaded successfully.")   

    retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    system_prompt = (
        "Use the given context to answer the question. "
        "If you don't know the answer, say you don't know. "
        "Use three sentence maximum and keep the answer concise. "
        "Context: {context}"
    )

    llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.5)  # Reduced temperature for more focused output
    print("LLM initialized.")

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
    
    while True:
        try:
            question = input("Enter your query (or type 'exit' to quit): ")
            if question.lower() == 'exit':
                break
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

        except KeyboardInterrupt:
            print("\nExiting...")
            return
    
    return 

if __name__ == "__main__":
    main()