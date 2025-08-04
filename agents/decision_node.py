from utils.llm import get_llm
from agents.weather_agent import get_weather
from agents.rag_agent import ask_pdf
import re

def extract_city(query):
    match = re.search(r'weather in ([\w\s]+)', query, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return None

def decide_and_route(query):
    model = get_llm()
    decision_prompt = f"""
    You are a routing agent. 
    Decide whether this question is about weather or about a PDF document.

    Query: "{query}"

    Respond with exactly one word: "weather" or "pdf".
    """
    response = model.generate_content(decision_prompt).text.strip().lower()

    if "weather" in response:
        city = extract_city(query) or "London"
        return get_weather(city)
    else:
        return ask_pdf(query)
