from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv, find_dotenv
from langchain.chains import RetrievalQA  # Corrected import
from langchain_openai import ChatOpenAI
import pinecone
from langchain.schema import Document
from langchain_pinecone import Pinecone as LangchainPinecone

load_dotenv(find_dotenv())

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")  # Updated model

pc = pinecone.Pinecone()
index_name = 'bhagwat-gita-quotes'
index = pc.Index(index_name)

# Using the vector store
query = "what are benefits of meditation?"  # Corrected spelling
query_embedding = embeddings.embed_query(query)


response = index.query(
    vector=query_embedding,
    top_k=3,
    include_metadata=True
)

print("--- Direct Pinecone Query Results ---")
for match in response['matches']:
    print(f"Score: {match['score']}")
    print(f"Text: {match['metadata'].get('text')}")
    print("-" * 40)
print("-" * 40)

llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.5)  # Reduced temperature for more focused output

docs = [Document(page_content=match['metadata']['text']) for match in response['matches']]

vectorstore = LangchainPinecone.from_existing_index(index_name=index_name, embedding=embeddings)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

qa_chain = RetrievalQA.from_llm(
    llm=llm,
    retriever=retriever
)
# Run query
result = qa_chain.invoke({"query": query})
print(f"\n--- RetrievalQA Output ---")
print(result['result'])

# from langchain.chains import create_retrieval_chain
# from langchain.chains.combine_documents import create_stuff_documents_chain
# from langchain_core.prompts import ChatPromptTemplate

# system_prompt = (
#     "Use the given context to answer the question. "
#     "If you don't know the answer, say you don't know. "
#     "Use three sentence maximum and keep the answer concise. "
#     "Context: {context}"
# )
# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", system_prompt),
#         ("human", "{input}"),
#     ]
# )
# question_answer_chain = create_stuff_documents_chain(llm, prompt)
# chain = create_retrieval_chain(retriever, question_answer_chain)

# result = chain.invoke({"input": query})
# print(result)