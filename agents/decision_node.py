from utils.llm import get_llm
from agents.weather_agent import get_weather
from agents.rag_agent import ask_pdf
import re


def decide_and_route(query):
    model = get_llm()
    decision_prompt = f"""
    You are a routing agent. Decide if the user's query is about weather or about a PDF document. If it is about weather, extract the city name from the query. If it is about a PDF, just reply 'pdf'.

    Query: "{query}"

    Respond in JSON format:
    {{"route": "weather" or "pdf", "city": "<city name>" or null}}
    """
    response = model.generate_content(decision_prompt).text.strip()
    import json
    import re
    try:
        decision = json.loads(response)
    except Exception:
        if "weather" in response:
            decision = {"route": "weather", "city": None}
        else:
            decision = {"route": "pdf", "city": None}

    if decision["route"] == "weather":
        city = decision.get("city")
        if not city or city.lower() == "none":
            match = re.search(r'weather in ([\w\s]+)', query, re.IGNORECASE)
            if match:
                city = match.group(1).strip()
        city = city or "Dehradun"
        return get_weather(city)
    else:
        return ask_pdf(query)
