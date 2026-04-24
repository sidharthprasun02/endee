import os
import uuid
import fitz  # PyMuPDF
from typing import List, Dict, Any
from fastapi import UploadFile
from app.utils.text_utils import chunk_text
from app.core.config import settings


class DocumentProcessor:
    def __init__(self):
        os.makedirs(settings.UPLOAD_DIR, exist_ok=True)

    async def save_upload(self, file: UploadFile) -> str:
        file_ext = os.path.splitext(file.filename)[1].lower()
        unique_name = f"{uuid.uuid4()}{file_ext}"
        file_path = os.path.join(settings.UPLOAD_DIR, unique_name)

        content = await file.read()
        with open(file_path, "wb") as f:
            f.write(content)

        return file_path

    def extract_text_from_pdf(self, file_path: str) -> List[Dict[str, Any]]:
        pages = []
        doc = fitz.open(file_path)

        for page_num, page in enumerate(doc, start=1):
            text = page.get_text("text")

            # ✅ DEBUG PRINT (CORRECT PLACE)
            print("PAGE TEXT SAMPLE:", text[:200])

            if text and text.strip():
                pages.append({
                    "page_number": page_num,
                    "text": text.strip()
                })

        doc.close()
        return pages

    def extract_text_from_txt(self, file_path: str) -> List[Dict[str, Any]]:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()

        return [{"page_number": None, "text": text.strip()}]

    def process_document(self, file_path: str, original_filename: str) -> List[Dict[str, Any]]:
        ext = os.path.splitext(original_filename)[1].lower()

        if ext == ".pdf":
            raw_sections = self.extract_text_from_pdf(file_path)
        elif ext == ".txt":
            raw_sections = self.extract_text_from_txt(file_path)
        else:
            raise ValueError("Unsupported file type. Only PDF and TXT are allowed.")

        processed_chunks = []

        for section in raw_sections:
            chunks = chunk_text(
                section["text"],
                chunk_size=settings.CHUNK_SIZE,
                overlap=settings.CHUNK_OVERLAP
            )

            for idx, chunk in enumerate(chunks):
                processed_chunks.append({
                    "chunk_index": idx,
                    "page_number": section["page_number"],
                    "text": chunk
                })

        # ✅ DEBUG PRINT (CORRECT PLACE)
        print("TOTAL CHUNKS:", len(processed_chunks))

        return processed_chunks