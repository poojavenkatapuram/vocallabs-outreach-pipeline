from services.ocean import search_companies
from services.prospeo_search import search_person
from services.prospeo import find_person
from services.brevo import send_email

from utils.save_lead import save_lead
from utils.logger import logger

print("=" * 60)
print("VOCALLABS OUTREACH AUTOMATION PIPELINE")
print("=" * 60)

company_name = input("\nEnter company name: ")

print("\n[STEP 1] Searching company using Ocean API...")

try:
    company_result = search_companies(company_name)

    print("\nOcean Result:")
    print(company_result)

except Exception as e:
    print("\nOcean Error:")
    print(e)

print("\n[STEP 2] Finding decision makers using Prospeo Search...")

search_result = search_person(company_name)

print("\nSearch Result:")
print(search_result)

if not search_result.get("results"):
    print("\nNo decision makers found.")
    exit()

email = None
first_name = None
full_name = None

for result in search_result["results"]:

    try:
        full_name = result["person"]["full_name"]

        print(f"\nTrying: {full_name}")

        person_result = find_person(
            full_name,
            company_name
        )

        if (
            person_result
            and not person_result.get("error")
            and "person" in person_result
        ):

            email = person_result["person"]["email"]["email"]
            first_name = person_result["person"]["first_name"]

            print(f"\nSUCCESS: {full_name}")
            print(f"Email: {email}")

            logger.info(f"Company: {company_name}")
            logger.info(f"Decision Maker: {full_name}")
            logger.info(f"Email: {email}")

            break

    except Exception as e:
        print("Skipped:", e)

if not email:
    print("\nNo verified email found.")
    exit()

confirm = input(
    "\nSend outreach email? (yes/no): "
)

if confirm.lower() != "yes":
    print("\nEmail sending cancelled.")
    exit()

print("\n[STEP 3] Sending Email using Brevo...")

email_result = send_email(
    email,
    first_name
)

print("\nBrevo Result:")
print(email_result)

save_lead(
    company_name,
    full_name,
    email,
    "Email Sent"
)

logger.info(f"Email Sent Successfully to {email}")

print("\nLead saved to leads.csv")
print("Activity logged to pipeline.log")

print("\nPipeline Completed Successfully!")