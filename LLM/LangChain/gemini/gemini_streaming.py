import google.generativeai as genai
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash", generation_config={"temperature": 0})

prompt = "Write a scientific paper outlining the mathematical foundation of our universe."

# Streaming response
for chunk in model.generate_content(prompt, stream=True):
    print(chunk.text, end="", flush=True)  # Optional: add `print('-'*100)` after each for clarity
