def fibonacci(n):
    # Handle edge cases: n must be a non-negative integer
    assert isinstance(n, int) and n >= 0, "Fibonacci number cannot be negative or non-integer."

    # Base cases
    if n == 0 or n == 1:
        return n
    
    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(1))
print(fibonacci(2))

print(fibonacci(3))

print(fibonacci(10))

