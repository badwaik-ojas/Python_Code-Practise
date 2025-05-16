from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
from langchain.prompts import PromptTemplate

load_dotenv(find_dotenv())  # Finds and loads .env

template = '''
You are an experienced virologist.
Write a few sentences about the following virus:
{virus} in {language}.
'''

promt_template = PromptTemplate.from_template(template)

prompt = promt_template.format(virus="CORONA", language="German")

print(prompt)

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

output = llm.invoke(prompt)
print(output.content)
