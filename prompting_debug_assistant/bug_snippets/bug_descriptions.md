## Bug 1 – bug1.py 
**Intended behavior:** Compute factorial(n) recursively and print factorial(5) == 120.  
**Issue type:** SyntaxError — missing colon after function definition `def factorial(n)`  
**Notes:** Add the missing colon and verify indentation.  

---

## Bug 2 – bug2.js
**Intended behavior:** Return the nth Fibonacci number (0-indexed). Example: fib(6) == 8.  
**Issue type:** Logical error — incorrect update order inside the loop causing calculation to be wrong.  
**Notes:** Update both variables in a way that preserves previous values (use tuple-style swap or temporary variable).  

---

## Bug 3 – bug3.java  
**Intended behavior:** Parse the array of strings to integers and print their sum (10 + 30 = 40).  
**Issue type:** RuntimeException — NullPointerException (or NumberFormatException if value invalid).  
**Notes:** Validate inputs for null before parsing or filter/clean the input array.  

---

## Bug 4 – bug4.cpp
**Intended Behavior**: Print all elements of an integer array.  
**Issue Type**: Off-by-one loop error.  
**Notes**: Loop uses `i <= size` instead of `i < size`, causing access beyond array bounds and potential crash.

---

##  Bug 5 – bug5.js 
**Intended behavior:** Return an array of names `["Alice","Bob"]` from a users collection.  
**Issue type:** Type error / misuse — attempting to use `map` on an object.  
**Notes:** Convert object to array first (e.g., `Object.values(users).map(u => u.name)`) or iterate Object.keys/Object.values.  

---

## Bug 6 – bug6.js
**Intended Behavior**: Read a text file asynchronously and print its contents. 
**Issue Type**: Library misuse. 
**Notes**: Callback parameters are reversed (`data, err` instead of `err, data`), so the error and data are misinterpreted.
