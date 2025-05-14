def sum_of_digits(n):
    # Step 3: Handle unintentional cases
    assert n >= 0 and int(n) == n, "The number has to be a positive integer only."
    
    # Step 2: Define the base case
    if n == 0:
        return 0
    
    # Step 1: Recursive case
    return (n % 10) + sum_of_digits(n // 10)

# Testing the function
print(sum_of_digits(4))         # Output: 4
print(sum_of_digits(12))        # Output: 3
print(sum_of_digits(112))       # Output: 4
print(sum_of_digits(1234))      # Output: 10
