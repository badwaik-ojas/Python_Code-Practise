from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


text = """
Mojo is a new programming language designed to combine the usability of Python with the performance of C. 
It is particularly optimized for artificial intelligence and machine learning workloads, making it a compelling 
choice for developers working in these domains.
"""

template = """
Write a concise and short summary of the following text:
Text: {text}

Translate the summary into the following language: {language}
"""

prompt = PromptTemplate(
    input_variables=["text", "language"],
    template=template.strip()
)

get_tokens = llm.get_num_tokens(prompt.format(text=text, language='English'))

chain = prompt | llm

summary = chain.invoke({
    "text": text,
    "language":"hindi"
})

print(summary.content)

