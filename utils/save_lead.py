import csv
import os

def save_lead(company, person, email, status):

    file_exists = os.path.isfile("leads.csv")

    with open("leads.csv", "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Company",
                "Decision Maker",
                "Email",
                "Status"
            ])

        writer.writerow([
            company,
            person,
            email,
            status
        ])