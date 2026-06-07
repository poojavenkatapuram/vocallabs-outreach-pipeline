import os
import requests

PROSPEO_API_KEY = os.getenv("PROSPEO_API_KEY")


def find_email(full_name, company):
    """
    Find verified email using Prospeo
    """

    headers = {
        "X-KEY": PROSPEO_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "name": full_name,
        "company": company
    }

    try:
        response = requests.post(
            "https://api.prospeo.io/email-finder",
            headers=headers,
            json=payload
        )

        return response.json()

    except Exception as e:
        print("Prospeo Error:", e)
        return None