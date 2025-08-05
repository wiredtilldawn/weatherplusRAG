from utils.embeddings import process_pdf_and_store
from utils.llm import get_llm

vectorstore = None  # Will be initialized after PDF upload

def initialize_vectorstore(pdf_path, progress_callback=None):
    global vectorstore
    vectorstore = process_pdf_and_store(pdf_path, progress_callback=progress_callback)

def ask_pdf(query):
    if not vectorstore:
        return "⚠️ Please upload a PDF first."
    
    retriever = vectorstore.as_retriever()
    docs = retriever.invoke(query)
    context = "\n".join([doc.page_content for doc in docs])

    model = get_llm()
    prompt = f"Answer based on the following context:\n\n{context}\n\nQuestion: {query}"
    response = model.generate_content(prompt)
    return response.text


from config import PDF_PATH
def get_vectorstore():
    global vectorstore
    if not vectorstore:
        vectorstore = process_pdf_and_store(PDF_PATH)
    return vectorstore

def run_rag_agent(query):
    vs = get_vectorstore()
    retriever = vs.as_retriever()
    docs = retriever.invoke(query)
    context = "\n".join([doc.page_content for doc in docs])
    model = get_llm()
    prompt = f"Answer based on the following context:\n\n{context}\n\nQuestion: {query}"
    response = model.generate_content(prompt)
    return response.text
