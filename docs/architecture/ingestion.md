# Ingestion Pipeline

The ingestion pipeline is responsible for transforming official FIA regulations into structured data that can be indexed and queried by the ApexIQ Retrieval-Augmented Generation (RAG) engine.

Current flow:

```text
Knowledge Base
      │
      ▼
Document Loader
      │
      ▼
PDF Parser
      │
      ▼
Document Pages
```

Future flow:

```text
Knowledge Base
      │
      ▼
Document Loader
      │
      ▼
Extractor
 ├── PyMuPDF
 ├── pdfplumber
 └── OCR
      │
      ▼
Document Pages
      │
      ▼
Chunk Service
      │
      ▼
Embeddings
      │
      ▼
FAISS
```

The parser layer is intentionally isolated to allow multiple extraction strategies without affecting downstream components.