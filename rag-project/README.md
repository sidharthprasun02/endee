# 🚀 RAG Application using Endee Vector Database

## 📌 Overview
This project implements a Retrieval-Augmented Generation (RAG) system using the Endee Vector Database.

It allows:
- Storing text as embeddings
- Performing semantic search
- Generating answers using retrieved context

---

## 🧠 Architecture

User Query → Embedding → Vector Search (Endee) → Context Retrieval → LLM → Answer

---

## ⚙️ Tech Stack

- Python (FastAPI)
- Endee Vector Database (C++)
- OpenAI / Mock LLM
- Requests (API communication)

---

## 🔧 Setup Instructions

### 1. Clone repo
```bash
git clone https://github.com/YOUR_USERNAME/rag-endee-app.git
cd rag-endee-app