from typing import Dict, Any, List
from app.core.config import settings
from app.services.embedding_service import EmbeddingService
from app.services.endee_client import search_vector
from app.services.llm_service import LLMService


class RAGService:
    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.llm_service = LLMService()

    def ask(self, question: str, top_k: int = None) -> Dict[str, Any]:
        k = top_k or settings.TOP_K

        # Step 1: Embed query
        query_embedding = self.embedding_service.embed_text(question)

        # Step 2: Search in Endee (FUNCTION call, not class)
        response = search_vector(query_embedding)

        matches = response.get("results", []) if isinstance(response, dict) else response

        sources: List[Dict[str, Any]] = []
        context_parts = []

        for match in matches[:settings.MAX_CONTEXT_CHUNKS]:
            metadata = match.get("metadata", {})
            text = metadata.get("text", "")
            score = float(match.get("score", 0.0))

            sources.append({
                "chunk_id": str(match.get("id", "")),
                "document_id": metadata.get("document_id", ""),
                "filename": metadata.get("filename", ""),
                "text": text,
                "score": score,
                "page_number": metadata.get("page_number")
            })

            context_parts.append(
                f"[Source: {metadata.get('filename', 'unknown')}, "
                f"Page: {metadata.get('page_number', 'N/A')}]\n{text}"
            )

        context = "\n\n".join(context_parts) if context_parts else "No relevant context found."

        # Step 3: Generate answer
        answer = self.llm_service.generate_answer(
            question=question,
            context=context
        )

        return {
            "answer": answer,
            "sources": sources
        }