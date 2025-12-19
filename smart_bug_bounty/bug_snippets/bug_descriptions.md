# Bug Descriptions and Expected Behavior

## bug1.py (Python)
- **Function**: `calculate_grade_stats(grades)`
- **Intended Behavior**: Calculate the arithmetic mean of all grades strictly greater than 60. If no grades match, it should return 0 or handle the case gracefully.
- **Current Bug**: `ZeroDivisionError` is raised when the filtered list `passing_grades` is empty because `count` becomes 0.

## bug2.js (JavaScript)
- **Function**: `getDetails(ids)`
- **Intended Behavior**: Accept an array of IDs, perform asynchronous API calls for each, wait for all calls to finish, and return an array containing the results.
- **Current Bug**: The use of `forEach` with an `async` callback results in the function returning the empty `results` array immediately, without waiting for the promises to resolve.

## bug3.java (Java)
- **Function**: `validateToken(inputToken)`
- **Intended Behavior**: Return `true` only if the content of `inputToken` is identical to `secretToken`, and handle `null` inputs safely by returning `false`.
- **Current Bug**: 
    1. Uses `==` for string comparison (reference equality) instead of `.equals()` (content equality).
    2. Throws `NullPointerException` on `inputToken.length()` because the null check is missing before dereferencing.

## bug4.py (Python)
- **Function**: `load_config(filepath)`
- **Intended Behavior**: Open a JSON file safely, parse it, and return a dictionary where user values override defaults. It must ensure the file handle is closed properly even if errors occur.
- **Current Bug**:
    1. **Resource Leak**: Uses `open()` without `close()` or a context manager (`with`).
    2. **Logic Error**: `config.update(default_config)` overwrites the loaded user configuration with defaults, reversing the intended precedence.

## bug5.c (C)
- **Function**: `process_user_input()`
- **Intended Behavior**: Read a username from standard input into a buffer of 50 characters, ensuring no memory corruption occurs if the input is longer.
- **Current Bug**: Uses the deprecated `gets()` function which lacks bounds checking, allowing a user to write past the end of `buffer` (Stack Buffer Overflow).

## bug6.php (PHP)
- **Function**: `checkAdminHash($input_hash)`
- **Intended Behavior**: strictly compare the input string hash against the stored hash to ensure they are identical characters.
- **Current Bug**: Uses loose comparison (`==`). In PHP, if both strings look like scientific notation (e.g., start with "0e" followed by digits), they are cast to floats (`0.0 == 0.0`) and return `true`, bypassing authentication (Magic Hash vulnerability).
