from langchain_community.document_loaders import UnstructuredPDFLoader

# 📄 Load PDF
pdf_path = "D:/RAG/gita.pdf"
loader = UnstructuredPDFLoader(pdf_path)
data = loader.load()  # This gives a list with one Document object
print(data[:1000])
