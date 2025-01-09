import requests

SIMBAD_TAP_URL = "https://simbad.u-strasbg.fr/simbad/sim-tap/sync"

def query_brightest_star():
    """
    Query SIMBAD for the brightest star.
    """
    query = """
    SELECT TOP 1 main_id, ra, dec, flux_v
    FROM basic
    WHERE flux_v IS NOT NULL
    ORDER BY flux_v ASC
    """
    headers = {"Content-Type": "application/x-sql"}
    response = requests.post(SIMBAD_TAP_URL, headers=headers, data=query)
    if response.status_code == 200:
        return response.text  # Change to .json() if SIMBAD API supports it
    else:
        return {"error": f"Failed to query SIMBAD: {response.status_code}"}
