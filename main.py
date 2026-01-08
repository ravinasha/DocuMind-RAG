from fastapi import FastAPI, UploadFile, File
from rag_engine import index_document, answer
from utils import extract_text
import shutil

app = FastAPI()

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    path = f"temp/{file.filename}"
    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    text = extract_text(path)
    index_document(text, file.filename)
    return {"status": "Indexed successfully"}

@app.get("/ask")
def ask(q: str):
    return {"answer": answer(q)}

@app.post("/reset")
def reset():
    from db import collection
    collection.delete_many({})
    return {"status": "Knowledge base cleared"}
