from IPython.display import Image, display
display(Image(filename="C:/Users/Ojal/Downloads/Ojal.jpeg"))


import base64

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

byte_image = encode_image("C:/Users/Ojal/Downloads/Ojal.jpeg")

from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")  # or gemini-pro

from langchain_core.messages import HumanMessage

prompt = "What is in this image?"
human_message = HumanMessage(content=[
    {"type": "text", "text": prompt},
    {
        "type": "image_url",
        "image_url": {
            "url": f"data:image/jpeg;base64,{byte_image}"
        }
    }
])

response = llm.invoke([human_message])
print(response.content)
