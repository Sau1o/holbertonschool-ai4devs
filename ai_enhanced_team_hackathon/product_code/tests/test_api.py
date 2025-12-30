from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_process_command_success():
    payload = {
        "user_id": "test_user",
        "text": "Create a new CRM lead for Alice"
    }
    response = client.post("/api/process", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["detected_intent"] == "create_crm_lead"
    assert "name" in data["extracted_payload"]

def test_process_command_empty():
    payload = {
        "user_id": "test_user",
        "text": ""
    }
    response = client.post("/api/process", json=payload)
    # The API is designed to treat empty string as empty, 
    # but strictly Pydantic accepts empty strings unless validated.
    # In our main.py logic, we raise 400 manually.
    assert response.status_code == 400
