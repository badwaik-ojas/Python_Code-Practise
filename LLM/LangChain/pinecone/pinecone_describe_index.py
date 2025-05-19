import random
from pinecone import Pinecone

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # Finds and loads .env

pinecone = Pinecone()
index_name = "langchain"
index = pinecone.Index(index_name)
print(index.describe_index_stats())

