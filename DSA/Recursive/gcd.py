def gcd(a, b):
    # Step 3: Handle unintentional cases
    assert int(a) == a and int(b) == b, "The numbers must be integers only."
    
    # Convert negative numbers to positive
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    
    # Step 2: Base case
    if b == 0:
        return a

    # Step 1: Recursive case
    return gcd(b, a % b)

# Testing the function
print(gcd(48, 18))  # Expected: 6
print(gcd(-48, 18)) # Expected: 6
print(gcd(48, -18)) # Expected: 6
print(gcd(0, 18))   # Expected: 18
print(gcd(18, 0))   # Expected: 18
