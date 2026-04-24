import math

# GLOBAL storage (important)
VECTOR_DB = []

class EndeeClient:
    def __init__(self):
        pass

    def upsert_chunks(self, document_id, filename, chunks, embeddings):
        for chunk, emb in zip(chunks, embeddings):
            VECTOR_DB.append({
                "embedding": emb,
                "text": chunk["text"],
                "filename": filename
            })
        print("TOTAL STORED:", len(VECTOR_DB))
        return len(chunks)

    def search(self, query_embedding, top_k=4):
        print("TOTAL VECTORS:", len(VECTOR_DB))

        def cosine(a, b):
            dot = sum(x*y for x,y in zip(a,b))
            mag1 = math.sqrt(sum(x*x for x in a))
            mag2 = math.sqrt(sum(x*x for x in b))
            return dot / (mag1 * mag2 + 1e-9)

        scored = []
        for item in VECTOR_DB:
            score = cosine(query_embedding, item["embedding"])
            scored.append((score, item))

        scored.sort(reverse=True, key=lambda x: x[0])

        return [x[1] for x in scored[:top_k]]