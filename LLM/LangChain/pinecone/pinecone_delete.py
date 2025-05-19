import random
from pinecone import Pinecone

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # Finds and loads .env

pinecone = Pinecone()
pinecone.list_indexes()
index_name = "langchain"

# Generate 5 random vectors of dimension 1536
vectors = [[random.random() for _ in range(1536)] for _ in range(5)]

ids = ['a', 'b', 'c', 'd', 'e']

index_name = "langchain"
index = pinecone.Index(index_name)

#index.delete(ids=["d"])

stats = index.describe_index_stats()
print(stats)

