import google.generativeai as genai
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

for model in genai.list_models():
    print(f"{model.name} — {'can generate content' if 'generateContent' in model.supported_generation_methods else 'no generation'}")
