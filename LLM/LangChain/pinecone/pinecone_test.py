from pinecone import Pinecone
from pinecone import ServerlessSpec
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # Finds and loads .env

pinecone = Pinecone()
pinecone.list_indexes()


index_name = "langchain"

# Check if index exists before creation
if index_name not in pinecone.list_indexes().names():
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
