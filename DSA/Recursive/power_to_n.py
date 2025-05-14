def power(base, exp):
    # Step 3: Handle unintentional cases
    assert int(exp) == exp, "Exponent must be an integer only."

    # Step 2: Base case
    if exp == 0:
        return 1
    elif exp < 0:
        # Handle negative exponents
        return 1 / (base * power(base, exp + 1))
    
    # Step 1: Recursive case
    return base * power(base, exp - 1)

# Testing the function with various cases
print(power(2, 3))  # Expected: 8
print(power(5, 0))  # Expected: 1
print(power(2, -2)) # Expected: 0.25
print(power(-3, 3)) # Expected: -27
