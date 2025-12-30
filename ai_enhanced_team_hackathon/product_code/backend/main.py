from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Any
import uvicorn

app = FastAPI(title="V2W Agent API")

# --- Data Models ---
class CommandRequest(BaseModel):
    user_id: str
    text: str

class CommandResponse(BaseModel):
    status: str
    detected_intent: str
    extracted_payload: Dict[str, Any]
    message: str

# --- Mock AI Logic (Simulating LLM) ---
def mock_llm_processor(text: str):
    text_lower = text.lower()
    
    # Logic simulating intent classification
    if "lead" in text_lower or "crm" in text_lower:
        return {
            "intent": "create_crm_lead",
            "payload": {"name": "Detected Name", "source": "voice_command"}
        }
    elif "remind" in text_lower:
        return {
            "intent": "set_reminder",
            "payload": {"task": text, "time": "10:00 AM"}
        }
    else:
        return {
            "intent": "unknown",
            "payload": {}
        }

# --- Endpoints ---
@app.post("/api/process", response_model=CommandResponse)
async def process_command(request: CommandRequest):
    if not request.text:
        raise HTTPException(status_code=400, detail="Text input is empty")
    
    print(f"Processing command for user {request.user_id}: {request.text}")
    
    # Simulate AI Processing
    ai_result = mock_llm_processor(request.text)
    
    return CommandResponse(
        status="success",
        detected_intent=ai_result["intent"],
        extracted_payload=ai_result["payload"],
        message="Command processed successfully"
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
