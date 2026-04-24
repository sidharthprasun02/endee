from app.services.embedding_service import EmbeddingService
from app.services.endee_client import create_index, insert_vector

embedding_service = EmbeddingService()

create_index()

docs = [
    "Endee is a vector database for AI applications.",
    "RAG improves LLM responses using retrieval."
]

for doc in docs:
    vec = embedding_service.embed_text(doc)
    insert_vector(vec, doc)

print("Data stored!")