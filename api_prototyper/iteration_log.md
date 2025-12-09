# API Iteration Log – TaskFlow API

This document tracks the iterative improvements made to the TaskFlow API prototype based on testing and specification alignment.

## Iteration 1
- **Issue:** Missing Endpoint Implementation (Spec Mismatch).
  - *Description:* The OpenAPI specification (v1.5.0) defined an endpoint `GET /projects/{id}/tasks` to list tasks within a specific project. However, the initial prototype in `src/index.js` only implemented the global `GET /tasks/:taskId` and `POST` creation, missing the project-specific list view.
- **AI Suggestion:** Implement a new GET route `/projects/:projectId/tasks`. This route should validate if the project exists first, then filter the global `tasks` array to return only items matching the requested `projectId`.
- **Fix:** Added the following endpoint to `src/index.js`:
  ```javascript
  app.get('/projects/:projectId/tasks', (req, res) => {
      const project = projects.find(p => p.id === req.params.projectId);
      if (!project) return res.status(404).json({ code: 404, message: "Project not found" });
      
      const projectTasks = tasks.filter(t => t.projectId === req.params.projectId);
      res.json(projectTasks);
  });
