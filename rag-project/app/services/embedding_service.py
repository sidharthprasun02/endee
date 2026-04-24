import random

class EmbeddingService:
    def embed_text(self, text: str):
        # Fake embedding (size must match index dimension)
        return [random.random() for _ in range(384)]