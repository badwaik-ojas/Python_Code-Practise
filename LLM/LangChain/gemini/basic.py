# langchain + Google Generative Language API
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # Finds and loads .env

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.8
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{question}")
])

chain = prompt | llm
response = chain.invoke({"question": "What is the capital of France"})
print(response.content)
