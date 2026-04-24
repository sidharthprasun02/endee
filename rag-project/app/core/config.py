from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # App details
    APP_NAME: str = "RAG with Endee"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    # Gemini
    GEMINI_API_KEY: str = ""

    # (Optional) OpenAI — can keep or remove
    OPENAI_API_KEY: str = ""
    OPENAI_CHAT_MODEL: str = "gpt-4o-mini"
    OPENAI_EMBEDDING_MODEL: str = "text-embedding-3-small"

    # Endee
    ENDEE_BASE_URL: str = "http://localhost:8080"
    ENDEE_API_KEY: str = ""
    ENDEE_INDEX_NAME: str = "rag_docs"

    # Chunking settings
    CHUNK_SIZE: int = 800
    CHUNK_OVERLAP: int = 150
    TOP_K: int = 4
    MAX_CONTEXT_CHUNKS: int = 4

    # Uploads folder
    UPLOAD_DIR: str = "uploads"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()