import os
import requests
from dotenv import load_dotenv

load_dotenv()

PROSPEO_API_KEY = os.getenv("PROSPEO_API_KEY")


def find_person(full_name, company_name):
    url = "https://api.prospeo.io/enrich-person"

    headers = {
        "X-KEY": PROSPEO_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "only_verified_email": True,
        "data": {
            "full_name": full_name,
            "company_name": company_name
        }
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json=payload
        )

        print("Status Code:", response.status_code)

        return response.json()

    except Exception as e:
        print("Prospeo Error:", e)
        return None