import os

# Load API keys from environment variables for security and clean coding
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
PDF_PATH = "data/sample.pdf"

LANGCHAIN_TRACING_V2 = True
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")