## Bug Report – bug1.py
- **Summary**: Syntax error in `for` loop statement.  
- **Root Cause**: Missing colon (`:`) after `for n in numbers`.  
- **Resolution**: Added the missing colon to properly define the loop: `for n in numbers:`.  
- **Lesson Learned**: Python syntax is strict—always verify indentation and punctuation in control structures.

---

## Bug Report – bug2.js
- **Summary**: Incorrect logic for determining even numbers.  
- **Root Cause**: Condition used `num % 2 == 1`, identifying odd numbers as even.  
- **Resolution**: Updated the condition to `num % 2 == 0` and simplified to `return num % 2 === 0;`.  
- **Lesson Learned**: Test boolean logic with both expected true and false cases to catch inverted conditions early.

---

## Bug Report – bug3.java
- **Summary**: Array index out-of-bounds exception.  
- **Root Cause**: Attempted to access index `2` in a two-element array.  
- **Resolution**: Either added a third element (`{10, 20, 30}`) or changed access to a valid index (`nums[1]`).  
- **Lesson Learned**: Always confirm array length before accessing by index; use `array.length` for bounds checking.

---

## Bug Report – bug4.cpp
- **Summary**: Off-by-one error in loop iteration.  
- **Root Cause**: Loop condition used `i <= size`, iterating one step beyond array bounds.  
- **Resolution**: Changed to `i < size` so the loop runs from `0` to `size - 1`.  
- **Lesson Learned**: Off-by-one errors are common—always reason through loop boundaries with explicit examples.

---

## Bug Report – bug5.py
- **Summary**: Type error when calculating numeric average.  
- **Root Cause**: Elements in `grades` list were strings, not numbers.  
- **Resolution**: Converted all elements to integers with `map(int, grades)` before summing.  
- **Lesson Learned**: Ensure data is in the correct type before performing mathematical operations.

---

## Bug Report – bug6.js
- **Summary**: File read callback parameters reversed.  
- **Root Cause**: `fs.readFile` callback defined as `(data, err)` instead of `(err, data)`.  
- **Resolution**: Swapped argument order and verified with `fs.readFile('test.txt', 'utf8', (err, data) => {...})`.  
- **Lesson Learned**: Always check official API documentation for correct function signatures and parameter order.
