from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def chunk_data(data, chunk_size=256, chunk_overlap=0):
    print("Chunking data...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunks = text_splitter.split_documents(data)
    print("Data chunked successfully.")
    print("*"*50)
    print(f"Total chunks created: {len(chunks)}")
    print("*"*50)
    print("sample chunk content:")
    print(chunks[0].page_content if chunks else "No chunks created.")
    return [Document(page_content=chunk.page_content, metadata=chunk.metadata, id=i) for i, chunk in enumerate(chunks)]

# data = chunk_data(load_from_file_util.load_document(input("Enter Path to PDF file: ")))

# # D:/RAG/Designing_Large_Language_Model_Applications.pdf

# print(data[1].page_content)  # Second page (index starts at 0)

