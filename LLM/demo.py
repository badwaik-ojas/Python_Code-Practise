from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the model and tokenizer
model_name = "distilgpt2"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

input_text = "what is it?"
inputs = tokenizer(input_text, return_tensors="pt")
outputs = model.generate(inputs["input_ids"], max_length=50)

generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(generated_text)
 