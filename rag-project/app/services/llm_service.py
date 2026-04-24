import google.generativeai as genai
from app.core.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)


class LLMService:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def generate_answer(self, question: str, context: str) -> str:
        prompt = f"""
Answer the question using the context below.

Context:
{context}

Question:
{question}

Answer:
"""

        response = self.model.generate_content(prompt)
        return response.text