from fastapi import FastAPI, UploadFile, File
from agents.classifier_agent import classify_input
from agents.email_agent import parse_email
from agents.json_agent import process_json
from memory.memory_store import save_memory
import json

app = FastAPI()

@app.post("/intake")
async def intake(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode(errors="ignore")

    classification = classify_input(text)
    format_ = classification['format']
    intent = classification['intent']

    if format_ == "email":
        parsed = parse_email(text)
    elif format_ == "json":
        parsed = process_json(json.loads(text))
    else:
        parsed = {"note": "PDF processing not yet implemented."}

    save_memory(file.filename, {
        "format": format_,
        "intent": intent,
        **parsed
    })
    return {"status": "processed", "output": parsed}