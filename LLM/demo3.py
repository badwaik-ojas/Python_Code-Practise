from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Step 1: Load the tokenizer and model
model_name = "facebook/bart-large-cnn"  # Pre-trained summarization model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Step 2: Create a pipeline for summarization
summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

# Step 3: Input text for summarization
text = """
Hugging Face's Transformers library is an open-source project designed to make working with large pre-trained language models easier.
It provides tools to use, train, and deploy models for tasks like text classification, summarization, translation, and question answering.
The library supports popular models like BERT, GPT, T5, and many more, making it a go-to choice for NLP practitioners and researchers.
"""

# Step 4: Perform summarization
summary = summarizer(f"summarize: {text}", max_length=50, min_length=25, do_sample=False)

# Step 5: Display the result
print("Original Text:")
print(text)
print("\nSummary:")
print(summary[0]['summary_text'])
