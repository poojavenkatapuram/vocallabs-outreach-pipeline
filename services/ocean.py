import os
import requests
from dotenv import load_dotenv

load_dotenv()

OCEAN_API_TOKEN = os.getenv("OCEAN_API_TOKEN")

def search_companies():
    headers = {
        "X-Api-Token": OCEAN_API_TOKEN,
        "Content-Type": "application/json"
    }

    payload = {
        "companiesFilters": {
            "primaryLocations": {
                "includeCountries": ["us"]
            }
        },
        "size": 5
    }

    response = requests.post(
        "https://api.ocean.io/v3/search/companies",
        headers=headers,
        json=payload
    )

    return response.json()