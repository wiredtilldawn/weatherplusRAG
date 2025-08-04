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
    docs = retriever.get_relevant_documents(query)
    context = "\n".join([doc.page_content for doc in docs])

    model = get_llm()
    prompt = f"Answer based on the following context:\n\n{context}\n\nQuestion: {query}"
    response = model.generate_content(prompt)
    return response.text

def get_vectorstore():
    # Initialize and return a new vectorstore instance per request
    pass

def run_rag_agent(query):
    vectorstore = get_vectorstore()
    # ...existing code...
