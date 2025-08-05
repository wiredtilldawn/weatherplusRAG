from langgraph.graph import StateGraph, END
from dataclasses import dataclass
from agents.weather_agent import get_weather
from agents.rag_agent import ask_pdf
from utils.llm import get_llm


# Define the state for the graph
@dataclass
class QueryState:
    query: str
    route: str = None
    city: str = None
    answer: str = None

# Node: Decision node using LLM

def decision_node(state: QueryState) -> QueryState:
    model = get_llm()
    decision_prompt = f"""
    You are a routing agent. Decide if the user's query is about weather or about a PDF document.
    If it is about weather, always extract the city name from the query. If no city is mentioned, use "Dehradun".
    If it is about a PDF, just reply 'pdf'.

    Query: "{state.query}"

    Respond in JSON format:
    {{"route": "weather" or "pdf", "city": "<city name>"}}
    """
    response = model.generate_content(decision_prompt).text.strip()
    import json, re
    try:
        decision = json.loads(response)
    except Exception:
        if "weather" in response:
            decision = {"route": "weather", "city": None}
        else:
            decision = {"route": "pdf", "city": None}
    state.route = decision["route"]
    city = decision.get("city")
    # Fallback: try to extract city from query if LLM fails
    if state.route == "weather" and (not city or city.lower() == "none"):
        match = re.search(r'weather in ([\w\s]+)', state.query, re.IGNORECASE)
        if match:
            city = match.group(1).strip()
    state.city = city
    return state

# Node: Weather node

def weather_node(state: QueryState) -> QueryState:
    city = state.city or "Dehradun"
    state.answer = get_weather(city)
    return state

# Node: PDF RAG node

def pdf_node(state: QueryState) -> QueryState:
    state.answer = ask_pdf(state.query)
    return state

# Build the LangGraph pipeline

graph = StateGraph(QueryState)
graph.add_node("decision", decision_node)
graph.add_node("weather", weather_node)
graph.add_node("pdf", pdf_node)


# Use add_conditional_edges for decision node
graph.add_conditional_edges(
    "decision",
    lambda s: s.route,
    {
        "weather": "weather",
        "pdf": "pdf"
    }
)
graph.add_edge("weather", END)
graph.add_edge("pdf", END)

graph.set_entry_point("decision")


# --- LangSmith tracing integration ---
from langsmith import traceable


# Compile the graph (tracing handled via @traceable and environment variables)
langgraph_pipeline = graph.compile()

@traceable
def run_langgraph_pipeline(query: str):
    state = QueryState(query=query)
    output = langgraph_pipeline.invoke(state)
    # langgraph_pipeline.invoke returns a dict with 'state' key
    final_state = output.get('state', output)
    # Handle both dataclass and dict cases
    if isinstance(final_state, dict):
        return final_state.get('answer')
    return getattr(final_state, 'answer', None)
