# 📚 LlamaIndex Knowledge Base Chatbot

A **Retrieval-Augmented Generation (RAG)** chatbot that allows users to ask questions about their documents.

The system indexes documents using **LlamaIndex**, retrieves relevant information using vector embeddings, and generates answers using a **Groq LLM**. Users can upload PDFs directly from the interface and chat with the contents of the documents.

---

## 🚀 Features

- 📄 Chat with your documents
- 📥 Upload PDF files directly from the UI
- ⚡ Fast responses with cached index
- 🧠 Retrieval-Augmented Generation (RAG)
- 💬 ChatGPT-style chat interface
- 🔍 Semantic document search using embeddings

---

## 🧠 How It Works

The system follows a **RAG (Retrieval-Augmented Generation) pipeline**:

```
Documents (TXT / PDF)
        ↓
Document Loader
        ↓
Chunking
        ↓
Embeddings (HuggingFace)
        ↓
VectorStoreIndex (LlamaIndex)
        ↓
Retriever
        ↓
Groq LLM
        ↓
Generated Answer
```

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – Web interface
- **LlamaIndex** – Document indexing & retrieval
- **Groq LLM** – Language model inference
- **HuggingFace Embeddings**
- **PyPDF** – PDF parsing

---

## 📂 Project Structure

```
llamaindex-knowledge-base
│
├── app.py                # Streamlit UI
├── index_pipeline.py     # Index creation and query engine
├── requirements.txt      # Project dependencies
├── README.md
├── .gitignore
│
└── data/                 # Knowledge base documents
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/yourusername/llamaindex-knowledge-base.git
cd llamaindex-knowledge-base
```

Create a virtual environment (optional but recommended):

```
python -m venv venv
```

Activate it:

**Windows**

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Running the Application

Start the Streamlit app:

```
streamlit run app.py
```

The interface will open in your browser.

---

## 📥 Using the Chatbot

1. Upload a **PDF document** from the interface
2. The system will **index the document**
3. Ask questions about the content
4. The chatbot retrieves relevant information and generates answers

Example questions:

```
What is artificial intelligence?
Explain machine learning.
Summarize the uploaded document.
```

---

## 📌 Future Improvements

- Support multiple document uploads
- Add persistent vector databases (FAISS / Chroma)
- Improve chunking strategies
- Deploy the application online

---

## 📜 License

This project is for learning and experimentation with **Retrieval-Augmented Generation systems**.
