def decimal_to_binary(n):
    # Step 3: Handle unintentional cases
    assert int(n) == n, "The parameter must be an integer only."
    
    # Step 2: Base case
    if n == 0:
        return 0
    
    # Step 1: Recursive case
    return n % 2 + 10 * decimal_to_binary(n // 2)

# Testing the function
print(decimal_to_binary(10))  # Expected: 1010
print(decimal_to_binary(13))  # Expected: 1101
print(decimal_to_binary(0))   # Expected: 0
