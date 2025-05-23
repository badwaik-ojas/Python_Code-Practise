import os
from dotenv import load_dotenv, find_dotenv
import getpass

load_dotenv(find_dotenv())

if not os.getenv("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Provide your Google API Key: ")

# print(os.environ["GOOGLE_API_KEY"])

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

models = genai.list_models()
for model in models:
    print(model.name, "|", model.display_name, "|", "Supports multimodal:" if "generateContent" in model.supported_generation_methods else "")

# for model in models:
#     print((model.name, model.display_name))

model = genai.GenerativeModel("gemini-1.5-flash")

# response = model.generate_content("Explain quantum computing to a 10-year-old.")
# print(response.text)


