# AI-Powered Workflow Configuration

## Overview
This configuration aligns the AI assistant (GitHub Copilot) with our project standards, specifically addressing the pain points of **Test Coverage** and **Documentation Drift** identified in the baseline.

## Global Settings
- **Chat Context:** Enabled for current file + open tabs.
- **Inline Suggestions:** Enabled.
- **Privacy:** Public code matching blocked.

## Language-Specific Strategy

### Java (Backend/Spring)
- **Style:** Google Java Style Guide.
- **Testing:** Enforce JUnit 5 + Mockito patterns for all service layer logic.
- **Boilerplate:** AI instructions to prioritize Lombok annotations over manual getters/setters.

### Python (Scripts/Automation)
- **Style:** PEP 8 compliance.
- **Type Hinting:** Strict type hints required for function signatures.

## Specialized AI Workflows

### 1. Automated Documentation Generator ( addressing "Documentation Drift")
- **Trigger:** When completing a class or method signature.
- **Rule:** Generate Javadoc (Java) or Docstrings (Python) automatically.
- **Requirement:** Must include `@param`, `@return`, and `@throws` descriptions.

### 2. Unit Test Scaffolding (addressing "Test Coverage Gaps")
- **Trigger:** Selecting a method and using the `/tests` command.
- **Template:** "Given [Pre-condition], When [Action], Then [Expected Result]".
