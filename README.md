# Vocallabs Outreach Automation Pipeline

## Overview

This project automates lead discovery and outreach using Ocean.io, Prospeo, and Brevo APIs.

The pipeline:

1. Accepts a company name.
2. Searches for company information.
3. Finds decision makers automatically.
4. Enriches contact information to get verified email addresses.
5. Sends outreach emails automatically.
6. Stores successful leads in a CSV file.
7. Logs pipeline activity.

---

## APIs Used

### Ocean.io
Used for company discovery and company intelligence.

### Prospeo
Used for:
- Searching decision makers
- Email enrichment
- Email verification

### Brevo
Used for sending outreach emails.

---

## Project Structure

```text
vocallabs-outreach-pipeline/

├── services/
│   ├── ocean.py
│   ├── prospeo.py
│   ├── prospeo_search.py
│   ├── brevo.py
│   └── eazyreach.py

├── utils/
│   ├── save_lead.py
│   └── logger.py

├── main.py
├── leads.csv
├── pipeline.log
├── .env
├── requirements.txt
└── README.md
```

---

## Workflow

Company Name
↓
Ocean API
↓
Prospeo Search Person
↓
Prospeo Email Enrichment
↓
Brevo Email Delivery
↓
Lead Storage + Logging

---

## Features

- Automated company lookup
- Automated decision maker discovery
- Verified email enrichment
- Outreach email automation
- CSV lead storage
- Activity logging
- Retry mechanism for finding valid contacts

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
OCEAN_API_TOKEN=your_token
PROSPEO_API_KEY=your_key
BREVO_API_KEY=your_key
```

---

## Run

```bash
python3 main.py
```

---

## Sample Output

```text
Enter company name: Google

Searching company...

Trying: Trisha Dean

SUCCESS
Email: trishadean@google.com

Email Sent Successfully
```

---

## Future Improvements

- CRM Integration
- Batch Processing
- Dashboard UI
- Multi-channel Outreach
- Analytics Reporting
