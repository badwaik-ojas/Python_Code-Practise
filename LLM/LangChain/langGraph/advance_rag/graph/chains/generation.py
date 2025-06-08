from langchain import hub
from langchain.output_parsers import StructuredOutputParser

from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model='gpt-4-turbo', temperature=0)
prompt = hub.pull("rlm/rag-prompt")
# parser = StructuredOutputParser.from_llm(llm, method="function_calling")

generation_chain = prompt | llm | StrOutputParser()
