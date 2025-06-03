### Project: Multi-Format Intake Agent with Intelligent Routing & Context Memory

# Directory structure (virtual)
# /agents/classifier_agent.py
# /agents/json_agent.py
# /agents/email_agent.py
# /memory/memory_store.py
# /mcp/main.py
# /utils/helpers.py
# /requirements.txt
# /README.md

# --- README.md ---

# Multi-Format Intake Agent with Intelligent Routing & Context Memory

## 🧠 Objective
Build a multi-agent AI system that:
- Accepts data in **PDF**, **JSON**, or **Email (text)** format
- Classifies the **input format** and **intent**
- Routes to specialized agents for structured extraction
- Maintains shared context memory for audit and chaining

---

## 🏗️ Architecture Overview

```
[Input File] ──▶ [Classifier Agent] ──▶ [Specialized Agent]
                     │                       │
                     └──────▶ [Shared Memory Module] ◀─────┘
```

### Agents
- **Classifier Agent**: Determines format & intent → routes data
- **JSON Agent**: Maps JSON to schema, detects anomalies
- **Email Parser Agent**: Extracts sender, urgency, CRM-style metadata

### Shared Memory
- Powered by Redis
- Stores:
  - Source, format, timestamp
  - Extracted metadata
  - Conversation/thread ID

---

## 🚀 Tech Stack
- Python
- FastAPI
- Redis
- Uvicorn
- Optional: Langchain, OpenAI/Gemini LLM, Docker

---

## 🧪 Sample Inputs
Place test files inside `/data/`:
- `sample_email.txt`
- `sample_payload.json`
- `sample_invoice.pdf`

---

## 🔧 How to Run

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Start Redis (if not already running)
```bash
redis-server
```

### 3. Run the FastAPI App
```bash
uvicorn mcp.main:app --reload
```

### 4. Test the API
Use Postman or curl:
```bash
curl -X POST "http://127.0.0.1:8000/intake" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@data/sample_email.txt"
```

---

## 🗂 Folder Structure
```
project-root/
├── agents/
│   ├── classifier_agent.py
│   ├── email_agent.py
│   └── json_agent.py
├── memory/
│   └── memory_store.py
├── mcp/
│   └── main.py
├── utils/
│   └── helpers.py
├── data/
│   ├── sample_email.txt
│   ├── sample_payload.json
│   └── sample_invoice.pdf
├── requirements.txt
└── README.md
```

---

## 📹 Submission Requirements
- ✅ Working code
- ✅ ReadMe and sample files
- ✅ Demo video showing intake, classification, and memory

---

## 📌 Future Enhancements
- PDF Agent with `PyMuPDF`
- Add Docker support
- Integrate OpenAI or Gemini for smarter extraction
- Implement webhook callback / CRM logging

---

Crafted with 🧠 Rajnikant Sharma
