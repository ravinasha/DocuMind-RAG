# DocuMind-RAG

A document-based AI Question Answering system using Retrieval Augmented Generation.


# How You Present the Project

DocuMind is a document-based AI assistant that uses Retrieval Augmented Generation. Users upload documents, the system extracts and indexes content into vector embeddings stored in MongoDB, and during chat, it retrieves the most relevant chunks and generates answers strictly from the document with proper citations.

## Run Instructions

### Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

### Frontend
cd frontend
streamlit run app.py

