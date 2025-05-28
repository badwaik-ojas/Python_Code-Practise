def factorial_tail(n, acc=1):
    if n == 0:
        return acc
    elif n < 0:
        print("Factorial is not defined for negative numbers.")
        raise ValueError("Factorial is not defined for negative numbers.")
    else:
        return factorial_tail(n-1, acc*n)
    
print(factorial_tail(5))  # Output: 120