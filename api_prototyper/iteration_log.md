# API Iteration Log – TaskFlow API

This document records the iterative improvements made to the source code to address bugs, missing features, and stability issues.

## Iteration 1
- **Problem identified:**
  The API lacked a specific endpoint to list tasks belonging to a single project. The only way to see tasks was to access them individually by ID, which made the frontend integration impossible for the "Project Board" view.
- **AI Suggestion:**
  Implement a new nested GET route `/projects/:projectId/tasks`. This route should first validate if the project exists and then filter the global tasks array to return only those matching the `projectId`.
- **Final fix:**
  Added the following endpoint to `src/index.js`:
  ```javascript
  // Added in Iteration 1
  app.get('/projects/:projectId/tasks', (req, res) => {
      const project = projects.find(p => p.id === req.params.projectId);
      if (!project) {
          return res.status(404).json({ code: 404, message: "Project not found" });
      }
      const projectTasks = tasks.filter(t => t.projectId === req.params.projectId);
      res.json(projectTasks);
  });
