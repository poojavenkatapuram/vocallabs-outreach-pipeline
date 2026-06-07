import os
import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("OCEAN_API_TOKEN")

headers = {
    "X-Api-Token": token
}

url = "https://api.ocean.io/v2/credits/balance"

response = requests.get(url, headers=headers)

print("Status:", response.status_code)
print(response.text)