import google.generativeai as genai
from config import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)

def get_llm():
    # You can use "gemini-1.5-flash" for faster responses
    return genai.GenerativeModel("gemini-1.5-flash")
