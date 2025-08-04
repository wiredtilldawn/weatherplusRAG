from agents.decision_node import decide_and_route
from utils.evaluator import evaluate_response

def run_agent(query):
    answer = decide_and_route(query)
    evaluate_response(query, answer)
    return answer

if __name__ == "__main__":
    print(run_agent("What is the weather in Gorakhpur?"))
