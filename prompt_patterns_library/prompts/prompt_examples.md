# Prompt Testing Examples

## Example 1 – Refactoring Legacy Code
**Template Used**: /prompts/refactoring_legacy_code.md  
**Prompt**:  
**Role**: Senior Software Engineer  
**Task**: Refactor the provided legacy Java code to use modern language features and improve maintainability.  
**Input Placeholder**:  
\`\`\`java
public List<String> filterNames(List<String> names) {
    List<String> result = new ArrayList<>();
    for (String name : names) {
        if (name.startsWith("A")) {
            result.add(name.toUpperCase());
        }
    }
    return result;
}
\`\`\`

**AI Output**:  
\`\`\`java
public List<String> filterNames(List<String> names) {
    return names.stream()
            .filter(name -> name.startsWith("A"))
            .map(String::toUpperCase)
            .collect(Collectors.toList());
}
\`\`\`
**Changes Made**:  
- Replaced imperative \`for\` loop with declarative \`Stream API\`.  
- Used method reference \`String::toUpperCase\` for cleaner syntax.  
- Removed temporary \`result\` list creation.  

**Feedback**: The output correctly utilized Java 8+ features to reduce boilerplate. The logic remains identical but is much more readable.  

---

## Example 2 – Security Auditing
**Template Used**: /prompts/security_auditing.md  
**Prompt**:  
**Role**: Application Security Specialist  
**Task**: Audit the following Python code for common security vulnerabilities (SQL Injection, XSS, etc.) and suggest fixes.  
**Input Placeholder**:  
\`\`\`python
user_id = request.args.get('id')
query = f"SELECT * FROM users WHERE id = {user_id}"
cursor.execute(query)
\`\`\`

**AI Output**:  
**Vulnerability Report**:  
- **[Critical]: SQL Injection** Directly inserting \`user_id\` into the query string allows attackers to manipulate the database execution (e.g., \`id=1 OR 1=1\`).  

**Remediation**:  
\`\`\`python
user_id = request.args.get('id')
# Use parameterized queries to treat input as data, not executable code
query = "SELECT * FROM users WHERE id = %s"
cursor.execute(query, (user_id,))
\`\`\`

**Feedback**: The model correctly identified the SQL injection risk inherent in f-strings for queries and provided the standard parameterized solution.  

---

## Example 3 – Docstring Generation
**Template Used**: /prompts/docstring_generation.md  
**Prompt**:  
**Role**: Technical Writer  
**Task**: Generate comprehensive documentation for the provided function adhering to Google Style standards.  
**Input Placeholder**:  
\`\`\`python
def calculate_compound_interest(principal, rate, time, n):
    return principal * (1 + rate/n) ** (n*time)
\`\`\`

**AI Output**:  
\`\`\`python
def calculate_compound_interest(principal, rate, time, n):
    """Calculates the compound interest.

    Args:
        principal (float): The initial amount of money.
        rate (float): The annual interest rate (in decimal form).
        time (int): The number of years the money is invested or borrowed for.
        n (int): The number of times that interest is compounded per year.

    Returns:
        float: The amount of money accumulated after n years, including interest.
    """
    return principal * (1 + rate/n) ** (n*time)
\`\`\`

**Feedback**: Excellent adherence to Google Style. It correctly inferred the types (float/int) based on typical financial context.  

---

## Example 4 – Unit Test Generation
**Template Used**: /prompts/unit_test_generation.md  
**Prompt**:  
**Role**: QA Automation Engineer  
**Task**: Write a complete unit test suite for the given function using Jest (JavaScript).  
**Input Placeholder**:  
\`\`\`javascript
function divide(a, b) {
    if (b === 0) throw new Error("Cannot divide by zero");
    return a / b;
}
\`\`\`

**AI Output**:  
\`\`\`javascript
describe('divide function', () => {
    // Happy Path
    test('should correctly divide two positive numbers', () => {
        expect(divide(10, 2)).toBe(5);
    });

    test('should handle negative numbers', () => {
        expect(divide(-10, 2)).toBe(-5);
    });

    // Boundary/Edge Case
    test('should throw error when dividing by zero', () => {
        expect(() => divide(5, 0)).toThrow("Cannot divide by zero");
    });
});
\`\`\`

**Feedback**: The model covered standard cases and correctly used \`.toThrow\` for the exception.  

---

## Example 5 – Architecture Explanation
**Template Used**: /prompts/architecture_explanation.md  
**Prompt**:  
**Role**: Senior Software Architect  
**Task**: Explain the design patterns and architectural structure of the code using simple analogies for a junior developer.  
**Input Placeholder**:  
\`\`\`java
public class DatabaseConnection {
    private static DatabaseConnection instance;
    private DatabaseConnection() {}
    public static synchronized DatabaseConnection getInstance() {
        if (instance == null) {
            instance = new DatabaseConnection();
        }
        return instance;
    }
}
\`\`\`

**AI Output**:  
**Design Pattern Identified**: Singleton Pattern.  

**Analogy**:  
Imagine the President's office in a country. There can only be **one** President at a time.  
The \`private DatabaseConnection()\` is like locking the doors so no one can just walk in and declare themselves President.  
The \`getInstance()\` method is the official receptionist: everyone is directed to the **same, single person**.  

**Feedback**: The analogy is clear and relatable for a beginner. It explains the purpose of the private constructor effectively.
