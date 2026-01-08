import streamlit as st
import requests

st.title("📄 DocuMind - Document Q&A Assistant")

backend = "http://localhost:8000"

uploaded = st.file_uploader("Upload Document")

if uploaded:
    files = {"file": uploaded.getvalue()}
    r = requests.post(f"{backend}/upload", files={"file": uploaded})
    st.success("Document Indexed")

query = st.text_input("Ask a question")

if st.button("Ask"):
    r = requests.get(f"{backend}/ask", params={"q": query})
    st.write(r.json()["answer"])

if st.button("Clear Knowledge Base"):
    requests.post(f"{backend}/reset")
    st.success("Knowledge base reset")
