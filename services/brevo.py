import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
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
            "email": "venkatapuram.pooja.22031@iitgoa.ac.in"
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
                This is a test email sent using the Brevo API.
                </p>

                <p>
                Ocean API and Brevo integration are working successfully.
                </p>

                <p>
                Regards,<br>
                Pooja
                </p>
            </body>
        </html>
        """
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json=payload
        )

        print("Status Code:", response.status_code)
        print("Response:", response.text)

        return response.json()

    except Exception as e:
        print("Brevo Error:", e)
        return None