## Bug Report – bug1.py
- **File Name**: `bug1.py`  
- **Bug Summary**: The script failed to run due to a `SyntaxError` immediately upon execution. 
- **Root Cause**: The function definition `def factorial(n)` was missing the mandatory colon (`:`) at the end of the line, which violates Python syntax rules.  
- **Resolution**: Added the missing colon to the function definition (`def factorial(n):`).  
- **Lesson Learned**: Pay close attention to syntax highlighting in IDEs, as missing punctuation is a common source of immediate execution errors in Python.

---

## Bug Report – bug2.js
- **File Name**: `bug2.js`  
- **Bug Summary**: The function returned incorrect Fibonacci sequence values (e.g., `fib(6)` returned a wrong number).  
- **Root Cause**: Sequential variable updates (`a = b; b = a + b`) caused `b` to be calculated using the *newly updated* value of `a`, rather than the *previous* value, corrupting the sequence logic.  
- **Resolution**: Implemented array destructuring (`[a, b] = [b, a + b]`) to update both variables simultaneously using their original values from the start of the iteration.  
- **Lesson Learned**: When swapping or updating dependent variables in a loop, ensure the order of operations preserves the necessary state, or use simultaneous assignment features.  

---

## Bug Report – bug3.java
- **File Name**: `bug3.java`
- **Bug Summary**: The `isEven` function incorrectly identified odd numbers as even (or vice-versa).  
- **Root Cause**: The condition `if (num % 2 == 1)` checks for a remainder of 1, which identifies *odd* numbers. This logic was inverted relative to the function name `isEven`.  
- **Resolution**: Changed the condition to `if (num % 2 == 0)` to correctly identify numbers with no remainder when divided by 2.  
- **Lesson Learned**: Verify that boolean conditions explicitly match the semantic intent of the function name (e.g., `isEven` vs `isOdd`).  

---

## Bug Report – bug4.cpp
- **File Name**: `bug4.cpp`
- **Bug Summary**: Array iteration caused an off-by-one error, leading to potential crashes or undefined behavior.  
- **Root Cause**: The loop condition `i <= size` allowed the index `i` to access `arr[size]`, which is one step past the valid memory range of the array (0 to `size-1`).  
- **Resolution**: Changed the loop condition to `i < size` to stop iteration at the last valid index.  
- **Lesson Learned**: In zero-indexed languages like C++, always use strict inequality (`<`) when iterating up to the size of a container.  

---

## Bug Report – bug5.js
- **File Name**: `bug5.js`
- **Bug Summary**: Attempting to use `.map()` on a plain object caused a TypeError / Logic Error.  
- **Root Cause**: The `users` variable was an Object, but the code tried to use `.map()` (or implied its use), which is an Array prototype method. Objects are not directly iterable via `.map()` without conversion.  
- **Resolution**: Converted the object values into an array using `Object.values(u)` before calling `.map()`, enabling efficient and correct iteration over the user data.  
- **Lesson Learned**: JavaScript Objects do not possess Array methods like `.map()` by default. To iterate over an object's data, you must explicitly convert it to an array first using static methods such as `Object.values()`, `Object.keys()`, or `Object.entries()`.  

---

## Bug Report – bug6.js
- **File Name**: `bug6.js`  
- **Bug Summary**: File reading operation printed garbage or failed to handle errors correctly.  
- **Root Cause**: The callback function signature `(data, err)` was inverted. The Node.js `fs.readFile` method uses an "error-first" pattern (`err, data`), causing the error object to be interpreted as content.  
- **Resolution**: Swapped the parameters in the callback function to `(err, data)` to match the standard Node.js API signature.  
- **Lesson Learned**: Always consult the official documentation for API callback signatures, especially when working with standard libraries like Node.js `fs`, which rely on the specific order of arguments.  
