# Team Ideation

## Brainstormed Ideas
1. **AI Code Doc Generator**: Reads a GitHub repository and automatically generates a Wiki/Documentation site using LLMs.
2. **Contextual Meeting Assistant**: Listens to meetings and not only transcribes but creates Jira tickets and Calendar events automatically via API.
3. **Voice-to-Workflow Agent (V2W)** ✅ (Chosen)

## Problem Statement
Professionals using automation tools (like n8n, Zapier) often need to trigger workflows manually while away from the computer. Navigating dashboards on mobile is slow and clumsy. There is a need for a "headless" interface where natural language (voice or text) is instantly converted into structured API calls to trigger complex business automations.

## MVP Features
1. **Audio/Text Input Interface**: Minimalist mobile web UI to record voice or type commands.
2. **AI Intent Parser**: An LLM agent that receives the natural language and maps it to a specific predefined webhook schema (JSON).
3. **Webhook Dispatcher**: Logic to send the cleaned payload to the correct URL.
4. **Feedback Loop**: Visual confirmation that the external tool accepted the request.

## Team Roles
| Member  | Role                  | Responsibilities                                         |
|---------|-----------------------|----------------------------------------------------------|
| Alice   | AI Engineer           | Prompt Engineering, Intent Classification, LLM Integration|
| Bob     | Frontend Dev          | UI/UX, Voice API implementation, Mobile responsiveness    |
| Charlie | Backend/DevOps        | API routing, Server setup, Security/Auth                 |
| Diana   | Product Owner/QA      | Defining use cases, Mocking automation endpoints, Testing |
