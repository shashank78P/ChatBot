import uuid
from embedding import generate_embedding 
from text_splitter import recursive_character_text_splitter


def textDataHandler(content, vectorStore,namespace, metadata, context):
    chunks = recursive_character_text_splitter(content)
    vectors = []
    for i, chunk in enumerate(chunks):
        modifiedContent = f"Context: {context} : {i + 1}| Content: {chunk.page_content}"
        vector_embeddings = generate_embedding([modifiedContent])
        for i in range(0, len(vector_embeddings)):
            vectors.append({
                'id': str(uuid.uuid4()),
                "values": vector_embeddings[i], 
                "metadata": {**metadata, 'content': modifiedContent}
            })
        
    vectorStore.upsert(
        vectors=vectors,
        namespace= namespace
    )
    return chunks