import requests
from app.core.config import settings

BASE_URL = settings.ENDEE_BASE_URL
INDEX_NAME = settings.ENDEE_INDEX_NAME


def create_index():
    url = f"{BASE_URL}/index/create"
    data = {
        "index_name": INDEX_NAME,
        "dimension": 384
    }
    return requests.post(url, json=data).json()


def insert_vector(vector, text):
    url = f"{BASE_URL}/index/{INDEX_NAME}/vector/insert"

    data = {
        "vectors": [
            {
                "id": text[:10],
                "values": vector,
                "metadata": {"text": text}
            }
        ]
    }

    return requests.post(url, json=data).json()


def search_vector(vector):
    url = f"{BASE_URL}/index/{INDEX_NAME}/search"

    data = {
        "query_vector": vector,
        "top_k": settings.TOP_K
    }

    return requests.post(url, json=data).json()