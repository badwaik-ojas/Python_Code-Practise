import tiktoken
import chuck_the_data
import load_from_file_util

def calculate_embedding_cost(chunks, model="text-embedding-ada-002", price_per_1k_tokens=0.0001):
    enc = tiktoken.encoding_for_model(model)
    total_tokens = sum(len(enc.encode(doc.page_content)) for doc in chunks)
    return total_tokens, total_tokens / 1000 * price_per_1k_tokens

data = load_from_file_util.load_document("D:/RAG/Designing_Large_Language_Model_Applications.pdf")
chunks = chuck_the_data.chunk_data(data)

tokens, cost = calculate_embedding_cost(chunks)
print(f"Total tokens: {tokens}, Estimated cost: ${cost:.6f}")
