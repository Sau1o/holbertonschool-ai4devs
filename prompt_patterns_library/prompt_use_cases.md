# Prompt Use Cases

## Code Quality
- **Refactoring Legacy Code**
  - **Goal**: Modernize syntax and improve maintainability of older codebases.
  - **Input**: Legacy function or class snippet.
  - **Output**: Refactored code using modern language features (e.g., Java streams, Python list comprehensions) + brief changelog.

- **Complexity Reduction**
  - **Goal**: Reduce Cyclomatic Complexity in nested logic.
  - **Input**: Deeply nested conditional block.
  - **Output**: Flattened logic structure using guard clauses or strategy patterns.

- **Security Auditing**
  - **Goal**: Identify common vulnerabilities (SQL Injection, XSS) before commit.
  - **Input**: Raw code block handling user input or database queries.
  - **Output**: List of potential vulnerabilities and sanitized code suggestions.

## Debugging
- **Error Log Analysis**
  - **Goal**: Translate cryptic stack traces into actionable fixes.
  - **Input**: Raw stack trace or error log segment.
  - **Output**: Plain English explanation of the error + potential root causes.

- **Logic Isolation**
  - **Goal**: Identify where the code logic diverges from expected behavior without running it.
  - **Input**: Code block + description of "Expected" vs "Actual" behavior.
  - **Output**: Step-by-step execution analysis highlighting the logical divergence.

- **Rubber Ducking**
  - **Goal**: Simulate a pair programmer to talk through a blocking issue.
  - **Input**: Description of the problem and current assumptions.
  - **Output**: Socratic questions to challenge assumptions and guide the user to the solution.

## Documentation
- **Docstring Generation**
  - **Goal**: Standardize function/method documentation (e.g., Javadoc, Docstring).
  - **Input**: Undocumented function signature and body.
  - **Output**: Formatted documentation block adhering to project style guide (params, returns, raises).

- **README Creation**
  - **Goal**: Create a high-level overview for a new module or repository.
  - **Input**: List of file names and core main function code.
  - **Output**: `README.md` content including Installation, Usage, and Features sections.

- **Architecture Explanation**
  - **Goal**: Explain complex design patterns used in a snippet for junior developers.
  - **Input**: Complex class structure or interface definitions.
  - **Output**: Simplified analogy or diagrammatic description of how components interact.

## Testing
- **Unit Test Generation**
  - **Goal**: Create comprehensive test coverage for a specific function.
  - **Input**: Source function code.
  - **Output**: Test suite (e.g., JUnit, PyTest) covering happy paths and common failures.

- **Edge Case Identification**
  - **Goal**: Discover boundary conditions that might break the code.
  - **Input**: Function signature and business logic description.
  - **Output**: List of extreme inputs (nulls, max values, empty strings) to test against.

- **Mock Data Creation**
  - **Goal**: Generate realistic dummy data for testing environments.
  - **Input**: JSON schema or SQL table definition.
  - **Output**: Diverse dataset (JSON array or SQL INSERT statements) respecting constraints.
