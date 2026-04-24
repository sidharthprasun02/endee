import os
import uuid
import logging
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.core.config import settings
from app.models.schemas import UploadResponse, AskRequest, AskResponse, HealthResponse
from app.services.document_processor import DocumentProcessor
from app.services.embedding_service import EmbeddingService
from app.services.endee_client import EndeeClient
from app.services.rag_service import RAGService
print("🚀 NEW ROUTES FILE IS RUNNING")
logger = logging.getLogger(__name__)
router = APIRouter()

document_processor = DocumentProcessor()
embedding_service = EmbeddingService()
endee_client = EndeeClient()
rag_service = RAGService()


@router.get("/health", response_model=HealthResponse)
def health_check():
    return HealthResponse(
        status="ok",
        app=settings.APP_NAME,
        version=settings.APP_VERSION
    )


@router.post("/upload", response_model=UploadResponse)
async def upload_document(file: UploadFile = File(...)):
    allowed_extensions = {".pdf", ".txt"}
    ext = os.path.splitext(file.filename)[1].lower()

    if ext not in allowed_extensions:
        raise HTTPException(status_code=400, detail="Only PDF and TXT files are supported.")

    try:
        file_path = await document_processor.save_upload(file)
        document_id = str(uuid.uuid4())

        chunks = document_processor.process_document(file_path, file.filename)
        if not chunks:
            raise HTTPException(status_code=400, detail="No readable text found in document.")

        texts = [chunk["text"] for chunk in chunks]
        embeddings = [embedding_service.embed_text(t) for t in texts]

        stored_count = endee_client.upsert_chunks(
            document_id=document_id,
            filename=file.filename,
            chunks=chunks,
            embeddings=embeddings
        )

        logger.info("Uploaded and indexed file=%s chunks=%s", file.filename, stored_count)

        return UploadResponse(
            message="Document uploaded and indexed successfully.",
            document_id=document_id,
            filename=file.filename,
            chunks_stored=stored_count
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.exception("Upload failed")
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")


@router.post("/ask", response_model=AskResponse)
def ask_question(payload: AskRequest):
    try:
        result = rag_service.ask(question=payload.question, top_k=payload.top_k)
        return AskResponse(**result)
    except Exception as e:
        logger.exception("Question answering failed")
        raise HTTPException(status_code=500, detail=f"Question answering failed: {str(e)}")
