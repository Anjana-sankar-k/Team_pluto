import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
NASA_API_KEY = os.getenv("NASA_API_KEY")

def fetch_neo_data(start_date, end_date):
    """
    Fetch near-Earth objects (NEOs) data for a given date range.
    """
    url = "https://api.nasa.gov/neo/rest/v1/feed"
    params = {
        "start_date": start_date,
        "end_date": end_date,
        "api_key": NASA_API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch NEO data: {response.status_code}"}
