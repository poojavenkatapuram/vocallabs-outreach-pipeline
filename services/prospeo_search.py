import os
import requests
from dotenv import load_dotenv

load_dotenv()

PROSPEO_API_KEY = os.getenv("PROSPEO_API_KEY")


def search_person(company_name):

    url = "https://api.prospeo.io/search-person"

    headers = {
        "X-KEY": PROSPEO_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "page": 1,
        "filters": {
            "company": {
                "names": {
                    "include": [company_name]
                }
            },
            "person_seniority": {
                "include": [
                    "Founder/Owner",
                    "C-Suite"
                ]
            }
        }
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    print("Status Code:", response.status_code)

    return response.json()