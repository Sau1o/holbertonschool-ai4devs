# Prompt Testing Examples

## Example 1: Refactoring
**Template Source**: `/prompts/refactoring.md`  

**Prompt Used (Filled)**:  
**Role**: Senior Software Engineer  
**Task**: Refactor the provided code to improve readability and performance.  
**Input Data**:  
\`\`\`python
def f(x): return x*2 if x > 0 else 0
\`\`\`  
**Constraints**: Keep the same business logic, but update syntax to modern standards.  
**Expected Output**: The optimized code block followed by a list of changes.  

**AI Output Received**:  
\`\`\`python
def calculate_double_positive(value: int) -> int:
    """Returns double the value if positive, else zero."""
    if value > 0:
        return value * 2
    return 0
\`\`\`
**Changes**: Renamed function for clarity; added type hinting; added docstring.  

**Feedback**:  
- **Structure**: Pass.  
- **Accuracy**: The logic was preserved correctly.  
- **Constraint Check**: Variable renaming improved readability as requested.  

---

## Example 2: Security Auditing
**Template Source**: `/prompts/security_auditing.md`  

**Prompt Used (Filled)**:  
**Role**: Application Security Specialist  
**Task**: Analyze the code below for security vulnerabilities.  
**Input Data**:  
\`\`\`javascript
const query = "SELECT * FROM users WHERE name = '" + req.body.name + "'";
db.execute(query);
\`\`\`  
**Constraints**: Focus on OWASP Top 10 vulnerabilities.  
**Expected Output**: A list of vulnerabilities found (Severity: Issue) and a patched code version.  

**AI Output Received**:  
**Vulnerability Found**:  
- **Critical**: SQL Injection. Concatenating user input directly into queries.  
**Patched Code**:  
\`\`\`javascript
const query = "SELECT * FROM users WHERE name = ?";
db.execute(query, [req.body.name]);
\`\`\`  

**Feedback**:  
- **Structure**: Pass.  
- **Accuracy**: Correctly identified SQL Injection.  
- **Constraint Check**: Provided the parameterized query fix as expected.  

---

## Example 3: Docstring Generation
**Template Source**: `/prompts/docstring_generation.md`  

**Prompt Used (Filled)**:  
**Role**: Technical Writer  
**Task**: specific documentation for the function.  
**Input Data**:  
\`\`\`java
public int add(int a, int b) { return a + b; }
\`\`\`  
**Constraints**: Follow the Javadoc format.  
**Expected Output**: The code block with correct comments/docstrings inserted.  

**AI Output Received**:  
\`\`\`java
/**
 * Adds two integers.
 * * @param a The first integer.
 * @param b The second integer.
 * @return The sum of a and b.
 */
public int add(int a, int b) { return a + b; }
\`\`\`  

**Feedback**:  
- **Structure**: Pass.  
- **Accuracy**: Javadoc tags (@param, @return) are correct.  
- **Constraint Check**: Style guide was respected.  

---

## Example 4: Unit Test Generation
**Template Source**: `/prompts/unit_test_generation.md`  

**Prompt Used (Filled)**:  
**Role**: QA Automation Engineer  
**Task**: Write unit tests for the provided logic.  
**Input Data**:  
\`\`\`python
def is_even(n): return n % 2 == 0
\`\`\`  
**Constraints**: Use the PyTest framework. Cover happy paths and edge cases.  
**Expected Output**: Complete, runnable test file code.  

**AI Output Received**:  
\`\`\`python
import pytest
from main import is_even

def test_is_even_positive():
    assert is_even(4) == True

def test_is_odd_positive():
    assert is_even(5) == False

def test_zero():
    assert is_even(0) == True
\`\`\`  

**Feedback**:  
- **Structure**: Pass.  
- **Accuracy**: Tests cover the basic logic logic accurately.  
- **Constraint Check**: PyTest syntax was used correctly.  

---

## Example 5: Error Analysis
**Template Source**: `/prompts/error_analysis.md`  

**Prompt Used (Filled)**:  
**Role**: DevOps Engineer  
**Task**: Analyze the stack trace to find the root cause.  
**Input Data**:  
\`TypeError: Cannot read properties of undefined (reading 'map') at renderList\`  
**Constraints**: Explain in simple terms suitable for a junior developer.  
**Expected Output**: Summary of the error, the specific file/line responsible, and the fix.  

**AI Output Received**:  
**Summary**: You are trying to loop through a list that doesn't exist yet.  
**Location**: `renderList` function.  
**Fix**: Add a check before the map: `if (list && list.length) { list.map(...) }`.  

**Feedback**:  
- **Structure**: Pass.  
- **Accuracy**: Correct interpretation of the JS error.  
- **Constraint Check**: The explanation was simplified for a junior level as requested.
