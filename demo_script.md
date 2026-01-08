
# DocuMind-RAG Demo Script

## Introduction
Hello, this is DocuMind, a Document Question & Answer assistant built using Retrieval Augmented Generation.

## Upload Document
Upload a PDF or DOCX file. The system extracts text, chunks it, generates embeddings, and stores them in MongoDB.

## Ask Questions
Ask questions related to the uploaded document. The system retrieves relevant chunks and answers strictly from the document with citations.

## Hallucination Control
If information is not found, the system responds:
"I couldn’t find this information in the uploaded document."

## Reset Knowledge Base
Clear the vector database to upload new documents.

## Closing
DocuMind ensures accurate, grounded, and citation-backed answers.
