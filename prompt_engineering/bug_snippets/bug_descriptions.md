Here’s a complete set of buggy code snippets and their descriptions.
Each file name and folder path is specified as requested.

---

### 🗂 Folder structure

```
bug_snippets/
├── bug1.py
├── bug2.js
├── bug3.java
├── bug4.cpp
├── bug5.py
└── bug_descriptions.md
```

---

### 🐛 **bug1.py** — Syntax Error

```python
# Intended to calculate the average of a list of numbers

def average(numbers)
    total = sum(numbers)
    avg = total / len(numbers)
    return avg

print(average([10, 20, 30, 40]))
```

---

### 🐛 **bug2.js** — Logical Error

```javascript
// Intended to check if a number is prime

function isPrime(n) {
  if (n <= 1) return false;
  for (let i = 2; i < n / 2; i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
}

console.log(isPrime(9));  // Expected: false, Actual: true
```

---

### 🐛 **bug3.java** — Runtime Exception

```java
// Intended to print the length of each string in an array

public class Bug3 {
    public static void main(String[] args) {
        String[] words = {"apple", "banana", null, "grape"};

        for (String word : words) {
            System.out.println(word.length());
        }
    }
}
```

---

### 🐛 **bug4.cpp** — Off-by-One / Loop Logic Error

```cpp
// Intended to print all elements of an array

#include <iostream>
using namespace std;

int main() {
    int nums[] = {1, 2, 3, 4, 5};
    int length = sizeof(nums) / sizeof(nums[0]);

    for (int i = 0; i <= length; i++) {
        cout << nums[i] << " ";
    }
    cout << endl;
    return 0;
}
```

---

### 🐛 **bug5.py** — Misuse of Data Type / Library

```python
# Intended to sort a list of numbers in ascending order

import math

numbers = [10, 5, 20, 1]
sorted_numbers = math.sort(numbers)  # math module doesn't have 'sort'

print(sorted_numbers)
```

---

### 📝 **bug_descriptions.md**

#### **bug1.py – Syntax Error**

* **Intended behavior:** Compute the average of a list of numbers.
* **Bug:** Missing colon (`:`) after the function definition.
* **Effect:** Causes a `SyntaxError` and prevents the program from running.

---

#### **bug2.js – Logical Error**

* **Intended behavior:** Return `true` if a number is prime, otherwise `false`.
* **Bug:** Loop condition uses `i < n / 2`, missing the square root optimization and missing equality check (`<=`). For small composites like 9, it skips divisor 3.
* **Effect:** Incorrectly returns `true` for non-prime numbers.

---

#### **bug3.java – Runtime Exception**

* **Intended behavior:** Print the length of each string.
* **Bug:** The array contains a `null` element; calling `.length()` on it causes a `NullPointerException`.
* **Effect:** Program crashes at runtime.

---

#### **bug4.cpp – Off-by-One Error**

* **Intended behavior:** Print all array elements.
* **Bug:** Loop condition `i <= length` iterates one step too far.
* **Effect:** Accesses memory outside array bounds, causing undefined behavior or crash.

---

#### **bug5.py – Misuse of Data Type / Library**

* **Intended behavior:** Sort numbers in ascending order.
* **Bug:** Uses `math.sort()` instead of the correct list method `numbers.sort()` or built-in `sorted(numbers)`.
* **Effect:** Raises an `AttributeError` because `math` module doesn’t have a `sort` function.

---

Would you like me to zip these files into a downloadable archive (`bug_snippets.zip`)?
