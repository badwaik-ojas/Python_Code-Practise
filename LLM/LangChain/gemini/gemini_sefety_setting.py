from langchain_google_genai import HarmCategory, HarmBlockThreshold
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv, find_dotenv
import google.generativeai as genai

prompt = "How to shoot an animal"

load_dotenv(find_dotenv())
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

llm1 = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
response = llm1.invoke(prompt)
print("response1: ", response.content)
print("+++++++++++++++++ XXXX +++++++++++++++++")

safety_config = {
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
}

llm2 = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    safety_settings=safety_config
)

response = llm2.invoke(prompt)
print("response2: ", response.content)


