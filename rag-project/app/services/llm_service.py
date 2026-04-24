class LLMService:
    def generate_answer(self, question: str, context: str):
        return f"""
Mock Answer (RAG Demo)

Question:
{question}

Answer:
Based on retrieved context, Endee is a vector database used for AI applications and retrieval-augmented generation (RAG).

Context Used:
{context[:300]}
"""