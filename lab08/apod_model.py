import requests

API_URL = "https://api.nasa.gov/planetary/apod"
API_KEY = "DEMO_KEY"

def get_apod(date=None):
    params = {"api_key": API_KEY}
    if date:
        params["date"] = date
    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API call failed: {response.status_code}")
