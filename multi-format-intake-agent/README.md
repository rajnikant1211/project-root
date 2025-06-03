# Multi-Format Intake Agent with Intelligent Routing & Context Memory

## Overview
The Multi-Format Intake Agent is an AI-driven system designed to intelligently classify and route incoming data in various formats, including PDF, JSON, and Email. The system maintains context to support downstream processing and audits, ensuring efficient data extraction and management.

## Project Structure
```
multi-format-intake-agent
├── agents
│   ├── classifier_agent.py       # Classifier Agent for format and intent classification
│   ├── json_agent.py             # JSON Agent for processing JSON data
│   └── email_parser_agent.py      # Email Parser Agent for extracting information from emails
├── mcp
│   └── orchestrator.py            # Orchestrator for managing agent interactions
├── memory
│   ├── memory_store.py            # Shared memory module for storing metadata and extracted fields
│   └── schema.py                  # Schema definitions for memory storage
├── utils
│   ├── pdf_utils.py               # Utility functions for handling PDF files
│   ├── email_utils.py             # Utility functions for processing email content
│   └── json_utils.py              # Utility functions for handling JSON data
├── data
│   ├── sample_email.txt           # Sample email body for testing
│   ├── sample_invoice.json        # Sample JSON document representing an invoice
│   └── sample_document.pdf        # Sample PDF document for testing
├── requirements.txt                # Project dependencies
├── README.md                       # Project documentation
└── main.py                        # Entry point for the application
```

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/multi-format-intake-agent.git
   cd multi-format-intake-agent
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Start the application:
   ```
   python main.py
   ```

2. Send data in PDF, JSON, or Email format to the service endpoint. The Classifier Agent will classify the input and route it to the appropriate extraction agent.

## Features
- **Multi-Format Support**: Accepts and processes data in PDF, JSON, and Email formats.
- **Intelligent Routing**: Classifies input and routes it to specialized agents for extraction.
- **Context Memory**: Maintains context for efficient downstream processing and audits.
- **Anomaly Detection**: Identifies missing fields or anomalies in the extracted data.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.