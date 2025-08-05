
from langsmith import Client
client = Client()

def evaluate_response(query, response):
    # Feedback logging removed; rely on automatic LangSmith tracing only
    pass
