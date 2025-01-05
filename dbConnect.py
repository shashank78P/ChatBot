from constants import PINECONE_API_KEY, INDEX_NAME, PINECONE_API_KEY, REGION, DIMENSION, METRIC, CLOUD
from langchain_pinecone import PineconeVectorStore
from embedding import get_embedding_model_instance
from pinecone import Pinecone, ServerlessSpec

vector_store = None
def get_db_instance():
    global vector_store
    
    if vector_store is not None:
        return vector_store
    embedding_model = get_embedding_model_instance()

    pc = Pinecone(
        api_key=PINECONE_API_KEY
    )

    
    if INDEX_NAME not in pc.list_indexes().names():
        pc.create_index(
            name=INDEX_NAME,
            dimension=DIMENSION,
            metric=METRIC,
            spec=ServerlessSpec(
                cloud=CLOUD,
                region=REGION
            )
        )

    vector_store = pc.Index(INDEX_NAME)
    return vector_store


















# def connectToDBAndCreateSchemas():
#     client = weaviate.Client(
#         url="http://localhost:8080",
#         additional_headers={
#             # "X-HuggingFace-Api-Key": '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'
#             "X-Google-Studio-Api-Key": GOOGLE_API_KEY,
#         }                 
#     )
#     if not client.is_ready():
#         return null
    
#     print(dir(client))
    

#     # client.collections.create(
#     # "LLM_Collections",
#     # properties=[
#     #     Property(name="content", data_type=DataType.TEXT),
#     #     Property(name="content_type", data_type=DataType.TEXT),
#     # ],
#     # vectorizer_config=[
#     #     Configure.NamedVectors.multi2vec_palm(
#     #         name="title_vector",
#     #         # Define the fields to be used for the vectorization - using image_fields, text_fields, video_fields
#     #         # image_fields=[
#     #         #     Multi2VecField(name="poster", weight=0.9)
#     #         # ],
#     #         text_fields=[
#     #             Multi2VecField(name="content", weight=1)
#     #         ],
#     #     )
#     # ])

#     class_name = 'Content'
    
#     existing_classes = client.schema.get()["classes"]
    
#     print("Existing classes")
#     print(existing_classes)
    
#     is_class_name_exists = any(cls["class"] == class_name for cls in existing_classes)
    
#     # client.schema.delete_all()
#     # Define the schema
#     schema = {
#         "classes": [
#             {
#                 "class": class_name,  # Class name
#                 "description": "Stores various types of media content (video, audio, text, image)",
#                 "vectorizer": "",
#                 # "moduleConfig": {
#                 #     "text2vec-huggingface": {
#                 #         "model": "sentence-transformers/all-MiniLM-L6-v2",
#                 #         "options": {
#                 #             "waitForModel": True,
#                 #             "useGPU": False,
#                 #             "useCache": True
#                 #         }
#                 #     } 
#                 # },
#                 "properties": [
#                     {
#                         "name": "contentType",
#                         "dataType": ["string"],
#                         "description": "The type of content, e.g., VIDEO, AUDIO, TEXT, IMAGE",
#                         "indexInverted": True  # Helps with filtering by contentType
#                     },
#                     {
#                         "name": "content",
#                         "dataType": ["text"],
#                         "description": "The main content, which could be text, URL to audio/video, or image data",
#                         "moduleConfig": {
#                         "text2vec-huggingface": {
#                             "skip": False,
#                             "vectorizePropertyName": False
#                         } 
#                     }
#                     },
#                     # {
#                     #     "name": "vector",
#                     #     "dataType": ["number[]"],
#                     #     "description": "Vector representation of the content for similarity searches",
#                     # }
#                 ]
#             }
#         ]
#     }
    
#     if not is_class_name_exists:
#         client.schema.create(schema)
#         print(f"Schema created for {class_name} class.")
#     else:
#         print(f"{class_name} class already exists in the schema.")

#     return client
