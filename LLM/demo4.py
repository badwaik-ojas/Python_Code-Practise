from transformers import AutoTokenizer

# Load a pre-trained tokenizer (e.g., BERT)
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

text = "Hugging Face makes working with NLP models easy!"
tokens = tokenizer.encode(text, add_special_tokens=True)
print("Token IDs:", tokens)

decoded_text = tokenizer.decode(tokens)
print("Decoded Text:", decoded_text)

from transformers import pipeline
sentiment_analyzer = pipeline("sentiment-analysis")
result = sentiment_analyzer("I love using Hugging Face models!")
print(result)
sentiment_analyzer = pipeline("feature-extraction")
result = sentiment_analyzer("I love using Hugging Face models!")
print(result)

