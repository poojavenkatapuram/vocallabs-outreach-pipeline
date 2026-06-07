import os
import requests
from dotenv import load_dotenv

load_dotenv()

BREVO_API_KEY = os.getenv("BREVO_API_KEY")


def send_email(to_email, first_name):

    url = "https://api.brevo.com/v3/smtp/email"

    headers = {
        "accept": "application/json",
        "api-key": BREVO_API_KEY,
        "content-type": "application/json"
    }

    payload = {
        "sender": {
            "name": "Pooja",
            "email": "pooja@poojavenkatapuram.online"
        },
        "to": [
            {
                "email": to_email,
                "name": first_name
            }
        ],
        "subject": "Automation Outreach",
        "htmlContent": f"""
        <html>
            <body>
                <h2>Hello {first_name}</h2>

                <p>
                This email was sent automatically using the
                Vocallabs Outreach Pipeline.
                </p>

                <p>
                Ocean API, Prospeo API and Brevo API are
                successfully integrated.
                </p>

                <p>
                Regards,<br>
                Pooja
                </p>
            </body>
        </html>
        """
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    print("Status Code:", response.status_code)

    return response.json()