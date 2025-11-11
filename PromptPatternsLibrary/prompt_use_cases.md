# Prompt Use Cases

## Code Quality

* **Refactoring**

  * **Goal**: Simplify and optimize existing code for better readability and performance.
  * **Input**: Function or class in any programming language.
  * **Output**: Cleaner, modular version with clear explanations of improvements.

* **Style Enforcement**

  * **Goal**: Maintain consistent code formatting and naming conventions.
  * **Input**: Code snippet or module.
  * **Output**: Reformatted code following defined style guides (e.g., PEP8, ESLint).

* **Code Review Automation**

  * **Goal**: Automatically detect code smells and suggest improvements.
  * **Input**: Repository or function-level code.
  * **Output**: List of potential issues with recommendations for fixes.

## Debugging

* **Error Diagnosis**

  * **Goal**: Identify causes of runtime or syntax errors.
  * **Input**: Code block with error message or stack trace.
  * **Output**: Explanation of error, cause, and corrected code.

* **Performance Profiling**

  * **Goal**: Detect and resolve performance bottlenecks.
  * **Input**: Code exhibiting slow execution.
  * **Output**: Optimization suggestions and sample revised code.

## Documentation

* **Auto-Doc Generation**

  * **Goal**: Automatically produce docstrings or markdown documentation.
  * **Input**: Function, class, or module code.
  * **Output**: Structured documentation in the chosen format (e.g., reStructuredText, JSDoc).

* **Code Explanation**

  * **Goal**: Simplify complex logic for knowledge transfer or onboarding.
  * **Input**: Block of source code.
  * **Output**: Human-readable explanation of how the code works.

## Testing

* **Unit Test Generation**

  * **Goal**: Create test cases to validate function behavior.
  * **Input**: Source code of a function or method.
  * **Output**: Unit test suite (e.g., pytest, JUnit) with example inputs/outputs.

* **Edge Case Discovery**

  * **Goal**: Identify missing or untested input conditions.
  * **Input**: Function or existing test suite.
  * **Output**: List of uncovered edge cases and test suggestions.

## Collaboration & Review

* **Code Review Summaries**

  * **Goal**: Summarize pull requests or code diffs for team review.
  * **Input**: Git diff or PR description.
  * **Output**: Structured review summary highlighting major changes and risks.

* **Commit Message Improvement**

  * **Goal**: Rewrite commit messages to follow best practices (e.g., Conventional Commits).
  * **Input**: Raw or unclear commit message.
  * **Output**: Concise, standardized commit message with clear intent.

## Code Generation

* **Boilerplate Creation**

  * **Goal**: Quickly scaffold code for new modules, APIs, or components.
  * **Input**: High-level requirements or API schema.
  * **Output**: Pre-built code structure following best practices.

* **Snippet Suggestion**

  * **Goal**: Provide short reusable code snippets for common tasks.
  * **Input**: Description of task or algorithm.
  * **Output**: Optimized code snippet in chosen programming language.

## DevOps & Automation

* **Script Generation**

  * **Goal**: Create automation scripts for deployment or configuration.
  * **Input**: Description of desired automation task.
  * **Output**: Bash, PowerShell, or Python script ready to execute.

* **CI/CD Pipeline Templates**

  * **Goal**: Generate configuration files for automated testing and deployment.
  * **Input**: Project stack and environment details.
  * **Output**: YAML or JSON configuration for tools like GitHub Actions, Jenkins, or GitLab CI.
