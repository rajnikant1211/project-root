class Orchestrator:
    def __init__(self, classifier_agent, json_agent, email_parser_agent, memory_store):
        self.classifier_agent = classifier_agent
        self.json_agent = json_agent
        self.email_parser_agent = email_parser_agent
        self.memory_store = memory_store

    def process_input(self, raw_input):
        # Classify the input format and intent
        classification_result = self.classifier_agent.classify(raw_input)
        input_format = classification_result['format']
        intent = classification_result['intent']

        # Store metadata in memory
        self.memory_store.store_metadata(raw_input, input_format, intent)

        # Route to the appropriate agent based on classification
        if input_format == 'email':
            return self.email_parser_agent.parse(raw_input)
        elif input_format == 'json':
            return self.json_agent.extract(raw_input)
        elif input_format == 'pdf':
            # Handle PDF processing if needed
            pass
        else:
            raise ValueError("Unsupported input format")

    def get_memory(self):
        return self.memory_store.get_all_data()