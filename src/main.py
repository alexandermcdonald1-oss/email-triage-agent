from dotenv import load_dotenv
from classifier import classify_email

load_dotenv()

email_text = """
Subject: Electricity Bill

Your electricity bill of $234.50 is due on 15 June 2026.
Please pay before the due date to avoid late fees.
"""

result = classify_email(email_text)

print("Category:", result["category"])
print("Subcategory:", result["subcategory"])
print("Action required:", result["action_required"])
print("Priority:", result["priority"])
print("Summary:", result["summary"])
print("Recommended action:", result["recommended_action"])
print("Due date:", result["due_date"])
print("Amount:", result["amount"])