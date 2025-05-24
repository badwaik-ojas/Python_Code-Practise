def load_from_wikipedia(url, language="en", load_max_docs=1):
    from langchain_community.document_loaders import WikipediaLoader    
    from langchain.text_splitter import RecursiveCharacterTextSplitter

    # Load the document from Wikipedia
    loader = WikipediaLoader(query=url, lang=language, load_max_docs=load_max_docs)
    data = loader.load()

    return data

# print("Loading Wikipedia page...")
# print("docs:", load_from_wikipedia("https://en.wikipedia.org/wiki/Artificial_intelligence"))
# print("+"*50)
# print("docs:", load_from_wikipedia("Artificial_intelligence"))