# API Requirements – TaskFlow Management API

## Domain Overview
The TaskFlow API facilitates collaborative project management, allowing teams to create projects, track tasks, assign responsibilities, and monitor progress. It serves as the backend backbone for web dashboards and mobile applications, ensuring data consistency across platforms.

## Target Users
- **Frontend Developers:** Building the web application interface (Kanban boards/Lists).
- **Mobile Developers:** Creating iOS/Android apps for on-the-go task updates.
- **Integration Partners:** Third-party services syncing data (e.g., Calendar tools, Slack bots).
- **Admins:** Managing organizational users and access levels.

## Core Operations
1.  **Create Project:** Initialize a new container for tasks.
2.  **List Projects:** Retrieve a paginated list of projects user has access to.
3.  **Create Task:** Add a new item to a specific project with title and description.
4.  **Get Task Details:** specific task metadata by ID.
5.  **Update Task Status:** Transition task workflow (e.g., To Do -> In Progress).
6.  **Assign User:** Associate a user ID with a task.
7.  **Add Comment:** Append a text note to a task's history.
8.  **Filter Tasks:** Search tasks by criteria (priority, assignee, due date).
9.  **Upload Attachment:** Link a file/document to a task.
10. **Delete Task:** Soft-delete (archive) a task from the view.
11. **Register User:** Create a new user account.
12. **Get User Profile:** Retrieve authenticated user details and preferences.

## Data Validation Rules
- **Task Title:** Required; Minimum 3 characters, Maximum 140 characters.
- **Description:** Optional; Maximum 2000 characters.
- **Priority:** Must be an Enum: `LOW`, `MEDIUM`, `HIGH`, `CRITICAL`.
- **Status:** Must be a valid transition based on current state (state machine logic applies).
- **Due Date:** Must be a valid timestamp (ISO 8601) and cannot be set to the past upon creation.
- **Email:** Must strictly follow RFC 5322 regex format.
- **IDs:** Must be valid UUID v4 strings.

## Non-Functional Requirements
- **Latency:** Read operations < 150ms; Write operations < 300ms (p95).
- **Authentication:** OAuth2 standard with JWT (JSON Web Tokens) for stateless auth.
- **Rate Limits:**
    - Public endpoints: 60 requests/minute per IP.
    - Authenticated endpoints: 1000 requests/minute per user.
- **Availability:** 99.9% uptime SLA.
- **Pagination:** Cursor-based pagination required for all list endpoints.
- **Security:** All traffic must use HTTPS (TLS 1.2+).
