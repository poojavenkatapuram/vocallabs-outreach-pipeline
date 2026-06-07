import os
import requests
from dotenv import load_dotenv

load_dotenv()

OCEAN_API_TOKEN = os.getenv("OCEAN_API_TOKEN")

def search_companies(domain):

    headers = {
        "X-Api-Token": OCEAN_API_TOKEN,
        "Content-Type": "application/json"
    }

    payload = {
        "size": 5,
        "companiesFilters": {
            "lookalikeDomains": [
                domain
            ]
        }
    }

    response = requests.post(
        "https://api.ocean.io/v3/search/companies",
        headers=headers,
        json=payload
    )

    print("Status Code:", response.status_code)
    print("Response:", response.text)

    return response.json()