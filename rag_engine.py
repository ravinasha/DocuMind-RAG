from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from db import collection

embeddings = OpenAIEmbeddings()
llm = ChatOpenAI(model="gpt-4o-mini")

def index_document(text, filename):
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=150)
    chunks = splitter.split_text(text)

    for i, chunk in enumerate(chunks):
        vec = embeddings.embed_query(chunk)
        collection.insert_one({
            "content": chunk,
            "embedding": vec,
            "source": filename,
            "chunk": i
        })

def search(query):
    qvec = embeddings.embed_query(query)
    docs = list(collection.find())
    scored = sorted(docs, key=lambda d: sum([a*b for a,b in zip(d["embedding"], qvec)]), reverse=True)
    return scored[:5]

def answer(query):
    results = search(query)
    context = "\n".join([r["content"] for r in results])

    if not context.strip():
        return "I couldn’t find this information in the uploaded document."

    prompt = f"Answer strictly from this content:\n{context}\n\nQuestion: {query}"
    response = llm.invoke(prompt)

    citations = "\n".join([f"[{r['source']} | Chunk {r['chunk']}]" for r in results])
    return f"{response.content}\n\nSources:\n{citations}"
