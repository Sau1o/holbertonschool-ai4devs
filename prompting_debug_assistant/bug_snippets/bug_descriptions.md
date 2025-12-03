## bug1.py (Syntax error)
**Intended behavior:** Compute factorial(n) recursively and print factorial(5) == 120.
**Bug type:** SyntaxError — missing colon after function definition `def factorial(n)`
**What to look for / fix:** Add the missing colon and verify indentation.

---

## Bug 2 – bug2.js
**Intended Behavior**: Return `true` if a number is even, and `false` otherwise.  
**Issue Type**: Logical error.  
**Notes**: The condition uses `num % 2 == 1` instead of `num % 2 == 0`, inverting the logic for even/odd numbers.

---

## Bug 3 – bug3.java
**Intended Behavior**: Print the third element in an integer array.  
**Issue Type**: Runtime exception.  
**Notes**: Accessing `nums[2]` in an array of size 2 causes an `ArrayIndexOutOfBoundsException`.

---

## Bug 4 – bug4.cpp
**Intended Behavior**: Print all elements of an integer array.  
**Issue Type**: Off-by-one loop error.  
**Notes**: Loop uses `i <= size` instead of `i < size`, causing access beyond array bounds and potential crash.

---

## Bug 5 – bug5.py
**Intended Behavior**: Calculate the average of a list of grades.  
**Issue Type**: Data type misuse.  
**Notes**: Elements are strings; `sum(grades)` raises `TypeError`. Must convert to integers or floats before summing.

---

## Bug 6 – bug6.js
**Intended Behavior**: Read a text file asynchronously and print its contents.  
**Issue Type**: Library misuse.  
**Notes**: Callback parameters are reversed (`data, err` instead of `err, data`), so the error and data are misinterpreted.
