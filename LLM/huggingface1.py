from transformers import pipeline

article_text = 'Prompt Construction: Before feeding input into the model, some LLMs may require further instructions, known as a prompt. For summarization tasks, the prompt might be as simple as adding summarize: before the article text. This helps the model understand what task to perform.'

summarizer = pipeline("summarization")
summary = summarizer(article_text)
print(summary)