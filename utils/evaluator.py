from langsmith import Client
import uuid

client = Client()

def evaluate_response(query, response):
    run_id = str(uuid.uuid4())
    client.create_feedback(
        run_id,
        key="ai_response_eval",
        score=1.0,
        comment=f"Query: {query} | Response: {response}"
    )
    return run_id
