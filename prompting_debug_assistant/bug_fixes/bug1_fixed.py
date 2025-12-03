# Fixed SyntaxError: Added colon after function definition
def factorial(n): 
    if n < 0:
        raise ValueError("Negative input not allowed")
    if n == 0:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    result = factorial(5)
    print(result)
    # Verification
    assert result == 120, f"Expected 120, got {result}"
