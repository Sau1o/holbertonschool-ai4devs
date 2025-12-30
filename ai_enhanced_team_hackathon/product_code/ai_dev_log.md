# AI Development Log

## Prompt 1: Backend Setup
**User:** Create a simple FastAPI (Python) backend for the Voice-to-Workflow Agent. I need one endpoint `POST /api/process` that accepts a JSON body `{"text": "string", "user_id": "string"}`. The endpoint should mock an LLM response that extracts a JSON payload from the text and returns it.

**AI Output:** generated `app.py` with `CommandRequest` Pydantic model and a function that simulates AI extraction logic using basic string matching or a hardcoded response.

**Action:** ✅ Applied. Added `uvicorn` server startup instructions and a basic mock dictionary to simulate the "Intent Parser".

---

## Prompt 2: Frontend Interface
**User:** Create a single file HTML/JS frontend using Tailwind CSS. It should have a text area for input, a "Send Command" button, and a section to display the JSON response from the backend.

**AI Output:** generated `index.html` with a clean UI, a `fetch` function calling `http://localhost:8000/api/process`, and logic to format the JSON response.

**Action:** ✅ Applied. Added error handling to the fetch request to display connection errors to the user.

---

## Prompt 3: Testing Strategy
**User:** Write a basic `pytest` unit test for the `POST /api/process` endpoint to ensure it returns 200 OK and the expected structure.

**AI Output:** generated `test_main.py` using `fastapi.testclient`.

**Action:** ✅ Applied without changes.
