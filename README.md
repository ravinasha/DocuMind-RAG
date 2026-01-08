# DocuMind-RAG

A document-based AI Question Answering system using Retrieval Augmented Generation.

## Run Instructions

### Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

### Frontend
cd frontend
streamlit run app.py
