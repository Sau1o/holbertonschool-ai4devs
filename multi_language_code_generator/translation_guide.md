# Translation Guide - Package Dependency Resolver

This document outlines the idiomatic differences, common pitfalls, and best practices encountered when porting the Dependency Resolver algorithm from Python (Reference) to Java and JavaScript.

## General Challenge: Determinism
A major challenge across all languages was ensuring **deterministic output**. Topological sorts can have multiple valid solutions.
- **Python:** Used `sorted()` on dictionary keys and neighbors before processing to ensure order.
- **Java:** Required `PriorityQueue` or `Collections.sort()` to match the test expectations.
- **JavaScript:** `Array.sort()` behavior is generally consistent for strings, but iteration order over Objects was historically not guaranteed (though mostly predictable in modern engines).

---

## Python → Java

### Idiomatic Differences
- **Typing:** Python's dynamic typing allows flexible structures like `{"A": ["B"]}`. Java requires explicit type definitions (`Map<String, List<String>>`).
- **Data Structures:**
  - Python `dict` → Java `HashMap` (or `LinkedHashMap` for insertion order).
  - Python `deque` → Java `Queue` interface (implemented by `LinkedList` or `PriorityQueue`).
- **Return Values:** Python can return a dynamic dict with mixed types (`bool`, `list`, `str`). Java required creating a dedicated static inner class (`ResolutionResult`) or a POJO to hold structured results safely.

### Common Pitfalls
- **Boilerplate Overhead:** Translating 20 lines of Python logic often results in 50+ lines of Java due to imports, class structure, and type declarations.
- **Equality Checks:** Comparing strings in Python uses `==`. In Java, `==` compares references; `string.equals()` must be used.

### Best Practices
- **Use POJOs:** Instead of returning a `Map<String, Object>` (which is messy and unsafe), define a strict class for the result.
- **Interface Coding:** Program to the interface (`List`, `Map`) rather than the implementation (`ArrayList`, `HashMap`) to allow swapping implementations (e.g., for sorting).

---

## Python → JavaScript (Node.js)

### Idiomatic Differences
- **Queues:** Python has `collections.deque` for O(1) pops from the front. JavaScript Arrays are used as queues, but `.shift()` is **O(n)**, which can degrade performance on large datasets.
- **Iteration:** Python's `for item in list` is equivalent to JS `for (const item of list)`. However, iterating objects requires `Object.keys()` or `Object.entries()`.

### Common Pitfalls
- **Sorting behavior:** JS `.sort()` sorts efficiently for strings, but for numbers, it converts to strings first (e.g., "10" comes before "2"). While not an issue for package names, it's a constant risk in translation.
- **Variable Scope:** Python's function scope vs. JS block scope (`let`/`const`) usually isn't an issue, but accidentally using `var` or forgetting declaration can leak variables.

### Best Practices
- **Map Object:** Prefer using ES6 `Map` over plain Objects `{}` for hashmaps, as `Map` preserves insertion order better and has a cleaner API for checking existence (`has` vs `hasOwnProperty`).
- **Linting:** Use strict mode or TypeScript to catch type-related errors that Python might have handled dynamically or thrown at runtime.
