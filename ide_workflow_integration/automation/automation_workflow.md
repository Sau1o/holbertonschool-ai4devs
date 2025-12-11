# IDE Automation Workflow

## 1. Current IDE & Tools (Context)
To establish the productivity baseline for these automations, the current environment is defined as:
- **IDE:** Visual Studio Code
- **Extensions:** GitHub Copilot, Java Extension Pack, Python, ESLint.
- **Tools:** Docker, n8n (local), WSL2.

## 2. Pain Points Identified
The following bottlenecks are addressed by the automations below:
1.  **Manual Boilerplate:** Excessive time spent on repetitive Java/Spring DTOs and test classes.
2.  **Documentation Drift:** API docs and code comments are frequently out of sync.
3.  **Slow Debugging Cycle:** Context switching required to run manual scripts.

## 3. Productivity Metrics
- **Avg task completion:** 3.5 hours (Target: Reduce via boilerplating)
- **Bug fix turnaround:** 4 hours (Target: Reduce via auto-tests)
- **Weekly commits:** ~15 commits (Target: Increase throughput)

## 4. Automation Configurations

### VS Code Tasks Configuration
File: `automation/tasks.json`
This configuration integrates the scripts directly into the IDE workflow.

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Auto-Doc: Generate Javadoc",
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
      "presentation": { "reveal": "silent" },
      "detail": "Addresses Documentation Drift"
    },
    {
      "label": "Test-Scaffold: Create Unit Test",
      "type": "shell",
      "command": "bash",
      "args": [
        "${workspaceFolder}/automation/scaffold_tests.sh",
        "${fileBasenameNoExtension}",
        "${fileDirname}"
      ],
      "group": "test",
      "presentation": { "reveal": "always" },
      "detail": "Addresses Manual Boilerplate"
    }
  ]
}
