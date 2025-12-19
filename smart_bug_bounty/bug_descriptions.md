# Bug Descriptions

## bug1.py
- **Intended Behavior**: Calculate the average of passing grades (>60) and find the student with the highest score.
- **Current Issue**: 
    1. `calculate_average`: Raises `ZeroDivisionError` if the filtered list is empty (no grades > 60).
    2. `get_best_student`: Returns `None` if the highest score in the list is 0 (initialization issue) or fails to handle negative scores correctly.

## bug2.js
- **Intended Behavior**: Fetch multiple user profiles asynchronously and return them as a list.
- **Current Issue**: Usage of `Array.prototype.forEach` with an `async` callback. The main function `getAllProfiles` returns the empty `profiles` array immediately without waiting for the asynchronous fetch operations to complete.

## bug3.java
- **Intended Behavior**: Manage an inventory list, allowing adding items and checking for existence.
- **Current Issue**:
    1. `checkItemExists`: Uses `==` operator for String comparison instead of `.equals()`, leading to false negatives.
    2. `addItem`: Throws `NullPointerException` if input is null (checked length before null check).
    3. `getItemByIndex`: Incorrect boundary check (`index > items.size()`) allows `index == items.size()` to pass, causing `IndexOutOfBoundsException`.

## bug4.py
- **Intended Behavior**: Parse a log file to count errors and collect warnings.
- **Current Issue**:
    1. Resource Leak: Opens a file using `open()` without a `with` statement or `f.close()`, potentially leaving file descriptors open.
    2. Parsing Logic: Weak parsing that assumes a rigid structure and doesn't handle empty lines gracefully.
