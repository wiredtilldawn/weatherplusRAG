<<<<<<< HEAD
# weatherplusRAG
assignment - Neura Dynamics
=======

# Assignment - AI Engineer

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd assignment-neuraDynamics
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set your API keys as environment variables:
   ```bash
   export GOOGLE_API_KEY=your_google_api_key
   export QDRANT_API_KEY=your_qdrant_api_key
   export OPENWEATHER_API_KEY=your_openweather_api_key
   export LANGCHAIN_API_KEY=your_langchain_api_key
   ```

4. Run the Streamlit UI:
   ```bash
   streamlit run app.py
   ```

## Implementation Details

- Uses LangGraph for agentic pipeline and decision node.
- Integrates LangChain for LLM and RAG.
- Embeddings generated and stored in Qdrant vector database.
- Weather data fetched via OpenWeatherMap API.
- RAG-based PDF QA using LangChain loaders and retrievers.
- LangSmith used for LLM response evaluation.
- Streamlit UI for chat interface demonstration.

## Deliverables

- Python code in this repository.
- LangSmith logs/screenshots in `langsmith_logs/`.
- Test results in `tests/`.
- Streamlit UI demo (`app.py`).
- Loom video link in this README.
>>>>>>> 2e96a541 (primary)
