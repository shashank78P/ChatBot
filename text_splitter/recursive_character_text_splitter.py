from langchain.text_splitter import RecursiveCharacterTextSplitter

def recursive_character_text_splitter(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap=50)
    return text_splitter.create_documents([documents])