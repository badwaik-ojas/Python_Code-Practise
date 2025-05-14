
from datasets import load_dataset
from transformers import pipeline
xsum_dataset = load_dataset("xsum", version = "1.2.0", cache_dir ="D:/temp",trust_remote_code=True)
x = xsum_dataset["train"]
x.to_pandas()
summarizer = pipeline(
	task = "summarization",  
	mode = "t5-small",  
	min_length = 20,  
	max_length = 50,
	truncation = True, 
	model_kargs={"cache_dir":"D:/temp"})
results = summarizer(xsum_dataset["document"])