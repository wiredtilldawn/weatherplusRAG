import google.generativeai as genai
import os
from langchain_qdrant import QdrantVectorStore
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from qdrant_client import QdrantClient
from config import QDRANT_URL, GOOGLE_API_KEY, QDRANT_API_KEY
from qdrant_client.http import models as rest



genai.configure(api_key=GOOGLE_API_KEY)


def get_google_embedding(text):
    result = genai.embed_content(
        model="models/embedding-001",
        content=text
    )
    return result["embedding"]


from langchain.embeddings.base import Embeddings

class GoogleEmbeddingWrapper(Embeddings):
    """Wrapper to integrate Google embeddings with LangChain/Qdrant."""
    def embed_documents(self, texts):
        return [get_google_embedding(t) for t in texts]
    def embed_query(self, text):
        return get_google_embedding(text)

embeddings = GoogleEmbeddingWrapper()

def process_pdf_and_store(pdf_path, progress_callback=None):
    from langchain_community.document_loaders import PyPDFLoader
    try:
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()
    except Exception as e:
        print(f"Error loading PDF: {e}")
        return None

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(documents)

    client = QdrantClient(
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY
    )

    try:
        client.get_collection("pdf_docs")
    except:
        client.create_collection(
            collection_name="pdf_docs",
            vectors_config=rest.VectorParams(size=768, distance=rest.Distance.COSINE)
        )

    vectorstore = QdrantVectorStore(
        client=client,
        collection_name="pdf_docs",
        embedding=embeddings
    )

    BATCH_SIZE = 5
    total_batches = (len(docs) + BATCH_SIZE - 1) // BATCH_SIZE
    for i in range(0, len(docs), BATCH_SIZE):
        batch = docs[i:i+BATCH_SIZE]
        vectorstore.add_documents(batch)
        if progress_callback:
            progress_callback(i // BATCH_SIZE, total_batches)

    return vectorstore

