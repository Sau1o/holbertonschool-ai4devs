# High-Level Architecture Plan

## Overview
The V2W (Voice-to-Workflow) Agent acts as a translation layer between natural language and structured API requests. It is composed of a mobile-first frontend, a middleware API for orchestration, and an AI processing layer.

## Components

### 1. Frontend (Client)
- **Tech Stack:** React Native or PWA (React + Tailwind).
- **Responsibilities:**
  - Capture Audio (MediaRecorder API).
  - User Authentication.
  - CRUD interface for `AutomationHooks`.
  - Display logs/history.

### 2. Backend API (Orchestrator)
- **Tech Stack:** Python (FastAPI) or Node.js (Express).
- **Responsibilities:**
  - Handle Auth/Session.
  - Receive Audio blobs -> Send to STT Service.
  - Receive Text -> Query Database for available Hooks for that user.
  - Construct prompt with User Input + Available Hooks List.
  - Send to LLM.
  - **Dispatcher:** Send the resulting JSON to the User's Target URL (`AutomationHook.target_url`).

### 3. AI Services Layer
- **Speech-to-Text (STT):** OpenAI Whisper API (or local Whisper on server).
  - *Input:* Audio File.
  - *Output:* Transcribed Text.
- **Intelligence (LLM):** GPT-4o-mini or GPT-3.5-turbo (JSON Mode).
  - *Input:* Transcribed Text + List of Hook Descriptions.
  - *Output:* Selected Hook ID + Extracted JSON Payload.

### 4. Data Storage
- **Tech Stack:** PostgreSQL (via Supabase).
- **Responsibilities:** Store Users, Hooks configuration, and execution Logs.

## Data Flow
1. **User** speaks "Add John Doe, email john@example.com to my CRM" into the App.
2. **App** sends audio to **Backend**.
3. **Backend** sends audio to **Whisper API** -> receives text.
4. **Backend** fetches user's hooks (e.g., "CRM Add", "Slack Notify").
5. **Backend** sends Text + Hook Schemas to **LLM**.
6. **LLM** determines intent is "CRM Add" and extracts `{"name": "John Doe", "email": "john@example.com"}`.
7. **Backend** POSTs that JSON to the user's n8n webhook URL.
8. **Backend** saves result to DB and returns success to **App**.
