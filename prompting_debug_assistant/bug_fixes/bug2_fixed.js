// Fixed Logical error: used destructuring for simultaneous update
function fib(n) {
    if (n <= 1) return n;
    let a = 0;
    let b = 1;
    for (let i = 1; i < n; i++) {
        // Fix: Update a and b simultaneously
        [a, b] = [b, a + b];
    }
    return b;
}

const result = fib(6);
console.log(result); // Expected 8
console.assert(result === 8, `Expected 8, got ${result}`);
