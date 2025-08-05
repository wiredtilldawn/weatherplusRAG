import google.generativeai as genai
from config import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)

def get_llm():
    return genai.GenerativeModel("gemini-1.5-flash-8b")
