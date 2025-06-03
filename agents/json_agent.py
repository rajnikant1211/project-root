def process_json(input_json):
    required_fields = ["id", "amount", "customer"]
    missing = [field for field in required_fields if field not in input_json]
    return {"mapped": input_json, "missing_fields": missing}
