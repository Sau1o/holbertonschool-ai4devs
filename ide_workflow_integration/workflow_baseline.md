# Workflow Baseline

## Current IDE Setup
**Primary IDE:** Visual Studio Code

**Key Extensions & Tools:**
- **Code Assistance:** GitHub Copilot, Copilot Chat
- **Formatting/Linting:** Prettier, ESLint, SonarLint
- **Backend Development:** Java Extension Pack (Red Hat), Spring Boot Tools, Pylance (Python)
- **Version Control:** GitLens, GitHub Pull Requests and Issues
- **Infrastructure:** Docker, Kubernetes

**Workflow Environment:**
- **OS:** Windows 11 (WSL2 integration)
- **Terminal:** Zsh via WSL2
- **Automation:** n8n (local instance for workflow automation)

## Pain Points
1. **Manual Boilerplate Generation:** Excessive time spent writing repetitive code for DTOs, Entity mappings, and basic CRUD operations in Java/Spring, slowing down feature delivery.
2. **Test Coverage Gaps:** Writing comprehensive unit tests (JUnit/Mockito) feels disconnected from the development process, often done as an afterthought, leading to brittle code.
3. **Documentation Drift:** Project READMEs and API documentation (Swagger) frequently become outdated compared to the actual codebase, causing confusion during integration.

## Productivity Metrics
| Metric Category | Current Baseline | Note |
| :--- | :--- | :--- |
| **Average Time per Task** | 3.5 hours | For medium complexity backend features |
| **Bug Fix Turnaround** | 4 hours | From report to PR open |
| **Commits per Week** | ~15-20 commits | Variation depends on meeting load |
