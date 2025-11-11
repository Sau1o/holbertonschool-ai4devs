# Prompt Testing Examples

## Example 1 – Bug Fixing

**Prompt**:

  * **Role**: Debugging Assistant
  * **Task**: Analyze the provided Python code and bug description to find the bug and suggest a fix.
  * **Input**:
      * **Code**:
        ```python
        def get_last_n_items(items, n):
          # Get the last n items from a list
          return items[len(items) - n - 1:]

        print(get_last_n_items([1, 2, 3, 4, 5], 2))
        ```
      * **Bug Description**: "I want the last 2 items, so `[4, 5]`, but it's returning `[3, 4, 5]`."

**AI Output**:

## Bug 1 – `get_last_n_items`

**AI Diagnosis**: The slice `items[len(items) - n - 1:]` is incorrect. By subtracting `n` and then another `1`, the slice starts one element too early. For a list of 5 items and `n=2`, the start index calculates to `5 - 2 - 1 = 2`, which is index `[2]`. This results in returning `n+1` items.

**Suggested Fix**: Change the slice to `items[len(items) - n:]`. A simpler way to write this in Python is to use a negative index: `items[-n:]`.

**Fixed Code**:

```python
def get_last_n_items(items, n):
  # Get the last n items from a list
  # Use negative slicing for simplicity and correctness
  return items[-n:]

print(get_last_n_items([1, 2, 3, 4, 5], 2))
# Output: [4, 5]
```

**Feedback**: Excellent. The diagnosis is correct, the fix is accurate, and it even provided a more Pythonic alternative (`items[-n:]`), which is the preferred solution.

-----

## Example 2 – Unit Test Generation

**Prompt**:

  * **Role**: QA Engineer
  * **Task**: Write a suite of unit tests for the given Python function using the `pytest` framework.
  * **Input**:
    ```python
    def format_user_name(first_name, last_name, title=""):
        """Formats a user's full name."""
        if not first_name or not last_name:
            return "Error: Missing required name"
        
        full_name = f"{first_name} {last_name}"
        if title:
            return f"{title} {full_name}"
        return full_name
    ```

**AI Output**:

```python
import pytest
from your_module import format_user_name # Assuming function is in 'your_module.py'

def test_format_name_basic():
    assert format_user_name("John", "Doe") == "John Doe"

def test_format_name_with_title():
    assert format_user_name("Jane", "Smith", title="Dr.") == "Dr. Jane Smith"

def test_format_name_missing_first_name():
    assert format_user_name("", "Doe") == "Error: Missing required name"

def test_format_name_missing_last_name():
    assert format_user_name("John", "") == "Error: Missing required name"

def test_format_name_empty_title_is_ignored():
    assert format_user_name("Peter", "Jones", title="") == "Peter Jones"

def test_format_name_with_none_input():
    assert format_user_name(None, "Doe") == "Error: Missing required name"
    assert format_user_name("Jane", None) == "Error: Missing required name"
```

**Feedback**: Very good. The output covers the main happy path, the titled path, and the error conditions (missing names). It also correctly identified that `None` inputs should be tested and that an empty `title` string should be ignored.

-----

## Example 3 – Code Explanation

**Prompt**:

  * **Role**: Tech Lead / Mentor
  * **Task**: Explain what the following JavaScript code does, how it works, and its potential side effects.
  * **Input**:
    ```javascript
    const users = [
      { id: 1, name: "Alice", age: 25, status: "active" },
      { id: 2, name: "Bob", age: 30, status: "inactive" },
      { id: 3, name: "Charlie", age: 35, status: "active" }
    ];

    const activeUserNames = users
      .filter(user => user.status === "active")
      .map(user => user.name.toUpperCase());
    ```

**AI Output**:
This code snippet processes a list of user objects to extract the names of active users and convert them to uppercase.

Here is a step-by-step breakdown:

1.  **`users.filter(user => user.status === "active")`**:

      * This method iterates over the `users` array.
      * It checks each `user` object to see if its `status` property is strictly equal to `"active"`.
      * It returns a **new array** containing only the users who passed this test. In this case, the new array would be:
        ```
        [
          { id: 1, name: "Alice", age: 25, status: "active" },
          { id: 3, name: "Charlie", age: 35, status: "active" }
        ]
        ```

2.  **`.map(user => user.name.toUpperCase())`**:

      * This method is called on the **result** of the `.filter()` (the new array of active users).
      * It iterates over this new array and transforms each element.
      * For each active `user` object, it accesses the `name` property (e.g., "Alice") and calls the `.toUpperCase()` method on it.
      * It returns another **new array** containing only these transformed values.
      * The final value of `activeUserNames` will be:
        ```
        ["ALICE", "CHARLIE"]
        ```

**Potential Side Effects**:

  * There are no side effects. The original `users` array is not modified. `.filter()` and `.map()` are non-mutating and return new arrays.

**Feedback**: Perfect. The explanation is clear, breaks down the chain of operations correctly, shows the intermediate result, and correctly identifies that there are no side effects.

-----

## Example 4 – Regex Generation

**Prompt**:

  * **Role**: Data Validation Specialist
  * **Task**: Create a regular expression (regex) to validate a 6-digit hexadecimal color code, with or without a leading `#`.
  * **Input**:
      * **Valid**: `#FF0000`, `E6E6FA`, `#a0c4ff`
      * **Invalid**: `FF000`, `#GG0000`, `#1234567`

**AI Output**:
Here is the regex pattern:

`/^#?([a-fA-F0-9]{6})$/`

**Explanation**:

  * `^` : Asserts the position at the start of the string.
  * `#?` : Matches the literal character `#`. The `?` makes it optional (matches 0 or 1 time).
  * `(`...`)` : Groups the main expression.
  * `[a-fA-F0-9]` : A character class that matches any lowercase letter from 'a' to 'f', any uppercase letter from 'A' to 'F', or any digit from '0' to '9'.
  * `{6}` : A quantifier that matches exactly 6 of the preceding character class.
  * `$` : Asserts the position at the end of the string.
  * The `^` and `$` anchors are crucial to ensure the *entire* string matches the pattern, preventing partial matches on invalid strings like `#1234567`.

**Feedback**: Correct. The regex handles the optional `#`, is case-insensitive for the hex characters, and correctly enforces the 6-character length. The explanation is detailed and accurate.

-----

## Example 5 – Refactoring

**Prompt**:

  * **Role**: Senior Developer
  * **Task**: Refactor the given Python code for clarity and maintainability.
  * **Input**:
    ```python
    def get_permission_level(user_role):
        if user_role == "admin":
            return 4
        elif user_role == "editor":
            return 3
        elif user_role == "contributor":
            return 2
        elif user_role == "viewer":
            return 1
        else:
            return 0
    ```

**AI Output**:

```python
def get_permission_level(user_role):
    """
    Returns the permission level for a given user role.
    
    Refactored to use a dictionary lookup for better readability
    and O(1) average-case performance.
    """
    ROLE_PERMISSIONS = {
        "admin": 4,
        "editor": 3,
        "contributor": 2,
        "viewer": 1,
    }
    
    # Use .get() to provide a default value (0) if the role is not found.
    return ROLE_PERMISSIONS.get(user_role, 0)

```

**Inline Comments on Changes**:

1.  **Replaced `if/elif` chain with Dictionary**: A long `if/elif` chain checking for string equality is less efficient and harder to maintain than a dictionary (hash map) lookup.
2.  **Used `.get()` for Default Case**: Using `dictionary.get(key, default_value)` gracefully handles cases where the `user_role` is not in the map (the `else` case), returning `0` without needing an extra check.
3.  **Added Docstring**: Added a basic docstring explaining the function's purpose and the refactoring logic.

**Feedback**: Great. The refactor is a significant improvement. It correctly uses a dictionary lookup, and the use of `.get()` to handle the default case is the standard, clean way to do this. The extra comments explaining *why* the change was made are very valuable.
