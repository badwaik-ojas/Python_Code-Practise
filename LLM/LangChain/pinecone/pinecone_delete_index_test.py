from pinecone import Pinecone
from pinecone import ServerlessSpec
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # Finds and loads .env

pinecone = Pinecone()
pinecone.list_indexes()


index_name = "bhagwat-gita-quotes"

if index_name in pinecone.list_indexes().names():
    print(f"Deleting index: {index_name}")
    pinecone.delete_index(index_name)
    print("Index deleted.")
else:
    print(f"Index '{index_name}' does not exist.")
