<div align="center">

# 🏎️ ApexIQ

### AI-Powered Motorsport Knowledge Platform

An intelligent **Retrieval-Augmented Generation (RAG)** platform designed to answer questions about official motorsport regulations using natural language.

Built for engineers, students, racing teams, researchers and motorsport enthusiasts.

> 🚧 **This project is under active development as part of the Oracle Next Education (ONE) Tech Challenge. New features are continuously being implemented.**

---

![Status](https://img.shields.io/badge/status-under_development-orange)
![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)
![License](https://img.shields.io/badge/license-MIT-green)

</div>

---

# 📖 Overview

ApexIQ is an AI-powered **Retrieval-Augmented Generation (RAG)** platform created to make official motorsport regulations searchable through natural language.

Instead of manually browsing hundreds of pages of FIA documentation, users can simply ask questions and receive accurate, explainable, and source-grounded answers.

The platform combines semantic search, vector databases and Large Language Models (LLMs) to deliver reliable information while maintaining references to the original regulations.

Designed with scalability in mind, ApexIQ aims to support multiple championships, multilingual responses and cloud-native deployment.

---

# 🎯 Project Goals

- Build an intelligent assistant specialized in official motorsport regulations.
- Deliver accurate answers grounded in FIA documentation.
- Support multiple motorsport championships.
- Provide multilingual assistance.
- Demonstrate modern AI Engineering practices through a complete RAG application.

---

# ✨ Features

## 🤖 Artificial Intelligence

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Source-grounded Answers
- Multilingual Responses *(planned)*

## 📚 Knowledge Base

- Automatic PDF Discovery
- Structured Document Processing
- Smart Document Chunking *(in development)*
- Multi-Championship Support

## ⚙️ Infrastructure

- FastAPI Backend
- Modular Architecture
- Cloud Deployment *(OCI planned)*

---

# 🏁 Supported Championships

| Championship | Status |
|--------------|:------:|
| Formula 1 | ✅ |
| Formula 2 | ✅ |
| Formula 3 | 🚧 |
| Formula E | 🚧 |
| WEC | 🚧 |
| IndyCar | 🚧 |
| IMSA | 🚧 |
| Super Formula | 🚧 |

---

# 🏗️ System Architecture

```text
Knowledge Base
        │
        ▼
Document Loader
        │
        ▼
Multi-Strategy Parser
        │
        ▼
Smart Chunk Service
        │
        ▼
Embedding Generator
        │
        ▼
Vector Database (FAISS)
        │
        ▼
Retriever
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
| AI | LangChain · FAISS · Embeddings |
| Frontend | React · TypeScript · TailwindCSS |
| Database | FAISS |
| Deployment | Oracle Cloud Infrastructure (OCI) |

---

# 🗺️ Roadmap

- ✅ Project Foundation
- ✅ Backend Architecture
- ✅ Knowledge Base
- ✅ Automatic PDF Discovery
- ✅ PDF Parsing
- ⏳ Smart Chunk Service
- ⏳ Embedding Generation
- ⏳ Vector Database
- ⏳ Retrieval Pipeline
- ⏳ LLM Integration
- ⏳ React Frontend
- ⏳ Multilingual Support
- ⏳ OCI Deployment

---

# 📅 Development Status

## Current Sprint

🟢 **Sprint 2 — Knowledge Base**

### ✅ Completed

- Backend architecture
- Knowledge Base organization
- Automatic document discovery
- PDF parser
- Domain models

### 🚧 In Progress

- Smart chunk generation
- Embedding pipeline
- Vector database integration

### 📌 Planned

- AI chat interface
- Multilingual support
- Cloud deployment
- OCR support for non-readable PDFs

---

# 📷 Preview

Application screenshots and demonstrations will be added as development progresses.

---

# 📚 Documentation

Project documentation is available inside the `docs/` directory.

It includes:

- Architecture
- Roadmap
- Sprint Notes
- Architecture Decision Records (ADR)
- Known Issues
- API Documentation

---

# 📜 License

This project is licensed under the MIT License.
