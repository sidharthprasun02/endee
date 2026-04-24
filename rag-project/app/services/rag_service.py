from typing import Dict, Any, List
from app.core.config import settings
from app.services.embedding_service import EmbeddingService
from app.services.endee_client import EndeeClient
from app.services.llm_service import LLMService


class RAGService:
    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.endee_client = EndeeClient()
        self.llm_service = LLMService()

    def ask(self, question: str, top_k: int = None) -> Dict[str, Any]:
        k = top_k or settings.TOP_K

        # Step 1: Embed query
        query_embedding = self.embedding_service.embed_text(question)

        # Step 2: Search
        matches = self.endee_client.search(query_embedding, k)
        print("MATCHES:", matches)

        context_parts = []
        sources = []

        for match in matches:
            text = match.get("text", "")

            if text:
                context_parts.append(text)

            sources.append({
    "chunk_id": "local_" + str(len(sources)),   # fake id
    "document_id": "local_doc",                 # fake doc id
    "filename": match.get("filename", ""),
    "text": text,
    "score": 1.0                               # fake score
})

        context = "\n\n".join(context_parts)

        print("CONTEXT:", context)  # DEBUG

        # Step 3: Generate answer
        answer = self.llm_service.generate_answer(
            question=question,
            context=context
        )

        return {
            "answer": answer,
            "sources": sources
        }