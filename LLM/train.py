from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset
# Load dataset
dataset = load_dataset("imdb")
# Load tokenizer and model
model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)
# Tokenize dataset
def preprocess_function(examples):
    return tokenizer(examples["text"], truncation=True, padding=True, max_length=128)
tokenized_datasets = dataset.map(preprocess_function, batched=True)
# Split dataset
train_dataset = tokenized_datasets["train"].shuffle(seed=42).select(range(2000))  # Subset for faster training
test_dataset = tokenized_datasets["test"].shuffle(seed=42).select(range(500))
# Define training arguments
training_args = TrainingArguments(
    output_dir="./results",
    eval_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=3,
    weight_decay=0.01,
    save_strategy="epoch",
    logging_dir="./logs",
)
# Define trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
)
# Fine-tune model
trainer.train()
