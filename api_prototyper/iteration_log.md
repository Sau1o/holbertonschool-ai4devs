# Iteration Log

## Iteration 1
- Issue: Missing endpoint to list tasks specific to a project.
- AI Suggestion: Create a nested GET route `/projects/:projectId/tasks` that filters tasks by project ID.
- Fix: Implemented `app.get('/projects/:projectId/tasks', ...)` in `src/index.js` to return filtered tasks.

## Iteration 2
- Issue: Status updates in PATCH requests were strictly case-sensitive, causing errors for inputs like "done".
- AI Suggestion: Normalize the status input to uppercase before validating against the allowed Enum values.
- Fix: Added `.toUpperCase()` logic to the status validation in `PATCH /tasks/:taskId`.
