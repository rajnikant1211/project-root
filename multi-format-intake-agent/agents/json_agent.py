class JSONAgent:
    def __init__(self, memory_store):
        self.memory_store = memory_store

    def extract_and_reformat(self, json_input):
        # Implement extraction and reformatting logic here
        formatted_data = {}
        anomalies = []

        # Example extraction logic (to be customized)
        if 'invoice_number' not in json_input:
            anomalies.append('Missing invoice_number')
        else:
            formatted_data['invoice_number'] = json_input['invoice_number']

        # Add more fields as necessary
        # ...

        return formatted_data, anomalies

    def validate_json(self, json_input):
        # Implement JSON validation logic here
        return True  # Placeholder for actual validation logic

    def process(self, json_input):
        if not self.validate_json(json_input):
            return None, ['Invalid JSON format']

        formatted_data, anomalies = self.extract_and_reformat(json_input)
        return formatted_data, anomalies