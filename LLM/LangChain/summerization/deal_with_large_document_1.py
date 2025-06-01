from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

from langchain.chains.summarize import load_summarize_chain
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter

with open('LLM/LangChain/summerization/speech.txt', encoding="utf-8") as file:
    text = file.read()

# ------------------ MAP PROMPT (for each chunk) ------------------

map_prompt = """Write a short and concise summary of the following:
Text:
```{text}```

Concise Summary:"""

map_prompt_template = PromptTemplate(
    input_variables=["text"],
    template=map_prompt
)

# ------------------ COMBINE PROMPT (summary of summaries) ------------------

combine_prompt = """Write a concise summary of the following text that covers the key points.
Add a title to the summary.
Start your summary with an introduction paragraph that gives an overview of the topic,
followed by bullet points if possible, and end the summary with a conclusion phrase.

Text:
```{text}```"""

combine_prompt_template = PromptTemplate(
    input_variables=["text"],
    template=combine_prompt
)


text_splitter = RecursiveCharacterTextSplitter(chunk_size = 512, chunk_overlap=64)
chunks = text_splitter.create_documents([text])

chain = load_summarize_chain(
    llm,
    chain_type='map_reduce',
    map_prompt=map_prompt_template,
    combine_prompt=combine_prompt_template,
    verbose=True
)

summary = chain.invoke(
chunks
)

print(summary['output_text'])


