from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI  # pending official release
from dotenv import load_dotenv
import getpass
load_dotenv()

prompt = PromptTemplate.from_template("Translate the following to French: {text}")
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

chain = prompt | llm | StrOutputParser()
print(chain.invoke({"text": "Hello, how are you?"}))
