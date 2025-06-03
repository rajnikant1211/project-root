class MemoryStore:
    def __init__(self):
        self.memory = {}

    def store_input_metadata(self, source, input_type, timestamp):
        self.memory['input_metadata'] = {
            'source': source,
            'type': input_type,
            'timestamp': timestamp
        }

    def store_extracted_fields(self, agent_name, extracted_fields):
        if 'extracted_fields' not in self.memory:
            self.memory['extracted_fields'] = {}
        self.memory['extracted_fields'][agent_name] = extracted_fields

    def store_conversation_id(self, conversation_id):
        self.memory['conversation_id'] = conversation_id

    def get_memory(self):
        return self.memory

    def clear_memory(self):
        self.memory.clear()