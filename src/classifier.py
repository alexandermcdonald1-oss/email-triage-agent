from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()


def classify_email(email_text):
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
    )

    prompt = f"""
You are an email triage assistant.

Classify the email using the category definitions below and determine whether action is required.

Categories:

Property
- Conveyancing
- Real estate
- Property managers
- Rates
- Council notices
- Legal matters relating to property
- Mortgages

Finance
- Bills
- Invoices
- Receipts
- Banking
- Investments
- Tax
- Insurance
- Utilities

School
- Pacific Lutheran College
- School communications
- Sporting activities
- Parent notifications
- School fees

ApprovedMods
- Vehicle modifications
- GVM upgrades
- Engineering certifications
- Vehicle inspections
- Customers or suppliers of ApprovedMods

Security
- Login alerts
- MFA notifications
- Password resets
- Security warnings
- Fraud alerts

Personal
- Family
- Friends
- Social events
- Travel
- Medical

Newsletter
- Subscribed newsletters
- Information updates
- Industry news

Marketing
- Promotions
- Sales
- Discounts
- Advertising

Other
- Anything else

Return ONLY valid JSON in this format:

{{
  "category": "Property | Finance | School | ApprovedMods | Security | Personal | Newsletter | Marketing | Other",
  "subcategory": "Short specific subcategory",
  "gmail_label": "Property | Finance | School | ApprovedMods | Security | Personal | Newsletter | Marketing | Other",
  "confidence": "High | Medium | Low",
  "action_required": true,
  "action_type": "Pay | Read | Respond | Schedule | Review | None",
  "priority": "High | Medium | Low",
  "summary": "One sentence summary",
  "recommended_action": "What Alex should do next, or null",
  "due_date": "YYYY-MM-DD or null",
  "amount": "Dollar amount or null",
  "sender_type": "Business | School | Government | Bank | Retailer | Individual | Other"
}}

Rules:
- Choose exactly one category.
- If no action is needed, set action_required to false.
- If no action is needed, set action_type to "None".
- If no due date exists, set due_date to null.
- If no amount exists, set amount to null.
- If no recommended action exists, set recommended_action to null.
- Return JSON only. Do not include markdown.

Email:

{email_text}
"""

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    result = response.output_text.strip()

    try:
        return json.loads(result)
    except json.JSONDecodeError:
        print("Model returned invalid JSON:")
        print(result)
        raise