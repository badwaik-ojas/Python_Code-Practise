
inputs = tokenizer("What is the capital of France?", return_tensors="pt")
outputs = model(**inputs)
print(outputs)
