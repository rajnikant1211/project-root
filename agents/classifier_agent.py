def classify_input(input_text):
    """
    Dummy classifier - Replace with LLM call in production.
    """
    if input_text.strip().startswith("{"):
        return {"format": "json", "intent": "Invoice"}
    elif "From:" in input_text:
        return {"format": "email", "intent": "RFQ"}
    else:
        return {"format": "pdf", "intent": "Complaint"}