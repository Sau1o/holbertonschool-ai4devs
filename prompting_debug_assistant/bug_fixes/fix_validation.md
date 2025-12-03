# Fix Validation Log

## Bug 1 – bug1_fixed.py
- **Input**: `factorial(5)`
- **Expected Output**: `120`
- **Actual Output**: `120` ✅
- **Notes**: SyntaxError resolved by adding the colon.

## Bug 2 – bug2_fixed.js
- **Input**: `fib(6)`
- **Expected Output**: `8`
- **Actual Output**: `8` ✅
- **Notes**: Logic fixed using destructuring `[a, b] = [b, a + b]` to prevent overwriting `a` prematurely.

## Bug 3 – bug3_fixed.java
- **Input**: `isEven(4)`
- **Expected Output**: `true`
- **Actual Output**: `true` ✅
- **Input**: `isEven(5)`
- **Expected Output**: `false`
- **Actual Output**: `false` ✅
- **Notes**: Changed condition from `num % 2 == 1` to `num % 2 == 0`.

## Bug 4 – bug4_fixed.cpp
- **Input**: Array `{10, 20, 30, 40, 50}`
- **Expected Output**: Print 5 values, ending at 50.
- **Actual Output**: Prints 10, 20, 30, 40, 50 successfully. ✅
- **Notes**: Loop condition changed to `i < size` to avoid index out of bounds.

## Bug 5 – bug5_fixed.js
- **Input**: Object `{ alice: {name: "Alice"}, bob: {name: "Bob"} }`
- **Expected Output**: `["Alice", "Bob"]`
- **Actual Output**: `["Alice", "Bob"]` ✅
- **Notes**: Used `Object.values(u).map(...)` to correctly iterate over user objects.

## Bug 6 – bug6_fixed.js
- **Input**: File `test.txt` with content "Hello World"
- **Expected Output**: Console log "File content: Hello World"
- **Actual Output**: "File content: Hello World" ✅
- **Notes**: Swapped callback arguments from `(data, err)` to standard `(err, data)`.
