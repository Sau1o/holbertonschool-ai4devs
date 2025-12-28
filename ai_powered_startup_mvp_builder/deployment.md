# Deployment Details

## 🔗 Links
| Component | URL | Status |
|-----------|-----|--------|
| **Live Demo** | `https://ai-content-refiner-Sau1o.vercel.app` | 🟢 Online (Placeholder) |
| **GitHub Repo** | `https://github.com/Sau1o/ai-content-refiner` | 🟢 Public |
| **Backend API** | `https://ai-content-refiner-api.onrender.com` | 🟢 Online (Placeholder) |

## 🏗️ Infrastructure
* **Frontend:** Deployed on **Vercel** (React + Vite).
* **Backend:** Deployed on **Render** (FastAPI + Python).
* **CI/CD:** Automatic deploys from GitHub `main` branch.

## ⚙️ Configuration
* **Frontend Environment:**
    * `VITE_API_URL`: Points to the Render Backend URL.
* **Backend Environment:**
    * `CORS_ORIGINS`: configured to allow requests from the Vercel Frontend.
