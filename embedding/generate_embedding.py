from .get_embedding_model_instance import get_embedding_model_instance 
# content : str[]
def generate_embedding(content):
    # Generate embedding
    print("content")
    print(content)
    embedding_model = get_embedding_model_instance()
    embedding = embedding_model.embed_documents(content)
    return embedding
