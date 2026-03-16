# RAG-OFFICE-Assistant
Retrieval-Augmented Generation (RAG) assistant for office documents
Sure! Here’s the **complete README content** you can directly paste into your `README.md` file:

---

# 📚 RAG Document Assistant

A **Retrieval-Augmented Generation (RAG)** application that allows users to ask questions about local **PDF and DOCX documents**.
The system retrieves relevant information from documents using **semantic search** and generates answers using **Meta Llama-3** through the **HuggingFace Router API**.

The application is built using **LangChain, FAISS, HuggingFace Embeddings, and Streamlit**.

---

# 🚀 Project Overview

Large Language Models (LLMs) are powerful but have limitations:

* They cannot access **private or local documents**
* They may produce **hallucinated answers**

This project solves these problems using **Retrieval-Augmented Generation (RAG)**.

Instead of relying only on the LLM's knowledge, the system:

1. Retrieves **relevant information from documents**
2. Provides that context to the LLM
3. The LLM generates an answer based on the **retrieved document content**

This ensures the responses are **grounded in the actual documents**.

---

# 🧠 How the System Works

```
User Question
      │
      ▼
Convert Question to Embedding
      │
      ▼
FAISS Vector Database Search
      │
      ▼
Retrieve Top 3 Relevant Chunks
      │
      ▼
Prompt Construction
(Context + Question)
      │
      ▼
Meta Llama-3 (via HuggingFace Router)
      │
      ▼
Generated Answer
```

---

# ⚙️ Tech Stack

| Technology                       | Purpose                                |
| -------------------------------- | -------------------------------------- |
| **Python**                       | Core programming language              |
| **LangChain**                    | RAG pipeline orchestration             |
| **FAISS**                        | Vector similarity search               |
| **Sentence Transformers**        | Text embeddings                        |
| **Meta Llama-3 8B Instruct**     | Language model for answering questions |
| **HuggingFace Router API**       | Model inference                        |
| **Streamlit**                    | Interactive web interface              |
| **PyPDFLoader / Docx2txtLoader** | Document parsing                       |

---

# 📂 Project Structure

```
Genai_project/
│
├── data/
│   ├── sample1.pdf
│   ├── sample2.docx
│
├── vectorstore/
│   ├── index.faiss
│   ├── index.pkl
│
├── ingest.py
├── rag_app.py
├── .env
├── .gitignore
└── README.md
```

---

# 🔄 Project Workflow

The project consists of **two main components**:

## 1️⃣ Document Ingestion (`ingest.py`)

This script processes documents and creates a **vector database** for semantic search.

### Steps Performed

1. Load documents from the **data folder**
2. Extract text from:

   * PDF files
   * DOCX files
3. Split documents into smaller text chunks
4. Convert chunks into **vector embeddings**
5. Store embeddings in a **FAISS vector database**

### Document Loading

* `PyPDFLoader`
* `Docx2txtLoader`

These loaders extract text from PDF and DOCX files.

### Text Splitting

Documents are split using:

* `RecursiveCharacterTextSplitter`
* `chunk_size = 1000`, `chunk_overlap = 200`

This improves **semantic retrieval accuracy**.

### Embedding Model

* `sentence-transformers/all-MiniLM-L6-v2`

Converts text into **dense numerical vectors** used for similarity search.

---

## 2️⃣ RAG Web Application (`rag_app.py`)

The Streamlit application allows users to interact with the system through a **chat interface**.

### Steps Performed

1. Load the FAISS vector database
2. Convert the user question into an embedding
3. Retrieve the **top 3 most relevant document chunks**
4. Combine the retrieved context with the question
5. Send the prompt to **Meta Llama-3**
6. Display the generated answer in the UI

---

# 💬 Streamlit User Interface

The application provides a **ChatGPT-style interface** where users can ask questions about their documents.

### Features

* Chat-based document question answering
* Persistent chat history
* Fast retrieval using FAISS
* Efficient embedding caching
* Local document understanding

**Sidebar**: Shows the retrieved chunks for transparency and debugging.

---

# 🔑 Environment Configuration

Create a `.env` file in the root directory:

```
HF_TOKEN=your_huggingface_router_api_token
```

This token is used to access the **HuggingFace Router API** for running the Llama-3 model.

---

# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/rag-document-assistant.git
cd rag-document-assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

### Step 1 — Add Documents

Place your documents inside the **data folder**.

Supported formats:

* `.pdf`
* `.docx`

Example:

```
data/
 ├── research_paper.pdf
 ├── resume.docx
```

---

### Step 2 — Generate Vector Database

Run the ingestion script:

```bash
python ingest.py
```

This will create a **vectorstore/** folder containing the FAISS index.

---

### Step 3 — Start the RAG Application

Run the Streamlit app:

```bash
streamlit run rag_app.py
```

The application will open in your browser.

---

# 🧪 Example Queries

* What is the main topic of the document?
* Summarize the key points.
* What conclusions are mentioned in the paper?
* Explain the methodology described.

---

# 🎯 Key Features

* Retrieval-Augmented Generation (RAG)
* Semantic document search
* PDF and DOCX support
* Chat-based interface
* Efficient vector storage with FAISS
* LLM-powered document understanding

---

# 📈 Future Improvements

* Upload documents directly in the UI
* Show document source citations
* Add conversation memory
* Stream LLM responses in real-time
* Deploy to **Streamlit Cloud** or **HuggingFace Spaces**
* Support additional file formats

---

# 👨‍💻 Author

**Aditya Jangiti**

This project demonstrates how **vector search and LLMs can be combined** to build intelligent document assistants.

---

⭐ If you found this project useful, consider **starring the repository**.

---


