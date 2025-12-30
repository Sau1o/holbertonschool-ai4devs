# Deployment Documentation

## 1. Project Links
- **GitHub Repository:** `https://github.com/hackathon-team/v2w-agent-mvp`
- **Live Frontend (Vercel):** `https://v2w-agent-demo.vercel.app`
- **Live Backend API (Render):** `https://v2w-api.onrender.com/docs`

---

## 2. Backend Deployment (Render.com)
We chose Render for the Python/FastAPI backend due to native support for Python web services and easy HTTPS setup.

### Preparation
1. Created `requirements.txt` in root:
   ```text
   fastapi
   uvicorn
   pydantic
   ```
2. Committed code to GitHub.

### Steps
1. Logged into Render and clicked **"New Web Service"**.
2. Connected the GitHub repository.
3. **Settings Configured:**
   - **Root Directory:** `.` (Root of repo)
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn product_code.backend.main:app --host 0.0.0.0 --port $PORT`
   - **Environment Variables:**
     - `PYTHON_VERSION`: `3.9.0`
4. Clicked **"Deploy Web Service"**.
5. Verified status: **Live**.

---

## 3. Frontend Deployment (Vercel)
We chose Vercel for the static frontend because of its zero-config setup for HTML/JS projects and global CDN.

### Preparation
1. Updated `index.html` `fetch` URL to point to the production backend:
   ```javascript
   // Changed http://localhost:8000 to [https://v2w-api.onrender.com](https://v2w-api.onrender.com)
   const API_URL = '[https://v2w-api.onrender.com/api/process](https://v2w-api.onrender.com/api/process)'; 
   ```

### Steps
1. Logged into Vercel and clicked **"Add New Project"**.
2. Imported the same GitHub repository.
3. **Settings Configured:**
   - **Framework Preset:** Other (Static)
   - **Root Directory:** `product_code/frontend` (This ensures Vercel serves `index.html` from the correct subfolder).
4. Clicked **"Deploy"**.
5. Verified status: **Ready**.

---

## 4. Post-Deployment Verification
- Opened `https://v2w-agent-demo.vercel.app`.
- Typed "Create a lead for Saulo".
- Clicked "Process Command".
- Verified that the JSON response returned from the Render API (`https://v2w-api.onrender.com`) was displayed correctly on the screen.
