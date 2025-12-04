## Bug 1 – bug1.py
**AI Diagnosis**: The code raises a `SyntaxError` because the function definition line `def factorial(n)` is missing a colon (`:`) at the end. Python requires a colon to mark the start of a function block.  
**Suggested Fix**: Add a colon at the end of the definition: `def factorial(n):`.  
**Alternative Fixes Tested**: None.  
**Result**: Syntax error resolved; function runs correctly.  

---

## Bug 2 – bug2.js
**AI Diagnosis**: The function returns incorrect Fibonacci numbers because the variables are updated sequentially inside the loop. When `a = b` runs, the old value of `a` is lost, so the subsequent line `b = a + b` uses the *new* `a`, resulting in an incorrect sequence calculation.  
**Suggested Fix**: Use array destructuring to update both variables simultaneously: `[a, b] = [b, a + b];`.  
**Alternative Fixes Tested**: Using a temporary variable (`let temp = a; a = b; b = temp + b;`). Both work, but destructuring is cleaner.  
**Result**: Logic corrected; `fib(6)` now returns 8.  

---

## Bug 3 – bug3.java
**AI Diagnosis**: The function `isEven` returns `true` for odd numbers because the condition `num % 2 == 1` checks if the remainder is 1. This is the logic for identifying odd numbers, not even ones.  
**Suggested Fix**: Change the condition to check for a remainder of 0: `if (num % 2 == 0)`.  
**Alternative Fixes Tested**: `if (num % 2 != 1)` (works for positive integers but strictly checking for 0 is safer/clearer).  
**Result**: Function now correctly identifies even numbers.  

---

## Bug 4 – bug4.cpp
**AI Diagnosis**: The loop causes an index out-of-bounds error (or undefined behavior) because the condition `i <= size`   allows `i` to equal `size`. Valid array indices in C++ range from `0` to `size - 1`. Accessing `arr[size]` reads memory outside the array.  
**Suggested Fix**: Change the loop condition to strict inequality: `i < size`.   
**Alternative Fixes Tested**: None.  
**Result**: Loop iterates through all valid elements without crashing.  

---

## Bug 5 – bug5.js
**AI Diagnosis**: The code attempts to iterate over user data using `Object.keys`, which works but can be verbose. The comment implies an intention to map over the object directly, which would cause a `TypeError` if attempted. The cleanest way to map values from an object is using `Object.values`.  
**Suggested Fix**: Use `Object.values(u)` to get the array of user objects directly, then map: `return Object.values(u).map(user => user.name);`.  
**Alternative Fixes Tested**: `Object.keys(u).map(key => u[key].name)` (Original code style, works but less readable).  
**Result**: Code cleanly extracts names `["Alice", "Bob"]`.  

---

## Bug 6 – bug6.js
**AI Diagnosis**: The file read operation fails or prints garbage because the callback signature is incorrect. Node.js `fs.readFile` uses an "error-first" callback pattern: `(err, data)`. The current code uses `(data, err)`, meaning the error object is being treated as the file content.  
**Suggested Fix**: Swap the parameters in the callback function: `(err, data) => { ... }`.  
**Alternative Fixes Tested**: None.  
**Result**: File content is printed correctly; errors are handled properly.  
