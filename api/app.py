from flask import Flask, render_template, request
# from main import fetch_neo_data  # Update main.py to export fetch_neo_data if necessary
from api.main import fetch_neo_data
from api.gemini_api import GeminiAstronomyClient
from api.utils import validate_date

app = Flask(__name__)  # Ensure 'static_folder' is set correctly if not standard


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        birth_date = request.form["birth_date"]

        if not validate_date(birth_date):
            error = "Invalid date format. Please use YYYY-MM-DD."
            return render_template("index.html", error=error)

        # Fetch NEO data
        neo_data = fetch_neo_data(birth_date, birth_date)
        if "error" in neo_data:
            neo_error = neo_data["error"]
            neos = []
        else:
            neos = neo_data.get("near_earth_objects", {}).get(birth_date, [])
            neo_error = None

        # Fetch Celestial Data
        client = GeminiAstronomyClient()
        celestial_data = client.fetch_celestial_data(birth_date)
        if "error" in celestial_data:
            celestial_error = celestial_data["error"]
            constellation = None
            fun_fact = None
        else:
            celestial_error = None
            constellation = celestial_data.get(
                "constellation", "No major celestial events observed."
            )
            fun_fact = celestial_data.get(
                "fun_fact", "It was a great time to stargaze!"
            )

        return render_template(
            "results.html",
            birth_date=birth_date,
            neos=neos,
            neo_error=neo_error,
            constellation=constellation,
            fun_fact=fun_fact,
            celestial_error=celestial_error,
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
