import os
import requests

OCEAN_API_TOKEN = os.getenv("OCEAN_API_TOKEN")


def search_companies(company_name):
    """
    Search similar companies using Ocean.io API
    """

    headers = {
        "Authorization": f"Bearer {OCEAN_API_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "company_name": company_name
    }

    try:
        response = requests.post(
            "https://api.ocean.io/v1/search",
            headers=headers,
            json=payload
        )

        return response.json()

    except Exception as e:
        print("Ocean Error:", e)
        return None