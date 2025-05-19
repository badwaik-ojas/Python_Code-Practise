from pinecone import Pinecone
from pinecone import ServerlessSpec
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # Finds and loads .env

pinecone = Pinecone()
pinecone.list_indexes()
index_name = "langchain"

# Select the index
index = pinecone.Index(index_name)

# Describe the index stats
stats = index.describe_index_stats()
print(stats)
