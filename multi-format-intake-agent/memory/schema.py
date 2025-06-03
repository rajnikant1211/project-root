from pydantic import BaseModel
from typing import Optional, Dict, Any

class MemorySchema(BaseModel):
    source: str
    type: str
    timestamp: str
    extracted_fields: Dict[str, Any]
    conversation_id: Optional[str] = None