# Install latest packages
# pip install langchain langchain-community openai pypdf

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

with open('LLM/LangChain/summerization/speech.txt', encoding="utf-8") as file:
    text = file.read()


text_splitter = RecursiveCharacterTextSplitter(chunk_size = 512, chunk_overlap=64)
chunks = text_splitter.create_documents([text])

# Custom Initial Prompt
initial_template = """
Write a concise summary of the following text. Focus on the key ideas and extract critical insights.

Text:
{text}

Summary:
"""
initial_prompt = PromptTemplate(template=initial_template, input_variables=["text"])

# Custom Refine Prompt
refine_template = """
Your job is to refine the existing summary based on the additional text below.

Existing Summary:
{existing_answer}

Additional Text:
{text}

Please revise the summary to include any new information, keeping it concise. Provide:
- An introduction
- Bullet points for key ideas
- A final conclusion

Refined Summary:
"""
refine_prompt = PromptTemplate(
    template=refine_template,
    input_variables=["existing_answer", "text"]
)

# Load Refine Chain
chain = load_summarize_chain(
    llm=llm,
    chain_type="refine",
    question_prompt=initial_prompt,
    refine_prompt=refine_prompt,
    return_intermediate_steps=False,
    verbose=True
)

# Run summarization
summary = chain.run(chunks)
print(summary)
