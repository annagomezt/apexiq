<p align="center">

<img src="docs/banner.png" width="100%">

</p>

<h1 align="center">
🏎 ApexIQ
</h1>

<p align="center">
<b>AI Assistant for FIA Formula 1 Regulations</b>
</p>

<p align="center">

An intelligent Retrieval-Augmented Generation (RAG) assistant capable of answering questions about the official FIA Formula One Sporting Regulations using semantic search and Large Language Models.

</p>

---

## 🚀 Overview

ApexIQ is an AI-powered assistant developed to make FIA Formula One regulations easier to search, understand and explore.

Instead of manually browsing hundreds of pages of official documentation, users can ask questions in natural language and receive accurate, grounded answers with references to the original regulations.

The assistant combines:

- 📄 Official FIA Sporting Regulations
- 🧠 Retrieval-Augmented Generation (RAG)
- 🔍 Semantic Search
- 🤖 Large Language Models
- 🌍 Automatic multilingual responses

---

# ✨ Features

- ✅ Ask questions using natural language
- ✅ Semantic document retrieval
- ✅ Grounded answers with official references
- ✅ Source citations
- ✅ Multi-language support
- ✅ Modern ChatGPT-inspired interface
- ✅ Fast vector search
- ✅ Responsive frontend

---

# 🌍 Multi-language Support

ApexIQ automatically detects the language used by the user.

Examples:

| User Language | Assistant Response |
|---------------|-------------------|
| English | English |
| Portuguese | Portuguese |
| German | German |
| Spanish | Spanish |
| French | French |
| Italian | Italian |

No language selection is required.

---

# 🏗 Architecture

<p align="center">

<img src="docs/architecture.png" width="900">

</p>

Workflow:

```
User

↓

React + Vite Frontend

↓

FastAPI Backend

↓

AI Engine

├── Prompt Builder

├── Retriever

├── Embedding Model

└── Vector Database

↓

Official FIA Regulations

↓

LLM

↓

Grounded Answer
```

---

# ⚙ Tech Stack

## Frontend

- React
- TypeScript
- TailwindCSS
- Vite

## Backend

- FastAPI
- Python

## AI

- LangChain
- HuggingFace Embeddings
- Sentence Transformers
- ChromaDB
- Retrieval-Augmented Generation (RAG)

## Deployment

- Vercel (Frontend)
- Render / Oracle Cloud (Backend)

---

# 📂 Project Structure

```
ApexIQ

apps/

    backend/

        api/

        services/

        models/

        data/

    frontend/

        src/

            components/

            pages/

            types/

docs/

README.md
```

---

# 🚀 Installation

## Clone repository

```bash
git clone https://github.com/YOUR_USERNAME/apexiq.git
```

```
cd apexiq
```

---

## Backend

```
cd apps/backend
```

Create virtual environment

```
python -m venv .venv
```

Activate

Windows

```
.venv\Scripts\activate
```

Linux

```
source .venv/bin/activate
```

Install dependencies

```
pip install -r requirements.txt
```

Run server

```
uvicorn main:app --reload
```

---

## Frontend

```
cd apps/frontend
```

Install

```
npm install
```

Run

```
npm run dev
```

---

# 🖥 Running

Backend

```
http://127.0.0.1:8000
```

Frontend

```
http://localhost:5173
```

---

# 📖 Example Questions

English

```
What is the maximum speed allowed in the pit lane?
```

Portuguese

```
Qual é o limite de velocidade no pit lane?
```

German

```
Wie hoch ist das Tempolimit in der Boxengasse?
```

Spanish

```
¿Cuál es el límite de velocidad en el pit lane?
```

---

# 💬 Example Response

```
According to Regulation B1.6.3 (Page 10),

The speed limit in the pit lane is 80 km/h during the Competition.

Source:
Sporting Regulations
Page 10
```

---

# 📚 Dataset

The assistant uses the official FIA Formula One Sporting Regulations as its knowledge base.

Documents are:

- Chunked
- Embedded
- Indexed
- Retrieved using semantic similarity

Only retrieved chunks are sent to the language model.

---

# 🔍 AI Pipeline

```
PDF

↓

Text Extraction

↓

Chunking

↓

Embeddings

↓

Vector Database

↓

Semantic Search

↓

Prompt Builder

↓

LLM

↓

Answer
```

---

# 📸 Screenshots

## Home

<img src="docs/interface.png">

---

## Example Conversation

<img src="docs/chat.png">

---

## Deploy

<img src="docs/deploy.png">

---

# 📈 Future Improvements

- Conversation history
- Authentication
- User accounts
- OCR support
- Multiple regulation versions
- FIA Technical Regulations
- FIA Financial Regulations
- Streaming responses
- Voice assistant
- Mobile version

---

# 🎯 Challenge Requirements

✔ GitHub Repository

✔ Documentation

✔ AI Agent

✔ Retrieval-Augmented Generation

✔ Semantic Search

✔ PDF Processing

✔ Deployment

✔ Working Application

---

# 👩‍💻 Author

**Ana Beatriz Gomes Santos**

Software Engineering Student

LinkedIn:

https://linkedin.com/in/SEU-LINK

GitHub:

https://github.com/SEU-USUARIO

---

# 📄 License

This project was developed for educational purposes as part of the **Oracle Next Education (ONE)** AI Challenge.

The FIA documents remain the intellectual property of the Fédération Internationale de l'Automobile (FIA).

---

<p align="center">

Made with ❤️ using Python, FastAPI, React and Artificial Intelligence.

</p>