import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def fetch_celestial_data(date):
    """
    Fetch celestial event and constellation data from Gemini API (or similar).
    """
    url = "https://api.gemini.com/astronomy/celestial_event"  # Placeholder URL, adjust based on API docs
    params = {
        "date": date,
        "api_key": GEMINI_API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch celestial data: {response.status_code}"}
