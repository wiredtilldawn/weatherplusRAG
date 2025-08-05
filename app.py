import streamlit as st
import os
import hashlib
from main import run_agent
from agents.rag_agent import initialize_vectorstore

st.set_page_config(page_title="AI Engineer Assignment", page_icon="🤖")

st.title("AI Engineer Assignment Demo")
st.markdown("### Upload a PDF for RAG-based Q&A")

def get_file_hash(file_bytes):
    return hashlib.md5(file_bytes).hexdigest()

uploaded_pdf = st.file_uploader("Upload PDF", type=["pdf"])
if uploaded_pdf is not None:
    pdf_bytes = uploaded_pdf.read()
    file_hash = get_file_hash(pdf_bytes)
    cache_path = f"data/cache_{file_hash}.pdf"

    if not os.path.exists(cache_path):
        with open(cache_path, "wb") as f:
            f.write(pdf_bytes)

        st.info("🔄 Processing PDF and creating embeddings...")
        progress_text = st.empty()
        progress_bar = st.progress(0)

        initialize_vectorstore(cache_path, progress_callback=lambda i, total: (
            progress_bar.progress((i + 1) / total),
            progress_text.markdown(f"Embedding chunk {i+1}/{total}...")
        ))

        progress_text.markdown("✅ Embeddings created successfully!")
        st.success("PDF uploaded and processed!")
    else:
        st.info("⚡ Using cached embeddings for this PDF!")
        initialize_vectorstore(cache_path)

st.markdown("### Ask a question")
user_query = st.text_input("Enter your question:")

if st.button("Submit"):
    if user_query:
        with st.spinner("Processing..."):
            answer = run_agent(user_query)
        st.success(answer)
