from PIL import Image
import google.generativeai as genai
import os
from dotenv import load_dotenv
import getpass

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

img = Image.open("C:/Users/Ojal/Downloads/Ojal.jpeg")

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(["Desribe the Image and people:.", img])
print(response.text)
