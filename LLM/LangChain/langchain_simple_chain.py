from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableLambda
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # Finds and loads .env

# 1. Create a prompt template
template = """
You are an experienced virologist.
Write a few sentences about the following virus:
{virus} in {language}.
"""

prompt = PromptTemplate.from_template(template)

# 2. Initialize the LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# 3. Build a simple chain using the | operator
chain = (
    prompt
    | llm
    | RunnableLambda(lambda x: x.content)  # Extract content from the AIMessage
)

# 4. Invoke the chain
response = chain.invoke({"virus": "CORONA", "language": "Spanish"})
print(response)
