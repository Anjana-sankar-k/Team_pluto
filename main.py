from nasa_api import fetch_neo_data, interpret_neo_data
from utils import validate_date

def main():
    print("🚀 Welcome to the Cool Space Facts Finder!")
    birth_date = input("Enter your birth date (YYYY-MM-DD): ")
    
    if not validate_date(birth_date):
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    # Fetch and interpret NEO data
    neo_data = fetch_neo_data(birth_date, birth_date)
    if "error" in neo_data:
        print(neo_data["error"])
    else:
        print(f"🚀 Near-Earth Objects on {birth_date}:")
        print(interpret_neo_data(neo_data, birth_date))

if __name__ == "__main__":
    main()
