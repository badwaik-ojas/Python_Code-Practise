from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

from langchain_openai import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

text = """
Mojo is a new programming language designed to combine the usability of Python with the performance of C. 
It is particularly optimized for artificial intelligence and machine learning workloads, making it a compelling 
choice for developers working in these domains.
"""

message = [
    SystemMessage(content='You are an expert copywriter with expertise in summarization'),
    HumanMessage(content=f"Please provide a short and concise summary of the following text:\n text: {text}")
]

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

response = llm.invoke(message)

print(response.content)