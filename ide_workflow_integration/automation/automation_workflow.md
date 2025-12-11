# IDE Automation Workflow Strategy

## 1. Current IDE Setup & Tools
To provide context for the automations below, here is the current environment:
- **IDE:** Visual Studio Code
- **Extensions:** GitHub Copilot, Java Extension Pack (Spring Boot), Python, ESLint
- **Workflow Tools:** Docker, WSL2, n8n (local)

## 2. Pain Points Analysis
The following 3 pain points are directly addressed by the automation scripts:
- **Pain Point 1: Documentation Drift.** API documentation and code comments frequently fall out of sync, causing integration errors.
- **Pain Point 2: Manual Boilerplate.** Developers spend excessive time writing repetitive DTOs and test scaffolding, slowing down feature delivery.
- **Pain Point 3: Slow Debugging Cycle.** Context switching between the IDE and terminal for routine tasks breaks concentration and flow.

## 3. Productivity Metrics Baseline
- **Average Time per Task:** 3.5 hours (Target: Reduce via automation)
- **Bug Fix Turnaround:** 4 hours (Target: Improve via auto-tests)
- **Weekly Commits:** ~15 commits (Target: Increase throughput)

## 4. Automation Configurations

### A. Task Runner Configuration (`tasks.json`)
This configuration integrates the Python and Shell scripts into the VS Code "Run Task" menu.

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
      "detail": "Solves Pain Point 1 (Documentation Drift)"
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
      "detail": "Solves Pain Point 2 (Manual Boilerplate)"
    }
  ]
}
