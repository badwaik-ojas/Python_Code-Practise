# from dotenv import load_dotenv, find_dotenv
# load_dotenv(find_dotenv())  # Load environment variables

# import pinecone
# from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain.vectorstores import Pinecone
# from langchain.chains import RetrievalQA
# from langchain.chat_models import ChatOpenAI  # updated import for ChatOpenAI
# from langchain.schema import Document

# pinecone.init(api_key=pinecone_api_key, environment=pinecone_env)

# index_name = 'bhagwat-gita-quotes'
# index = pinecone.Index(index_name)

# # Initialize OpenAI embeddings (updated model name)
# embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# # Example query
# query = "what are benefits of meditation?"

# # Get query embedding
# query_embedding = embeddings.embed_query(query)

# # Query Pinecone index directly (optional)
# response = index.query(
#     vector=query_embedding,
#     top_k=3,
#     include_metadata=True
# )

# print("Raw Pinecone query results:")
# for match in response['matches']:
#     print(f"Score: {match['score']}")
#     print(f"Text: {match['metadata'].get('text', 'N/A')}")
#     print("-" * 40)

# # Prepare documents from matches for LangChain retriever
# docs = []
# for match in response['matches']:
#     text = match['metadata'].get('text')
#     if text:
#         docs.append(Document(page_content=text))

# # Create LangChain Pinecone vectorstore from existing index
# vectorstore = Pinecone.from_existing_index(index_name=index_name, embedding=embeddings)

# # Create retriever from vectorstore
# retriever = vectorstore.as_retriever()

# # Initialize ChatOpenAI LLM
# llm = ChatOpenAI(temperature=2)

# # Create RetrievalQA chain
# qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# # Run query through chain
# answer = qa_chain.run(query)
# print("\nAnswer from RetrievalQA chain:")
# print(answer)
