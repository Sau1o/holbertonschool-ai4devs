## Bug 1 – bug1.py  
**Intended Behavior**: Compute the factorial of a number `n` recursively and print the result (e.g., factorial(5) equals 120). 
**Issue Type**: SyntaxError (Missing Punctuation).  
**Notes**: The function definition `def factorial(n)` lacks the required colon (`:`) at the end. In Python, a colon is mandatory to introduce a new code block/scope.

---

## Bug 2 – bug2.js  
**Intended Behavior**: Return the nth Fibonacci number in the sequence (0, 1, 1, 2, 3, 5, 8...).  
**Issue Type**: Logical Error (Incorrect Variable Update).  
**Notes**: The variables are updated sequentially (`a = b` then `b = a + b`), which causes `b` to be calculated using the *new* value of `a` instead of the *old* one. This results in an incorrect sequence.  

---

## Bug 3 – bug3.java
**Intended Behavior**: Return `true` if the input number is even, and `false` otherwise.  
**Issue Type**: Logical Error (Incorrect Condition).  
**Notes**: The condition `num % 2 == 1` explicitly checks if a number is odd. To check for even numbers, the condition must verify that the remainder is zero (`num % 2 == 0`).  

---

## Bug 4 – bug4.cpp
**Intended Behavior**: Iterate through an integer array and print all its valid elements.  
**Issue Type**: Off-by-one Error (Array Index Out of Bounds).  
**Notes**: The loop condition `i <= size` allows the index to reach `size`, which refers to memory just past the end of the array (valid indices are `0` to `size-1`). This leads to undefined behavior or a crash.  

---

## Bug 5 – bug5.js
**Intended Behavior**: Return an array of names extracted from a `users` data structure.  
**Issue Type**: TypeError (Invalid Method on Object).  
**Notes**: The code attempts to call `.map()` on `users`, which is a plain JavaScript Object. Since `.map()` is an Array prototype method, this throws an error. The object must be converted to an array (e.g., via `Object.values()`) first.  

---

## Bug 6 – bug6.js
**Intended Behavior**: Read a text file asynchronously using the Node.js `fs` module and print its content.  
**Issue Type**: API Misuse (Incorrect Callback Signature).  
**Notes**: The standard Node.js error-first callback pattern expects `(err, data)`. The code defines `(data, err)`, causing the error object to be misinterpreted as the file content and vice versa.  
