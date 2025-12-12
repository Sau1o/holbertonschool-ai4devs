# IDE Automation Configuration

## 1. Environment & Tools (Context)
This automation workflow is designed for the current development environment:
- **IDE:** Visual Studio Code
- **Extensions:** GitHub Copilot, Java Extension Pack, Python, ESLint
- **Tools:** Docker, WSL2, n8n (local)

## 2. Identified Pain Points
These scripts address three specific productivity bottlenecks:
1.  **Documentation Drift:** API documentation frequently lags behind code changes.
2.  **Manual Boilerplate:** Excessive time spent setting up repetitive test classes.
3.  **Slow Debugging Cycle:** Context switching to run manual terminal commands breaks flow.

## 3. Productivity Metrics
We aim to improve the following metrics:
- **Avg task completion:** 90 min (Target: Reduce via automation)
- **Bug fix turnaround:** 2 hours (Target: Improve via auto-tests)
- **Weekly commits:** ~25 commits (Target: Increase throughput)

## 4. Automation Implementations

### A. VS Code Task Configuration (`tasks.json`)
Copy this content to `.vscode/tasks.json` or use directly if the IDE supports markdown parsing.

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "AI: Auto-Generate Docs",
      "type": "shell",
      "command": "python3",
      "args": [
        "${workspaceFolder}/automation/ai_doc_generator.py",
        "--file",
        "${file}",
        "--language",
        "${fileExtname}"
      ],
      "group": "build",
      "detail": "Solves Documentation Drift"
    },
    {
      "label": "AI: Scaffold Tests",
      "type": "shell",
      "command": "bash",
      "args": [
        "${workspaceFolder}/automation/scaffold_tests.sh",
        "${fileBasenameNoExtension}",
        "${fileDirname}"
      ],
      "group": "test",
      "detail": "Solves Manual Boilerplate"
    }
  ]
}
