'''
Under the hood, this pipeline selects a default LLM (large language model), configures it, and processes the input 
text, producing a summary. While this approach is quick and easy, there may be times when you’ll want more control 
over how the pipeline operates. This is where configuring the pipeline becomes useful.

'''

from transformers import pipeline
article_text = "I woke up early. did my breakfast, went for shopping. It was a calm day"
summarizer = pipeline("summarization")
summary = summarizer(f"summarize: {article_text}" )
print(summary)