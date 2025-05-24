"""
    Insert data into a Pinecone index.
"""
from dotenv import load_dotenv, find_dotenv
import pinecone
from pinecone import Pinecone as PineconeClient
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore as LangChainPinecone
import load_from_file_util
import chuck_the_data

def insert_into_pinecone():

    load_dotenv(find_dotenv())  # Finds and loads .env

    # Initialize Pinecone client and index
    pinecone_client = PineconeClient()  # Connects using env vars
    index = pinecone_client.Index("rag-system")  # Actual index object
    stats = index.describe_index_stats()


    # Initialize OpenAI embeddings
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")  # Updated model

    # Initialize the vector store
    index_name = "rag-system"
    vectorstore = LangChainPinecone(index=index, embedding=embeddings)

    if stats['total_vector_count']>0:
        index.delete(delete_all=True)
        print(f"Deleted all vectors from index '{index_name}'.")
    else:
        print(f"No vectors to delete in index '{index_name}'.")
    # load data
    data = load_from_file_util.load_document("LLM/bhagwat_gita_quotes.txt")

    # chunk the data
    chunks = chuck_the_data.chunk_data(data, chunk_size=400, chunk_overlap=50)

    # Insert data into Pinecone
    print(f"Inserting {len(chunks)} chunks into Pinecone index '{index_name}'...")
    print("*"*50)
    for i, chunk in enumerate(chunks):
        vectorstore.add_texts([chunk.page_content], metadatas=[{"source": f"chunk-{i}"}])
        print(f"Inserted chunk {i+1}/{len(chunks)} into Pinecone index '{index_name}'.")
    print("*"*50)
    print("All chunks inserted successfully.")

if __name__ == "__main__":
    insert_into_pinecone()