def load_document(file):
    import os
    name, ext = os.path.splitext(file)

    if ext == ".pdf":
        from langchain_community.document_loaders import PyPDFLoader
        print("Loading", file)
        loader = PyPDFLoader(file)
    elif ext == ".txt":
        from langchain_community.document_loaders import TextLoader
        print("Loading", file)
        loader = TextLoader(file, encoding="utf-8")
    elif ext == '.docx':
        from langchain_community.document_loaders import Docx2txtLoader
        print("Loading", file)
        loader = Docx2txtLoader(file)
    else:
        print("Unsupported file type:", ext)
        return None
    print("Document Loaded")
    print("*"*50)
    return loader.load()

# D:/RAG/Designing_Large_Language_Model_Applications.pdf
# data = load_document(input("Enter Path to PDF file: "))

# print(data[1].page_content)  # Second page (index starts at 0)

# print(data[10].metadata)


