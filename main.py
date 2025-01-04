from nasa_api import fetch_neo_data
from gemini_api import fetch_celestial_data  # Hypothetical API call for Gemini
from utils import validate_date

def main():
    print("Welcome to the Cool Space Facts Finder!")
    birth_date = input("Enter your birth date (YYYY-MM-DD): ")
    
    if not validate_date(birth_date):
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    # Fetch NEO data from NASA API
    neo_data = fetch_neo_data(birth_date, birth_date)
    if "error" in neo_data:
        print(neo_data["error"])
    else:
        print(f"🚀 On {birth_date}, here's the closest Near-Earth Object!")
        neos = neo_data.get("near_earth_objects", {}).get(birth_date, [])
        if not neos:
            print("No NEOs were near Earth on this date.")
        else:
            for neo in neos:
                print(f"Name: {neo['name']}")
                print(f"  Diameter: {neo['estimated_diameter']['meters']['estimated_diameter_max']} meters")
                print(f"  Velocity: {neo['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']} km/h")
                print(f"  Miss Distance: {neo['close_approach_data'][0]['miss_distance']['kilometers']} km")
                print(f"  Hazardous: {'Yes' if neo['is_potentially_hazardous_asteroid'] else 'No'}")
                print()

    # Fetch Celestial Data from Gemini API (or other alternative)
    celestial_data = fetch_celestial_data(birth_date)
    if "error" in celestial_data:
        print(celestial_data["error"])
    else:
        print(f"🌠 Celestial Event for {birth_date}:")
        print(celestial_data.get("constellation", "No major celestial events observed."))
        print(f"Fun fact: {celestial_data.get('fun_fact', 'It was a great time to stargaze!')}")

if __name__ == "__main__":
    main()
