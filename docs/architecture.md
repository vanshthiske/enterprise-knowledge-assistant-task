# System Architecture

## Components

1. Document Loader
2. Chunking Module
3. Embedding Model
4. Vector Database
5. Retriever
6. LLM
7. Streamlit Interface

## Data Flow

User Uploads Documents
↓
Text Extraction
↓
Chunking
↓
Embedding Generation
↓
FAISS Index
↓
User Query
↓
Retriever
↓
LLM
↓
Answer + Sources

## Scalability

- Replace FAISS with Pinecone.
- Deploy with Docker.
- Add FastAPI backend.
- Add Redis cache.