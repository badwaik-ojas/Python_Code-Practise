from transformers import AutoModel, AutoTokenizer
model_name = "bert-base-uncased"
model = AutoModel.from_pretrained(model_name)  # Load a general BERT model
tokenizer = AutoTokenizer.from_pretrained(model_name)  # Load tokenizer

text = "Hugging Face makes working with NLP models easy!"
tokens = tokenizer.encode(text, add_special_tokens=True)
print("Token IDs:", tokens)
decoded_text = tokenizer.decode(tokens)
print("Decoded Text:", decoded_text)

from transformers import pipeline
model_name = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"
model = AutoModel.from_pretrained(model_name)  #
tokenizer = AutoTokenizer.from_pretrained(model_name)  # Load tokenizer

sentiment_analyzer = pipeline("sentiment-analysis", model=model_name, tokenizer=tokenizer)
result = sentiment_analyzer("I love using Hugging Face models!")
print(result)
