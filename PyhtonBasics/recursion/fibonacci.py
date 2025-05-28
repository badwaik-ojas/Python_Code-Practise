'''
Fibonacci Series & Recursion - Complete Notes
What is the Fibonacci Series?
The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding numbers.
Example Series: 1, 1, 2, 3, 5, 8, 13, 21, 34...
Pattern:

Position 0: 1
Position 1: 1
Position 2: 1 + 1 = 2
Position 3: 1 + 2 = 3
Position 4: 2 + 3 = 5
Position 5: 3 + 5 = 8
'''

def fibonacci(n):
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        value = fibonacci(n-1) + fibonacci(n-2)
        print(value)
        return value
    
print(fibonacci(10))