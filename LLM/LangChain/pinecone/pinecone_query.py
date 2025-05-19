import random
from pinecone import Pinecone

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # Finds and loads .env

pinecone = Pinecone()
pinecone.list_indexes()
index_name = "langchain"

import random

# Generate a query vector
query_vector = [random.random() for _ in range(1536)]

index_name = "langchain"
index = pinecone.Index(index_name)

# fetched = index.fetch(ids=['c', 'd'])
# print(fetched)

# Perform vector similarity search
response = index.query(
    vector=query_vector,
    top_k=3,
    include_values=False,   # Don't return the actual vector values
    include_metadata=False  # Optional: don't return metadata either
)

print(response)