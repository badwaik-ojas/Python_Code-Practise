from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
from langchain.prompts import PromptTemplate

with open('LLM/LangChain/summerization/speech.txt', encoding="utf-8") as file:
    text = file.read()

# print(text)

docs = [Document(page_content=text)]

prompt_template = '''
write a concise and short summary of the following text.
text: {text}
'''

prompt = PromptTemplate(
    input_variables=['text'],
    template=prompt_template
)

chain = load_summarize_chain(
    llm,
    chain_type='stuff',
    prompt=prompt,
    verbose=True
)

summary = chain.invoke(
docs
)

print(summary['output_text'])


