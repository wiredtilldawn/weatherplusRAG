from agents.langgraph_pipeline import run_langgraph_pipeline
from utils.evaluator import evaluate_response

def run_agent(query):
    answer = run_langgraph_pipeline(query)
    return answer

if __name__ == "__main__":
    print(run_agent("What is the weather in Gorakhpur?"))
