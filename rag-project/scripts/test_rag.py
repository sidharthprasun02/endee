from app.services.rag_service import RAGService

rag = RAGService()

response = rag.ask("What is Endee?")

print("\nAnswer:\n", response["answer"])
print("\nSources:\n", response["sources"])