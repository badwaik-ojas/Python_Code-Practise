### 📦 LangChain Project Boilerplate with .env, GPT-4, and Pinecone

# ✅ Folder Structure
# my_langchain_app/
# ├── .env
# ├── app.py
# ├── requirements.txt
# └── utils/
#     └── rag.py

# ---------------- .env ----------------
# Place in root folder (DO NOT COMMIT TO GIT)
"""
OPENAI_API_KEY="sk-..."
PINECONE_API_KEY="pc-..."
PINECONE_ENVIRONMENT="us-west1-gcp"
"""

# -------------- requirements.txt --------------
# Install dependencies with: pip install -r requirements.txt
"""
python-dotenv
openai
langchain
pinecone-client
"""

# -------------- utils/rag.py --------------
import os
import pinecone
from langchain.vectorstores import Pinecone
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from dotenv import load_dotenv, find_dotenv

# Load env variables
load_dotenv(find_dotenv(), override=True)

# Init Pinecone
pinecone.init(
    api_key=os.environ.get("PINECONE_API_KEY"),
    environment=os.environ.get("PINECONE_ENVIRONMENT")
)

# Set up LangChain components
def get_qa_chain(index_name: str):
    llm = ChatOpenAI(model_name="gpt-4", openai_api_key=os.environ.get("OPENAI_API_KEY"))
    embeddings = OpenAIEmbeddings(openai_api_key=os.environ.get("OPENAI_API_KEY"))
    vectorstore = Pinecone.from_existing_index(index_name=index_name, embedding=embeddings)
    return RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())

# -------------- app.py --------------
from utils.rag import get_qa_chain

if __name__ == "__main__":
    index_name = "my-legal-doc-index"  # ensure it's already created and populated
    chain = get_qa_chain(index_name)

    print("Ask a question about your docs:")
    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit"]:
            break
        response = chain.run(query)
        print("AI:", response)
