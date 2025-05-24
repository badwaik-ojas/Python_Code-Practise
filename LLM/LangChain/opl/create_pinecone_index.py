from pinecone import Pinecone
from pinecone import ServerlessSpec
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # Finds and loads .env

def create_pinecone_index(index_name = "rag-system"):
    """
    Create a Pinecone index if it doesn't already exist.
    """
    # Initialize Pinecone
    pinecone = Pinecone()
    
    # List existing indexes
    existing_indexes = pinecone.list_indexes()
    print("Existing indexes:", existing_indexes)

    # Check if index exists before creation
    if index_name not in existing_indexes.names():
        print(f"Creating index: {index_name}")
        pinecone.create_index(
            name=index_name,
            dimension=1536,  # for OpenAI text-embedding-3-small or 3-large
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",      # can also be "gcp"
                region="us-east-1"  # check [available regions](https://docs.pinecone.io/docs/regions)
            )
        )
        print("Index created!")
    else:
        print(f"Index '{index_name}' already exists.")
    return index_name

if __name__ == "__main__":
    create_pinecone_index()