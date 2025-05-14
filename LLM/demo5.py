import pdfplumber

# Extracting text from the PDF
with pdfplumber.open("C:/Users/Ojal/Downloads/lekl101.pdf") as pdf:
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
print(text[:500])  # Preview the first 500 characters

from transformers import AutoTokenizer, AutoModelForQuestionAnswering, TrainingArguments, Trainer
from datasets import load_dataset

# Load pre-trained tokenizer and model
model_name = "bert-large-uncased-whole-word-masking-finetuned-squad"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)

# Load your dataset (convert your PDF content into QA format first)
# For demonstration, using SQuAD:
dataset = load_dataset("squad")

# Tokenize the dataset
def preprocess_function(examples):
    inputs = tokenizer(
        examples["question"], examples["context"], truncation=True, padding="max_length", max_length=384
    )
    inputs["start_positions"] = examples["answers"]["answer_start"][0]
    inputs["end_positions"] = [
        ans["answer_start"][0] + len(ans["text"][0]) for ans in examples["answers"]
    ]
    return inputs

tokenized_dataset = dataset.map(preprocess_function, batched=True)

# Training arguments
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    learning_rate=3e-5,
    num_train_epochs=3,
    per_device_train_batch_size=8,
    weight_decay=0.01,
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["validation"],
)

# Fine-tune the model
trainer.train()
