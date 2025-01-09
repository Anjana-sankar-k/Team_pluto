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

def interpret_neo_data(neo_data, date):
    """
    Interpret NEO data to make it more engaging and understandable.
    """
    near_objects = neo_data.get("near_earth_objects", {}).get(date, [])
    if not near_objects:
        return f"No Near-Earth Objects were near Earth on {date}."

    interpretations = []
    for neo in near_objects:
        name = neo.get("name", "Unknown")
        diameter = neo["estimated_diameter"]["meters"]["estimated_diameter_max"]
        velocity = neo["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"]
        miss_distance = neo["close_approach_data"][0]["miss_distance"]["kilometers"]
        hazardous = "Yes" if neo["is_potentially_hazardous_asteroid"] else "No"

        interpretations.append(
            f"Asteroid Name: {name}\n"
            f"- Diameter: {diameter:.2f} meters\n"
            f"- Velocity: {float(velocity):,.2f} km/h\n"
            f"- Miss Distance: {float(miss_distance):,.2f} km\n"
            f"- Potentially Hazardous: {hazardous}\n"
            f"- Fun Fact: {'This asteroid passed closer to Earth than the Moon!' if float(miss_distance) < 384400 else 'This asteroid passed at a safe distance from Earth.'}"
        )
    return "\n".join(interpretations)
