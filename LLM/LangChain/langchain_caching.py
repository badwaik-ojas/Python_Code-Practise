from langchain_openai import ChatOpenAI
from langchain.globals import set_llm_cache
from langchain_community.cache import InMemoryCache
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # Finds and loads .env
llm = ChatOpenAI(model_name="gpt-3.5-turbo-instruct")
set_llm_cache(InMemoryCache())

prompt = "Tell me a joke that a toddler can understand."
response = llm.invoke(prompt)
