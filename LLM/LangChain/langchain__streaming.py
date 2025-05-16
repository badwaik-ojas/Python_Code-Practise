from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # Finds and loads .env

llm = ChatOpenAI()
for chunk in llm.stream("Explain quantum mechanics in one sentence"):
    print(chunk.content, end="", flush=True)

