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

# Insert vectors into the index
response = index.upsert(vectors=zip(ids, vectors), namespace='demo-namespace')
print(response)  # {'upserted_count': 5}

fetched = index.fetch(ids=['c', 'd'])
print(fetched)

# Create a new vector of 1536 dimensions (e.g., all 0.5s)
# updated_vector = [0.5] * 1536

# # Update the vector with ID 'c'
# response = index.upsert(vectors=[('c', updated_vector)])
# print(response)  # {'upserted_count': 1}

# fetched = index.fetch(ids=['c', 'd'])
# print(fetched)
