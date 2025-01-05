
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from constants import EMBEDDING_MODEL, GOOGLE_API_KEY

def get_embedding_model_instance():
    return GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL, google_api_key=GOOGLE_API_KEY)