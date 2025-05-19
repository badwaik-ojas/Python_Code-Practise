from langchain_text_splitters import RecursiveCharacterTextSplitter
import tiktoken
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


# Create a text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,         # tokens or characters, depending on length_function
    chunk_overlap=50,
    length_function=len     # could use token counter instead for token-aware chunking
)

# Read a long text file
with open("LLM/bhagwat_gita_quotes.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

# Create chunks
chunks = text_splitter.create_documents([raw_text])

print(chunks[0])

def count_tokens(texts, model="text-embedding-3-small"):
    encoding = tiktoken.encoding_for_model(model)
    return sum(len(encoding.encode(doc)) for doc in texts)

token_count = count_tokens([chunk.page_content for chunk in chunks])
print(f"Total tokens: {token_count}")

from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")  # Updated model

# Embed one chunk (example)
vector = embeddings.embed_query(chunks[0].page_content)

print(vector)

