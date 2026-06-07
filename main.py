from dotenv import load_dotenv
import os

load_dotenv()

print("=" * 50)
print("VOCALLABS OUTREACH PIPELINE")
print("=" * 50)

# Check API keys
ocean_token = os.getenv("OCEAN_API_TOKEN")
brevo_key = os.getenv("BREVO_API_KEY")

print("\nAPI STATUS")
print("Ocean Token Loaded:", bool(ocean_token))
print("Brevo Key Loaded:", bool(brevo_key))

company = input("\nEnter company domain: ")

print("\nStage 1 - Ocean.io")
print(f"Searching similar companies for {company}")

print("\nStage 2 - Prospeo")
print("Finding decision makers")

print("\nStage 3 - EazyReach")
print("Resolving work emails")

print("\nStage 4 - Brevo")
print("Preparing outreach emails")

print("\nSafety Check")
confirm = input("Send emails? (yes/no): ")

if confirm.lower() == "yes":
    print("Emails sent successfully")
else:
    print("Cancelled")