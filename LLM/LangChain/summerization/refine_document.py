from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

from langchain.chains.summarize import load_summarize_chain
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter

with open('LLM/LangChain/summerization/speech.txt', encoding="utf-8") as file:
    text = file.read()


text_splitter = RecursiveCharacterTextSplitter(chunk_size = 512, chunk_overlap=64)
chunks = text_splitter.create_documents([text])

chain = load_summarize_chain(
    llm,
    chain_type='refine',
    verbose=True
)

summary = chain.invoke(
chunks
)

print(summary['output_text'])


