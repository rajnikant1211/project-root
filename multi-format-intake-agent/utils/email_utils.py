def parse_email_body(email_body):
    # Function to parse the email body and extract relevant information
    # This is a placeholder for actual parsing logic
    parsed_data = {
        "sender": "example@example.com",
        "intent": "Request for Quotation",
        "urgency": "High"
    }
    return parsed_data

def format_crm_record(parsed_data):
    # Function to format the parsed email data into a CRM-style record
    crm_record = {
        "contact": parsed_data["sender"],
        "request": parsed_data["intent"],
        "priority": parsed_data["urgency"]
    }
    return crm_record

def extract_sender(email_body):
    # Function to extract the sender's email address from the email body
    # This is a placeholder for actual extraction logic
    return "example@example.com"