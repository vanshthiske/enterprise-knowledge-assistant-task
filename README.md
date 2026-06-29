# Enterprise Knowledge Assistant

AI-powered RAG application for enterprise document question answering.

## Features

- PDF, DOCX, TXT support
- Semantic search
- FAISS vector database
- LLM-based answers
- Source citation
- Conversation history
- Hallucination prevention

## Tech Stack

- Python
- Streamlit
- LangChain
- FAISS
- Groq Llama 3
- FastEmbed

## Installation

```bash
pip install -r requirements.txt
```

```bash
streamlit run app.py
```

## Architecture

Document → Chunking → Embeddings → FAISS → Retrieval → LLM → Answer

## Limitations

- No authentication
- No multi-user support

## Future Improvements

- Hybrid search
- API deployment
- Re-ranking
- Authentication

## Architecture Diagram


User Question
      ↓
Retriever
      ↓
FAISS Vector Store
      ↓
Relevant Chunks
      ↓
Llama 3 (Groq)
      ↓
Answer + Sources