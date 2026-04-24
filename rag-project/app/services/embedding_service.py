import random

class EmbeddingService:
    def embed_text(self, text: str):
        return [random.random() for _ in range(384)]