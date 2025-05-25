def ask_questions(question):
    from langchain.chains import create_retrieval_chain
    from langchain.chains.combine_documents import create_stuff_documents_chain
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_openai import OpenAIEmbeddings
    from dotenv import load_dotenv, find_dotenv
    from langchain.chains import RetrievalQA  # Corrected import
    from langchain_openai import ChatOpenAI
    import pinecone
    from langchain_pinecone import Pinecone as LangchainPinecone
    from langchain_core.runnables import RunnablePassthrough

    load_dotenv(find_dotenv())
    llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.5)  # Reduced temperature for more focused output


    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")  # Updated model

    pc = pinecone.Pinecone()
    index_name = "rag-system"
    index = pc.Index(index_name)

    vectorstore = LangchainPinecone.from_existing_index(index_name=index_name, embedding=embeddings)

    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    system_prompt = (
        "Use the given context to answer the question. "
        "If you don't know the answer, say you don't know. "
        "Use three sentence maximum and keep the answer concise. "
        "Context: {context}"
    )
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )
    context_docs = retriever.invoke(question)
    print(f"Retrieved {len(context_docs)} documents relevant to the question.")
    print("\n","*"*50,"\n")
    for i, doc in enumerate(context_docs):
        print(f"Document {i+1}:")
        print(doc.page_content)
        print("\n","*"*50,"\n")
    
    print("Creating Question-Answer Chain...")
    chain = RunnablePassthrough() | prompt | llm

    print("Retrieval chain created.")
    result = chain.invoke({"context": context_docs, "input": question})
    
    return result.content

if __name__ == "__main__":
    while True:
        try:
            question = input("Enter your question (or type 'exit' to quit): ")
            if question.lower() == 'exit':
                break
            answer = ask_questions(question)
            print(f"Answer: {answer}")
        except Exception as e:
            print(f"An error occurred: {e}")
            break

