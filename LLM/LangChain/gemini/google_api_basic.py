import google.generativeai as genai

genai.configure(api_key="AIzaSyDLIAVYV3n4sDTLSujuF3_sTSyiMIKDwFE")

for model in genai.list_models():
    print(f"{model.name} — {'can generate content' if 'generateContent' in model.supported_generation_methods else 'no generation'}")
