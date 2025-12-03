## Bug 1 – bug1.py
**Intended Behavior**: Compute factorial(n) recursively and print factorial(5) == 120.
**Issue Type**: SyntaxError.
**Notes**: Missing colon after function definition `def factorial(n)`.

---

## Bug 2 – bug2.js
**Intended Behavior**: Return the nth Fibonacci number (e.g., fib(6) should be 8).
**Issue Type**: Logical error.
**Notes**: Incorrect variable update order inside the loop; `a` is overwritten before `b` uses its old value.

---

## Bug 3 – bug3.java
**Intended Behavior**: Return `true` if a number is even, and `false` otherwise.
**Issue Type**: Logical error.
**Notes**: The condition `num % 2 == 1` checks for odd numbers, effectively inverting the logic for `isEven`.

---

## Bug 4 – bug4.cpp
**Intended Behavior**: Print all elements of an integer array.
**Issue Type**: Off-by-one error.
**Notes**: The loop condition `i <= size` accesses an index out of bounds; it should be `i < size`.

---

## Bug 5 – bug5.js
**Intended Behavior**: Return an array of names from a users collection.
**Issue Type**: Type error / Misuse of data types.
**Notes**: The `users` variable is an object, not an array, so standard array methods like `.map()` cannot be applied directly without conversion.

---

## Bug 6 – bug6.js
**Intended Behavior**: Read a text file asynchronously and print its content.
**Issue Type**: Library misuse.
**Notes**: The callback parameters are reversed (`data, err`) instead of the standard Node.js signature (`err, data`).
