from evaluate import load

# Load ROUGE metric
rouge = load("rouge")

# Example predictions and references
predictions = ["The cat is on the mat."]
references = ["A cat is sitting on the mat."]

# Calculate ROUGE score
results = rouge.compute(predictions=predictions, references=references)
print(results)
