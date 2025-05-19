from langchain_text_splitters import RecursiveCharacterTextSplitter
import tiktoken
from dotenv import load_dotenv, find_dotenv
import pinecone
from langchain_community.vectorstores import Pinecone
from langchain_openai import OpenAIEmbeddings

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
print(f"length of chunks: {len(chunks)}")

print(chunks[0])

def count_tokens(texts, model="text-embedding-3-small"):
    encoding = tiktoken.encoding_for_model(model)
    return sum(len(encoding.encode(doc)) for doc in texts)

token_count = count_tokens([chunk.page_content for chunk in chunks])
print(f"Total tokens: {token_count}")

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")  # Updated model

pc = pinecone.Pinecone()
print("delete all indexes")
for i in pc.list_indexes().names():
    print(f"deleting index: {i}")
    pc.delete_index(i)

index_name = 'bhagwat-gita-quotes'
print("check if index exist")
if index_name not in pc.list_indexes().names():
    print(f"Creating index: {index_name}")
    pc.create_index(
        name=index_name,
        dimension=1536,  # for OpenAI text-embedding-3-small or 3-large
        metric="cosine",
        spec=pinecone.ServerlessSpec(
            cloud="aws",      # can also be "gcp"
            region="us-east-1"  # check [available regions](https://docs.pinecone.io/docs/regions)
        )
    )
print("Index created!")

vectors = [
    {
        "id": f"chunk-{i}",
        "values": embeddings.embed_query(chunk.page_content),
        "metadata": chunk.metadata | {"text": chunk.page_content}
    }
    for i, chunk in enumerate(chunks)
]

index = pc.Index(index_name)
index.upsert(vectors=vectors)




