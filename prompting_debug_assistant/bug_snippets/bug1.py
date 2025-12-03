# Syntax error example: intended to compute factorial recursively
def factorial(n)  # <-- missing colon causes a SyntaxError
    if n < 0:
        raise ValueError("Negative input not allowed")
    if n == 0:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    print(factorial(5))
