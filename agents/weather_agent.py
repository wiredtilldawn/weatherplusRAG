import requests
from config import OPENWEATHER_API_KEY

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200:
        return f"Error fetching weather: {data.get('message', 'Unknown error')}"
    return f"Weather in {city}: {data['weather'][0]['description']}, Temp: {data['main']['temp']}°C"
