<div align="center">

# 🏎️ ApexIQ

### AI-Powered Enterprise Knowledge Platform

A modular Retrieval-Augmented Generation (RAG) platform capable of indexing, understanding and answering questions over documents from multiple domains using natural language.

Designed for technical documentation, enterprise knowledge bases, regulations, manuals and structured documents.

> 🚧 **Developed as part of the Oracle Next Education (ONE) AI Agents Challenge.**

---

![Status](https://img.shields.io/badge/status-under_development-orange)
![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)
![License](https://img.shields.io/badge/license-MIT-green)

</div>

---

# 📖 Overview

ApexIQ is an AI-powered **Retrieval-Augmented Generation (RAG)** platform designed to transform collections of documents into an intelligent conversational knowledge base.

Instead of manually browsing hundreds of pages of documentation, users can simply ask questions in natural language and receive accurate, explainable, and source-grounded answers.

The platform combines document processing, semantic search, vector databases and Large Language Models (LLMs) to deliver reliable information while preserving references to the original source documents.

Its modular architecture allows support for multiple document formats, multiple domains, multilingual responses and cloud-native deployment.

---

# 🎯 Example Use Cases

ApexIQ is domain-agnostic and can be adapted to different knowledge bases.

Possible applications include:

- 🏢 Enterprise Documentation
- 📚 Technical Manuals
- ⚖️ Legal & Compliance
- 📑 HR Policies
- 💰 Financial Documents
- 📦 Operational Procedures
- 📊 Business Reports
- 🏥 Healthcare Documentation
- 🎓 Educational Platforms
- 🏎️ Motorsport Regulations

### Current Showcase Dataset

- ✅ Formula 1 Regulations
- ✅ Formula 2 Regulations

---

# ✨ Features

## 🤖 Artificial Intelligence

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Source-Grounded Answers
- Explainable Responses
- Multilingual Support *(planned)*

## 📚 Knowledge Base

- Automatic Document Discovery
- Intelligent Document Processing
- Smart Chunk Generation
- Metadata Extraction
- Multi-Domain Knowledge Base

## 📄 Supported Formats

| Format | Status |
|---------|:------:|
| PDF | ✅ |
| DOCX | 🚧 |
| XLSX | 🚧 |
| PPTX | 🚧 |
| Markdown | 🚧 |
| CSV | 🚧 |
| JSON | 🚧 |
| HTML | 🚧 |

## ⚙️ Infrastructure

- FastAPI Backend
- Modular Architecture
- REST API
- OCI Cloud Deployment *(planned)*

---

# 🏗️ System Architecture

```text
                Documents

 PDF   DOCX   XLSX   PPTX
  │      │      │      │
 CSV  JSON  HTML  Markdown
              │
              ▼
      Document Loaders
              │
              ▼
    Unified Document Model
              │
              ▼
     Document Pipeline
              │
              ▼
     Smart Chunk Service
              │
              ▼
     Embedding Generator
              │
              ▼
      Vector Database
          (FAISS)
              │
              ▼
      Semantic Retriever
              │
              ▼
     Large Language Model
              │
              ▼
          REST API
              │
              ▼
       React Frontend
```

---

# 🚀 Technology Stack

| Layer | Technologies |
|--------|--------------|
| Backend | Python · FastAPI |
| AI | LangChain · Sentence Transformers · FAISS |
| Frontend | React · TypeScript · TailwindCSS |
| Vector Database | FAISS |
| Cloud | Oracle Cloud Infrastructure (OCI) |

---

# 🛣️ Roadmap

## ✅ Phase 1 — Foundation

- Backend Architecture
- Knowledge Base
- Automatic Document Discovery
- PDF Processing
- Document Pipeline
- Smart Chunk Generation

## 🚧 Phase 2 — AI Core

- Embedding Generation
- Vector Database
- Semantic Search
- Retrieval Pipeline
- Prompt Engineering
- LLM Integration

## 📄 Phase 3 — Multi-Format Support

- DOCX Loader
- XLSX Loader
- PPTX Loader
- Markdown Loader
- CSV Loader
- JSON Loader
- HTML Loader

## ☁️ Phase 4 — Deployment

- Docker
- Oracle Cloud Infrastructure
- CI/CD Pipeline
- Production Environment

---

# 📅 Development Status

## Current Sprint

🟢 **Sprint 3 — AI Core**

### ✅ Completed

- Backend Architecture
- Knowledge Base
- Automatic Document Discovery
- PDF Parser
- Domain Models
- Document Pipeline
- Regulation Extraction
- Smart Chunk Generation

### 🚧 In Progress

- Embedding Generation
- Vector Database (FAISS)
- Semantic Search

### 📌 Planned

- Retrieval Pipeline
- LLM Integration
- Chat API
- React Frontend
- Multilingual Support
- OCR Support
- OCI Deployment

---

# 📷 Preview

Application screenshots, architecture diagrams and deployment demonstrations will be added as development progresses.

---

# 📚 Documentation

Project documentation is available in the `docs/` directory.

Contents include:

- Architecture
- Roadmap
- Sprint Notes
- Architecture Decision Records (ADR)
- API Documentation
- Development Guidelines

---

# 📜 License

This project is licensed under the MIT License.