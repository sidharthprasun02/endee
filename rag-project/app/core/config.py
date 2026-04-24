from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    OPENAI_API_KEY: str
    OPENAI_CHAT_MODEL: str
    OPENAI_EMBEDDING_MODEL: str

    ENDEE_BASE_URL: str
    ENDEE_API_KEY: str
    ENDEE_INDEX_NAME: str

    CHUNK_SIZE: int
    CHUNK_OVERLAP: int
    TOP_K: int
    MAX_CONTEXT_CHUNKS: int

    class Config:
        env_file = ".env"


settings = Settings()