from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import time
import random

app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Default Vite port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RefineRequest(BaseModel):
    url: str
    tone: str

@app.get("/")
def read_root():
    return {"status": "AI Content Refiner API is running"}

@app.post("/refine")
async def refine_content(request: RefineRequest):
    # Simulate processing delay (scraping + AI generation)
    time.sleep(3) 
    
    # Mock Response Logic
    # In a real app, you would scrape the URL and send text to an LLM here.
    
    mock_responses = {
        "Professional Mentor": (
            "## Executive Summary\n\n"
            "Based on the documentation provided, I have refined the core concepts for clarity. "
            "Focusing on scalability and maintainability, the proposed architecture aligns well with industry standards. "
            "I recommend reviewing the API endpoints specifically for edge cases.\n\n"
            "* **Strength:** Modular design.\n"
            "* **Action Item:** optimize database queries."
        ),
        "Casual Developer": (
            "Yo! Checked out the docs you sent. 🚀\n\n"
            "The setup looks pretty chill. I dig the component structure, it's super clean. "
            "Just a heads up, the auth flow might be a bit tricky for new contributors, so maybe add some comments there? "
            "Otherwise, looks like a solid stack to build on!"
        ),
        "Enthusiastic": (
            "This is absolutely amazing! 🌟\n\n"
            "I just read through the documentation and the potential here is incredible! "
            "The way you've handled the data flow is brilliant. I can't wait to see this go live. "
            "Great job on the clear examples, they make adoption so much easier!"
        )
    }

    response_text = mock_responses.get(request.tone, "Content refined successfully.")
    
    return {
        "original_url": request.url,
        "selected_tone": request.tone,
        "refined_content": response_text
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
