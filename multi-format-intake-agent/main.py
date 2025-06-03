from fastapi import FastAPI, UploadFile, Form
from agents.classifier_agent import ClassifierAgent
from mcp.orchestrator import Orchestrator

app = FastAPI()

classifier_agent = ClassifierAgent()
orchestrator = Orchestrator(classifier_agent)

@app.post("/upload/")
async def upload_file(file: UploadFile):
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