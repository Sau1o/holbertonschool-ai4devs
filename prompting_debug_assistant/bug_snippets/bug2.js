// Logical error example: intended to compute the nth Fibonacci number (0-indexed)
function fib(n) {
    // Intended: fib(0)=0, fib(1)=1, fib(2)=1, ...
    if (n <= 1) return n;
    let a = 0;
    let b = 1;
    for (let i = 1; i < n; i++) {
        // BUG: swapped update order causes incorrect sequence
        a = b;
        b = a + b;
    }
    return b;
}

console.log(fib(6)); // expected 8 but will print wrong value
