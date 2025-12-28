# AI Content Refiner - MVP

This project is a Minimum Viable Product (MVP) for the AI Content Refiner. It consists of a **FastAPI** backend (Python) and a **React + Vite** frontend.

## 📂 Project Structure

```text
mvp_code/
├── backend/            # FastAPI Application
│   ├── main.py
│   └── requirements.txt
├── frontend/           # React Application
│   ├── src/
│   ├── public/
│   └── package.json
└── README.md           # This file
```

## 🚀 Prerequisites

Ensure you have the following installed on your machine:
* **Python 3.8+**
* **Node.js 16+** & **npm**

---

## 🛠️ Backend Setup (API)

The backend runs on port `8000`.

### 1. Navigate to the backend directory
Open your terminal and run:
```bash
cd backend
```

### 2. Create a Virtual Environment (Recommended)
Isolate your dependencies by creating a virtual environment.

* **Windows:**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```
* **macOS / Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

### 3. Install Dependencies
Install the required Python packages listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Start the Server
Run the FastAPI server using Uvicorn:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
> **Success:** You should see a message saying `Application startup complete`. The API will be available at `http://localhost:8000`.

---

## 🎨 Frontend Setup (UI)

The frontend runs on port `5173` (by default).

### 1. Navigate to the frontend directory
Open a **new** terminal window (keep the backend running) and run:
```bash
cd frontend
```

### 2. Install Dependencies
Install the required Node.js packages:
```bash
npm install
```

### 3. Start the Development Server
Launch the React application:
```bash
npm run dev
```

### 4. Access the Application
Open your browser and navigate to the URL shown in the terminal (usually):
* `http://localhost:5173`

---

## ⚙️ Configuration & Environment Variables

### Backend Configuration
Currently, the backend does not require a `.env` file for this MVP.
* **CORS:** The backend is configured to accept requests from `http://localhost:5173`. If your frontend runs on a different port, update the `allow_origins` list in `backend/main.py`.

### Frontend Configuration
The frontend communicates with the backend via the hardcoded URL `http://localhost:8000`.
* To change this API URL, update the `fetch` call in `frontend/src/App.jsx`.

---

## 📦 Dependencies Summary

### Backend (`requirements.txt`)
* `fastapi`: Web framework for building APIs.
* `uvicorn`: ASGI server implementation.
* `pydantic`: Data validation using Python type hints.
* `python-multipart`: Required for form data parsing.

### Frontend (`package.json`)
* `react`, `react-dom`: UI library.
* `vite`: Build tool and development server.
* `tailwindcss`, `postcss`, `autoprefixer`: CSS styling framework.
* `lucide-react`: Icon library.
* `react-markdown`: For rendering the AI's markdown response.
