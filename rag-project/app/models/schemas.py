from typing import List, Optional
from pydantic import BaseModel, Field


class UploadResponse(BaseModel):
    message: str
    document_id: str
    filename: str
    chunks_stored: int


class AskRequest(BaseModel):
    question: str = Field(..., min_length=3)
    top_k: Optional[int] = 4
    session_id: Optional[str] = None


class SourceChunk(BaseModel):
    chunk_id: str
    document_id: str
    filename: str
    text: str
    score: float
    page_number: Optional[int] = None


class AskResponse(BaseModel):
    answer: str
    sources: List[SourceChunk]


class HealthResponse(BaseModel):
    status: str
    app: str
    version: str
