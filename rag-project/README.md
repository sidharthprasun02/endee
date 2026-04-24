# RAG Document QA App using Endee + Gemini

## Overview

This project is a **Retrieval-Augmented Generation (RAG) application** that allows users to:

* Upload PDF/TXT documents
* Convert text into embeddings
* Store embeddings in a vector database (Endee)
* Ask questions based on uploaded documents
* Generate answers using Gemini LLM

The system **only answers based on document content** (not general knowledge unless extended).

---

## Architecture

```
User Upload → Text Extraction → Chunking → Embeddings
→ Store in Endee Vector DB

User Question → Query Embedding → Vector Search (Endee)
→ Retrieve Context → Gemini LLM → Final Answer
```

---

## Tech Stack

* **Backend:** FastAPI (Python)
* **Vector DB:** Endee
* **Embeddings:** Sentence Transformers / OpenAI (optional)
* **LLM:** Gemini API
* **PDF Processing:** PyMuPDF (fitz)
* **Others:** Requests, Uvicorn

---

## Project Structure

```
app/
│── api/               # FastAPI routes
│── core/              # Config settings
│── services/          # Embedding, RAG, LLM, Endee client
│── utils/             # Text chunking
│── uploads/           # Uploaded documents
│── main.py            # Entry point
```

---

## Setup Instructions

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/rag-endee-app.git
cd rag-endee-app
```

---

### Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Setup Environment Variables

Create a `.env` file in root:

```env
# Gemini API
GEMINI_API_KEY=your_gemini_api_key

# Endee
ENDEE_BASE_URL=http://localhost:8080
ENDEE_INDEX_NAME=rag_docs

# Optional
OPENAI_API_KEY=your_openai_key
```

---

### Start Endee Server

Make sure Endee is running:

```bash
http://localhost:8080
```

---

### Run FastAPI Server

```bash
uvicorn app.main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## Usage

### 1. Upload Document

* Upload PDF or TXT file
* System splits into chunks
* Embeddings are generated
* Stored in Endee

---

### 2. Ask Questions

Example:

```
What is information security?
Difference between A* and AO*?
Explain arrays
```

---

### Important Behavior

* Answers ONLY from uploaded documents ✅ 
* If context not found → "Not found in document" ❌ 
* No general knowledge (unless extended) ❌

---

## Common Issues & Fixes

### No results found (`MATCHES: []`) ❌ 

* Check embeddings are stored
* Ensure search API is working
* Verify chunking is correct

---

### Gemini quota exceeded (429) ❌ 

* Free tier limit reached
* Wait 24 hours OR upgrade plan

---

### Wrong answers / empty context ❌ 

* Improve chunk size
* Check extracted text
* Ensure embeddings match query

---

### PDF text not extracted ❌

* Some PDFs are scanned images
* Use OCR if needed

---

## Improvements (Future Work)

* Hybrid mode (Document + General AI)
* UI enhancement
* Local embeddings (no API limit)
* Better search ranking
* OCR support for scanned PDFs

---

## Example Flow

1. Upload: `Information Security.pdf`
2. Ask:

   ```
   What is information security?
   ```
3. Output:

   ```
   Answer generated from document context
   ```

---

## Author

* Sidharth Prasun

---

## License

This project is for educational and learning purposes.

---

## If you found this helpful

Give it a ⭐ on GitHub!
