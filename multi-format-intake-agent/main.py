from fastapi import FastAPI, UploadFile, Form
try:
    from agents.classifier_agent import ClassifierAgent
    from agents.json_agent import JSONAgent
    from agents.email_parser_agent import EmailParserAgent
    from mcp.orchestrator import Orchestrator
except ImportError as e:
    raise ImportError("Required modules not found. Please ensure 'agents.classifier_agent', 'agents.json_agent', 'agents.email_parser_agent', and 'mcp.orchestrator' exist and are accessible.") from e

from fastapi.middleware.cors import CORSMiddleware
from memory.memory_store import MemoryStore

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize memory store and agents
memory_store = MemoryStore()
classifier_agent = ClassifierAgent(memory_store)
json_agent = JSONAgent(memory_store)
email_parser_agent = EmailParserAgent(memory_store)
orchestrator = Orchestrator(classifier_agent, json_agent, email_parser_agent, memory_store)

from fastapi import File

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    response = orchestrator.process_input(content, file.filename)
    return response

@app.post("/submit_email/")
async def submit_email(email_body: str = Form(...)):
    response = orchestrator.process_input(email_body, "email")
    return response

@app.get("/")
def read_root():
    return {"message": "Welcome to the Multi-Format Intake Agent API"}