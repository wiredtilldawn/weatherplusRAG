import os

print("========== LangSmith / LangChain Tracing Diagnostics ==========")
print("LANGCHAIN_TRACING_V2:", os.getenv("LANGCHAIN_TRACING_V2"))
print("LANGCHAIN_API_KEY set:", os.getenv("LANGCHAIN_API_KEY"))
print("LANGCHAIN_PROJECT:", os.getenv("LANGCHAIN_PROJECT"))

print("LANGSMITH_TRACING:", os.getenv("LANGSMITH_TRACING"))
print("LANGSMITH_ENDPOINT:", os.getenv("LANGSMITH_ENDPOINT"))
print("LANGSMITH_API_KEY set:", os.getenv("LANGSMITH_API_KEY"))
print("LANGSMITH_PROJECT:", os.getenv("LANGSMITH_PROJECT"))
print("===============================================================")
